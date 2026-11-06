MacroPAD showpiece viewer

This simplified viewer uses the TinywhoopGate project explorer's Three.js
0.170.0 and OrbitControls foundation, theme integration, feature-edge helper
and offline gzip-buffer geometry approach. It has an automatic exploded-view
introduction and normal orbit/zoom interaction, without the explorer's parts
tree, BOM, configuration panels, assembly controls or downloads.

The public page is a visual overview of a development prototype, not a
released fabrication package. Both shell meshes and the switch plate are
registered from their actual print STLs. Other CAD parts use the assembled
reference meshes. TPU shapes represent nominal compression, not simulated
material deformation. Encoders are not selected or displayed.

The CAD and viewer implementation were created with substantial assistance
from OpenAI Codex under the owner's direction. Reused Three.js and the MX
reference model retain their notices in THIRD_PARTY_LICENSE.txt.

No telemetry, external runtime dependencies, or network geometry requests.
Reduced-motion mode opens the assembled model without automatic animation.
