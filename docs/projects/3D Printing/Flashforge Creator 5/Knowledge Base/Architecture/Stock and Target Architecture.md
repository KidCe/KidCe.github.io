
## For future Claude

This architecture note separates the stock Creator 5 Pro control graph from the proposed staged open stack, based on local firmware evidence and repository documentation checked on 2026-08-27. The target architecture is a design direction, not proof that a printer can already operate safely without the vendor binary.

## Stock architecture

~~~mermaid
flowchart TD
    Init[Buildroot init] --> App[usr/prog/app_startup.sh]
    App --> Mounts[Persistent mounts and kernel modules]
    App --> Update[USB and firmware update scan]
    App --> FFE[firmwareExe]
    FFE --> KStart[Klipper start.sh]
    KStart --> Bootstrap[cmd_mcu and checkEboard]
    Bootstrap --> Klipper[Vendor Klipper host]
    FFE <-->|private UDS /tmp/uds| Klipper
    Klipper --> Motion[/dev/ttyS2 motion MCU]
    Klipper --> Extruder[/dev/ttyS5 E-board]
    Klipper --> Heater[/dev/ttyS4 heater board]
    Klipper --> Level[/dev/ttyS7 level board]
    FFE --> UI[Framebuffer and touch UI]
    FFE --> Orca[Vendor Orca HTTP API]
    FFE --> Camera[Camera and media]
    FFE --> Cloud[Optional cloud and MQTT]
~~~

The central failure boundary is app_startup.sh: the local factory-rootfs inspection shows that init checks for the file and executes it directly. The file then mixes platform setup, update handling, and application startup. See [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](../Recovery/Device Evidence and Partition Layout.md) for the exact observed permission failure.

## Target architecture

~~~mermaid
flowchart TD
    Init2[Small init or service supervisor] --> Platform[c5p-platform]
    Init2 --> Rescue[c5p-recovery]
    Platform --> Bootstrap2[c5p-mcu-bootstrap]
    Bootstrap2 --> Klipper2[Reviewed C5P Klipper host]
    Klipper2 --> MCUs[Four subordinate MCUs]
    Klipper2 <--> Moonraker2[Moonraker API]
    Moonraker2 <--> Mainsail2[Mainsail web UI]
    Moonraker2 <--> Slicer[OrcaSlicer and clients]
    Init2 --> Camera2[Independent camera service]
    Camera2 --> Mainsail2
    Init2 --> Updater[Signed A/B updater]
    Rescue --> Fallback[Known-good stock or rescue slot]
    Health[Health checks and watchdog] --> Platform
    Health --> Bootstrap2
    Health --> Klipper2
    Health --> Moonraker2
~~~

The target moves operator and file-control functions into Moonraker and Mainsail, keeps pre-Klipper work in a small platform/bootstrap layer, and preserves an explicit recovery path. The safety-critical boundary remains the vendor MCU bootstrap, custom Klipper modules, heater/motion ownership, and fault shutdown.

## File evidence

| Observation | Local path | Interpretation |
| --- | --- | --- |
| Init directly invokes the startup shell | research-sources\factory-inspection\... and C5P-UNBRICK-RUNBOOK.md | Startup file mode is operationally critical |
| Loop and optional services are launched from a directory | research-sources\Creator-5-Scripts\scripts\loop\loop.sh | Mods can be separated from the main startup file after a guarded hook |
| MCU bootstrap precedes Klipper | research-sources\flashforge-firmware-1.9.8-extracted\klipper\start.sh | Bootstrap cannot be replaced by a G-code macro |
| Custom host modules exist | research-sources\flashforge-firmware-1.9.8-extracted\klipper\extras\ | Vendor Klipper is a fork, not a stock install |
| Vendor application owns UI/API/media/update paths | research-sources\flashforge-firmware-1.9.8-extracted\firmwareExe and static-analysis notes | Replacement must be staged and traced |

## Design constraints

- Keep the known vendor kernel and stock Klipper during early experiments.
- Validate with heaters and motion disabled before testing any control path.
- Do not make Moonraker and Flashforge both own the same print files.
- Put boot, update, and recovery changes behind explicit physical and operator gates.
- Keep external clients behind the documented API boundary; do not infer a hybrid Orca protocol.
