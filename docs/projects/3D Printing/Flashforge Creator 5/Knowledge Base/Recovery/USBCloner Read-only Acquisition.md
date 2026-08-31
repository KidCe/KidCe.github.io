
## For future Claude

This note is the canonical no-write BootROM and USBCloner acquisition workflow for the Flashforge Creator 5 Pro evidence package, consolidated on 2026-08-27. It stops at read-only acquisition and validation; it contains no active write profile. Device-specific constants are owned by [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](Device Evidence and Partition Layout.md).

## Required hardware and software

- Windows PC, ESD precautions, and a known data-capable USB cable with the device end removed.
- Access to J29 USB pads and K4/BOOT pads on the target board.
- One matched Ingenic USBCloner version with its complete directory, driver, SPL, U-Boot, DDR definitions, and core executable.
- At least 20 GB free space for readback, hashes, and working copies.
- USBLogView or Device Manager for enumeration evidence.

The original vendor tool package is not redistributed in this Second Brain package. See [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Archive and Copy Manifest](../Sources/Archive and Copy Manifest.md).

## Gate 1 - enumerate only

1. Disconnect mains power before board work.
2. Connect only J29 ground and data pads. Do not connect USB 5 V.
3. Bridge K4/BOOT and power the printer.
4. Record the USB event and compare it with the exact tested identifier in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](Device Evidence and Partition Layout.md).
5. If the event differs or is absent, stop and inspect wiring, ground, driver, and board identity.

## Gate 2 - RAM-only Stage 2

1. Close stale cloner/core processes.
2. Use one matched USBCloner directory; never mix versions.
3. Load the no-write profile copied under Sources/Recovery Kits.
4. Confirm READ-only policies and disabled erase/security options in the UI.
5. Save the complete log.

The tested unit reached Stage 2 and completed no-write policies. Earlier mismatched tooling stopped near 60 percent with STAGE2 NOT READY. That is a tool/compatibility observation, not a reason to enable erase.

## Gate 3 - bounded read-only chunks

Use the copied PowerShell helpers only after the first two gates:

~~~powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\New-C5PReadBatch.ps1 -ClonerRoot 'C:\Tools\cloner-2.5.58.2-windows_alpha' -OutputRoot 'E:\C5P-Recovery' -StartMiB 0 -Count 16 -InstallProfile
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\Test-C5PReadBatch.ps1 -BatchDirectory 'E:\C5P-Recovery\batch-00000000-00F00000'
~~~

Continue only with non-overlapping batches that pass continuity, size, and hash checks. USBCloner may append to an existing READ output, so each generated batch directory must be new and empty.

## Gate 4 - join and freeze

After every batch is independently validated, join the chunks with Join-C5PChunks.ps1. Record image size, GPT, chunk manifest, tool version, profile hash, and final SHA-256 in a dated evidence note. Preserve the original image unchanged and work only from copies.

The local archive's c5p-usb-unbrick-kit\README.md and docs\c5p-deep-unbrick\UNBRICK-GUIDE.md contain the full operator draft. Their credentials, vendor downloads, and unvalidated write material are not repeated here.

## Recovery boundary

This workflow reads and validates data. It does not diagnose every brick, acquire RPMB, prove boot0/boot1 bootability, or authorize writing. For any repair decision continue with [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Offline Repair and Validation](Offline Repair and Validation.md).
