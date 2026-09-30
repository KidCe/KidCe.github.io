# Flashforge Creator 5 knowledge base

Practical guides, recovery evidence and firmware research for the Creator 5 family. Physical findings primarily describe one Creator 5 Pro. Check the model, firmware and evidence level on each page before applying a procedure.

## Setup and modifications

Begin with the [modding baseline](Guides/Modding Baseline - Root Loop and Mainsail.md) and its prerequisites. The [optional modification matrix](Guides/Optional Mod Matrix.md) records the status and limitations of additional features.

| Task | Guide |
| --- | --- |
| Camera streaming and remote display | [Camera and remote screen](Guides/Camera and Remote Screen.md) |
| Package manager and web interface updates | [Entware, Moonraker and Mainsail](Guides/Entware Moonraker and Mainsail Updates.md) |
| Print metadata, adaptive mesh and slicer setup | [Print workflow and OrcaSlicer](Guides/Print Workflow Adaptive Mesh and OrcaSlicer.md) |
| Chamber heating and fan control | [Heat and fan routing](Guides/Heat and Fan Routing.md) |
| Persistent SSH host keys | [SSH host-key persistence](Guides/SSH Host Key Persistence.md) |

## Recovery

Read the [recovery overview](Recovery/Recovery Overview.md) first. It defines the sequence from identification and backups to diagnosis and any separately reviewed repair.

| Task | Guide |
| --- | --- |
| Identify the tested hardware and storage geometry | [Device evidence and partition layout](Recovery/Device Evidence and Partition Layout.md) |
| Acquire and validate a backup without writing | [Read-only USBCloner acquisition](Recovery/USBCloner Read-only Acquisition.md) |
| Diagnose an image and plan a case-specific repair | [Offline repair and validation](Recovery/Offline Repair and Validation.md) |
| Use the tested temporary maintenance connection | [Temporary ADB access](Recovery/Temporary ADB Access.md) |

## Architecture and firmware

- [Stock and target architecture](Architecture/Stock and Target Architecture.md): service relationships and the proposed open stack.
- [Vendor firmware and Klipper](Firmware/Vendor Firmware and Klipper.md): findings from static inspection of firmware 1.9.8.
- [Open firmware migration](Firmware/Open Firmware Migration.md): staged feasibility roadmap and validation boundaries.

## Evidence levels

| Label | Meaning |
| --- | --- |
| P1 | Physically executed or measured on one Creator 5 Pro |
| S1 | Supported by static inspection of an image, script, configuration or binary |
| R1 | A repository statement at a recorded revision |
| C1 | A community report without independent confirmation |
| I1 | An inference requiring a confirming test |
| TBD | Not sufficiently investigated |

## Sources and history

[Repository and revision registry](https://github.com/KidCe/KidCe.github.io/blob/main/docs/projects/3D%20Printing/Flashforge%20Creator%205/Knowledge%20Base/Sources/Repository%20and%20Revision%20Registry.md) records source precedence and inspected revisions. [Source snapshots](https://github.com/KidCe/KidCe.github.io/tree/main/docs/projects/3D%20Printing/Flashforge%20Creator%205/Knowledge%20Base/Sources) and [historical notes](https://github.com/KidCe/KidCe.github.io/tree/main/docs/projects/3D%20Printing/Flashforge%20Creator%205/Root) remain available in the repository for traceability.

[Project overview](../Flashforge Creator 5.md)

