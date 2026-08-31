
## For future Claude

This note is the canonical offline repair and read-back workflow for the Flashforge Creator 5 Pro recovery package, consolidated on 2026-08-27. It deliberately stops at a reviewed, case-specific write design and does not provide a generic flash command. The known startup-permission repair was prepared but not written in the recorded evidence.

## 1. Freeze the evidence

- Keep the original MMC0 user-area image on independent storage.
- Record its byte size and SHA-256 in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](Device Evidence and Partition Layout.md).
- Mark the original read-only and work from a copy or extracted partition.
- Never mount the only image read-write and never use repairing fsck on it.

## 2. Prove the target layout

Parse the target image's GPT and derive each partition offset from start LBA times 512. Compare the result with the device-specific table in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](Device Evidence and Partition Layout.md). Do not copy offsets from another printer.

## 3. Diagnose narrowly

Mount Linux filesystems read-only with journal replay disabled. Capture mount results, filesystem metadata, startup file mode/owner/hash, device-owned backups, update logs, and active slot state. A repair is justified only when the cause is supported by evidence.

For the recorded incident, init directly executed app_startup.sh. The file was mode 600, while the device-local pre-change copy was mode 755 and differed only by the loop-hook line. That supports a one-file repair for that printer, not a universal repair image.

## 4. Build a separate repair

Extract only the affected partition from a working copy. Change one intended item. Verify source provenance, owner/group, mode, shell syntax, filesystem consistency, and the complete difference list. Preserve calibration, identity, network, account, and device-specific data unless the repair case explicitly requires them.

## 5. Write design gate

Only after independent review, create one FILE policy for the exact target range:

- input size equals the target partition size;
- offset comes from the target GPT;
- storage target is MMC0;
- exactly one policy is enabled;
- erase, eFuse, security, GPP, RPMB, and unrelated policies remain disabled;
- input and profile hashes are recorded;
- stable power and an independent recovery path are ready.

The copy under Sources/Recovery Kits is the no-write profile. It is not a write authorization.

## 6. Read back before boot

Read the exact written range into a new file and compare byte-for-byte with the prepared partition. Only a matching size and SHA-256 close the write step. Then remove K4/J29, power off cleanly, and test a normal boot with heaters and motion disabled.

## Validation checklist

- [ ] Device identity and board revision recorded
- [ ] Complete read-only MMC0 user area acquired
- [ ] GPT and region boundary verified
- [ ] Original image frozen and independently copied
- [ ] Exact repair cause proven
- [ ] Repair partition size and offset independently reviewed
- [ ] Read-back compared byte-for-byte
- [ ] UI, storage, network, temperature, MCU, and emergency-stop checks passed
- [ ] No heat, homing, motion, or printing before the no-motion baseline is accepted
