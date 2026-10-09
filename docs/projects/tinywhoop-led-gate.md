---
article:
  published: 2026-10-02
title: Tinywhoop LED Gate
hide:
  - toc
description: Three modular LED-gate concepts, from tested U profiles to a V-profile study and a planned 15 x 15 x 1 mm square-tube frame.
---

# Tinywhoop LED Gate

A modular racing gate with aluminum rails, 3D-printed connectors and segmented diffusers. The aim is a stable frame that is easy to assemble and visible from several directions.

**Project status · 4 October 2026.** U-profile prototypes have been tested. The V-profile and square-tube versions are untested concepts. All images below are CAD views, not photographs or proof of physical performance.

**Planned lighting:** WS2812 strips with 60 LEDs per meter, giving a 16.67 mm center spacing. The CAD views show 5 × 5 mm 5050 housings; 10 mm PCB width, 0.4 mm PCB thickness and roughly 1.6 mm housing height are illustrative until the actual strip is selected. [WS2812 family, Worldsemi](https://www.world-semi.com/products/ws2812b-v6.html).

| Concept | Status | Main finding / next question |
| --- | --- | --- |
| U-profile LED rail | Tested; not pursued further | Too easy to twist, including the inward-facing variant |
| V-profile LED rail | CAD concept; physical test pending | Test stiffness, retention and diffuser visibility from behind |
| 15 × 15 × 1 mm square tube | Preferred next experiment | Test the closed-section frame, then develop connectors and a diffuser |

<details class="concept-stage" markdown="1">
<summary>1 · U-profile prototypes — tested, insufficient stiffness</summary>

The original prototype used shallow U-profile LED rails with the LEDs facing the incoming drone. During the project owner's physical assembly tests, the rails twisted easily and the gate did not stand sufficiently rigidly.

A second prototype rotated the U profile by 90°, placing the LEDs toward the gate opening. The owner reported some improvement in the assembled frame, but it was still too flexible. Rotation changes the bending orientation; it does not increase the rail's intrinsic torsional rigidity.

U-shaped profiles remain useful LED carriers, but this section was not satisfactory as the structural rail for this gate.

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

These images document the earlier connector and foot arrangement. They are retained as design history; they are not a current build recommendation.

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

<details class="concept-stage" markdown="1">
<summary>2 · V-profile concept — awaiting a physical test</summary>

The [Jopassy V-profile rail](https://www.kaufland.de/product/443322038/) adds a closed triangular chamber below the LED bed. The hope is greater torsional rigidity than the shallow open U rail; the complete gate still needs a physical test.

Printed 90° and T junctions use solid blocks with profile sockets, end stops and retaining lips. Their central LED support remains flat. The aluminum rim geometry is estimated from the listing's 16 mm flank dimension and is adjustable in Fusion; the dimensions are not yet verified against the delivered rail.

**Main challenge: the diffuser.** The wide metal section obscures the cover from behind. A printed cover must extend beyond the profile's silhouette to expose illuminated shoulders. The revised 0.8 mm cover wraps around the F-shaped rims and widens into a balloon chamber. Wrap depth, clearance and chamber dimensions are adjustable in Fusion; rear glow, printability and clip fit remain untested.

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

<details class="concept-stage" open markdown="1">
<summary>3 · Square-tube concept — preferred next experiment</summary>

Use a **closed aluminum tube, 15 × 15 mm outside with a 1 mm wall**, as the structural rail. The LED strip can adhere to a flat outer face; a separate printed diffuser provides the light shape.

A continuous closed section is expected to resist twisting much better than the shallow open U section at comparable dimensions. That makes it the preferred next experiment, rather than a validated final solution. Printed connector stiffness and clearance can still determine how rigid the assembled gate feels. [Background: torsion of closed sections, MIT](https://ocw.mit.edu/courses/16-20-structural-mechanics-fall-2002/resources/unit12/).

The starting layout remains four roughly 600 mm frame rails and four roughly 400 mm offcut feet from meter lengths, allowing for saw kerf.

**Wraparound diffuser:** the project owner's new section combines a 20 mm round light chamber with side arms and hooks behind the tube. The 0.8 mm optical wall is retained. It widens beyond the 15 mm tube to leave plastic visible around the metal silhouette; rear illumination remains to be tested.

The refinement adds **0.15 mm clearance per tube face** and **0.4 mm entry ramps** to a **180 mm module**. Both rear hooks remain continuous: one 2D section is extruded along the whole module, with no intermediate steps for upright printing. Length, clearance and ramp depth are editable in Fusion; the section stays linked to the owner's original diffuser. These are starting values for a print trial, not proven fit tolerances.

**Next test:** print the separate 20 mm fit coupon and check installation force, retention and removal on the real tube. Then test a full module for rear glow and layer strength. Corner interfaces and the complete square-tube gate remain to be developed.

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

The square-tube diffuser base section was designed by the project owner. CAD refinements and documentation were prepared with substantial OpenAI Codex assistance under owner direction. Physical prototype observations are reported by the project owner; dimensions, fit and lighting of the unbuilt concepts remain provisional.

