
# Important Notes

## For future Claude

These are safety, persistence, and operational caveats extracted from the Discord dump. They are source statements, not independently confirmed recommendations.

## Firmware and startup safety

- Do **not** modify `app_startup.sh` again after installing the loop-script method. The Discord warning says that a syntax or logic error can brick the printer and require Flashforge service.
- Do not modify `start.sh` or `app_startup.sh` beyond the exact setup step required by the installation instructions.
- If either file was changed accidentally, remove or roll back the change safely before rebooting.
- Keep a recovery path through USB firmware rollback before experimenting.

## OTA update risk

Updates may overwrite `/etc/passwd` and other modifications. The dump says that the printer may check for updates over the WAN even in LAN-only mode.

The copied mitigation was to add these entries to `/etc/hosts`:

```text
127.0.0.1 update.flashforge.com
127.0.0.1 update.sz3dp.com
127.0.0.1 update.cn.sz3dp.com
```

This changes network behaviour and should be verified against the current firmware before use.

## Root and credentials

- The copied root account uses UID/GID `0` and is therefore equivalent to root.
- The source includes a username and password. Treat them as compromised because they were shared in Discord; change or remove them when possible.
- If the home directory is changed in `/etc/passwd`, the dump specifically mentions `/usr/data/home/pwned` as the writable alternative to `/root`.

## Persistence caveat

The discussion explored placing a script in `/etc/init.d`, but the answer was that this does not persist because `/etc` is a bind mount to `/usr/prog/etc`, mounted by `/etc/init.d/S09mount_mmc_prog`. A script in that location may be replaced or may not execute at startup.

## Mainsail and service startup

One report said that `enable-msmr.sh` worked when run manually but not at startup. The proposed workaround waited for Klippy before starting Nginx and Moonraker:

```sh
#!/bin/sh
(
    i=0
    while ! pgrep -f "klippy" > /dev/null 2>&1 && [ "$i" -lt 60 ]; do
        sleep 1
        i=$((i + 1))
    done

    if pgrep -f "klippy" > /dev/null 2>&1; then
        /usr/prog/nginx/sbin/nginx \
            -p /usr/prog/nginx \
            -c /usr/prog/nginx/conf/nginx.conf
        /usr/prog/klipper/moonrakerDaemon start
    fi
) &
```

This is a discussion workaround, not a confirmed universal fix.

## Camera and performance limits

- The Discord discussion says the camera hardware maxes out at `1280x720` and `30 FPS`.
- The camera path is software-encoded. Higher resolutions or frame rates may cause low FPS, MCU timeouts, or instability.
- One report saw around `20 FPS`; another described CPU usage reaching roughly `60%` when trying to increase the remote-screen frame rate.
- A setting called `cameraOpen` was mentioned, but the conversation did not establish whether it changes the camera error.
- Cloud camera functionality was not tested by the person who posted the 720p procedure; the procedure was used in LAN-only mode.
- OrcaSlicer may show the webcam in a browser while failing to load `http://<printer-ip>/webcam/?action=stream`. Port configuration and the Orca device UI are possible causes.

## Firmware script and recovery risk

- The C5 script was under heavy rewrite on 2026-08-15. The maintainer explicitly said not to run it until the rewrite was complete.
- The line `busybox devmem 0x00a130d1 8 1` writes to a hardware address. The discussion identifies a wrong offset for a kernel version as a possible boot-loop risk.
- A failure before the USB mount is reached can remove the USB recovery path.
- The script later introduced safe and experimental labels; new scripts were reported as experimental on 2026-08-17.
- The conversation repeatedly states that there is no known and tested recovery method beyond USB. UART output was intermittent, and USBCloner or JTAG were only speculative possibilities.
- One user reported needing a replacement mainboard after the remote-screen experiment.

## SSH host keys

The source reports that Dropbear host keys regenerate because `/etc/dropbear` points into temporary `/run`. The proposed persistence procedure was:

```sh
mv /etc/dropbear/dropbear_ecdsa_host_key /tmp
rm /etc/dropbear
mkdir /etc/dropbear
mv /tmp/dropbear_ecdsa_host_key /etc/dropbear
reboot
```

The source says this works because `/etc` becomes a bind mount to `/usr/prog/etc` after startup. This modifies persistent system state and should be backed up first.

Passwordless SSH using `authorized_keys` was discussed, but the installed Dropbear build was reported not to support it. The maintainer advised against unauthenticated SSH because the printer is not firewall-secured.

## Additional hardware and configuration cautions

- The bed was described as physically about `260 x 260 x 270 mm`, but using more than `256 mm` in Z may cause collisions.
- A suggested slicer build plate was `257 x 260 mm` using the Flashforge C5 build-plate model and texture, but another user warned that the front and tool-holder geometry can still cause collisions.
- The chamber-heater fan modification also disables the exhaust fan while the heater is active. The filter is on the recirculation fan, according to the source.

## Current repository status

Checked on 2026-08-24:

- Creator-5-Scripts main contains tweaks-c5.sh version 2.0.1.
- The script labels Legacy NAN, Entware, and Nginx optimization as experimental; Moonraker is labelled INDEV.
- The repository README now describes copying the repository into tweaks and running ./tweaks-c5.sh. This supersedes the older Discord procedure that manually moved loop.sh and edited app_startup.sh.
- Creator-5-Mods remains the tutorial collection and currently points users to root, the loop script, Mainsail, and the separate Creator-5-Scripts repository.

## Remote Screen repository warnings

The current Remote Screen installation guide confirms that it modifies internal printer files and has only been tested on a Creator 5 Pro running firmware 1.9.6. It requires backups before editing app_startup.sh or the Fluidd nginx configuration, syntax validation with sh -n, and a full post-reboot health check.

Its services use ports 8090 and 8091; port 8091 can generate touchscreen events. Do not expose either port directly to the public Internet.
