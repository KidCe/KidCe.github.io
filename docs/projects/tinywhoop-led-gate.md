---
article:
  published: 2026-10-02
  updated: 2026-10-27
  summary: Modular LED race gate for Tinywhoops from 15 x 15 mm aluminum tubes and printed parts, with an interactive 3D assembly guide and a cost estimate for 20 gates.
  image: assets/images/projects/tinywhoop-led-gate/assembly-explorer.jpg
  image_alt: CAD overview of the assembled SQ15 square-tube single gate with labeled corners, diffuser segments, foot brackets and end caps
  changes:
    - date: 2026-10-27
      summary: Restructured around the current square-tube design with project status, interactive assembly guide and a 20-gate cost estimate; earlier U and V concepts moved to the archive.
title: Modular Tinywhoop LED Gate
hide:
  - toc
description: Modular LED race gate for Tinywhoops from 15 x 15 mm aluminum tubes, printed corners and clip-on diffusers.
---

# Modular Tinywhoop LED Gate

A modular LED gate for Tinywhoop racing: aluminum square tubes, 3D-printed corners and feet, WS2812B LEDs and clip-on diffusers. It should be cheap enough to build twenty of them.

## Current status · 27 October 2026

| Part | Current version | Status |
| --- | --- | --- |
| Frame | 15 × 15 × 1 mm aluminum tube, 600 mm | Gate size not final |
| Corners | Printed 90° corner rev4 | Tube sockets fit; frame stands without screws |
| Diffuser | Clip-on SQ8W segments, 0.15 mm pinch per side | Clip fit chosen from printed test pieces |
| Feet | Foot bracket FB3.1, end cap v2, 250 mm legs | End cap fit OK; bracket and leg length still open |
| LEDs | WS2812B strip, 60 LEDs/m | Soldered across the corners; no plug connectors for now |

Not tested yet: a complete gate with lighting, its stability and the final leg length. All images on this page are CAD views.

## Assembly explorer

<style>
.tg-viewer{border:1px solid var(--md-default-fg-color--lightest);border-radius:.5rem;overflow:hidden;background:var(--md-code-bg-color)}
.tg-viewer iframe{display:block;width:100%;height:min(80vh,790px);border:0}
.tg-viewer__start{padding:1.2rem;text-align:center}
.tg-viewer__start img{display:block;width:100%;max-width:720px;margin:0 auto 1rem}
.tg-viewer__tabs{display:flex;gap:.5rem;flex-wrap:wrap;margin:.6rem 0}
</style>

<div class="tg-viewer__tabs">
<button class="md-button md-button--primary" id="tg-open-assembly" type="button">Assembly guide</button>
<button class="md-button" id="tg-open-parts" type="button">Individual parts</button>
</div>

<div class="tg-viewer" id="tg-viewer">
<div class="tg-viewer__start">
<img src="../../assets/images/projects/tinywhoop-led-gate/assembly-explorer.jpg" alt="CAD overview of the assembled SQ15 square-tube single gate with labeled corners, diffuser segments, foot brackets and end caps" width="1800" height="1420">
<p>Starts with the FB3.1 reference parts. The 3D viewer loads about 4 MB.</p>
<p><a href="../../assets/tinywhoopgate/viewer/index.html#build=sq15-v01">Open the large viewer</a> · <a href="../../assets/tinywhoopgate/viewer/TinywhoopGate-viewer-offline.zip" download>Offline package (30 MB)</a></p>
</div>
</div>

<noscript>The interactive viewer needs JavaScript. <a href="../../assets/tinywhoopgate/viewer/TinywhoopGate-viewer-offline.zip">Download the offline package</a>.</noscript>

<script>
(function () {
  var base = "../../assets/tinywhoopgate/viewer/";
  function open(parts) {
    var frame = document.createElement("iframe");
    frame.title = parts ? "Tinywhoop gate part explorer" : "Tinywhoop gate interactive assembly guide";
    frame.src = base + (parts ? "parts.html" : "index.html#build=sq15-v01");
    frame.allow = "fullscreen";
    frame.setAttribute("allowfullscreen", "");
    document.getElementById("tg-viewer").replaceChildren(frame);
  }
  document.getElementById("tg-open-assembly").onclick = function () { open(false); };
  document.getElementById("tg-open-parts").onclick = function () { open(true); };
})();
</script>

- **Assembly guide:** eight steps; the camera moves to each joint. M3 screws and inserts are optional.
- **Take it apart:** drag the orange handle of a joint or use the slider.
- **Individual parts:** each revision on its own, with its counterpart and the original STL/STEP print files.

