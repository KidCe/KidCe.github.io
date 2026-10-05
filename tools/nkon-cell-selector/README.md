# NKON Cell Selector in MkDocs

The existing standalone SVG comparison was imported from Site version 8, source
commit `606fdac1058c005341092ea6dcd3c2a3f2ecf1d1`. This directory contains the actual
source, research seed, identity module, updater, dated audit import and tests.
`dist/` is the maintained static app; `scripts/sync_wiki.py` generates the native
Wiki page and copies assets into `docs/assets/cell-selector/`. No iframe, backend,
ChatGPT runtime, account or chart CDN is required by this tool.

The 1 October 2026 snapshot has 72 **offers**, including 26 in stock, nine
orderable, 37 sold out and 19 discontinued. It is a historical audit. The ZIP
provided again in Google Drive is the same audit, not a new verification.
All JSON files and the 72 screenshot bytes were preserved during migration.

## Setup and verification

From the Wiki repository root, with Python 3 and Node.js installed:

```powershell
python -m pip install -r requirements.txt -r tools/nkon-cell-selector/requirements.txt
Set-Location tools/nkon-cell-selector
npm ci
Set-Location ../..
python -m unittest discover -s tools/nkon-cell-selector/tests -p "test_*.py"
python tools/nkon-cell-selector/scripts/validate_snapshot.py
node tools/nkon-cell-selector/tests/test_variants.cjs
node tools/nkon-cell-selector/tests/test_wiki.cjs
python tools/nkon-cell-selector/scripts/sync_wiki.py
python tools/nkon-cell-selector/scripts/sync_wiki.py --check
python -m mkdocs build --strict
python -m mkdocs serve --dev-addr 127.0.0.1:8000
```

Browser acceptance uses installed Chrome in headless mode. With the preview
running, execute the following from this directory:

```powershell
$env:CELL_SELECTOR_URL = "http://127.0.0.1:8000/tools/cell-selector/"
npm run test:browser
```

The browser suite covers 320, 360, 390 px and desktop, full-page overflow,
details/evidence links, filter/favorite/highlight behavior, quantity boundaries,
effective prices, reload, internal navigation and local requests. The DOM suite
also checks deterministic interrupted animations, identical/missing values,
reduced motion, pack rounding and an Instant Navigation lifecycle. Current Wiki
configuration does not enable Instant Navigation. Its `document$` integration
was tested both with a lifecycle simulation and a separate Material build with
Instant Navigation enabled and a local `site_url`. Set `CELL_SELECTOR_INSTANT_URL`
to that test build to run the additional browser checks. Screenshots are written to the ignored
`test-results/` folder.

## Update the snapshot

Run from the Wiki repository root. First produce a candidate without replacing
the checked-in snapshot:

```powershell
python tools/nkon-cell-selector/dist/data/update_nkon.py --snapshot tools/nkon-cell-selector/dist/data/cells.json --output tools/nkon-cell-selector/dist/data/cells-new.json
python tools/nkon-cell-selector/scripts/validate_snapshot.py --snapshot tools/nkon-cell-selector/dist/data/cells-new.json
```

For saved shop HTML, add `--html-dir saved-pages`. That directory must contain
`manifest.json` mapping every exact category/product URL to its saved HTML file.
See `dist/data/UPDATE.txt`. No partial catalog, Cloudflare response, changed
identity or redirected existing offer may be accepted as a successful refresh.
Live HTTP operation remains incompletely validated because the original attempt
was blocked. Automated failure tests cover these stop conditions.

After reviewing the candidate and running relevant tests:

```powershell
Copy-Item tools/nkon-cell-selector/dist/data/cells-new.json tools/nkon-cell-selector/dist/data/cells.json
Remove-Item tools/nkon-cell-selector/dist/data/cells-new.json
python tools/nkon-cell-selector/scripts/sync_wiki.py
python tools/nkon-cell-selector/scripts/validate_snapshot.py
python -m mkdocs build --strict
```

### Import a complete visual audit

```powershell
python tools/nkon-cell-selector/scripts/import_visual_audit.py --audit-dir path/to/unpacked-audit
python tools/nkon-cell-selector/scripts/validate_snapshot.py
python tools/nkon-cell-selector/scripts/sync_wiki.py
```

Import requires all listing identities, the original snapshot digest and every
screenshot digest. Manufacturer facts remain separate. `audit_snapshot.py`
and `build_snapshot.py` preserve the original dated research replay and seed
rebuild. They replay old evidence and **do not** refresh live stock. Use them
only when intentionally reproducing that historical snapshot.

The seed builder now resolves the identity module from its own data directory
and replays the older index review before applying the visual audit. A regression
test compares the entire reconstructed historical snapshot, including every
manufacturer value and source contradiction, with the preserved imported data.

## Simplified Wiki interface

The radar and compact offer cards are the main interface. Extra specs and source
notes expand on demand. The separate tier-price chart/list is removed, while the
shared quantity still drives effective price, filtering and price-derived specs.
Axes and LUTs are tucked into Advanced display. On narrow screens, Filters and
advanced axis controls open a split view with the live chart above
independently scrolling controls, so adjustments remain visible immediately.

## Integration details

- CSS rules and DOM queries are scoped to `#fpv-nkon-tool`.
- Asset URLs resolve relative to `app.js`, preserving domain subdirectory use.
- A single page initializer observes Material `document$` when available.
  It is idempotent and destroys old page state, dialogs, animation frames,
  resize listeners and timers on page replacement. Child listeners disappear
  when the old markup is restored.
- Quantity, filters, axes, curves, favorites and highlights use versioned
  `fpv-wiki:nkon:*:v1` storage keys. Browser import is session-only.
- Original condition categories and verbatim condition evidence are preserved.
  Shop and datasheet currents, their conditions, unknown values, source conflicts
  and exact offer identities remain distinct.
- Layout responds to the tool container width as well as browser viewport size.
  Spec bar scales remain stable across filters; radar domains blend 70% whole-database bounds with 30% visible-offer bounds
  including favorites. A 50–100% database-reference slider preserves context. Price, price filters and Wh/€ use one effective
  quantity price calculation.

## Publication

The repository automatically deploys pushes to `main`/`master`. The integrated Wiki page was reviewed through a temporary phone preview and
publication was explicitly authorized on 5 October 2026. Future substantive
changes should be previewed again before publishing. The existing repository-level AI assistance disclosure also covers
this migration, implemented with substantial OpenAI Codex assistance.

The scale-reference slider interpolates both lower and upper bounds with the
whole snapshot, using the same effective quantity prices. Missing values are
excluded; empty comparisons retain database bounds. Linear stays the default.
