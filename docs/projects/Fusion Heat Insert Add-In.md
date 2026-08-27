
## For future Claude

Fusion Heat Insert Add-In is an active personal open-source project as of 2026-08-22. It adds guided heat-insert and screw-connection creation to Fusion 360 for 3D-printed parts; the linked GitHub repository is the source of truth for implementation details and current status.

# Fusion Heat Insert Add-In

## Overview

- Purpose: create paired heat-insert pockets, screw-clearance holes, and screw-head pockets from selected locations in a Fusion 360 design.
- User focus: reduce repetitive face, point, profile, and clearance selections when preparing printable parts.
- Repository: https://github.com/KidCe/FusionHeatInsertAddIn

## Current capabilities

- Managed create/edit workflow for connection sets.
- Hardware profiles for metric heat inserts and screws, including insert-hole tolerances.
- Preview mode and user-facing validation messages.
- Optional automatic Screw Entry Face suggestion from the selected sketch.
- Optional opposing Insert Entry Face detection with configurable gap tolerance under active development.
- Repository-based installation that copies only Fusion runtime files into the Fusion Add-ins folder.

## Current direction

Recent work focuses on reliable SketchPoint/Face selection handling and making opposing-face detection follow the actual direction into the screw-side body. The project remains active; Fusion-side testing is still required for geometry cases that cannot be reproduced by the local test suite.

## Current repository state (as of 2026-08-22)

- Development version: `0.5.16`.
- Branch: `feature/auto-detect-insert-face`.
- Latest pushed commit: `124e693` (`docs: document in-app reload workflow`).
- The latest README documents the normal development loop: run `Install Fusion Add-in.cmd`, then use `Solid > Create > Reload Threaded Insert Connections` in Fusion.
- The in-app reload reads the installed Fusion Add-ins copy. It does not pull from GitHub, watch the repository, reload other add-ins, or recover from startup/manifest failures; Fusion's native Scripts and Add-Ins dialog remains the fallback for those cases.
- Local validation completed on 2026-08-22: 43 `unittest` tests passed and the Add-In Python modules compiled successfully. Real Fusion geometry behavior still requires visual verification in Fusion 360.

The GitHub repository is the implementation source of truth; this project note is a dated status summary intended to remain suitable for later Obsidian-to-MkDocs export.

## Recent activity

- 2026-08-22: documented the project and captured the current selection and automatic-face-detection work in Dev Logs/2026-08-22 - Fusion Heat Insert Add-In.
- 2026-08-22: pushed commit `124e693` to the `feature/auto-detect-insert-face` branch and updated the README with the install-then-reload workflow and its limitations.

## Links

- GitHub repository: https://github.com/KidCe/FusionHeatInsertAddIn
