
## For future Claude

This note is the navigation and source-of-truth map for the curated Flashforge Creator 5 and Creator 5 Pro documentation package, created on 2026-08-27. It explains where each class of fact belongs and prevents procedures, measurements, and repository statuses from being duplicated across notes. Hardware findings are primarily one-device observations from a Creator 5 Pro.

## Read this first

1. Read [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Recovery Overview](Recovery/Recovery Overview.md) before any hardware or storage action.
2. Read [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Modding Baseline - Root Loop and Mainsail](Guides/Modding Baseline - Root Loop and Mainsail.md) before any software modification.
3. Use [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Repository and Revision Registry](Sources/Repository and Revision Registry.md) to resolve repository precedence and inspected revisions.
4. Use [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Archive and Copy Manifest](Sources/Archive and Copy Manifest.md) to find copied files and understand exclusions. Use [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Binary Artifact Inventory](Sources/Binary Artifact Inventory.md) for excluded local binaries.

## Single points of truth

| Information | Canonical note | Other pages must do |
| --- | --- | --- |
| Project status and archive relationship | [Projects/3D Printing/Flashforge Creator 5/Flashforge Creator 5](../Flashforge Creator 5.md) | Link here; do not recreate project status |
| File ownership and duplication rules | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Architecture/Single Points of Truth](Architecture/Single Points of Truth.md) | Follow its ownership table |
| Stock and target architecture | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Architecture/Stock and Target Architecture](Architecture/Stock and Target Architecture.md) | Link instead of copying service graphs |
| Root, loop, and Mainsail baseline | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Modding Baseline - Root Loop and Mainsail](Guides/Modding Baseline - Root Loop and Mainsail.md) | Treat as the only baseline procedure |
| Optional mod status | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Optional Mod Matrix](Guides/Optional Mod Matrix.md) | Link to detailed feature pages |
| Camera and remote screen | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Camera and Remote Screen](Guides/Camera and Remote Screen.md) | Do not claim a camera or touch test outside that note |
| Entware and Moonraker updates | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Entware Moonraker and Mainsail Updates](Guides/Entware Moonraker and Mainsail Updates.md) | Treat historical update recipes as unapproved |
| Print workflow and adaptive mesh | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Print Workflow Adaptive Mesh and OrcaSlicer](Guides/Print Workflow Adaptive Mesh and OrcaSlicer.md) | Keep slicer snippets and status there |
| Heating and fan routing | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Heat and Fan Routing](Guides/Heat and Fan Routing.md) | Do not copy an unvalidated macro elsewhere |
| SSH host-key persistence | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/SSH Host Key Persistence](Guides/SSH Host Key Persistence.md) | Link the procedure and its warning |
| Recovery decisions and gates | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Recovery Overview](Recovery/Recovery Overview.md) | Never shorten the gate sequence |
| Measured device facts and partition layout | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](Recovery/Device Evidence and Partition Layout.md) | Link exact values; do not generalize them |
| Read-only USBCloner acquisition | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/USBCloner Read-only Acquisition](Recovery/USBCloner Read-only Acquisition.md) | Use only device-derived boundaries |
| Offline repair and read-back | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Offline Repair and Validation](Recovery/Offline Repair and Validation.md) | Treat any write plan as case-specific |
| Temporary ADB maintenance path | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Temporary ADB Access](Recovery/Temporary ADB Access.md) | Never turn it into default boot behavior |
| Vendor firmware and Klipper surface | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Firmware/Vendor Firmware and Klipper](Firmware/Vendor Firmware and Klipper.md) | Keep static analysis separate from physical proof |
| Open-firmware plan | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Firmware/Open Firmware Migration](Firmware/Open Firmware Migration.md) | Treat all stock-free operation as unvalidated until tested |
| URLs, revisions, and source precedence | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Repository and Revision Registry](Sources/Repository and Revision Registry.md) | Add new revisions there first |
| Copied files, omitted blobs, and archive mapping | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Archive and Copy Manifest](Sources/Archive and Copy Manifest.md) | Preserve the copy boundary |
| Excluded binary fingerprints and locations | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Binary Artifact Inventory](Sources/Binary Artifact Inventory.md) | Do not infer that omitted binaries are missing from the archive |

## Package layout

~~~text
Knowledge Base/
├── 00 Index - Flashforge Creator 5.md
├── Architecture/
├── Guides/
├── Recovery/
├── Firmware/
├── Sources/
│   ├── Deep Unbrick/
│   ├── Creator-5-Mods/
│   ├── Creator-5-Scripts/
│   ├── Recovery Kits/
│   └── Firmware 1.9.8/
└── Assets/FCC/
~~~

The canonical notes are authored summaries. Files under Sources are provenance attachments or snapshots and are not authoritative merely because they are copied into the package.

## Evidence labels

- **P1 - physically confirmed:** executed or measured on one Creator 5 Pro.
- **S1 - statically confirmed:** supported by a local image, script, configuration, ELF, or symbol analysis.
- **R1 - repository source:** stated by a named repository at a recorded revision.
- **C1 - community report:** Discord or community statement not independently confirmed.
- **I1 - inference:** derived technical conclusion requiring a confirming test.
- **TBD:** not sufficiently investigated.

## Archive boundary

The source workspace is the local Flashforge archive. Its local README and the
new ARCHIVE-MANIFEST.md mark it as the backup. Raw device images, vendor
binaries, credentials, private keys, and unverified write artifacts are not
copied into this package.
