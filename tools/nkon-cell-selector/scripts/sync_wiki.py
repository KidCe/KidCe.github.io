"""Copy reviewed static assets into MkDocs, or check that they are synchronized."""
import argparse
import datetime
import json
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEST = ROOT.parents[1] / 'docs/assets/cell-selector'
PAGE = ROOT.parents[1] / 'docs/tools/cell-selector.md'

def wiki_page():
    snapshot = json.loads((ROOT / 'dist/data/cells.json').read_text(encoding='utf-8'))
    date = datetime.date.fromisoformat(snapshot['snapshotDate']).strftime('%d %B %Y').lstrip('0')
    count = len(snapshot['cells'])
    audited = sum(c.get('visualCheck') == 'verified' for c in snapshot['cells'])
    html = (ROOT / 'dist/index.html').read_text(encoding='utf-8')
    body = re.search(r'<body>([\s\S]*)</body>', html).group(1)
    body = body.replace('href="data/', 'href="../../assets/cell-selector/data/')
    return '''---
hide:
  - toc
---

# NKON Cell Selector

''' + f'Compare {count} NKON 21700 offers. Historical snapshot from {date}; check NKON before ordering.' + '''

''' + body + '''

<noscript>This comparison requires JavaScript. <a href="../../assets/cell-selector/data/cells.json">Download the snapshot</a> and <a href="../../assets/cell-selector/data/visual-audit.json">visual audit</a>.</noscript>
'''

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    source = ROOT / 'dist'
    files = [p for p in source.rglob('*') if p.is_file() and p.name != 'index.html'
             and '__pycache__' not in p.parts and not p.name.endswith('.pyc')]
    expected = {p.relative_to(source) for p in files}
    if args.check:
        assert PAGE.read_text(encoding='utf-8') == wiki_page(), 'Wiki page differs; run sync_wiki.py'
        actual = {p.relative_to(DEST) for p in DEST.rglob('*') if p.is_file()}
        mismatches = [str(p.relative_to(source)) for p in files
                      if not (DEST / p.relative_to(source)).is_file()
                      or p.read_bytes() != (DEST / p.relative_to(source)).read_bytes()]
        if actual != expected or mismatches:
            sys.exit('Wiki assets differ; run scripts/sync_wiki.py: ' + ', '.join(mismatches))
    else:
        PAGE.parent.mkdir(parents=True, exist_ok=True)
        PAGE.write_text(wiki_page(), encoding='utf-8')
        DEST.mkdir(parents=True, exist_ok=True)
        for p in files:
            target = DEST / p.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(p, target)
        # Remove only obsolete generated files inside the known asset directory.
        for p in DEST.rglob('*'):
            if p.is_file() and p.relative_to(DEST) not in expected:
                p.unlink()
    print(f'Wiki assets {"verified" if args.check else "synchronized"}: {len(files)} files')

if __name__ == '__main__':
    main()
