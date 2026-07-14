"""Tiny local drag-and-drop media manager for the MkDocs site."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
import threading
import unicodedata
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath
from urllib.parse import parse_qs, quote, unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MEDIA = DOCS / "assets" / "media"
METADATA = DOCS / "assets" / "media-metadata.json"
ALLOWED_EXTENSIONS = {
    ".avif", ".gif", ".jpeg", ".jpg", ".png", ".svg", ".webp",
    ".mp4", ".webm", ".mov", ".mp3", ".ogg", ".wav", ".m4a",
}
SVG_COLOR = re.compile(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?(?:[0-9a-fA-F]{2})?\b")


def slugify(filename: str) -> str:
    source = Path(filename).stem
    source = unicodedata.normalize("NFKD", source).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", source).strip("-").lower()
    return slug or "medium"


def page_files() -> list[str]:
    return sorted(p.relative_to(DOCS).as_posix() for p in DOCS.rglob("*.md"))


def checked_page(value: str) -> Path:
    relative = PurePosixPath(value)
    if relative.is_absolute() or ".." in relative.parts or relative.suffix != ".md":
        raise ValueError("Ungültige Seite")
    page = DOCS.joinpath(*relative.parts).resolve()
    if DOCS.resolve() not in page.parents or not page.is_file():
        raise ValueError("Seite wurde nicht gefunden")
    return page


def destination_for(page: Path, filename: str) -> Path:
    suffix = Path(filename).suffix.lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Dateityp {suffix or '(ohne Endung)'} wird nicht unterstützt")
    page_relative = page.relative_to(DOCS)
    page_folder = page_relative.parent if page_relative.stem == "index" else page_relative.with_suffix("")
    if not page_folder.parts:
        page_folder = Path("home")
    folder = MEDIA / page_folder
    folder.mkdir(parents=True, exist_ok=True)
    candidate = folder / f"{slugify(filename)}{suffix}"
    number = 2
    while candidate.exists():
        candidate = folder / f"{slugify(filename)}-{number}{suffix}"
        number += 1
    return candidate


def snippet_for(page: Path, media: Path, alt: str) -> str:
    relative = Path(os.path.relpath(media, page.parent)).as_posix()
    mime, _ = mimetypes.guess_type(media)
    clean_alt = (alt.strip() or media.stem.replace("-", " ")).replace("]", "")
    if mime and mime.startswith("video/"):
        return f'<video controls preload="metadata" src="{relative}"></video>'
    if mime and mime.startswith("audio/"):
        return f'<audio controls preload="metadata" src="{relative}"></audio>'
    return f"![{clean_alt}]({relative})"


def checked_media(value: str) -> Path:
    relative = PurePosixPath(value)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Ungültiger Medienpfad")
    media = DOCS.joinpath(*relative.parts).resolve()
    assets = (DOCS / "assets").resolve()
    if assets not in media.parents or not media.is_file() or media.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError("Medium wurde nicht gefunden")
    return media


def load_metadata() -> dict[str, str]:
    if not METADATA.exists():
        return {}
    value = json.loads(METADATA.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else {}


def save_metadata(value: dict[str, str]) -> None:
    METADATA.parent.mkdir(parents=True, exist_ok=True)
    METADATA.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def media_references(media: Path) -> list[str]:
    sources = [ROOT / "mkdocs.yml"] + [
        path for path in DOCS.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".css", ".html", ".yml", ".yaml"}
    ]
    references = []
    docs_path = media.relative_to(DOCS).as_posix()
    for source in sources:
        content = source.read_text(encoding="utf-8")
        relative = Path(os.path.relpath(media, source.parent)).as_posix()
        if relative in content or docs_path in content:
            references.append(source.relative_to(ROOT).as_posix())
    return list(dict.fromkeys(references))


def delete_media(media: Path) -> None:
    key = media.relative_to(DOCS).as_posix()
    metadata = load_metadata()
    if metadata.pop(key, None) is not None:
        save_metadata(metadata)
    media.unlink()


def media_items() -> list[dict[str, object]]:
    assets = DOCS / "assets"
    pages = [(page, page.read_text(encoding="utf-8")) for page in DOCS.rglob("*.md")]
    items = []
    metadata = load_metadata()
    for media in sorted(assets.rglob("*")):
        if not media.is_file() or media.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue
        used_on = []
        for page, content in pages:
            relative = Path(os.path.relpath(media, page.parent)).as_posix()
            if relative in content or media.relative_to(DOCS).as_posix() in content:
                used_on.append(page.relative_to(DOCS).as_posix())
        relative = media.relative_to(DOCS).as_posix()
        mime, _ = mimetypes.guess_type(media)
        items.append({
            "path": relative,
            "name": media.name,
            "url": f"/api/file?path={quote(relative)}",
            "kind": (mime or "application/octet-stream").split("/", 1)[0],
            "size": media.stat().st_size,
            "pages": used_on,
            "references": media_references(media),
            "description": metadata.get(relative, ""),
        })
    return items


def update_media_details(target: Path, requested_name: str, description: str) -> tuple[Path, list[str]]:
    name = f"{slugify(requested_name)}{target.suffix.lower()}"
    replacement = target.with_name(name)
    if replacement != target and replacement.exists():
        raise ValueError(f"{name} existiert bereits")
    updated: list[str] = []
    text_files = [ROOT / "mkdocs.yml"] + [
        path for path in DOCS.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".css", ".html", ".yml", ".yaml"}
    ]
    for source in text_files:
        content = source.read_text(encoding="utf-8")
        old_relative = Path(os.path.relpath(target, source.parent)).as_posix()
        new_relative = Path(os.path.relpath(replacement, source.parent)).as_posix()
        changed = content.replace(old_relative, new_relative)
        changed = changed.replace(target.relative_to(DOCS).as_posix(), replacement.relative_to(DOCS).as_posix())
        if source.suffix.lower() == ".md" and description.strip():
            changed = re.sub(
                r"!\[[^\]]*\]\(" + re.escape(new_relative) + r"\)",
                f"![{description.strip().replace(']', '')}]({new_relative})",
                changed,
            )
        if changed != content:
            source.write_text(changed, encoding="utf-8")
            updated.append(source.relative_to(ROOT).as_posix())
    old_key = target.relative_to(DOCS).as_posix()
    new_key = replacement.relative_to(DOCS).as_posix()
    metadata = load_metadata()
    metadata.pop(old_key, None)
    if description.strip():
        metadata[new_key] = description.strip()
    save_metadata(metadata)
    if replacement != target:
        target.replace(replacement)
    return replacement, updated


def svg_colors(media: Path) -> list[str]:
    if media.suffix.lower() != ".svg":
        raise ValueError("Der Farbeditor ist nur für SVG-Dateien verfügbar")
    content = media.read_text(encoding="utf-8")
    return list(dict.fromkeys(color.lower() for color in SVG_COLOR.findall(content)))


def update_svg_colors(media: Path, replacements: dict[str, str]) -> None:
    available = set(svg_colors(media))
    clean: dict[str, str] = {}
    for old, new in replacements.items():
        old, new = old.lower(), new.lower()
        if old not in available or not re.fullmatch(r"#[0-9a-f]{6}", new):
            raise ValueError("Ungültige SVG-Farbe")
        clean[old] = new
    if not clean:
        raise ValueError("Keine Farben zum Ändern ausgewählt")
    content = media.read_text(encoding="utf-8")
    changed = SVG_COLOR.sub(lambda match: clean.get(match.group(0).lower(), match.group(0)), content)
    temporary = media.with_name(f".{media.name}.colors")
    temporary.write_text(changed, encoding="utf-8")
    temporary.replace(media)


def replace_media(target: Path, uploaded_name: str, data: bytes) -> tuple[Path, list[str]]:
    new_suffix = Path(uploaded_name).suffix.lower()
    old_suffix = target.suffix.lower()
    if new_suffix not in ALLOWED_EXTENSIONS:
        raise ValueError("Nicht unterstützter Dateityp")
    if new_suffix != old_suffix and {new_suffix, old_suffix} != {".png", ".svg"}:
        raise ValueError("Nur PNG und SVG können gegeneinander ausgetauscht werden")
    if new_suffix == old_suffix:
        temporary = target.with_name(f".{target.name}.upload")
        temporary.write_bytes(data)
        temporary.replace(target)
        return target, []

    replacement = target.with_suffix(new_suffix)
    if replacement.exists():
        raise ValueError(f"{replacement.name} existiert bereits")
    text_files = [ROOT / "mkdocs.yml"]
    text_files.extend(
        path for path in DOCS.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".css", ".html", ".yml", ".yaml"}
    )
    changes: list[tuple[Path, str, str]] = []
    old_docs = target.relative_to(DOCS).as_posix()
    new_docs = replacement.relative_to(DOCS).as_posix()
    for source in text_files:
        content = source.read_text(encoding="utf-8")
        old_relative = Path(os.path.relpath(target, source.parent)).as_posix()
        new_relative = Path(os.path.relpath(replacement, source.parent)).as_posix()
        changed = content.replace(old_relative, new_relative).replace(old_docs, new_docs)
        if changed != content:
            changes.append((source, content, changed))

    temporary = replacement.with_name(f".{replacement.name}.upload")
    try:
        temporary.write_bytes(data)
        temporary.replace(replacement)
        for source, _, changed in changes:
            source.write_text(changed, encoding="utf-8")
        target.unlink()
    except OSError:
        for source, original, _ in changes:
            source.write_text(original, encoding="utf-8")
        if replacement.exists():
            replacement.unlink()
        raise
    metadata = load_metadata()
    old_key, new_key = target.relative_to(DOCS).as_posix(), replacement.relative_to(DOCS).as_posix()
    if old_key in metadata:
        metadata[new_key] = metadata.pop(old_key)
        save_metadata(metadata)
    return replacement, [source.relative_to(ROOT).as_posix() for source, _, _ in changes]


HTML = r'''<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width">
<title>FPVWiki Medien</title><style>
:root{color-scheme:dark;--bg:#090b10;--card:#151923;--line:#32394a;--pink:#ff3c91;--text:#f4f6fb;--muted:#9da7ba}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 80% 0,#27132b,transparent 38%),var(--bg);font:16px system-ui;color:var(--text)}
main{width:min(1180px,calc(100% - 32px));margin:45px auto}h1{font-size:clamp(30px,6vw,52px);margin:0 0 8px}h2{margin-top:55px}p,.meta{color:var(--muted)}
label{display:block;margin:24px 0 8px;font-weight:700}select,input{width:100%;padding:13px;border:1px solid var(--line);border-radius:9px;background:var(--card);color:var(--text);font:inherit}
.form{display:grid;grid-template-columns:1fr 1fr;gap:18px}.drop{margin-top:20px;border:2px dashed var(--line);border-radius:18px;padding:48px 20px;text-align:center;background:#11151dcc;cursor:pointer;transition:.15s}
.drop.over{border-color:var(--pink);background:#241421;transform:scale(1.01)}.drop strong{display:block;font-size:21px;margin-bottom:8px}.pink{color:var(--pink)}
.result{margin-top:14px;padding:16px;background:var(--card);border:1px solid var(--line);border-radius:12px}.result code{display:block;overflow:auto;padding:11px;background:#090b10;border-radius:7px;margin:9px 0;color:#f9b5d4}
button{border:0;border-radius:7px;padding:9px 13px;background:var(--pink);color:#fff;font-weight:700;cursor:pointer}.error{border-color:#a93b4b;color:#ffacb5}
.gallery-head{display:flex;gap:16px;align-items:end}.gallery-head div{flex:1}.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(245px,1fr));gap:18px;margin-top:22px}.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}.preview{height:180px;background:#080a0e;display:grid;place-items:center}.preview img,.preview video{width:100%;height:100%;object-fit:contain}.preview audio{width:90%}.info{padding:14px}.name{font-weight:750;overflow-wrap:anywhere}.path{font-size:12px;overflow-wrap:anywhere;margin:6px 0}.pages{font-size:13px;color:#c5ccda;min-height:38px}.replace{padding:16px;margin:12px 0 0;border-radius:9px;font-size:13px}.empty{text-align:center;padding:55px;color:var(--muted);grid-column:1/-1}
.secondary{margin-top:10px;background:#30384a}.danger{margin:10px 0 0 7px;background:#a82f45}.modal{position:fixed;inset:0;background:#05070bd9;display:none;place-items:center;padding:20px;z-index:5}.modal.open{display:grid}.dialog{width:min(520px,100%);max-height:90vh;overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:24px}.dialog h2{margin:0}.color-row{display:grid;grid-template-columns:90px 1fr;align-items:center;gap:14px;margin:16px 0}.color-row input{height:46px;padding:4px}.actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}.actions button:last-child{background:#4a5264}
@media(max-width:650px){.form{grid-template-columns:1fr}.gallery-head{display:block}.preview{height:220px}}
</style></head><body><main><h1>Medien <span class="pink">Drop</span></h1><p>Neue Medien ablegen oder bestehende Dateien in der Galerie finden und ersetzen.</p>
<div class="form"><div><label for="page">Zielseite</label><select id="page"></select></div><div><label for="alt">Bildbeschreibung (optional)</label><input id="alt" placeholder="z. B. Race Quad von oben"></div></div>
<div id="drop" class="drop"><strong>Neue Dateien hier ablegen</strong><span>oder klicken, um sie auszuwählen</span><input id="files" type="file" multiple hidden accept="image/*,video/*,audio/*"></div><section id="results"></section>
<h2>Alle Medien</h2><div class="gallery-head"><div><label for="search">Suchen</label><input id="search" type="search" placeholder="Dateiname, Pfad oder Seite …"></div><div><label for="filter">Typ</label><select id="filter"><option value="">Alle</option><option value="image">Bilder</option><option value="video">Videos</option><option value="audio">Audio</option></select></div></div>
<p id="count" class="meta"></p><section id="gallery" class="gallery"></section>
<div id="modal" class="modal"><div class="dialog"><h2>SVG-Farben anpassen</h2><p id="color-file"></p><div id="colors"></div><div class="actions"><button id="invert">Alle invertieren</button><button id="save-colors">Speichern</button><button id="cancel">Abbrechen</button></div></div></div>
<div id="details-modal" class="modal"><div class="dialog"><h2>Name und Beschreibung</h2><label for="media-name">Dateiname</label><input id="media-name"><label for="media-description">Beschreibung / Alt-Text</label><input id="media-description" placeholder="Was ist auf dem Bild zu sehen?"><div class="actions"><button id="save-details">Speichern</button><button id="cancel-details">Abbrechen</button></div></div></div>
<script>
const page=$('#page'),drop=$('#drop'),files=$('#files'),results=$('#results'),gallery=$('#gallery');let media=[],activeSvg=null,activeDetails=null;
fetch('/api/pages').then(r=>r.json()).then(p=>p.forEach(x=>page.add(new Option(x,x))));loadGallery();
drop.onclick=()=>files.click();files.onchange=()=>upload(files.files);
wireDrop(drop,list=>upload(list));$('#search').oninput=render;$('#filter').onchange=render;
function wireDrop(node,action){for(const event of ['dragenter','dragover'])node.addEventListener(event,e=>{e.preventDefault();e.stopPropagation();node.classList.add('over')});for(const event of ['dragleave','drop'])node.addEventListener(event,e=>{e.preventDefault();e.stopPropagation();node.classList.remove('over')});node.addEventListener('drop',e=>action(e.dataTransfer.files))}
async function loadGallery(){media=await fetch('/api/media').then(r=>r.json());render()}
function render(){const query=$('#search').value.toLowerCase(),kind=$('#filter').value;const shown=media.filter(m=>(!kind||m.kind===kind)&&[m.name,m.path,m.description,...m.references].join(' ').toLowerCase().includes(query));$('#count').textContent=`${shown.length} von ${media.length} Medien`;gallery.innerHTML='';if(!shown.length){gallery.innerHTML='<div class="empty">Keine passenden Medien gefunden.</div>';return}shown.forEach(m=>{
 const card=document.createElement('article');card.className='card';const visual=m.kind==='image'?`<img src="${m.url}" loading="lazy" alt="">`:m.kind==='video'?`<video src="${m.url}" controls preload="metadata"></video>`:`<audio src="${m.url}" controls preload="metadata"></audio>`;
 card.innerHTML=`<div class="preview">${visual}</div><div class="info"><div class="name">${esc(m.name)}</div><div class="path meta">${esc(m.path)}</div>${m.description?`<div class="pages">${esc(m.description)}</div>`:''}<div class="pages">${m.references.length?'Verwendet in: '+esc(m.references.join(', ')):'Keine Verweise gefunden'}</div><div class="drop replace"><strong>Zum Ersetzen hier ablegen</strong><span>PNG ↔ SVG wird automatisch verknüpft</span></div><button class="secondary edit-details">Name & Beschreibung</button>${m.name.toLowerCase().endsWith('.svg')?'<button class="secondary edit-colors">Farben anpassen</button>':''}<button class="danger delete">Löschen</button></div>`;
 const zone=card.querySelector('.replace');wireDrop(zone,list=>replace(m,list));zone.onclick=()=>pickReplacement(m);card.querySelector('.edit-details').onclick=()=>openDetails(m);card.querySelector('.edit-colors')?.addEventListener('click',()=>openColors(m));card.querySelector('.delete').onclick=()=>removeMedia(m);gallery.append(card)})}
function pickReplacement(item){const input=document.createElement('input');input.type='file';input.accept=item.kind==='image'?'image/*':'.'+item.name.split('.').pop();input.onchange=()=>replace(item,input.files);input.click()}
async function replace(item,list){if(list.length!==1)return alert('Bitte genau eine Datei ablegen.');const file=list[0],oldExt=item.name.split('.').pop().toLowerCase(),newExt=file.name.split('.').pop().toLowerCase();if(oldExt!==newExt&&!(['png','svg'].includes(oldExt)&&['png','svg'].includes(newExt)))return alert('Ein Wechsel des Dateityps ist nur zwischen PNG und SVG möglich.');const note=oldExt===newExt?'':`\n\nAlle Verweise werden automatisch von .${oldExt} auf .${newExt} aktualisiert.`;if(!confirm(`${item.name} wirklich durch ${file.name} ersetzen?${note}`))return;
 const r=await fetch('/api/replace',{method:'POST',headers:{'X-Path':encodeURIComponent(item.path),'X-Filename':encodeURIComponent(file.name)},body:file});const data=await r.json();if(!r.ok)return alert(data.error);if(data.updated?.length)alert(`Ersetzt. ${data.updated.length} Referenzdatei(en) wurden aktualisiert.`);await loadGallery()}
async function upload(list){if(!page.value)return alert('Bitte zuerst eine Zielseite auswählen.');for(const file of list){const box=document.createElement('div');box.className='result';box.textContent=`Lade ${file.name} …`;results.prepend(box);try{const r=await fetch('/api/upload',{method:'POST',headers:{'X-Page':encodeURIComponent(page.value),'X-Filename':encodeURIComponent(file.name),'X-Alt':encodeURIComponent($('#alt').value)},body:file});const data=await r.json();if(!r.ok)throw Error(data.error);box.innerHTML=`<strong>${esc(data.file)}</strong><code>${esc(data.snippet)}</code><button>Kopieren</button>`;box.querySelector('button').onclick=async()=>{await navigator.clipboard.writeText(data.snippet);box.querySelector('button').textContent='Kopiert ✓'};await loadGallery()}catch(e){box.classList.add('error');box.textContent=e.message}}}
async function openColors(item){const r=await fetch('/api/svg-colors?path='+encodeURIComponent(item.path)),data=await r.json();if(!r.ok)return alert(data.error);activeSvg=item;$('#color-file').textContent=item.path;$('#colors').innerHTML=data.colors.map((c,i)=>`<label class="color-row"><code>${esc(c)}</code><input type="color" data-old="${c}" value="${expand(c)}" aria-label="Farbe ${i+1}"></label>`).join('');$('#modal').classList.add('open')}
function expand(color){if(color.length===4)return '#'+[...color.slice(1)].map(x=>x+x).join('');return color.slice(0,7)}
$('#invert').onclick=()=>document.querySelectorAll('#colors input').forEach(input=>{const n=parseInt(input.value.slice(1),16)^0xffffff;input.value='#'+n.toString(16).padStart(6,'0')});$('#cancel').onclick=()=>$('#modal').classList.remove('open');
$('#save-colors').onclick=async()=>{const replacements={};document.querySelectorAll('#colors input').forEach(input=>replacements[input.dataset.old]=input.value);const r=await fetch('/api/svg-colors',{method:'POST',headers:{'Content-Type':'application/json','X-Path':encodeURIComponent(activeSvg.path)},body:JSON.stringify({replacements})});const data=await r.json();if(!r.ok)return alert(data.error);$('#modal').classList.remove('open');await loadGallery()};
function openDetails(item){activeDetails=item;$('#media-name').value=item.name.replace(/\.[^.]+$/,'');$('#media-description').value=item.description||'';$('#details-modal').classList.add('open')}$('#cancel-details').onclick=()=>$('#details-modal').classList.remove('open');
$('#save-details').onclick=async()=>{const payload={name:$('#media-name').value,description:$('#media-description').value};const r=await fetch('/api/media-details',{method:'POST',headers:{'Content-Type':'application/json','X-Path':encodeURIComponent(activeDetails.path)},body:JSON.stringify(payload)}),data=await r.json();if(!r.ok)return alert(data.error);$('#details-modal').classList.remove('open');await loadGallery()};
async function removeMedia(item){if(!confirm(`${item.name} wirklich löschen?`))return;let r=await fetch('/api/media?path='+encodeURIComponent(item.path),{method:'DELETE'}),data=await r.json();if(r.status===409){const list=data.references.join('\n• ');if(!confirm(`Dieses Medium wird noch verwendet:\n\n• ${list}\n\nTrotzdem endgültig löschen? Die Verweise bleiben bestehen und müssen anschließend angepasst werden.`))return;r=await fetch('/api/media?path='+encodeURIComponent(item.path)+'&force=1',{method:'DELETE'});data=await r.json()}if(!r.ok)return alert(data.error);await loadGallery()}
function $(s){return document.querySelector(s)}function esc(s){const d=document.createElement('div');d.textContent=s;return d.innerHTML}
</script></main></body></html>'''


class Handler(BaseHTTPRequestHandler):
    def json_response(self, status: int, value: object) -> None:
        data = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path == "/api/pages":
            self.json_response(200, page_files())
            return
        if parsed.path == "/api/media":
            self.json_response(200, media_items())
            return
        if parsed.path == "/api/svg-colors":
            try:
                media = checked_media(parse_qs(parsed.query).get("path", [""])[0])
                self.json_response(200, {"colors": svg_colors(media)})
            except (ValueError, OSError, UnicodeError) as error:
                self.json_response(400, {"error": str(error)})
            return
        if parsed.path == "/api/file":
            try:
                media = checked_media(parse_qs(parsed.query).get("path", [""])[0])
                data = media.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", mimetypes.guess_type(media)[0] or "application/octet-stream")
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Cache-Control", "no-cache")
                self.end_headers()
                self.wfile.write(data)
            except (ValueError, OSError) as error:
                self.json_response(404, {"error": str(error)})
            return
        data = HTML.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self) -> None:  # noqa: N802
        endpoint = urlparse(self.path).path
        if endpoint not in {"/api/upload", "/api/replace", "/api/svg-colors", "/api/media-details"}:
            self.json_response(404, {"error": "Nicht gefunden"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 100 * 1024 * 1024:
                raise ValueError("Die Datei ist leer oder größer als 100 MB")
            if endpoint == "/api/media-details":
                if length > 1024 * 1024:
                    raise ValueError("Anfrage ist zu groß")
                target = checked_media(self._header("X-Path"))
                payload = json.loads(self.rfile.read(length))
                if not isinstance(payload.get("name"), str) or not isinstance(payload.get("description"), str):
                    raise ValueError("Ungültige Angaben")
                replacement, updated = update_media_details(target, payload["name"], payload["description"])
                self.json_response(200, {"file": replacement.relative_to(ROOT).as_posix(), "updated": updated})
            elif endpoint == "/api/svg-colors":
                if length > 1024 * 1024:
                    raise ValueError("Farbanfrage ist zu groß")
                target = checked_media(self._header("X-Path"))
                payload = json.loads(self.rfile.read(length))
                replacements = payload.get("replacements")
                if not isinstance(replacements, dict):
                    raise ValueError("Ungültige Farbanfrage")
                update_svg_colors(target, replacements)
                self.json_response(200, {"file": target.relative_to(ROOT).as_posix(), "colors": svg_colors(target)})
            elif endpoint == "/api/replace":
                target = checked_media(self._header("X-Path"))
                replacement, updated = replace_media(target, self._header("X-Filename"), self.rfile.read(length))
                self.json_response(200, {"file": replacement.relative_to(ROOT).as_posix(), "updated": updated})
            else:
                page = checked_page(self._header("X-Page"))
                target = destination_for(page, self._header("X-Filename"))
                target.write_bytes(self.rfile.read(length))
                alt = self._header("X-Alt")
                if alt.strip():
                    metadata = load_metadata()
                    metadata[target.relative_to(DOCS).as_posix()] = alt.strip()
                    save_metadata(metadata)
                self.json_response(201, {"file": target.relative_to(ROOT).as_posix(), "snippet": snippet_for(page, target, alt)})
        except (ValueError, OSError, UnicodeError) as error:
            self.json_response(400, {"error": str(error)})

    def do_DELETE(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path != "/api/media":
            self.json_response(404, {"error": "Nicht gefunden"})
            return
        try:
            query = parse_qs(parsed.query)
            media = checked_media(query.get("path", [""])[0])
            references = media_references(media)
            if references and query.get("force", [""])[0] != "1":
                self.json_response(409, {"error": "Medium wird noch verwendet", "references": references})
                return
            delete_media(media)
            self.json_response(200, {"deleted": media.relative_to(DOCS).as_posix()})
        except (ValueError, OSError, UnicodeError) as error:
            self.json_response(400, {"error": str(error)})

    def _header(self, name: str) -> str:
        return unquote(self.headers.get(name, ""))

    def log_message(self, format: str, *args: object) -> None:
        pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Drag-and-drop media manager for FPVWiki")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://127.0.0.1:{args.port}"
    print(f"Medien-Tool läuft auf {url} (Beenden mit Strg+C)")
    if not args.no_browser:
        threading.Timer(0.4, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nBeendet.")


if __name__ == "__main__":
    main()
