# GateLink simulator

[Project overview](../tinywhoop-led-gate/index.md) · [GateLink wireless control](gatelink.md) · [Project log](log.md)

The simulator below always shows the current `main` of the GateLink code: the site rebuilds it automatically when GateLink changes. It runs offline in the browser with an emulated gateway, so no hardware is needed.

[Open the simulator full screen](../../assets/tinywhoopgate/gatelink-sim/index.html?demo=1){ .md-button }

<iframe class="gatelink-sim" src="../../../assets/tinywhoopgate/gatelink-sim/index.html?demo=1" title="GateLink simulator" loading="lazy" allow="fullscreen"></iframe>

**What to try**

- **Event:** run a full race with heats, laps and results; every step is a real GateLink command.
- **Presets:** build a gate's WLED presets with built-in symmetry (corners to rail centres, centres to corners, waterfall, fountain), map race states and race events to them, export `presets.json`, and send the whole configuration to the gate over the radio link.
- **Packets / Inspector:** every frame on air, byte by byte.

The 144-LED layout and the effects are approximations of WLED; the final wiring is undecided. The event animations on a real gate need GateLink usermod build 8.
