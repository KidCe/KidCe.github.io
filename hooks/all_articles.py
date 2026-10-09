"""Build one article stream from canonical pages; no duplicated article bodies."""
from datetime import date, datetime
from html import escape
from pathlib import PurePosixPath
from pathlib import Path
import re
from urllib.parse import unquote

import yaml
from mkdocs.exceptions import PluginError
from mkdocs.plugins import event_priority
from mkdocs.utils import get_relative_url


def _source(file):
    text = file.content_string
    if text is None:
        source = Path(file.abs_src_path)
        text = source.read_text(encoding="utf-8") if source.exists() else ""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}, text
    meta = yaml.safe_load(match.group(1)) or {}
    return meta, text[match.end():]


def _date(value, path):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return date.fromisoformat(str(value))
    except ValueError as error:
        raise PluginError(f"{path}: article.published must be YYYY-MM-DD") from error


def _plain(text):
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"(?<!\w)(\*|_)([^\n]+?)\1(?!\w)", r"\2", text)
    return re.sub(r"\s+", " ", text.replace("**", "").replace("___", "").replace("`", "")).strip()


def _summary(body):
    for block in body.split("\n\n"):
        block = block.strip()
        if not block or block.startswith(("#", "!", "<", "|", ">", "-", "*", "```")):
            continue
        return _plain(block)
    return ""


def _cover(body, path):
    base = PurePosixPath(path).parent
    match = re.search(r"!\[([^\]]*)\]\(([^)]+)\)", body)
    if not match:
        match = re.search(r'<img\b[^>]*src="([^"]+)"[^>]*>', body)
        if not match:
            return "assets/images/article-placeholder.svg", ""
        src = match.group(1)
        alt_match = re.search(r'\balt="([^"]*)"', match.group(0))
        alt = alt_match.group(1) if alt_match else ""
        # Raw HTML links are relative to the generated page directory.
        base = PurePosixPath(path).with_suffix("")
    else:
        alt, src = match.groups()
    src = unquote(src.split(' "')[0].strip("<>"))
    if re.match(r"^[a-zA-Z]+:", src) or src.startswith("//"):
        return "assets/images/article-placeholder.svg", ""
    from posixpath import normpath
    return normpath(str(base / src)), _plain(alt)


def collect(files):
    articles = []
    for file in files.documentation_pages():
        if not file.inclusion.is_included():
            continue
        meta, body = _source(file)
        settings = meta.get("article")
        # Existing Material blog posts already carry publication dates.
        if settings is None and file.src_uri.startswith("articles/posts/"):
            published = meta.get("date")
            if isinstance(published, dict):
                published = published.get("created")
            settings = {"published": published} if published else None
        if not settings or settings is False:
            continue
        if not isinstance(settings, dict):
            raise PluginError(f"{file.src_uri}: article must be a mapping or false")
        published = _date(settings.get("published"), file.src_uri)
        title_match = re.search(r"^#\s+(.+)$", body, re.M)
        title = meta.get("title") or (title_match.group(1) if title_match else "")
        summary = settings.get("summary") or meta.get("description") or _summary(body)
        if not title or not summary:
            raise PluginError(f"{file.src_uri}: article needs a title and summary")
        image, alt = _cover(body, file.src_uri)
        image = settings.get("image", image)
        alt = settings.get("image_alt", alt)
        if not isinstance(image, str) or image.startswith(("/", "../")) or ":" in image:
            raise PluginError(f"{file.src_uri}: article.image must be a docs-relative local path")
        if files.get_file_from_path(image) is None:
            raise PluginError(f"{file.src_uri}: article cover does not exist: {image}")
        section = settings.get("section") or {
            "wiki": "Wiki", "projects": "Projects", "builds": "Builds",
            "articles": "Blog", "tools": "Tools", "Web Tools": "Tools"
        }.get(file.src_uri.split("/")[0], "Article")
        if file.src_uri.startswith("wiki/repairs/"):
            section = "Repairs"
        articles.append(dict(file=file, published=published, title=_plain(title),
                             summary=_plain(summary), image=image, alt=alt, section=section))
    # Stable order when multiple articles share a publication day.
    return sorted(articles, key=lambda a: (-a["published"].toordinal(), a["file"].src_uri))


def render(articles, page, files):
    cards = ['<div class="all-articles" aria-label="All articles, newest first">']
    for article in articles:
        href = get_relative_url(article["file"].url, page.file.url)
        cover = get_relative_url(files.get_file_from_path(article["image"]).url, page.file.url)
        published = article["published"]
        cards.append(
            '<article class="article-row">'
            f'<a class="article-row__image no-lightbox" href="{escape(href, quote=True)}" '
            f'aria-label="{escape(article["title"], quote=True)}">'
            f'<img class="no-lightbox" src="{escape(cover, quote=True)}" '
            f'alt="{escape(str(article["alt"]), quote=True)}" loading="lazy" decoding="async"></a>'
            '<div class="article-row__copy">'
            f'<p class="article-row__meta"><span>{escape(str(article["section"]))}</span> · '
            f'<time datetime="{published.isoformat()}">{published.strftime("%d %b %Y")}</time></p>'
            f'<h2><a href="{escape(href, quote=True)}">{escape(article["title"])}</a></h2>'
            f'<p>{escape(article["summary"])}</p>'
            f'<a class="article-row__link" href="{escape(href, quote=True)}">Read article →</a>'
            '</div></article>'
        )
    cards.append("</div>")
    return "\n".join(cards)


@event_priority(-100)
def on_page_markdown(markdown, *, page, config, files):
    if page.file.src_uri == "all-articles.md":
        marker = "<!-- all-articles -->"
        if marker not in markdown:
            raise PluginError("all-articles.md is missing its article-list marker")
        return markdown.replace(marker, render(collect(files), page, files))
    settings = page.meta.get("article")
    if isinstance(settings, dict):
        published = _date(settings.get("published"), page.file.src_uri)
        line = f"Published: {published.strftime('%d %b %Y')}"
        if settings.get("updated"):
            updated = _date(settings["updated"], page.file.src_uri)
            if updated < published:
                raise PluginError(f"{page.file.src_uri}: updated date predates publication")
            line += f" · Updated: {updated.strftime('%d %b %Y')}"
        badge = f'\n\n<p class="article-dates">{escape(line)}</p>\n'
        markdown = re.sub(r"(^# .+$)", lambda match: match.group(0) + badge, markdown, count=1, flags=re.M)
        changes = settings.get("changes", [])
        if changes:
            if not isinstance(changes, list):
                raise PluginError(f"{page.file.src_uri}: article.changes must be a list")
            items = []
            for change in changes:
                if not isinstance(change, dict) or not change.get("summary"):
                    raise PluginError(f"{page.file.src_uri}: each change needs date and summary")
                changed = _date(change.get("date"), page.file.src_uri)
                if changed < published or not settings.get("updated") or changed > updated:
                    raise PluginError(f"{page.file.src_uri}: change date must be between published and updated")
                items.append(f"<li><time datetime='{changed.isoformat()}'>{changed.strftime('%d %b %Y')}</time> — {escape(str(change['summary']))}</li>")
            markdown += '\n\n<section class="article-changes" aria-label="Article changes"><h2>Article changes</h2><ul>' + "".join(items) + '</ul></section>\n'
    return markdown
