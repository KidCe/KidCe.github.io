
## For future Claude

This note owns the community heat/fan routing modification for the Flashforge Creator 5 Pro, consolidated on 2026-08-27. The goal is to decouple the cooling fan from the auxiliary chamber recirculation fan while the chamber heater is active. The source macro is preserved as a referenced attachment, not promoted to a safety-approved configuration.

## Source intent

The community tutorial edits the [gcode_macro M106] section in printer.macro.cfg. For fan index 2 it always runs the chamber recirculation fan but suppresses the cooling fan while the chamber target is above zero. For fan index 3 it suppresses the exhaust fan while the chamber heater is active.

Source: research-sources\Creator-5-Mods\Basic\Allow for Heating Without Cooling\README.md.

## Risks and validation

- The source says the same change can disable the exhaust fan while the chamber heater is active.
- The source does not provide a physical thermal-safety validation matrix.
- Fan indexes, names, macro ownership, and heater names must be checked against the exact target configuration.
- Validate temperature rise, fan failure behavior, emergency stop, chamber limits, and print cancellation before relying on this path.
- Keep this modification separate from camera, Entware, firmware, and open-Klipper experiments.

## Status

C1 community procedure; no physical validation claim. The canonical next step is a supervised, instrumented test on a recoverable printer with an independent temperature measurement and a documented abort procedure.
