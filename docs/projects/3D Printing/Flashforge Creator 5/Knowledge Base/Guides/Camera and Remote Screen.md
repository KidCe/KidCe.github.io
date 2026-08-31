
## For future Claude

This note owns camera and remote-screen information for the Flashforge Creator 5 project, consolidated on 2026-08-27. It combines a community 720p streamer recipe with the separate Creator 5 Pro remote-screen repository report. The camera and touch paths are not claimed as validated on the target printer during this refactor.

## Camera path

The community source places start_webcam.sh under the printer's MJPEG streamer directory and launches it through camera.sh in the loop script directory. The source script waits for /dev/video0 and starts mjpg_streamer at 1280x720 and 30 FPS on HTTP port 8080.

Source files:

- research-sources\Creator-5-Mods\Basic\Unlock camera to 720p\README.md
- research-sources\Creator-5-Mods\Basic\Unlock camera to 720p\start_webcam.sh
- research-sources\Creator-5-Scripts\scripts\scripts\camera.sh

The original UI may still report a camera error because firmwareExe expects its own camera integration. A browser stream is therefore not proof of vendor UI integration, cloud compatibility, or acceptable CPU load.

## Remote screen path

The repository check recorded a Creator 5 Pro Remote Screen project tested by its author on firmware 1.9.6. It captures /dev/fb0, converts frames to JPEG/MJPEG, integrates with Fluidd, and injects Goodix touchscreen events. The reported design is approximately 1 FPS, with MJPEG on port 8090 and touch input on port 8091.

Source: https://github.com/xenupy/creator5pro-remote-screen/tree/77ad1268869c8d2a1f7f25d810dd31e976b2ee33

Port 8091 can generate touchscreen events. Both ports must remain on a trusted LAN or behind an authenticated local tunnel; they must not be exposed to the public Internet. The remote-screen repository is not copied into the archive because no local snapshot was found.

## Performance and safety boundary

- C1: community reports mention around 20 FPS in one setup and high CPU use during higher-rate experiments.
- R1: the remote-screen repository reports approximately 1 FPS on the tested path.
- TBD: target-printer camera sensor, stable FPS, thermal impact, and cloud behavior.
- TBD: whether the target's firmware and board revision match the remote-screen test.
- Do not combine camera, touch injection, and firmwareExe changes in one first experiment.
