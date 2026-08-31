
# How to Install

## For future Claude

This note contains installation procedures copied from the Flashforge Creator 5 modding Discord. Keep procedures separate from warnings and later discussion findings in [Important Notes](Important Notes.md) and [Chat Knowledge](Chat Knowledge.md).

## Get Root

### Requirements

- USB flash drive. USB 3.1 drives may not work; try USB 2.0 if there are problems.
- Printer connected to a network so that SSH is available.

### Procedure

1. Format the USB drive as `FAT32`.
2. Place `runFirmwareExe.sh` in the root of the drive.
3. Turn the printer off, insert the USB drive, and start the printer.
4. The printer may remain on the Flashforge boot logo. Wait one minute so the script has time to run.
5. Turn the printer off, remove the USB drive, and start the printer again.

The copied instructions claimed that SSH access would then be available with a
shared root credential. That credential is intentionally redacted here because
it was exposed in the source material and must not be reused. Use only a unique
credential set by you on a trusted LAN, and change or remove it immediately
after recovery.

Script reference from the dump: `mods` / **Get Root**.

### Root script from the dump

The updated version creates a writable home directory under `/usr/data`:

```sh
#!/bin/sh
# The original dump appended a shared credential-bearing account entry.
# Do not copy that entry. Create a unique, temporary account only through a
# reviewed recovery procedure, then remove or disable it after use.
exit 0
```

## Add startup scripts safely

### Current repository method

