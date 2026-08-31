
## For future Claude

This note is the canonical baseline for the community root, loop-launcher, and Mainsail path on Flashforge Creator 5 family printers, consolidated on 2026-08-27. It separates the repository's current entry point from the older Discord procedure and does not reproduce the shared root credential. Compatibility and physical success remain device- and firmware-specific.

## Scope and gate

Use this page only after two clean stock boots, a printer-specific backup, confirmed firmware/model identity, and a recovery path. A broken main startup shell can prevent the normal USB update path, so follow [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Recovery Overview](../Recovery/Recovery Overview.md) before any edit.

The root bootstrap in the community source creates a UID 0 account with a shared password. The exact credential is intentionally not stored in the Second Brain. Treat it as compromised, use a trusted LAN only, and replace or remove it immediately if the path is used. The redacted source boundary is documented in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Archive and Copy Manifest](../Sources/Archive and Copy Manifest.md).

## Current repository entry point

The repository README inspected in the local archive says:

~~~text
Download the scripts and folders to the printer into a new folder called tweaks
Run: cd tweaks
Run: chmod +xwr tweaks-c5.sh
Run: ./tweaks-c5.sh
~~~

Source file: research-sources\Creator-5-Scripts\README.md. The local snapshot contains VERSION 2.0.2 in tweaks-c5.sh. Other dated checks in the archive record later repository revisions and different displayed versions, so the authoritative version and feature labels must be taken from the exact repository revision in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Repository and Revision Registry](../Sources/Repository and Revision Registry.md).

## Loop launcher model

The loop script from research-sources\Creator-5-Scripts\scripts\loop\loop.sh:

- scans /usr/prog/scripts/scripts for files ending in .sh;
- launches each script through sh in the background;
- writes launcher output to /tmp/launcher.sh.log;
- writes one output log per script under /tmp;
- intentionally does not wait for background scripts.

The older manual tutorial places loop.sh under /usr/prog/scripts/loop, creates /usr/prog/scripts/scripts, and inserts one launcher line immediately above the firmwareExe start line in /usr/prog/app_startup.sh. That tutorial is historical repository context. Do not install both an old manual copy and a newer repository-managed copy.

## Mainsail and Moonraker baseline

The community enable-msmr.sh source waits for a klippy process, then starts the stock Nginx configuration and moonrakerDaemon. Its source path is research-sources\Creator-5-Scripts\scripts\scripts\enable-msmr.sh. The older guide reports Mainsail on port 80 and Moonraker on port 7125, but those ports are not treated as universal facts here; verify the target configuration after boot.

The Mainsail path is a service overlay on the vendor stack. It does not prove that Flashforge's own UI, firmwareExe, camera integration, or print API has been removed. For print ownership and slicer routing, use [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Print Workflow Adaptive Mesh and OrcaSlicer](Print Workflow Adaptive Mesh and OrcaSlicer.md).

## Safe operational sequence

1. Record model, firmware, board revision, current network address, and a printer-local backup.
2. Copy only the exact source revision selected in the repository registry.
3. Preserve line endings and run shell syntax checks on copied scripts.
4. Install the baseline loop infrastructure first.
5. Check launcher and service logs after reboot.
6. Add Mainsail/Moonraker only after the loop path is stable.
7. Keep heaters, motion, camera, Entware, Nginx tuning, and firmware replacement outside this baseline until separately validated.

## Evidence boundary

- R1: repository README and scripts from the local Creator-5-Scripts snapshot.
- C1: manual root and loop steps from research-sources\Creator-5-Mods.
- S1: local firmware and recovery analysis showing that app_startup.sh is a startup failure boundary.
- P1: no claim of physical success is made by this note.
