
## For future Claude

This note documents the temporary, owner-initiated root ADB maintenance path over J29 after a normal Creator 5 Pro Linux boot, confirmed on 2026-08-27. It is not a BootROM recovery path and must not be made persistent by default because the tested adbd exposed an unauthenticated root shell to the physically connected host.

## Confirmed behavior

- With K4 open, normal boot did not enumerate J29 as ADB.
- The vendor kernel exposes a write-only OTG mode switch at /sys/devices/platform/apb/10000000.otg_phy/sw_switch_hsotg.
- Accepted inputs found by offline analysis are device, host, and none.
- Linking the existing FunctionFS ADB function, starting one adbd, and running the vendor USB helper produced a temporary ADB device.
- The shell returned uid=0(root) gid=0(root) groups=0(root).

Source snapshot: [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Deep Unbrick/ADB-RECOVERY-ACCESS](../Sources/Deep Unbrick/ADB-RECOVERY-ACCESS.md).

## Preconditions

- Linux has completed a normal boot.
- Root SSH or an equivalent local shell already exists.
- K4 is open and J29 wiring is already verified.
- The connected host is trusted and remains under physical control.

## Temporary activation

Use the active gadget paths discovered on the target. The tested sequence was:

~~~sh
SW=/sys/devices/platform/apb/10000000.otg_phy/sw_switch_hsotg
G=/sys/kernel/config/usb_gadget/adb_demo

printf 'device\n' > "$SW"
sleep 2
cd "$G"
test -L configs/b.1/ffs.adb || ln -s ../../functions/ffs.adb configs/b.1/ffs.adb

killall adbserver.sh 2>/dev/null
killall adbd 2>/dev/null
/usr/bin/adbd >/tmp/adbd-device-test.log 2>&1 &
sleep 2
/sbin/usb_adb_enable.sh
~~~

Do not hard-code b.1 for a universal tool. The vendor script may use another configuration name; discover and inspect it first. A short USB disconnect during UDC rebind is expected.

From Windows, use the matched ADB executable and verify:

~~~powershell
& $c5pAdb wait-for-device shell
~~~

Inside the shell:

~~~sh
id
pwd
uname -a
~~~

## Cleanup

Preferred cleanup is a normal reboot:

~~~sh
sync
reboot
~~~

Manual teardown is only appropriate after confirming the active gadget name:

~~~sh
echo '' > "$G/UDC"
killall adbserver.sh 2>/dev/null
killall adbd 2>/dev/null
rm -f "$G/configs/b.1/ffs.adb"
printf 'none\n' > "$SW"
~~~

This path cannot repair SPL/U-Boot, kernel, early userspace, or an unreadable usershare partition. It is a maintenance transport, not a permanent backdoor.
