# RatesManager

RatesManager is an EdgeTX tool for managing Betaflight rate profiles directly from a radio.

It keeps a local profile library, edits the active flight-controller profile, and synchronizes one or all three switch-accessible profiles over an ExpressLRS/CRSF connection. It supports temporary `Send TEMP` tests, persistent `Send FLASH` writes, backups, read-back verification, and rollback protection. The interface is designed for compact radios such as the RadioMaster Boxer as well as larger color radios.

Always remove propellers before testing a flight-controller write. RatesManager is an independent community project and is not affiliated with or endorsed by Betaflight, EdgeTX, ExpressLRS, or RadioMaster.

- [View RatesManager on GitHub](https://github.com/KidCe/RatesManager)
