# Ring LED strip comparison and recommendation (Claude, 2026-11-14)

Owner request: compare three BTF-LIGHTING WS2812B strips for the V5 ring before ordering. Priority: smoothest animated Hextech lighting that fits reliably without excessive heat or power.

**Nothing was purchased, printed or bench-tested.** Evidence classes used below:
- **[CAD]** measured by Claude from the V5 draft geometry (ring-axis frame, probes every 5°).
- **[MFR]** stated on a BTF-LIGHTING page (btf-lighting.com or the BTF store listing on Amazon.de).
- **[3P]** third-party seller or buyer report; not manufacturer-confirmed.
- **[ASSUMED]** typical value, not confirmed for this product.

## Recommendation

**Ring: option 3, BTF-LIGHTING Ultra-Narrow WS2812B, 3535, 144 LEDs/m, 7.2 mm PCB, IP30, white PCB.** Mount it on the trough's outer wall, LEDs facing inward. 50 pixels per ring.

**Hand strip and crystal: the same strip**, so the whole arm is one LED type, one protocol and one colour order. This needs V5 CAD changes that are not yet approved (see "CAD changes").

**Fallback:** option 1 (60 LEDs/m, 10 mm). It fits and is cheap, but 21 pixels around the ring will look stepped in chase effects.

**Rejected:** option 2 (5050, 144 LEDs/m). Buyers measure it at about 12 mm or more, which leaves about 1 mm total in a 13.0 mm wall.

The recommendation is conditional on test T-1 with a real sample. No BTF page I could read states thickness or minimum bend radius for any of the three.

## V5 ring geometry — [CAD]

| Feature | V5 draft |
|---|---|
| Trough outer wall radius | 55.9 mm (median; 55.5–56.2 around the ring) |
| Trough inner wall radius | 28.8 mm |
| Radial width | 27.1 mm |
| Floor | h = −3.50 mm |
| Cover seat in V5 | h ≈ 9.5 mm (0.3 mm lower than the original part, from the V5 clearance cut) |
| **Usable wall height under the seated cover** | **about 13.0 mm** |
| Outer wall circumference | 351.2 mm |
| Inner wall circumference | 181.0 mm |
| Wire notch, outer wall | 13.2 mm wide, about 3.5 mm tall at the floor, at 263.5°–277° |
| Wire notch, inner wall | 14.1 mm wide, full height, at 256.5°–284.5° |
| Passage from trough to arm cavity | passes a 7 mm cube probe |

## Comparison

| | 1. WS2812B 5050, 60/m | 2. WS2812B 5050, 144/m | 3. Ultra-Narrow WS2812B 3535, 144/m |
|---|---|---|---|
| PCB width | 10 mm [MFR, Amazon.de BTF ECO listing: 10 mm for IP30/IP65] | Listing says 10 mm [MFR]; buyers report about 12 mm and "13–14 mm" [3P]; generic 144/m strips are 12 mm [3P]. **Treat as 12 mm.** | **7.2 mm [MFR]** |
| Thickness | 2.13 mm for IP30 [MFR, ECO listing] | about 2.5 mm [3P] | not stated; about 2 mm [ASSUMED] |
| LED pitch | 16.67 mm (computed) | 6.94 mm (computed) | 6.94 mm (computed) |
| Cut points | every LED [MFR] | every LED [MFR] | every LED [MFR] |
| Solder joints in the reel | every 0.5 m [MFR, ECO page] | every 0.5 m [MFR, ECO page] | not stated |
| Max power | 11 W/m [MFR] = 0.18 W/LED | 25 W/m [MFR] = 0.17 W/LED | 0.3 W/LED [MFR] = 43 W/m |
| Min bend radius | not stated | not stated | not stated |
| PCB colour / IP | white or black, IP30 | black for 144/m, IP30 | white, IP30 [MFR] |
| **Wall-height margin in V5** (13.0 mm) [CAD] | 3.0 mm total | **about 1.0 mm total** | **5.8 mm total** |
| LEDs on outer wall [CAD] | 21 (350.0 mm, 1.2 mm left for the joint) | 50 (347.2 mm, 4.0 mm left) | 50 (347.2 mm, 4.0 mm left) |
| Angular step per pixel | 17.1° | 7.2° | 7.2° |
| Local bend at r = 55.9 (bend taken in the gap between LED bodies) | gap 11.7 mm → local radius about 39 mm | gap 1.9 mm → about 15 mm | gap 3.4 mm → about 27 mm |
| Fit verdict | Fits | Marginal; no room for print tolerance, solder blobs or wires | **Fits with margin** |
| Smoothness of chase/charge | Stepped | Smooth | Smooth |
| Hot spots through cover | Possible scalloping; pitch 16.7 mm vs about 24 mm throw | Low | Low |
| Brightness per pixel | High (5050) | High | Lower per pixel (3535) [ASSUMED], more pixels |

