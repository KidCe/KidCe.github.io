
## For future Claude

This note is the canonical recovery decision tree for the Flashforge Creator 5 Pro knowledge base, consolidated on 2026-08-27. It defines the order from physical inspection through read-only acquisition, diagnosis, and any separately reviewed repair. It does not authorize a write and does not generalize one board's measurements to other printers.

## Recovery sequence

~~~mermaid
flowchart TD
    Stop[Printer unstable or bricked] --> Safety[Power, ESD, mains and cable safety]
    Safety --> Identify[Record model, firmware, board and symptoms]
    Identify --> Booted{Does Linux boot?}
    Booted -->|yes| ADB[Temporary J29 ADB or SSH maintenance]
    Booted -->|no| Bootrom[K4/BOOT and J29 BootROM path]
    ADB --> Backup[Read and hash device-owned backups]
    Bootrom --> Enumerate[USB enumeration only]
    Enumerate --> Stage2[RAM-only Stage 2, no-write]
    Stage2 --> Read[Bounded MMC0 read-only acquisition]
    Read --> Verify[Continuity, size, GPT and hash validation]
    Backup --> Diagnose[Evidence-based diagnosis]
    Verify --> Diagnose
    Diagnose --> Narrow{Is one narrow repair proven?}
    Narrow -->|no| Review[Stop at immutable evidence and review]
    Narrow -->|yes| Prepare[Prepare a separate minimal repair image]
    Prepare --> Review2[Independent review of offset, size, mode and hash]
    Review2 --> Write[Case-specific write profile]
    Write --> Readback[Exact-range read-back and byte comparison]
    Readback --> Boot[Normal boot with heaters and motion disabled]
~~~

## Non-negotiable boundaries

- Disconnect mains power before board access or soldering.
- Never connect USB power from the adapter or use a USB-A-to-USB-A cable.
- Treat every USBCloner profile as executable hardware instructions.
- Default to no erase, no eFuse/security operation, no GPP/RPMB/boot-region write, and no whole-device write.
- Do not assume a USBCloner progress bar proves a complete device image.
- Do not run repairing fsck on the only copy of a filesystem.
- Do not reuse another printer's geometry, offsets, DDR profile, calibration, credentials, or image.
- After any repair, verify UI, storage, network, temperatures, MCU connectivity, and emergency stop before motion or heat.

## Route selection

- If Linux boots, use [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Temporary ADB Access](Temporary ADB Access.md) only as a temporary, physically connected maintenance path.
- If Linux does not boot but K4/J29 access is available, use [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/USBCloner Read-only Acquisition](USBCloner Read-only Acquisition.md).
- If the failure is a startup file or mode problem, use [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Offline Repair and Validation](Offline Repair and Validation.md) after the device-specific evidence is complete.
- If neither path is available, prefer the manufacturer service/recovery route over blind UART, JTAG, or bootloader experiments.

## Evidence status

The working C5P archive contains a physically confirmed BootROM read-only path, a complete MMC0 user-area readback, and a temporary post-boot ADB path for one unit. See [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](Device Evidence and Partition Layout.md) for the owned evidence and its limits.
