
# Repository Check

## For future Claude

This note records a live comparison between the Discord-derived notes and the linked GitHub repositories. Repository content is the current primary source for repository behaviour; Discord statements remain useful as historical reports and failure observations.

## Results

- [Creator-5-Scripts](https://github.com/FlashForge-C5-Modding-Group/Creator-5-Scripts): main contains tweaks-c5.sh v2.0.1. The README uses a tweaks folder and ./tweaks-c5.sh. The script labels several features experimental or INDEV. Current install path added to How to Install; old manual loop method marked historical.
- [Creator-5-Mods](https://github.com/FlashForge-C5-Modding-Group/Creator-5-Mods): tutorial collection. Current README points to root, Loop Script, Mainsail, and the separate Scripts repository. Repository split and prerequisites clarified.
- [Creator 5 Pro Remote Screen](https://github.com/xenupy/creator5pro-remote-screen): functional/tested claim on Creator 5 Pro firmware 1.9.6. Uses Fluidd, /dev/fb0, ports 8090/8091, and approximately 1 FPS. Current install locations, backups, validation, ports, and security warnings added.
- [OrcaSlicer PR #14933](https://github.com/OrcaSlicer/OrcaSlicer/pull/14933): still open. Adds FlashForge host flow calibration and reports a Creator 5 Pro test. Described as an unmerged PR/test artifact, not a released feature.
- [Moonraker](https://github.com/Arksine/moonraker): active upstream Python 3 API server for Klipper; client is separate. The old pinned update procedure is historical only.
- [Mainsail](https://github.com/mainsail-crew/mainsail): active upstream web interface project. The old Mainsail v2.18.2 download URL is stale as a current-release reference.

## Important correction

The older Discord instructions manually changed app_startup.sh to launch a loop script. The current Creator-5-Scripts repository provides a script-driven entry point and explicitly labels several functions experimental or in development. For a fresh install, follow the repository README and treat the old Discord procedure as historical context.

## Remote Screen correction

The current repository documents framebuffer capture, JPEG conversion, MJPEG streaming, Fluidd integration, coordinate mapping, Goodix touch injection, automatic startup, logging, backups, syntax validation, and recovery steps. It also documents a 1 FPS design limit and warns against exposing ports 8090/8091 to the public Internet.