The current [Creator-5-Scripts README](https://github.com/FlashForge-C5-Modding-Group/Creator-5-Scripts#how-to-run-scripts) describes a newer entry point than the older Discord messages:

1. Copy the repository contents to a new folder named tweaks on the printer using SCP, WinSCP, or cURL.
2. Enter the folder with cd tweaks.
3. Make the main script executable with chmod +xwr tweaks-c5.sh.
4. Run ./tweaks-c5.sh.

The current tweaks-c5.sh is version 2.0.1. Its menu marks Enable loop script & Mainsail as the normal entry, Enable Legacy NAN, Add Entware, and Optimize Nginx as experimental, and Update Moonraker as INDEV. Do not interpret the existence of a menu item as confirmation that it is safe for every firmware.

### Historical manual loop installation

The following method is retained from the older Discord discussion. Prefer the current repository method above when the repository instructions and this section differ.

The Discord instructions recommend using the `Creator-5-Scripts` repository and a loop script instead of repeatedly editing the main startup script.

Repository: [FlashForge-C5-Modding-Group/Creator-5-Scripts](https://github.com/FlashForge-C5-Modding-Group/Creator-5-Scripts/)

1. Download and extract the repository, or clone it with Git.
2. Move `scripts/loop/loop.sh` to `/usr/prog/scripts/loop/` on the printer. Create the directory if necessary:

   ```sh
   mkdir /usr/prog/scripts/loop/
   ```

3. Make the loop script executable:

   ```sh
   chmod +xwr /usr/prog/scripts/loop/loop.sh
   ```

4. Add this line directly above `/usr/prog/PROGRAM/software/firmwareExe &` in `/usr/prog/app_startup.sh`:

   ```sh
   /usr/prog/scripts/loop/loop.sh &
   ```

5. Create the script drop-in directory:

   ```sh
   mkdir /usr/prog/scripts/scripts/
   ```

6. Reboot the printer.

After setup, add executable `.sh` files to `/usr/prog/scripts/scripts/` instead of editing `start.sh` or `app_startup.sh` for every feature.

## Enable Entware

The Discord instructions state that Entware requires **Enable legacy NaN MIPS binaries** first. They also recommend setting the printer clock because it has no real-time clock and TLS verification needs a correct time.

Optional time-sync block for `app_startup.sh`:

```sh
# set time
(
    n=0
    while [ "$n" -lt 30 ]; do
        if ping -c1 -W2 time.nist.gov >/dev/null 2>&1; then
            rdate -s time.nist.gov
            break
        fi
        n=$((n + 1))
        sleep 2
    done
) &
```

Install Entware under persistent storage:

```sh
mkdir -p /usr/data/bin/opt
mount --bind /usr/data/bin/opt /opt
wget -O - http://bin.entware.net/mipselsf-k3.4/installer/generic.sh | sh
echo 'export PATH=/opt/bin:/opt/sbin:$PATH' >> /etc/profile
```

To start Entware services on boot, place this below the legacy-NaN `busybox devmem` line in `/usr/prog/app_startup.sh`:

```sh
mount --bind /usr/data/bin/opt /opt
[ -x /opt/etc/init.d/rc.unslung ] && /opt/etc/init.d/rc.unslung start
```

For the current shell:

```sh
export PATH=/opt/bin:/opt/sbin:$PATH
```

## Enable Moonraker and Mainsail

In `/usr/prog/klipper/start.sh`, uncomment these lines near the bottom:

```sh
/usr/prog/nginx/sbin/nginx -p /usr/prog/nginx -c /usr/prog/nginx/conf/nginx.conf
/usr/prog/klipper/moonrakerDaemon start
```

After reboot, the source reports Mainsail on port `80` and Moonraker on port `7125`. To use another Mainsail port, edit `/usr/data/nginx/sites-enabled/mainsail` and change `listen 80;`.

## Update Mainsail

The copied guide requires root access, Entware, and `opkg update`:

```sh
opkg update
opkg install curl
mv /usr/data/mainsail /usr/data/mainsailbackup
mkdir /usr/data/mainsail
cd /usr/data/mainsail
curl -LO https://github.com/mainsail-crew/mainsail/releases/download/v2.18.2/mainsail.zip
unzip mainsail.zip
```

Reboot afterward. The exact release in this old Discord guide may be outdated.

## Update Moonraker

The source procedure requires legacy NaN MIPS support, Entware, a persistent home directory, and an `lmdb` header under `/opt/include`. It recommends either copying the attached `lmdb.h` or downloading the Entware include archive:

```sh
cd /tmp
wget http://bin.entware.net/mipselsf-k3.4/include/include.tar.gz
mkdir -p /opt/include
gunzip -c include.tar.gz | tar x -C /opt/include/
```

Back up the existing installation and install the newer one:

```sh
mv /usr/prog/moonraker/moonraker /usr/prog/moonraker/moonraker-old
mv /usr/prog/moonraker/moonraker-env /usr/prog/moonraker/moonraker-env-old
opkg update
opkg install git git-http
cd /usr/prog/moonraker
git clone https://github.com/Arksine/moonraker.git
/usr/prog/klipper/moonrakerDaemon stop
opkg install python3 python3-pip
python3 -m pip install virtualenv
virtualenv --system-site-packages -p python3 ./moonraker-env
opkg install python3-dev python3-pillow python3-numpy python3-msgpack python3-cryptography python3-cffi python3-yaml python3-requests python3-setuptools libsodium libffi gcc lmdb
ln -sf $(ls /opt/lib/libsodium.so.*[0-9] | head -1) /opt/lib/libsodium.so
. ./moonraker-env/bin/activate
pip install -r /usr/prog/moonraker/moonraker/scripts/moonraker-requirements.txt
LMDB_FORCE_SYSTEM=1 pip install --no-build-isolation lmdb
```

Test it before rebooting:

```sh
python3 /usr/prog/moonraker/moonraker/moonraker/moonraker.py -d /usr/data
```

If it works, add the Entware `PATH` and Python environment to the top of `/usr/prog/klipper/moonrakerDaemon`:

```sh
export PATH=/opt/bin:/opt/sbin:$PATH
PYTHON=/usr/prog/moonraker/moonraker-env/bin/python3
```

Ensure Moonraker is enabled in `/usr/prog/klipper/start.sh` and reboot.

## Mainsail configuration file

The dump references a modified `mainsail.cfg` with conflicting SD-card configuration disabled. Upload it through the Mainsail or Fluidd configuration area and add this near the top of `printer.cfg`:

```ini
[include mainsail.cfg]
```

Reboot after uploading. The original attachment URL is not copied because Discord attachment URLs expire.

## Camera at 720p / 30 FPS

The source procedure requires `start_webcam.sh` in `/usr/prog/mjpg-streamer/`:

```sh
chmod 755 /usr/prog/mjpg-streamer/start_webcam.sh
```

Add this before `/usr/prog/PROGRAM/software/firmwareExe &` in `app_startup.sh`, then reboot:

```sh
# start mjpg-streamer before firmwareExe
sh /usr/prog/mjpg-streamer/start_webcam.sh
sleep 2
```

The source says the UI may still show “Failed to open camera” while the stream is available on port `8080`. Mainsail camera support requires the Mainsail, Moonraker, and camera procedures together.

## Adaptive bed meshing

The source procedure is:

1. In `/usr/data/firmwareRes/config/test.json`, review `keepBedTempPrint` (minutes; `0` disables the heat soak).
2. Place `ff_adaptive_mesh.py` in `/usr/prog/klipper/klippy/extras/`.
3. Add the adaptive mesh macros from the source to `/usr/data/config/printer.macro.cfg`.
4. Add `[ff_adaptive_mesh]` to `printer.cfg`, usually near other imported configuration sections.
5. Enable **Exclude objects** in OrcaSlicer.
6. Enable **Leveling before print** for each print; OrcaSlicer reportedly leaves it disabled by default.

The script must use Unix line endings. Later discussion mentions fixes for large start blocks, filenames with spaces, and rolling-log handling.

## Slicer setup

For layer information in Mainsail:

```gcode
SET_PRINT_STATS_INFO TOTAL_LAYER=[total_layer_count]
```

Add that to the machine start G-code. Immediately after `;BEFORE_LAYER_CHANGE`, add:

```gcode
SET_PRINT_STATS_INFO CURRENT_LAYER={layer_num + 1}
```

To enable slicer time, disable **Disable set remaining print time** in the printer settings. The source also recommends disabling Arc Fitting because Klipper converts it back to `G1`; a later report said this can help avoid “Timer too close!” MCU errors.

For the Creator 5 Pro, the source mentions changing `M191 S0` to `M191 S[chamber_temperature]` to preheat the chamber.

## Fluidd alongside Mainsail

The dump references a `setup_fluidd.sh` script that installs Fluidd under `/usr/data/fluidd` and exposes it on port `81`. It says to place the script in `/usr/data/home/pwned`, make it executable, and run it:

```sh
chmod +x /usr/data/home/pwned/setup_fluidd.sh
/usr/data/home/pwned/setup_fluidd.sh
```

The source also mentions `/usr/data/nginx/sites-available/` for changing which interface uses port `80` or `81`. The original script attachment is not reproduced here; use the repository or attachment source when available.