FB4.1 in the viewer is an untested latch experiment. Frame and leg lengths in the model are placeholders.

## Cost estimate · 20 gates

Prices include VAT and were checked on 27 October 2026. Printed parts are PETG.

| Item | Quantity for 20 gates | 20 gates | Per gate |
| --- | --- | ---: | ---: |
| Tube 15 × 15 × 1 mm, cut to 900 mm ([DOLD](https://www.dold-mechatronik.de/Vierkantrohr-15x15x1mm-Aluminium-EN-AW-6060-T66-AlMgSi05-0156kg-m-Zuschnitt-20-6000mm)); each piece sawn once into a 600 mm frame tube and a leg | 80 pieces | €188.65 | €9.43 |
| DOLD shipping, one parcel of about 11 kg ([rates](https://www.dold-mechatronik.de/Versandinformationen)) | 1 | €8.90 | €0.45 |
| WS2812B strip, 60 LEDs/m, 5 m reel (AliExpress) | 10 reels | €200–250 | €10.00–12.50 |
| PETG filament | about 14 kg | €140–210 | €7.00–10.50 |
| Wire, heat shrink, solder | lump sum | €20–40 | €1.00–2.00 |
| **Total** | | **€558–698** | **€28–35** |

Larger batches cost about the same per gate. DOLD's best price already applies from 50 pieces, and shipping stays one parcel. Reels are bought whole, so 25 gates are slightly dearer per gate.

| Batch | Tubes + shipping | LED reels | Total | Per gate |
| --- | ---: | ---: | ---: | ---: |
| 20 gates | €197.55 | 10 | €558–698 | €27.90–34.90 |
| 25 gates | €244.71 | 13 | €705–882 | €28.20–35.30 |
| 30 gates | €291.88 | 15 | €832–1,042 | €27.70–34.70 |

- **Tubes:** each gate needs four 600 mm frame tubes and four legs of about 300 mm (30 mm in the bracket, about 250 mm free, 20 mm in the end cap). The saw cut comes off the leg, so it ends up about 297 mm long; the exact leg length does not matter. Prices are DOLD cart prices for 50 or more pieces of one length, including cutting and logistics.
- **LEDs:** 4 × 0.6 m = 2.4 m (144 LEDs) per gate, so one 5 m reel covers two gates. €20–25 per reel is a current AliExpress estimate, not a specific listing. Datasheet: [Worldsemi WS2812B](https://www.world-semi.com/products/ws2812b-v6.html).
- **Filament:** 4 corners, 2 foot brackets, 4 end caps and 12 diffuser segments add up to about 545 cm³ of solid part volume per gate, roughly 0.7 kg of PETG. Infill lowers the real amount somewhat. The price assumes €10–15 per kg.
- **Small parts:** short wires to solder the strip across each corner, plus heat shrink and solder. Rough estimate.
- **Not included:** controller, power supply, cables between gates, and the optional M3 screws and inserts.

<details markdown="1">
<summary>Tube ordering options compared · 20 gates</summary>

DOLD cart totals including shipping to Germany, 27 October 2026. Every option needs 80 frame tubes of 600 mm and 80 legs. Leftover is only the saw cut.

| Order | Own saw cuts | Leg length | Tubes + shipping |
| --- | ---: | --- | ---: |
| 80 × 600 + 80 × 300 mm, cut by DOLD | 0 | 300 mm | €232.55 |
| 80 × 600 + 80 × 250 mm, cut by DOLD | 0 | 250 mm | €224.01 |
| **80 × 900 mm, cut into 600 + leg** | **80** | **≈ 297 mm** | **€197.55** |
| 40 × 1800 mm, cut into 2 × 600 + 2 legs | 120 | ≈ 297 mm | €194.16 |
| 80 × 850 mm, cut into 600 + leg | 80 | ≈ 247 mm | €189.01 |
| 40 × 1700 mm, cut into 2 × 600 + 2 legs | 120 | ≈ 247 mm | €185.54 |
| 80 × 1000 mm, cut into 600 + leg | 80 | ≈ 397 mm | €214.62 |
| 80 × 600 mm + legs in 10 × 10 mm tube, 20 × 1000 mm cut into 4 | 60 | ≈ 247 mm | €183.75 |

Pieces up to 1 m ship as a normal parcel; 1.2–1.8 m pieces cost €12.90–18.90 to ship, which cancels most of the saving. 10 × 10 mm legs save only a few euros and would need a new foot bracket and end cap.

Other shops were more expensive per metre: Hornbach €3.85 per 1 m tube ([product](https://www.hornbach.de/p/vierkantrohr-alu-natur-15x15x1-mm-1-m/8829160/)), the eBay seller metalexpres €4.25 per 1 m or €7.57 per 2 m plus €8.90 shipping ([listing](https://www.ebay.de/itm/322692115404)), Pegnitz-Schrauben €4.02 per 1 m ([product](https://www.pegnitz-schrauben.de/Vierkantrohr-Alu-Natur-1000mm-15-x-15-10mm-Wandstaerke)). At those prices the 80 one-metre tubes alone cost more than €300.

</details>

## Archive

Earlier concepts, newest first.

<details class="concept-stage" markdown="1">
<summary>Square-tube study · early October 2026</summary>

First study of the closed 15 × 15 × 1 mm tube as the structural rail, with the LED strip on a flat face and a wraparound clip diffuser in 180 mm modules. The current parts above grew out of it.

<div class="project-gallery">
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-clip-section.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-clip-section.png" alt="Wraparound clip section — The owner-designed 20 mm round light chamber sits in front of the 15 mm tube. Continuous rear hooks retain the cover; orange marks the LED-strip PCB." title="Wraparound clip section — The owner-designed 20 mm round light chamber sits in front of the 15 mm tube. Continuous rear hooks retain the cover; orange marks the LED-strip PCB." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Wraparound clip section</strong>The owner-designed 20 mm round light chamber sits in front of the 15 mm tube. Continuous rear hooks retain the cover; orange marks the LED-strip PCB.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-clip-assembled.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-clip-assembled.png" alt="Continuous light surface — A 180 mm module retains the original 0.8 mm optical wall. The cover widens beyond the tube, while its arms reach around the sides." title="Continuous light surface — A 180 mm module retains the original 0.8 mm optical wall. The cover widens beyond the tube, while its arms reach around the sides." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Continuous light surface</strong>A 180 mm module retains the original 0.8 mm optical wall. The cover widens beyond the tube, while its arms reach around the sides.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-clip-rear-hooks.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-clip-rear-hooks.png" alt="Continuous retaining edges — The rear hooks run the full module length. The same 2D section is extruded throughout, avoiding intermediate steps when printed upright." title="Continuous retaining edges — The rear hooks run the full module length. The same 2D section is extruded throughout, avoiding intermediate steps when printed upright." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Continuous retaining edges</strong>The rear hooks run the full module length. The same 2D section is extruded throughout, avoiding intermediate steps when printed upright.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-clip-rear-assembled.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-clip-rear-assembled.png" alt="Retained behind the tube — The rear hooks overlap the tube edges. Wider illuminated shoulders may remain visible from behind; actual glow and snap performance still need a physical test." title="Retained behind the tube — The rear hooks overlap the tube edges. Wider illuminated shoulders may remain visible from behind; actual glow and snap performance still need a physical test." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Retained behind the tube</strong>The rear hooks overlap the tube edges. Wider illuminated shoulders may remain visible from behind; actual glow and snap performance still need a physical test.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-led-strip.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/square-led-strip.png" alt="WS2812 strip on a flat face — 5050 housings and optical windows are shown at 16.67 mm pitch for 60 LEDs per meter. PCB dimensions and package height are illustrative." title="WS2812 strip on a flat face — 5050 housings and optical windows are shown at 16.67 mm pitch for 60 LEDs per meter. PCB dimensions and package height are illustrative." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>WS2812 strip on a flat face</strong>5050 housings and optical windows are shown at 16.67 mm pitch for 60 LEDs per meter. PCB dimensions and package height are illustrative.</figcaption>
</figure>
</div>
</details>

<details class="concept-stage" markdown="1">
<summary>V profile · dropped</summary>

[Jopassy V-profile rail](https://www.kaufland.de/product/443322038/) with a closed triangular chamber under the LED bed. CAD only; dropped in favor of the square tube. The wide metal section also hid the diffuser from behind.

<div class="project-gallery">
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-led-detail.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-led-detail.png" alt="LED strip on the V-profile bed — The strip lies on the flat LED support above the closed triangular cell. Packages remain below the upper clip rims." title="LED strip on the V-profile bed — The strip lies on the flat LED support above the closed triangular cell. Packages remain below the upper clip rims." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>LED strip on the V-profile bed</strong>The strip lies on the flat LED support above the closed triangular cell. Packages remain below the upper clip rims.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-retained-section.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-retained-section.png" alt="V-profile retention — Continuous F-shaped rims sit beneath the matched retaining lips. Final fit awaits the real extrusion." title="V-profile retention — Continuous F-shaped rims sit beneath the matched retaining lips. Final fit awaits the real extrusion." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>V-profile retention</strong>Continuous F-shaped rims sit beneath the matched retaining lips. Final fit awaits the real extrusion.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-retained-corner.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-retained-corner.png" alt="Profiles in the corner — Axial insertion under the retaining lips; a solid junction continues the flat LED support." title="Profiles in the corner — Axial insertion under the retaining lips; a solid junction continues the flat LED support." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Profiles in the corner</strong>Axial insertion under the retaining lips; a solid junction continues the flat LED support.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-tee.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-tee.png" alt="Three-way junction — The T connector provides the shared crossbar junction for stacked gates." title="Three-way junction — The T connector provides the shared crossbar junction for stacked gates." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Three-way junction</strong>The T connector provides the shared crossbar junction for stacked gates.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-diffuser-section.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-diffuser-section.png" alt="Diffuser cross-section — The 0.8 mm balloon wall wraps around both outer F-rim corners. Clip retention and rear glow need physical tests." title="Diffuser cross-section — The 0.8 mm balloon wall wraps around both outer F-rim corners. Clip retention and rear glow need physical tests." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Diffuser cross-section</strong>The 0.8 mm balloon wall wraps around both outer F-rim corners. Clip retention and rear glow need physical tests.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-diffuser-oblique.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-diffuser-oblique.png" alt="Diffuser over the V profile — A continuous extruded section returns along the outside flanks, with 0.25 mm nominal clearance around the rims." title="Diffuser over the V profile — A continuous extruded section returns along the outside flanks, with 0.25 mm nominal clearance around the rims." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Diffuser over the V profile</strong>A continuous extruded section returns along the outside flanks, with 0.25 mm nominal clearance around the rims.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-frame-layout.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/v-frame-layout.png" alt="V-profile gate layout — Assembly overview with four feet; mechanical stability has not yet been tested." title="V-profile gate layout — Assembly overview with four feet; mechanical stability has not yet been tested." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>V-profile gate layout</strong>Assembly overview with four feet; mechanical stability has not yet been tested.</figcaption>
</figure>
</div>
</details>

<details class="concept-stage" markdown="1">
<summary>U profile · dropped after testing</summary>

Shallow U-profile LED rails, first with the LEDs facing forward, then rotated 90° toward the opening. Both prototypes were built; the rails twisted too easily and the gate did not stand rigidly.

<div class="project-gallery">
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/u-led-detail.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/u-led-detail.png" alt="LED strip inside the U rail — Thin PCB and 5050 packages on the original LED bed; 16.67 mm spacing represents 60 LEDs per meter." title="LED strip inside the U rail — Thin PCB and 5050 packages on the original LED bed; 16.67 mm spacing represents 60 LEDs per meter." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>LED strip inside the U rail</strong>Thin PCB and 5050 packages on the original LED bed; 16.67 mm spacing represents 60 LEDs per meter.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/01-profile-section.png"><img src="../../assets/media/projects/tinywhoop-led-gate/01-profile-section.png" alt="Original U profile — An open, shallow section carries the LED strip." title="Original U profile — An open, shallow section carries the LED strip." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Original U profile</strong>An open, shallow section carries the LED strip.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/22-finished-oblique.png"><img src="../../assets/media/projects/tinywhoop-led-gate/22-finished-oblique.png" alt="Original gate layout — Printed connectors, segmented diffusers and four offcut feet. CAD illustration of the tested concept." title="Original gate layout — Printed connectors, segmented diffusers and four offcut feet. CAD illustration of the tested concept." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Original gate layout</strong>Printed connectors, segmented diffusers and four offcut feet. CAD illustration of the tested concept.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/u-inward-profile.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/u-inward-profile.png" alt="U profile rotated by 90° — The LEDs face the opening. This variant was also built and tested." title="U profile rotated by 90° — The LEDs face the opening. This variant was also built and tested." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>U profile rotated by 90°</strong>The LEDs face the opening. This variant was also built and tested.</figcaption>
</figure>
<figure>
<a href="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/u-inward-gate.png"><img src="../../assets/media/projects/tinywhoop-led-gate/concept-evolution/u-inward-gate.png" alt="Inward-facing U-profile frame — CAD layout with dedicated foot brackets. The physical prototype remained too flexible." title="Inward-facing U-profile frame — CAD layout with dedicated foot brackets. The physical prototype remained too flexible." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain"></a>
<figcaption><strong>Inward-facing U-profile frame</strong>CAD layout with dedicated foot brackets. The physical prototype remained too flexible.</figcaption>
</figure>
</div>

<details markdown="1">
<summary>Original U-profile CAD assembly gallery · archive</summary>

### Aluminum profile

LED aluminum profile, based visually on the [Jopassy U profile](https://www.kaufland.de/product/443322053/). The modeled contour is approximate.

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/01-profile-section.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/01-profile-section.png" alt="Profile section — Rounded clip channels outside; support ledges and stepped walls inside." title="Profile section — Rounded clip channels outside; support ledges and stepped walls inside." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Profile section</strong> Rounded clip channels outside; support ledges and stepped walls inside.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/02-profile-oblique.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/02-profile-oblique.png" alt="Short profile sample — The LED strip sits on the aluminum floor." title="Short profile sample — The LED strip sits on the aluminum floor." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Short profile sample</strong> The LED strip sits on the aluminum floor.</figcaption>
  </figure>

</div>

### Printed 90° connector · blue

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/03-corner-front.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/03-corner-front.png" alt="90° connector — Two perpendicular sockets form a frame corner." title="90° connector — Two perpendicular sockets form a frame corner." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>90° connector</strong> Two perpendicular sockets form a frame corner.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/04-corner-oblique.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/04-corner-oblique.png" alt="Profile sockets — The aluminum sections slide into the printed connector." title="Profile sockets — The aluminum sections slide into the printed connector." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Profile sockets</strong> The aluminum sections slide into the printed connector.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/05-corner-back.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/05-corner-back.png" alt="Rear and mounting holes — Holes provide attachment points for M3 heat-set inserts." title="Rear and mounting holes — Holes provide attachment points for M3 heat-set inserts." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Rear and mounting holes</strong> Holes provide attachment points for M3 heat-set inserts.</figcaption>
  </figure>

</div>

### Printed T connector · orange

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/06-t-front.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/06-t-front.png" alt="T connector — The same three-way part serves as a foot holder or frame junction." title="T connector — The same three-way part serves as a foot holder or frame junction." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>T connector</strong> The same three-way part serves as a foot holder or frame junction.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/07-t-oblique.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/07-t-oblique.png" alt="Open center — The central passage leaves room for cable routing." title="Open center — The central passage leaves room for cable routing." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Open center</strong> The central passage leaves room for cable routing.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/08-t-back.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/08-t-back.png" alt="Mounting face — Two upper holes align with the corner connector." title="Mounting face — Two upper holes align with the corner connector." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Mounting face</strong> Two upper holes align with the corner connector.</figcaption>
  </figure>

</div>

### 1 · Build the frame

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/09-corner-insertion.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/09-corner-insertion.png" alt="Insert the profiles — Push both aluminum sections into the corner sockets." title="Insert the profiles — Push both aluminum sections into the corner sockets." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Insert the profiles</strong> Push both aluminum sections into the corner sockets.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/10-corner-assembled.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/10-corner-assembled.png" alt="One assembled corner — The profiles meet at the printed connector." title="One assembled corner — The profiles meet at the printed connector." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>One assembled corner</strong> The profiles meet at the printed connector.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/11-frame-separated.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/11-frame-separated.png" alt="Four corners, four profiles — Arrange the frame parts before closing the square." title="Four corners, four profiles — Arrange the frame parts before closing the square." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Four corners, four profiles</strong> Arrange the frame parts before closing the square.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/12-frame-assembled.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/12-frame-assembled.png" alt="Closed frame — Four 600 mm sections form one gate." title="Closed frame — Four 600 mm sections form one gate." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Closed frame</strong> Four 600 mm sections form one gate.</figcaption>
  </figure>

</div>

### 2 · Add the feet

Each 1 m profile supplies a 600 mm gate bar and a roughly 400 mm foot offcut. The feet stand on edge for stiffness.

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/13-t-mounting.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/13-t-mounting.png" alt="Attach the foot holder — Bolt the T connector onto the outside of the lower corner." title="Attach the foot holder — Bolt the T connector onto the outside of the lower corner." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Attach the foot holder</strong> Bolt the T connector onto the outside of the lower corner.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/14-t-fastened.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/14-t-fastened.png" alt="Two M3 screws — Two upper screws and washers hold the T connector." title="Two M3 screws — Two upper screws and washers hold the T connector." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Two M3 screws</strong> Two upper screws and washers hold the T connector.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/15-foot-insertion.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/15-foot-insertion.png" alt="Insert the feet — One 400 mm offcut extends forward, the other backward." title="Insert the feet — One 400 mm offcut extends forward, the other backward." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Insert the feet</strong> One 400 mm offcut extends forward, the other backward.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/16-foot-system.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/16-foot-system.png" alt="Four feet — Both sides reuse the same T connector component." title="Four feet — Both sides reuse the same T connector component." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Four feet</strong> Both sides reuse the same T connector component.</figcaption>
  </figure>

</div>

### 3 · Clip on the diffusers

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/17-diffuser-insertion.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/17-diffuser-insertion.png" alt="Add the diffusers — The segmented covers approach the frame from the front." title="Add the diffusers — The segmented covers approach the frame from the front." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Add the diffusers</strong> The segmented covers approach the frame from the front.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/18-diffuser-detail.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/18-diffuser-detail.png" alt="Clip-on detail — A printed diffuser segment clips over the aluminum profile." title="Clip-on detail — A printed diffuser segment clips over the aluminum profile." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Clip-on detail</strong> A printed diffuser segment clips over the aluminum profile.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/19-bottom-diffuser.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/19-bottom-diffuser.png" alt="Bottom bar covered — Three approximately 200 mm segments cover one bar." title="Bottom bar covered — Three approximately 200 mm segments cover one bar." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Bottom bar covered</strong> Three approximately 200 mm segments cover one bar.</figcaption>
  </figure>

</div>

### 4 · Fit the foot caps

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/20-foot-cap.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/20-foot-cap.png" alt="Foot end cap — A full-surround trapezoid cap provides a wider ground contact at each foot end." title="Foot end cap — A full-surround trapezoid cap provides a wider ground contact at each foot end." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Foot end cap</strong> A full-surround trapezoid cap provides a wider ground contact at each foot end.</figcaption>
  </figure>

</div>

### The complete gate

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/21-finished-front.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/21-finished-front.png" alt="Incoming-drone view — The LED-facing side points toward the approaching drone." title="Incoming-drone view — The LED-facing side points toward the approaching drone." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Incoming-drone view</strong> The LED-facing side points toward the approaching drone.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/22-finished-oblique.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/22-finished-oblique.png" alt="Complete gate — A square illuminated frame with forward and rear supports." title="Complete gate — A square illuminated frame with forward and rear supports." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Complete gate</strong> A square illuminated frame with forward and rear supports.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/23-finished-rear.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/23-finished-rear.png" alt="Rear view — The aluminum frame remains visible behind the diffusers." title="Rear view — The aluminum frame remains visible behind the diffusers." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Rear view</strong> The aluminum frame remains visible behind the diffusers.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/24-finished-top.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/24-finished-top.png" alt="Foot layout — The top view shows the four opposing support sections." title="Foot layout — The top view shows the four opposing support sections." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Foot layout</strong> The top view shows the four opposing support sections.</figcaption>
  </figure>

</div>

### Extension · Double gate

The T connector also links two stacked frames. Diffuser details at the shared junction still need refinement.

<div class="project-gallery">

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/25-double-bare.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/25-double-bare.png" alt="Stacked frame — Two T junctions replace the upper corners at the shared bar." title="Stacked frame — Two T junctions replace the upper corners at the shared bar." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Stacked frame</strong> Two T junctions replace the upper corners at the shared bar.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/26-double-junction.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/26-double-junction.png" alt="Shared T junction — Upper and lower uprights meet the horizontal crossbar." title="Shared T junction — Upper and lower uprights meet the horizontal crossbar." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Shared T junction</strong> Upper and lower uprights meet the horizontal crossbar.</figcaption>
  </figure>

  <figure>
    <a href="../../assets/media/projects/tinywhoop-led-gate/27-double-complete.png">
      <img src="../../assets/media/projects/tinywhoop-led-gate/27-double-complete.png" alt="Double-gate concept — Two gates share one horizontal bar and the same foot system." title="Double-gate concept — Two gates share one horizontal bar and the same foot system." loading="lazy" width="1600" height="1200" style="aspect-ratio:4/3;object-fit:contain">
    </a>
    <figcaption><strong>Double-gate concept</strong> Two gates share one horizontal bar and the same foot system.</figcaption>
  </figure>

</div>


</details>
</details>
