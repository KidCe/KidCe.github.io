
## For future Claude

This note owns the community SSH host-key persistence procedure for Flashforge Creator 5 printers, consolidated on 2026-08-27. The procedure changes persistent system state after the /etc bind mount is active; it is not part of the minimum loop baseline and must be backed up before use.

## Why the source says keys regenerate

The community tutorial states that Dropbear reads /etc/dropbear, which initially points into temporary /run storage, while the persistent /etc bind mount is established later. The proposed mitigation makes /etc/dropbear a real directory after the persistent mount is active.

Source: research-sources\Creator-5-Mods\Basic\Make SSH host key persist\README.md and the duplicate historical tutorial at research-sources\Creator-5-Mods\Basic\SSH Persist\README.md.

## Historical procedure

~~~sh
mv /etc/dropbear/dropbear_ecdsa_host_key /tmp
rm /etc/dropbear
mkdir /etc/dropbear
mv /tmp/dropbear_ecdsa_host_key /etc/dropbear
sync
reboot
~~~

The source procedure must not be applied blindly. First inspect the target symlink, key presence, mount state, ownership, and available recovery. The commands above are a historical source excerpt, not a universal installer.

## Boundary

- Back up the relevant persistent system files first.
- Keep the printer on a trusted LAN.
- Do not infer that passwordless SSH or key persistence is supported by the installed Dropbear build.
- Record the before/after path and exact firmware.
- If the key is missing, stop rather than generating or overwriting unknown state.
