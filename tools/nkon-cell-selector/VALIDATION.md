# Local integration validation

Validated on 5 October 2026 in Windows, Python 3.12 and headless Google Chrome.
These are browser and host checks, not physical battery tests or a new NKON audit.

## Source and publication state

- Wiki source: `KidCe/KidCe.github.io`, commit
  `27cbd83383cea6fa69bcedddddd840ff4ba3da85`.
- Cell Selector: actual source repository, Site version 8, commit
  `606fdac1058c005341092ea6dcd3c2a3f2ecf1d1`.
- Local working branch: `integrate-nkon-cell-selector`.
- The user reviewed the temporary phone preview and authorized publication
  on 5 October 2026. `main`/`master` pushes trigger the existing deployment
  workflow; no separate hosting or deployment workflow was added.

## Preserved behavior

All filtered offers appear in the SVG radar, with favorites added independently
of filters. Stock includes unknown, and the six original condition categories
retain their source explanations. The original numeric ranges, protection and
discharge-current basis filters, sorting, CSV export, session JSON import,
offer details, model-family navigation and source links remain available.

One shared cell quantity drives tier price, price filter, radar price and Wh/€.
Radar axes blend 70% whole-database bounds and 30% visible offers including
favorites by default. A 50–100% database-reference slider preserves context; identical values get padded
domains and missing values produce gaps. The original 33-knot linear/low/middle/
high LUTs, 700 ms cosine ease-in-out, interrupted animation continuity, reduced
motion, strong highlight colors and glow remain. Spec bars have consistent colors
and shared scales across filtering. The separate tier-price chart and list were removed; quantity-aware pricing remains.

## Integration changes

- Native `tools/cell-selector.md`, linked under Web Tools. No iframe or old Site
  runtime requests. CSS selectors and queries are scoped to `#fpv-nkon-tool`.
- English interface, original evidence and technical notes preserved verbatim.
- Relative asset resolution supports the tested `/site/` URL prefix.
- Compact offer cards with four colored core specs and expandable additional specs.
- Mobile Filters and Axes open a split view: the live radar remains visible above
  independently scrolling controls. Larger slider handles improve touch operation.
- Introductory text and source tools are condensed; provenance stays in Sources
  and offer details. No separate lower tier-price visualization.
- Versioned Wiki storage for favorites, highlights, quantity, ranges, selected
  axes, LUTs and filter settings. Storage does not migrate between domains.
- Idempotent Material lifecycle, with abortable fetch/resize listener and cleanup
  of dialogs, animation frames, timers and download URLs. No chart instances or
  chart library were added; comparison remains SVG.
- Maintained source/pipeline under `tools/nkon-cell-selector`; generated page and
  assets checked by `sync_wiki.py --check`.
- Historical rebuild fixed: module import path and index-before-visual replay
  preserve all reviewed shop values and contradictions.
- Existing project-level AI assistance disclosure retained; migration performed
  with substantial OpenAI Codex implementation and documentation assistance.

## Checks passed

- 13 Python tests: exact identities, three Tenpower 50ME listings, condition/
  stock parsing, quantity tiers, manufacturer preservation, all screenshot
  digests, Cloudflare/403/429/redirect/incomplete-catalog failure preservation,
  and full historical seed reconstruction.
- Both JavaScript suites: all variants, stock filters, exact offer favorites,
  sibling details, duplicate-URL rejection, quantities around tier boundaries,
  pack rounding, effective price filter/Wh/€, missing and identical domains,
  interrupted domain and geometry continuity, reduced motion, empty results,
  highlight styling, persistence and page lifecycle.
- Browser widths 320, 360, 390 and 1440 px: no horizontal page overflow with
  filters, axes, cards/specs and offer dialogs. Favorites/highlights, curve
  selection, three exact 50ME offers, reload and saved state verified. Real slider
  drags update the visible chart; scrolling controls keeps the radar in place.
  Escape restores the chart and controls to the page without duplicate SVGs.
- Browser quantity boundaries for all Molicel P50B tiers; displayed effective
  price and price filtering agree. Offer screenshot and pipeline downloads
  return HTTP 200 beneath a URL prefix.
- Direct page entry, reload, internal Wiki link and browser history tested.
- Separate actual Material Instant Navigation build: two round trips without
  document reload, settings restored, exactly one snapshot fetch per mount.
- Fresh anonymous browser contexts: no login required, no old Site requests,
  no JavaScript errors from the integration.
- `cells.json`, `visual-audit.json`, `visual-changes.json` and all 72 screenshots
  are byte-identical to the imported source. Complete audit ZIP import verified
  source and screenshot hashes in an isolated copy; final replay matches all
  snapshot fields.
- Every CSS selector is scoped. Snapshot validation, generated-asset/page
  synchronization and `mkdocs build --strict` pass.

## Remaining limits

Prices and stock are the dated 1 October 2026 snapshot. No new live shop audit
was performed. The original HTTP updater was blocked by Cloudflare; its full
live fetch remains unvalidated, although parser and stop conditions are tested.
Reclaimed/mixed cells are not guaranteed to meet new-cell datasheet performance.
Original shop contradictions and missing values remain visible.

Current production configuration leaves Instant Navigation disabled. The
separate enabled build was only a local acceptance test. Mobile checks use
browser viewport emulation, not physical phones. Automated snapshot regression
tests encode the historical audit and need deliberate review when replacing
that audit with a new dated dataset.

The scale-reference slider interpolates both lower and upper bounds with the
whole snapshot, using the same effective quantity prices. Missing values are
excluded; empty comparisons retain database bounds. Linear stays the default.
