
## For future Claude

This note owns the Entware, Moonraker-update, and Mainsail-update material for the Flashforge Creator 5 project, consolidated on 2026-08-27. These procedures are historical community material and source snapshots, not an approved current installer. The supported baseline remains the guarded path in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Modding Baseline - Root Loop and Mainsail](Modding Baseline - Root Loop and Mainsail.md).

## Entware

The community flow binds persistent storage at /usr/data/bin/opt to /opt, installs the MIPS Entware environment, and adds /opt/bin and /opt/sbin to PATH. It states that legacy NaN MIPS support must be enabled first and that the printer clock matters for TLS verification.

Source files:

- research-sources\Creator-5-Mods\Intermediate\Enable Legacy NaN\README.md
- research-sources\Creator-5-Mods\Intermediate\Add Entware Package Manager\README.md
- research-sources\Creator-5-Scripts\scripts\scripts\nan-binary.sh
- research-sources\Creator-5-Scripts\scripts\scripts\entware.sh

The nan-binary.sh source writes a hardware register with busybox devmem. The offset is firmware- and kernel-specific and is not a universal safe command. Treat this feature as experimental and require a device-specific rollback plan.

## Mainsail update

The old guide moves /usr/data/mainsail to a backup, downloads a fixed Mainsail v2.18.2 ZIP, extracts it, and reboots. That URL is kept only as historical evidence from:

- research-sources\Creator-5-Mods\Intermediate\Update Mainsail\README.md
- research-sources\Creator-5-Scripts\tweaks-c5.sh

Do not treat v2.18.2 as the current release. Use a current, pinned upstream revision only after a compatible local test and a backup.

## Moonraker update

The old procedure installs build dependencies, copies or downloads an LMDB header, creates a Python virtual environment, clones Moonraker, and changes moonrakerDaemon. A community report says that a Moonraker update initially disconnected Mainsail and that reverting restored service. The source itself later marks Moonraker update INDEV.

Source files:

- research-sources\Creator-5-Mods\Hard\Update Moonraker\README.md
- research-sources\Creator-5-Mods\Hard\Update Moonraker\lmdb.h
- research-sources\Creator-5-Scripts\tweaks-c5.sh

No current Moonraker update recipe is canonical here. The safe status is: preserve the stock copy, test the new process manually, validate logs and API health, and only then consider persistence.

## Evidence boundary

- C1: copied community recipes and Discord reports.
- R1: current source snapshot menu labels and scripts.
- P1: no physical validation claimed.
