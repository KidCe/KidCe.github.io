
## For future Claude

This note is the staged roadmap for moving the Flashforge Creator 5 Pro toward a debuggable Linux/Klipper/Moonraker/Mainsail stack, based on local evidence and upstream documentation checked on 2026-08-27. It is a feasibility foundation, not a claim that stock-free heaters, motion, printing, MCU updates, or fault handling are already safe.

## Desired ownership model

- A reproducible or at least versioned Linux image.
- Separate platform, MCU bootstrap, Klipper, Moonraker, camera, update, and recovery services.
- Klipper as the sole printer-control authority.
- Moonraker as the documented API and integration layer.
- Mainsail as the primary web UI.
- Macros for operator workflows; modules only for protocol/state that macros cannot safely provide.
- No mandatory Flashforge cloud path in the safety-critical loop.

## Phases and exit criteria

| Phase | Goal | Exit criterion |
| --- | --- | --- |
| 0 | Restore stock and baseline | Two clean boots, backups, recovery path, no-motion/no-heat checks |
| 1 | Observe and split services | Process, UDS, MCU, file, and update responsibilities documented |
| 2 | Start vendor Klipper without firmwareExe | Heater and motion disabled; MCU and fault behavior understood |
| 3 | Move print/API/UI functions | Moonraker owns files and operations; supervised test prints pass |
| 4 | Port vendor Klipper changes | Every custom module and core diff has a reviewed reason |
| 5 | Rebuild userspace | Versioned rootfs, persistent data, logs, rollback, and license manifest |
| 6 | Kernel/BSP/bootloader work | Independent recovery and reproducible boot on each supported board |

## Macro boundary

Macros can orchestrate print start/end, pause/resume, fan logic, tool parking, filament response, adaptive mesh, and metadata when the underlying hardware commands already exist. They cannot replace kernel modules, pre-Klipper MCU bootstrap, custom serial protocols, early recovery, or timing-critical safety feedback.

## Highest-value next experiments

1. Capture a stock runtime snapshot: processes, ports, mounts, modules, file descriptors, and Klipper state.
2. Trace the private UDS during upload, start, pause, tool change, cancel, and fault events.
3. Correlate cmd_mcu, checkEboard, bootSerial functions, and actual UART traffic.
4. Attempt a heater-disabled manual vendor-Klipper start without firmwareExe.
5. Compare the vendor Klipper tree against an exact upstream baseline.
6. Build protocol fixtures and host-only tests before physical motion or heat.

## Showstoppers

- Unknown MCU bootstrap or protocol ownership.
- Heater/motor enable outside the reviewed Klipper path.
- Different silent board revisions.
- No independent early recovery.
- Vendor kernel modules with unclear source/license boundary.
- MIPS resource limits for Python, web, and camera services.
- Stock and Moonraker competing for file/history ownership.

## Current conclusion

A staged open userspace is technically plausible because the printer already exposes Linux, Klipper, separate MCUs, and a recoverable storage layout. The hardest boundary is firmwareExe, MCU bootstrap, vendor Klipper extensions, and physical safety. The next correct step is observation and heater-disabled validation, not a replacement image.
