
## For future Claude

This note records locally referenced binary artifacts that remain in the
archive instead of being copied into the searchable Second Brain package. It
prevents a missing-file assumption while keeping credentials, raw device
images, and opaque vendor payloads outside the canonical documentation tree.

## Archive-local artifacts

| Archive path | Size | SHA-256 | Package status |
| --- | ---: | --- | --- |
| local archive/Creator5Pro-factory-1.9.7.tgz | 225,304 bytes | F5594D72AA6362B4BD5A8F01D143F171F2D6C6AC62CC09984D23C361A7244CC0 | Not copied; encrypted or opaque payload |
| local archive/Creator5Pro-factory.tar.xz | 190,710,480 bytes | 45657924298A41B5CD48C0F4412B4B2FB67DF624AF666B494D6BCEA969CC5B7B | Not copied; vendor firmware archive |
| local archive/tmp-vmlinux.bin | 10,458,656 bytes | E04028E465548922381472604886D5A6A38DE8B0B6B5FAC4EF659A6332814C5B | Not copied; opaque analysis artifact |

The first bytes of the small TGZ are Salted__, so it is not a normal
extractable tarball in this workspace. The large factory archive is a
vendor payload and includes network configuration material by filename. The
opaque artifacts are therefore retained only in the private archive.

## Related canonical evidence

- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Recovery/Device Evidence and Partition Layout](../Recovery/Device Evidence and Partition Layout.md)
- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Archive and Copy Manifest](Archive and Copy Manifest.md)
- [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Firmware/Vendor Firmware and Klipper](../Firmware/Vendor Firmware and Klipper.md)

## For future updates

If one of these artifacts is ever copied, inspect it for credentials, device
identifiers, private keys, and licensing constraints first. Record the copied
path and a new hash in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Sources/Archive and Copy Manifest](Archive and Copy Manifest.md).