Bend check: every option bends in its flexible direction on the wall, with the LEDs on the inside of the curve. A generic 144/m strip specification gives "radius greater than 1 cm" [3P]; all three stay above that by calculation. This is not a BTF figure, so the sample must be seated in the printed ring before committing (T-1).

Why option 3 beats option 2: same pixel count and pitch, but 4.8 mm more height margin and nearly twice the flexible gap between LEDs. Why it beats option 1: 2.4× the angular resolution, which is what makes a rotating highlight or a circular fill read as motion on a ring this size.

## Installation geometry for the ring

- Strip on the **outer wall**, PCB against the wall, LEDs facing the centre, sitting on or just above the floor. 50 LEDs = 347.2 mm leaves a 4 mm gap at the joint for the solder pads.
- Put the strip's start at the notch (about 270°). Run the three wires across the floor to the inner-wall notch and down the passage. Connectorise on the cavity side; a connector housing is unlikely to pass the 7 mm passage.
- Cut the 50-LED piece from within one 0.5 m section so no factory joint sits on the curve.
- Light is indirect (LEDs face sideways, cover is above), which hides individual emitters. Most of the cover is under the gauge; the visible glow is a halo about 4–5 mm wide around the gauge unless the gauge is printed translucent.
- A white or light interior in the trough will help. LW-PLA in a light colour is fine.

## Hand strip and crystal

| Zone | CAD | With the 7.2 mm 144/m strip |
|---|---|---|
| Hand window | 13.3 mm wide × 238 mm long, 1.56 mm thick insert; **currently solid in V5**, about 7.9 mm of wall under it | 34 LEDs (236 mm). Needs a channel about 8.5 mm wide under the window |
| Crystal | 37 × 10 × 65 mm insert; **currently solid in V5**, about 6.7 mm of wall under it | 9 LEDs (62.5 mm) in a pocket behind the crystal |

- The "about 2.7 mm narrow accent strip" in the earlier BOM is not needed: the window is 13.3 mm wide, so the 7.2 mm strip fits and keeps the chain uniform.
- Direct view through a thin window shows individual LEDs unless the LED-to-diffuser distance is close to the pitch. At 144/m that is about 7 mm; at 60/m it would be about 17 mm, which the wall cannot give. So 144/m is the right density here too.
- Separate LED types are not preferable. Mixing types on one data line adds colour-order and timing risk for no gain.

## Updated counts and power

Per arm: **ring 50 + hand 34 + crystal 9 = 93 pixels** (was 21 + 14 + 4 = 39). Ring only: 50.

| Case | Pixels | Worst case at 0.3 W/LED [MFR] | Notes |
|---|---|---|---|
| Ring only | 50 | 3.0 A / 15 W | |
| Full arm | 93 | 5.6 A / 28 W | exceeds a 3 A bank and fuse if unlimited |

- Worst case is all pixels full white, which the effects never use. Blue/cyan at about 45 % brightness is roughly 15–20 mA per lit pixel [ASSUMED], so about 0.8–1.0 A for a fully lit ring and less for chase effects.
- **The WLED current limiter is mandatory with 93 pixels.** Recommended starting limit: **1000 mA per arm**, raised only after the temperature test. Keep the 3 A fuse: if the limiter is misconfigured the fuse opens.
- Heat depends on the brightness chosen, not on the density. 1000 mA is 5 W; in a closed PLA trough that still needs the 30-minute temperature check. Target: no surface above about 45 °C.
- Power bank: unchanged (5 V, 3 A capable, low-current mode).

## Controller, wiring and firmware impact

