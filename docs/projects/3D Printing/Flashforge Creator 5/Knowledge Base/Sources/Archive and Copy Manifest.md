
## For future Claude

This note records how the local Flashforge archive was mapped into the documentation package on 2026-08-27. It is the source-of-truth for copied versus intentionally excluded artifacts. The local archive remains the complete backup; this package is a safe, searchable documentation set rather than a binary firmware mirror.

## Archive root

Source workspace:

~~~text
the local Flashforge archive
~~~

The archive was uncommitted at the time of the refactor. Its README and ARCHIVE-MANIFEST.md mark it as archival. Its main groups are archived-profiles, assets, base-root, c5p-image-kit, c5p-usb-unbrick-kit, docs, recovery-kit, research, research-sources, tmp, and tools.

## Copied into this package

| Package path | Source path | Handling |
| --- | --- | --- |
| Assets/FCC/ | assets\c5p-mainboard-fcc-page11.jpg, assets\c5p-debug-header-candidate.png, and selected research-sources\fcc-c5p images/PDF | local visual evidence |
| Sources/Deep Unbrick/ | docs\c5p-deep-unbrick\ | source documents copied with source metadata |
| Sources/Creator-5-Mods/ | safe Markdown and source files from research-sources\Creator-5-Mods\ | source snapshot; credential-bearing root file omitted |
| Sources/Creator-5-Scripts/ | research-sources\Creator-5-Scripts\ | source snapshot of scripts and README |
| Sources/Recovery Kits/ | safe docs, profiles, and helper scripts from base-root, c5p-image-kit, and c5p-usb-unbrick-kit | source snapshot; vendor downloads and credentials omitted |
| Sources/Firmware 1.9.8/ | selected shell, Klipper config, and custom-module sources from research-sources\flashforge-firmware-1.9.8-extracted\ | static-analysis attachments only |

Copied source Markdown files are marked as source attachments and are not canonical procedures. Canonical notes link to them. See [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Binary Artifact Inventory](Binary Artifact Inventory.md) for the exact fingerprints and archive locations of excluded local binaries.

## Intentionally not copied

- Full MMC0 user-area image: no .img file was present in the archive inventory; the verified image remains at its external recovery location and is device-specific.
- Creator5Pro-factory-1.9.7.tgz and Creator5Pro-factory.tar.xz: vendor firmware packages.
- research-sources\ingenic-* archives and extracted cloner directories: vendor tool packages, binaries, keys, and large redundant snapshots.
- research-sources\flashforge-firmware-1.9.8-extracted\firmwareExe, kernel modules, archives, and other vendor binaries.
- tmp-vmlinux.bin and factory-inspection binary images.
- Password hashes, shared root credentials, private keys, serial/account/network data, and raw logs.
- Recovery write profiles and any device-specific prepared write artifact unless a future case explicitly requires them.

The exclusions are safety, privacy, licensing, and package-size boundaries. They do not delete or alter the archive.

## Copy rule for future updates

Add new external files under Sources only after checking for secrets, device identifiers, licensing constraints, and whether the file is a canonical note or an evidence attachment. Update this manifest and the repository registry together.
