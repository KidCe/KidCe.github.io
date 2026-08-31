
## For future Claude

[Flashforge Creator 5](Flashforge Creator 5.md) is a curated documentation project for routing, modding, recovery, firmware analysis, and open-stack planning for the Flashforge Creator 5 and Creator 5 Pro. This project note points to the canonical package created on 2026-08-27 and keeps the prior Root notes as historical material. Device-specific evidence is based on one Creator 5 Pro unless a page says otherwise.

The original local Flashforge workspace remains an archive and backup. It is not the current source of truth after this refactor.

## Canonical package

- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/00 Index - Flashforge Creator 5](Knowledge Base/00 Index - Flashforge Creator 5.md) - package entry point and single-point-of-truth map.
- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Architecture/Stock and Target Architecture](Knowledge Base/Architecture/Stock and Target Architecture.md) - stock architecture and staged target architecture.
- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Modding Baseline - Root Loop and Mainsail](Knowledge Base/Guides/Modding Baseline - Root Loop and Mainsail.md) - canonical baseline procedure and safety gates.
- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Recovery Overview](Knowledge Base/Recovery/Recovery Overview.md) - recovery decision tree and escalation boundaries.
- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](Knowledge Base/Recovery/Device Evidence and Partition Layout.md) - measured device evidence and partition facts.
- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Firmware/Open Firmware Migration](Knowledge Base/Firmware/Open Firmware Migration.md) - staged open-firmware roadmap and feasibility boundary.
- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Repository and Revision Registry](Knowledge Base/Sources/Repository and Revision Registry.md) - repository URLs, revisions, and source precedence.

## Key decisions

- Keep the local workspace as an archive; write new canonical knowledge into this project subtree.
- Give every fact one canonical home. Other pages link to that home instead of copying mutable values.
- Separate repository instructions, device observations, community reports, inferences, and open questions.
- Keep write-capable recovery profiles and raw device images outside the private documentation package unless an explicit future recovery case requires them.
- Treat this repository as a curated public snapshot: raw device images, credentials, private keys, vendor binaries, and unreviewed write artifacts stay outside it.

## Recent activity

- 2026-08-27: Refactored the local archive into the linked Second Brain package. Added source manifests, repository provenance, canonical modding guides, recovery evidence, firmware architecture, and copy-safe source attachments.

## Historical material

The older imported notes remain under [Projects/3D Printing/Flashforge Creator 5/Root/README](Root/README.md) and its sibling notes. They are retained for traceability, but they no longer own current procedures. See [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Legacy Vault Notes](Knowledge Base/Sources/Legacy Vault Notes.md).

## AI assistance disclosure

This documentation refactor was produced with substantial assistance from OpenAI Codex. The maintainer directed the structure and decisions and remains responsible for technical review, safety validation, licensing review, and any use on physical hardware.