- **Compatibility:** WS2812B 3535 uses the same single-wire protocol as the 5050 part. WLED LED type "WS281x", colour order GRB to be confirmed on the sample. 93 pixels is trivial for any ESP32.
- **Wiring:** unchanged in principle. Level shifter and 330–470 Ω series resistor stay. Feed 5 V to each zone in parallel as already drawn. Order of the data chain: ring → hand → crystal.
- **WLED:** LED count 93; segments ring `[0,50)`, hand `[50,84)`, crystal `[84,93)`; current limit 1000 mA. A remapped copy of the preset file is in `wled/presets_144.json` (the original `presets.json` for the 39-pixel layout is untouched). Neither file has been loaded on a device.
- **Standalone firmware:** `firmware/src/main.cpp` would need `RING=50, HAND=34, CRYSTAL=9`. Not edited.
- **Ring only at first:** set LED count 50 and one segment `[0,50)`.

## CAD changes

- **Ring: none.** The V5 trough takes option 3 (and option 1) as drawn.
- **Hand strip and crystal: required, not approved, not started.** A channel under the hand window and a pocket behind the crystal, each with a wire path to the cavity, and both inserts split back out as separate translucent parts. The centre seam (X = 211) runs along the hand window, which must be handled in that design.
- Optional: magnet pockets to retain the gauge over the cover.

## Where to buy — verification status

| Item | Source | Status |
|---|---|---|
| Ultra-Narrow WS2812B, variant "3535 144LEDs 7.2mm IP30", 1 m or 2 m | https://www.btf-lighting.com/products/ultra-narrow-ws2812b-addressable-rgbic-led-strip | Product and specs verified on the manufacturer page. Ships from China; the page says the customer handles customs. Price seen: about $18 (1 m), $32 (2 m) |
| Same strip on Amazon.de | — | **Not found/verified.** Search Amazon.de for `BTF-LIGHTING WS2812B 3535 144 7.2mm`; only buy a listing that states 3535, 144 LEDs/m and 7.2 mm |
| WS2812B 5050 144/m, 1 m, IP30 (option 2) | https://www.amazon.de/dp/B01CDTEJR0 | Listing verified to exist; not recommended |
| WS2812B 5050 60/m, 1 m, IP30 (option 1, fallback) | Amazon.de BTF-LIGHTING store | Exact listing not verified; choose 5 V, 60 LEDs/m, IP30, 1 m |

## Smallest sample order

1. **2 m of option 3** (one metre per arm covers ring + hand + crystal: 93 of 144 LEDs). If only testing first: 1 m.
2. **1 m of option 1** from Amazon.de as the fast-arriving fallback and for the first electronics bench test.

## Physical tests still required

1. **T-1 ring fit:** print the original `Circle_Light.stl` and the V5 cover. Measure printed wall height and trough width. Seat 50 LEDs of option 3 on the outer wall; check it lies flat without lifting, the joint gap, wire exit through the notch, and that the cover seats fully.
2. **Bend/stress:** leave the strip seated 24 h, then power it and flex-check for dead pixels.
3. **Diffusion:** view the halo with the gauge in place at working brightness; compare option 3 against option 1.
4. **Electrical:** colour order, measured current at the 1000 mA limit and at each preset, power-bank auto-off behaviour.
5. **Thermal:** 30 minutes at the chosen limit with the cover and gauge on; measure the trough wall and cover.
6. **Preset check on the device:** effect IDs, segment bounds, button mapping, flash behaviour.

Sources consulted: btf-lighting.com ultra-narrow product page and WS2812B 5 V collection; BTF-LIGHTING WS2812B ECO and WS2812B listings on Amazon.de; buyer reports on the 144/m 5050 width; superlightingled.com and ledyilighting.com generic 144/m specifications.

## Correction and update — 2026-11-15

- Earlier text said V5 had no LED channel for the hand strip or crystal. On closer inspection the original design has a sealed channel under the hand lens (about 11.3 × 2.2 mm) and a light well under the crystal. **V5.1 opens both** (owner-approved); see the V5.1 section of the V5 README.
- The crystal is lit by the hand strip passing under its well. Per-arm count is now **84** (ring 50 + hand 34; the last 11 hand pixels are under the crystal). Worst case at 0.3 W/LED is 5.0 A; the 1000 mA WLED limit still applies.
- The channel is 11.3 mm wide, so the 7.2 mm strip fits; a 10 mm strip would also fit there.
- **V5.2 correction:** hand strip is 33 LEDs (channel length 232.5 mm), so 83 per arm. Modelled as solids, both strips fit with zero interference: 5.6 mm clear under the cover, 2.0 mm under the hand lens.
