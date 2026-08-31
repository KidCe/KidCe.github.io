
## For future Claude

This note defines the information-ownership rules for the Flashforge Creator 5 knowledge base, created on 2026-08-27. It exists to stop the same port, offset, script status, or safety claim from drifting in several notes. A canonical note owns a fact; all other pages provide context and link to it.

## Ownership rules

| Fact class | Owner | Allowed elsewhere |
| --- | --- | --- |
| Project status and archive relationship | [Projects/3D Printing/Flashforge Creator 5/Flashforge Creator 5](../../Flashforge Creator 5.md) | Short link only |
| Measured board, USB, eMMC, GPT, file metadata, and device hashes | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](../Recovery/Device Evidence and Partition Layout.md) | Evidence label and link |
| Recovery safety gates | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Recovery Overview](../Recovery/Recovery Overview.md) | Warnings plus link |
| Read-only acquisition details | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/USBCloner Read-only Acquisition](../Recovery/USBCloner Read-only Acquisition.md) | Gate reference |
| Repair design and read-back requirements | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Offline Repair and Validation](../Recovery/Offline Repair and Validation.md) | Link only |
| Stock root/loop/Mainsail procedure | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Modding Baseline - Root Loop and Mainsail](../Guides/Modding Baseline - Root Loop and Mainsail.md) | Link only |
| Feature-specific mod instructions and status | The relevant page under [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Optional Mod Matrix](../Guides/Optional Mod Matrix.md) | Link only |
| Stock service graph and future architecture | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Architecture/Stock and Target Architecture](Stock and Target Architecture.md) | Link only |
| Vendor firmware structure and custom Klipper files | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Firmware/Vendor Firmware and Klipper](../Firmware/Vendor Firmware and Klipper.md) | Link and evidence label |
| Open-firmware sequencing and exit criteria | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Firmware/Open Firmware Migration](../Firmware/Open Firmware Migration.md) | Link only |
| Repository URL, revision, branch, and inspection date | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Repository and Revision Registry](../Sources/Repository and Revision Registry.md) | Use the registry entry |
| Local copied-file status and exclusions | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Archive and Copy Manifest](../Sources/Archive and Copy Manifest.md) | Use the manifest |

## Update protocol

1. Search the package for the fact and identify the owning note.
2. Update the owner with an as-of date and the source path or URL.
3. Replace duplicate values in non-owner pages with a link and short context.
4. Record a dated change in the project note or the dev log when the change is consequential.
5. Re-run link, frontmatter, and freshness checks.

## Source precedence

For a conflict, use this order:

1. A fresh physical observation on the target printer, recorded as P1.
2. A read-only local artifact from that printer, recorded as S1.
3. The exact repository revision recorded in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Repository and Revision Registry](../Sources/Repository and Revision Registry.md).
4. A dated community report, recorded as C1.
5. An inference, recorded as I1, which remains open until tested.

Repository instructions do not override device-specific safety evidence. A repository menu item is not proof of compatibility or physical success.

## What not to duplicate

- Do not copy the measured eMMC size into mod guides.
- Do not copy old Mainsail or Moonraker release URLs into current setup instructions.
- Do not copy credentials or password hashes from community root scripts.
- Do not call a full eMMC image what is only an MMC0 user-area image.
- Do not present host-side script tests as printer tests.
- Do not treat a source attachment under Sources as an approved procedure.
