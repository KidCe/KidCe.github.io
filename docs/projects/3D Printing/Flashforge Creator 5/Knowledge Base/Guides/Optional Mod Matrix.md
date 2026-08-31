
## For future Claude

This note is the feature index for optional Flashforge Creator 5 and Creator 5 Pro modifications, consolidated on 2026-08-27. It is a routing page rather than a second installation manual. Each feature owns its detailed status in a linked note, and repository labels are not treated as physical validation.

## Feature status

| Feature | Detail page | Source status | Current boundary |
| --- | --- | --- | --- |
| Camera at 1280x720 | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Camera and Remote Screen](Camera and Remote Screen.md) | C1/R1 | Not physically validated in this refactor |
| Creator 5 Pro remote screen | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Camera and Remote Screen](Camera and Remote Screen.md) | R1 | Repository reports firmware 1.9.6 test; ports must stay private |
| Entware | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Entware Moonraker and Mainsail Updates](Entware Moonraker and Mainsail Updates.md) | C1/R1 | Experimental; depends on legacy NaN path |
| Moonraker update | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Entware Moonraker and Mainsail Updates](Entware Moonraker and Mainsail Updates.md) | C1/R1 | Old recipe; current upstream install not established |
| Mainsail replacement | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Entware Moonraker and Mainsail Updates](Entware Moonraker and Mainsail Updates.md) | C1 | Old release URL is historical |
| SSH host-key persistence | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/SSH Host Key Persistence](SSH Host Key Persistence.md) | C1 | Persistent system change; backup first |
| Heat/fan decoupling | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Heat and Fan Routing](Heat and Fan Routing.md) | C1 | Macro is not a validated safety configuration |
| Adaptive mesh and print metadata | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Print Workflow Adaptive Mesh and OrcaSlicer](Print Workflow Adaptive Mesh and OrcaSlicer.md) | C1 | Firmware, log, and slicer interactions remain open |
| Flow calibration | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Print Workflow Adaptive Mesh and OrcaSlicer](Print Workflow Adaptive Mesh and OrcaSlicer.md) | R1 | OrcaSlicer PR #14933 was open at the recorded check |
| Open firmware | [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Firmware/Open Firmware Migration](../Firmware/Open Firmware Migration.md) | S1/I1/R1 | Research roadmap; no stock-free operation claim |

## Selection rule

Start with the baseline in [Projects/3D Printing/Flashforge Creator 5/Knowledge Base/Guides/Modding Baseline - Root Loop and Mainsail](Modding Baseline - Root Loop and Mainsail.md). Select one optional feature at a time, preserve a rollback, and record the exact firmware, board, source revision, and physical result. A feature marked experimental or INDEV is not an approval.
