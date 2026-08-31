
## For future Claude

This note owns print-start, layer metadata, adaptive-mesh, and OrcaSlicer routing information for the Flashforge Creator 5 project, consolidated on 2026-08-27. It keeps snippets and repository status in one place so slicer commands are not copied into several guides. The procedures are community-derived unless a separate physical result is recorded.

## Print metadata snippets

The historical guide adds these commands to machine start and layer-change G-code:

~~~gcode
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count]
SET_PRINT_STATS_INFO CURRENT_LAYER={layer_num + 1}
~~~

The exact placement around the slicer's BEFORE_LAYER_CHANGE marker and the printer's supported macro set must be checked before use. The source is the former vault note [Projects/3D Printing/Flashforge Creator 5/Root/How to Install](../../Root/How to Install.md) and the local community guide material.

## Adaptive mesh

The community procedure references firmwareRes/config/test.json, an ff_adaptive_mesh.py module under the Klipper extras directory, macros in printer.macro.cfg, an [ff_adaptive_mesh] section, OrcaSlicer Exclude objects, and a per-print Leveling before print setting. Later reports mention fixes for large start blocks, filenames with spaces, and rolling log handling.

Source boundary:

- C1: the procedure came from the copied Discord/modding material.
- S1: the extracted firmware contains vendor Klipper configuration and custom extras, but that does not validate this community module.
- TBD: exact source revision of ff_adaptive_mesh.py, current compatibility, log parser behavior, and target-printer result.

## OrcaSlicer routes

There are two separate integration concepts:

1. The Flashforge host flow uses a Flashforge-specific API and credentials.
2. Moonraker/ Klipper uses Moonraker APIs and does not automatically retain Flashforge upload/start behavior.

The repository analysis recorded an open OrcaSlicer Flow Calibration PR #14933 with a reported Creator 5 Pro test. It was not merged at the recorded check, so it is a PR/test artifact rather than a released feature.

Source: https://github.com/OrcaSlicer/OrcaSlicer/pull/14933

## Additional slicer notes

- The historical guide suggests disabling Arc Fitting because Klipper converts arcs back to G1; this is a performance/debug hypothesis, not a universal setting.
- For the Creator 5 Pro, the source suggests using M191 S[chamber_temperature] instead of M191 S0; validate chamber semantics before enabling.
- Keep Mainsail monitoring and printer-control ownership distinct from the selected OrcaSlicer host backend.

## Status

No physical print, pause, cancel, filament-fault, or recovery test is claimed by this note. Any test must record firmware, source revision, slicer version, configuration hash, and a supervised acceptance result.
