# Capacitor for FPV Racing

A good capacitor is still an important part of a reliable 5-inch FPV racing quad. If motors become unusually hot, the video system shows noise, the flight controller resets, or the quad suddenly feels inconsistent, a damaged, missing, or undersized ESC capacitor is worth checking. It is not a cure-all, but replacing it with a good low-ESR hybrid capacitor often helps.

## Recommended capacitors

For a normal 6S ESC with a radial, through-hole capacitor, these are the strongest choices from the comparison:

1. **Panasonic EEH-AZSV681UB** — best practical first choice.
2. **KEMET A7C3MW687M1VAAS011** — closest technical replacement.
3. **Rubycon 35PZK680M10X15** — excellent electrical alternative, but usually harder to source.

For a custom PCB, the **Panasonic EEH-ZU1V681UV** has the best electrical values. The **TDK/EPCOS B40950A7687M000** is another good SMD option. SMD parts are not drop-in replacements for a capacitor mounted on an ESC with free wires.

| Part | Installation | Key values | Example purchase and price* |
|---|---|---|---|
| [Panasonic EEH-AZSV681UB](https://www.mouser.com/ProductDetail/Panasonic/EEH-AZSV681UB?qs=Jslch3jnSjnutAv1zQYqTg%3D%3D) | Radial | 680 µF, 35 V, 11 mΩ, 4.0 A, 10 × 15.7 mm | Mouser Germany: about €2.76 for one; lower prices at quantity |
| [KEMET A7C3MW687M1VAAS011](https://at.farnell.com/kemet/a7c3mw687m1vaas011/alu-poly-kond-680uf-4a-35v-radial/dp/4757449) | Radial | 680 µF, 35 V, 11 mΩ, 4.0 A, 10 × 15.5 mm | Farnell listing: about €0.61 each from 10 |
| [Rubycon 35PZK680M10X15](https://www.digikey.com/en/products/detail/rubycon/35PZK680M10X15/27485823) | Radial | 680 µF, 35 V, 11 mΩ, 4.3 A, 10 × 15 mm | DigiKey listing: about US$2.87 for one |
| [Panasonic EEH-ZU1V681UV](https://www.mouser.de/de/ProductDetail/Panasonic-Industry/EEH-ZU1V681UV?qs=HoCaDK9Nz5duEjH7y2oWyg%3D%3D) | SMD | 680 µF, 35 V, 9 mΩ, 5.8 A, 10 × 16.8 mm | Mouser Germany: about €3.88 for one |
| [TDK B40950A7687M000](https://www.mouser.de/de/ProductDetail/TDK/B40950A7687M000) | SMD | 680 µF, 35 V, 15 mΩ, 5.4 A, 10 × 16.5 mm | Mouser Germany listing: about €2.77 for one |

\* Prices are example distributor listings from the research snapshot, not fixed quotes. Stock, packaging, region, and quantity can change the price.

## Why these specifications matter

### 35 V and 680 µF

A fully charged 6S LiPo reaches 25.2 V. A 35 V capacitor leaves 9.8 V of nominal headroom, which is a sensible minimum for a compact 6S ESC capacitor. It is not guaranteed transient protection: long battery leads, poor connectors, high current, and ESC layout can create short voltage spikes. Never intentionally operate the capacitor above its voltage rating.

The 680 µF local reservoir supplies short current pulses and reduces voltage ripple at the ESC battery input. More capacitance can help, but wiring, solder joints, mounting position, and ESR are equally important.

### ESR: the useful meaning of “internal resistance”

The important value is usually **ESR**, or equivalent series resistance. A simple approximation is:

`voltage ripple ≈ current ripple × ESR`

Lower ESR normally means less ripple voltage and less heat inside the capacitor. The radial Panasonic, KEMET, and Rubycon parts are all specified at about 11 mΩ. The Panasonic SMD part is specified at 9 mΩ; the TDK part at 15 mΩ. These values are normally measured at 100 kHz and 20 °C and should only be compared under matching conditions. Wiring inductance also contributes to the real transient impedance.

### Why hybrid instead of full polymer?

Hybrid aluminum electrolytic capacitors combine conductive polymer with liquid electrolyte. The polymer helps provide low ESR and high ripple-current capability, while the liquid electrolyte remains part of the wound aluminum-electrolytic system. This gives a useful combination of low impedance, compact size, temperature capability, and electrolytic construction.

Hybrid does not mean surge-proof. The capacitor still has a 35 V maximum rating and must be protected from excessive voltage, heat, reverse polarity, and crash damage.

## Installation

- Solder the radial capacitor directly across the ESC battery input: positive to VBAT and the marked negative lead to ground.
- Keep the connection short and low impedance.
- Insulate and mechanically secure the capacitor so a crash cannot bend the leads into a short circuit.
- A second capacitor in parallel can reduce effective ESR, but it cannot compensate for very long battery leads or poor solder joints.
- For a custom SMD board, provide the correct footprint and mechanical strain relief. Do not attach an SMD can to long unsupported wires.

The technical comparison used manufacturer datasheets and product pages from [Panasonic](https://na.industrial.panasonic.com/products/capacitors/polymer-capacitors/lineup/polymer-hybrid-aluminum-electrolytic-capacitor/series/142649/model/142864), [KEMET/YAGEO](https://content.kemet.com/datasheets/KEM_A4143_A7C3.pdf), [Rubycon](https://www.rubycon.co.jp/information/20250716-1/), and [TDK](https://product.tdk.com/en/search/capacitor/aluminum-electrolytic/hybrid-polymer/info?part_no=B40950A7687M000). Full solid-polymer capacitors were excluded from this hybrid-only selection.
