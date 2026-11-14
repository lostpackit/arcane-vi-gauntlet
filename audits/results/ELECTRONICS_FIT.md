# LED and electronics fit

Independent audit by Claude, 2026-11-14. Every dimension is marked **[MEASURED]** (computed from CAD in this repo) or **[ASSUMED]** (typical catalogue value, not checked against a datasheet or sample). No hardware exists yet and nothing was physically fitted.

## 1. What the CAD actually provides

### 1.1 Ring light (`Circle_Light.stl`, original part) — [MEASURED]

Ring-axis frame; the axis is tilted 1.9° from assembled Y. Probes every 5° around the ring.

| Dimension | Value |
|---|---|
| Part outer diameter | 130.0 mm |
| Annular trough, inner wall radius | 28.8 mm (probe scatter ±0.33) |
| Trough outer wall radius | 55.9 mm (±0.33) |
| **Trough radial width** | **27.1 mm** |
| Trough floor to rim / cover seat | −3.46 → +9.8, **13.3 mm deep** |
| Inner wall circumference | 181 mm |
| Outer wall circumference | 351 mm |
| Mid-trough circumference (r = 42.35) | 266 mm |
| Wire notch, inner wall | 14.1 mm wide, 256.5°–284.5°, floor to rim |
| Wire notch, outer wall | 13.2 mm wide, 263.5°–277°, about 3.5 mm tall (h ≤ 0) |
| Passage from trough to arm cavity | continuous for a 7 mm cube probe (1 mm voxel flood fill) |

### 1.2 Cover (`Circle_Light_Cover.stl`) — [MEASURED]

- 118.4 mm diameter, 10.5 mm overall height including a central cup that drops into the ring's hub.
- About 4.3 mm thick over the trough (h 9.8 → 14.1). Axis within 0.08° of the ring axis; centre offset 0.4 mm as placed in the sizing model.
- Radial clearance between cover and its pocket was **not resolved** by this audit. It needs the printed coupon (T-1).

### 1.3 V4 shell 08 — [MEASURED]

Same trough dimensions, but closed: solid ceiling at h = 9.81 and solid above it to h ≈ 26. The cover's volume is 99.7 % solid. **No LED can be installed in shell 08 as released** (ISSUES C-1).

### 1.4 Other light features in the original — [MEASURED]

- `Glove_Light_Strip.stl`: 13.3 mm wide × 1.56 mm thick × 238 mm long window on the back of the hand (X 204–217, Z 286–524). Fused solid in V4.
- `Crystal.stl`: 37 × 10 × 65 mm. Fused solid in V4 and cut at X=211.

### 1.5 What does not exist in the CAD

- No controller pocket, battery bay, switch holes or cable clips in either the 3MF parts examined or V4.
- The supplied `LED_Tape_Test_Channel_8p6mm/10p6mm` coupons correspond to no feature of the gauntlet.

## 2. Does an 8 mm or 10 mm strip fit?

This is answered for the **original ring part**. It is moot for V4 shell 08 until C-1 is fixed.

| Mounting | Strip width limit from CAD | 8 mm | 10 mm | 12 mm | Bend |
|---|---|---|---|---|---|
| On the **outer wall**, LEDs facing inward | wall height 13.3 mm [MEASURED] | fits, 5.3 mm spare | fits, 3.3 mm spare | 1.3 mm spare, too tight | r = 55.9 mm, easy for any flex strip |
| On the **inner wall**, LEDs facing outward | 13.3 mm | fits | fits | too tight | r = 28.8 mm; above the roughly 15–20 mm minimum typical of flex strips [ASSUMED] |
| Flat on the **floor**, LEDs facing the cover | 27.1 mm radial width | — | — | — | not possible with a straight flex strip (it cannot bend edgewise); needs a ring PCB or S-shape strip |
| Ring PCB on the floor | annulus Ø57.6–Ø111.8 [MEASURED] | PCB must have ID ≥ 58 mm and OD ≤ 111 mm, less print tolerance | | | — |

Strip thickness is not a constraint: radial room is 27 mm, against roughly 2–3 mm for a bare 5050 strip [ASSUMED].

Stated plainly:
- **Supported by measurement:** a bare (IP30) strip on 8 mm or 10 mm PCB fits the trough wall by height with margin, and the bend radius on the outer wall is comfortable.
- **Not supported:** 12 mm strips, and silicone-sleeved (IP65/67) versions of 10 mm strips, which are typically about 12 mm wide [ASSUMED].
- **Not yet proven:** printed wall height, solder-pad and wire bulk at the notch, and cover closure over the wiring. Do not order a quantity of strip until T-1 is done with a sample.

## 3. Recommended LED technology

Preference order, pending T-1:

1. **SK6812 or WS2812B, 5 V, bare IP30, 10 mm PCB, 60 LED/m**, on the outer wall facing inward. About 21 pixels around 351 mm. Indirect light onto a 4.3 mm diffuser hides hot spots, and 21 pixels is enough for chase, pulse and "charge-up" effects.
2. Same family at **144 LED/m** for smoother motion: about 50 pixels. Roughly 2.4× the current.
3. **SK6812 RGBW** if a clean white/ice-blue is wanted; same footprint [ASSUMED].
4. A ring PCB only if a specific product's ID/OD is confirmed against the annulus above.

Avoid 12 V/24 V pixel strips (WS2811/WS2815): they add a converter or a second rail for no benefit at this pixel count.

For the light-strip window and crystal (if V5 restores them): the same strip, a 238 mm run is about 14 pixels at 60/m, and 2–4 pixels behind the crystal, chained on the same data line.

## 4. Controller

- **ESP32-class board in the XIAO form factor** (Seeed XIAO ESP32-C3 or ESP32-S3), about 21 × 17.5–17.8 mm per vendor listings [ASSUMED from listings, not measured]. Small enough to mount on a removable sled; USB-C for flashing in place.
- **Firmware: WLED.** It provides addressable effects, presets and playlists, a brightness/current limiter, and multiple physical buttons with short/long/double-press actions mapped to presets (see WLED docs, kno.wled.ge → Features → Macros/Buttons). No custom code is needed for effect selection.
- One controller per gauntlet. Syncing the two arms is possible over Wi-Fi with WLED's sync feature; treat that as optional.
- Data line: 330–470 Ω series resistor at the first pixel, and either a 74AHCT125 level shifter or a short (< 15 cm) lead to the first pixel. 1000 µF across 5 V/GND at the strip.

## 5. Buttons

The wearer's hand is on the handle (Z ≈ 376) with fingers in the pull rings, so the thumb is the only free digit.

- **Two momentary buttons** reachable by the thumb of the gripping hand: on a small pod at one end of the handle, or on the inner wall beside it.
  - Button A: short = next effect preset, long = lights on/off.
  - Button B: short = brightness step, double = palette/colour.
- 12 × 12 mm tactile switches with caps, or 12 mm panel momentary switches [ASSUMED sizes]. Wire to GPIO and GND; WLED uses internal pull-ups.
- Avoid assigning the lights-off action to WLED's button 0 long-press beyond 5 s, which opens the setup access point.
- No holes should be drilled until the handle design (C-4) and the V5 knuckle layout are settled.

## 6. Power

Budget [ESTIMATE; 60 mA per RGB pixel at full white is the usual planning figure]:

| Configuration | Pixels | Worst case | Typical animated use at about 40 % |
|---|---|---|---|
| Ring only, 60/m | 21 | 1.3 A | 0.3–0.5 A |
| Ring, 144/m | 50 | 3.0 A | 0.7–1.2 A |
| Ring 60/m + light strip + crystal | about 39 | 2.3 A | 0.5–0.9 A |

Recommended arrangement:

- **A commercial 5 V USB power bank** (5,000–10,000 mAh) rather than bare lithium cells. It brings its own cell protection, charging and fuel gauge, charges outside the prop, and can be swapped. Choose one that does not auto-shut-off at low current, or that has a low-current mode.
- Location: at the **cuff opening** on a removable hook-and-loop or printed sled on the inner wall, or off-arm on a belt with a cable up the sleeve. The cuff interior is the only place that stays reachable after bonding.
- Set WLED's current limit to about 1.5 A (2 A if the bank and cable support it). This caps worst-case draw whatever the effect.
- Inline 3 A blade or polyfuse at the pack output; 20–22 AWG silicone wire for 5 V/GND (run from cuff to ring is roughly 250–350 mm); a 3-pin JST-SM or similar connector at the ring so shell and electronics can be separated. The 7 mm passage from the trough will pass three wires but probably **not** a connector housing [ASSUMED housing size]: connectorise on the cavity side.
- Strain-relieve every cable where it leaves a moving or removable part.

Estimated run time with a 5,000 mAh bank (about 3 Ah usable at 5 V): 6–10 h for the 21-pixel ring at typical brightness. [ESTIMATE]

Safety: no bare LiPo pouch cells against the forearm, no charging while worn, keep the pack removable, and verify nothing exceeds a comfortable touch temperature after 30 minutes at the chosen current limit.

## 7. Measurements blocked by missing hardware

- Actual strip PCB width, thickness, pad/wire bulk and minimum bend radius.
- Cover closure over installed strip and wires; cover retention and removal force.
- Diffusion quality through a 4.3 mm cover in the chosen filament.
- Controller, button and pack dimensions; sled and pocket design.
- Current draw and temperature at the chosen limit.

## 8. Gate status

- **Lighting: FAIL for V4 as released** (sealed chamber). For the original ring part, strip fit is supported by CAD and awaits T-1.
- **Electronics: BLOCKED** (no hardware selected, no mounting geometry exists).

## Addendum — 2026-11-14: strip selection for V5

The 60 LEDs/m preference in section 3 is superseded for visual quality by `electronics/LED_STRIP_COMPARISON.md`: BTF-LIGHTING Ultra-Narrow WS2812B 3535, 144 LEDs/m, 7.2 mm, 50 px on the outer wall. V5 usable wall height is about 13.0 mm (cover seat is 0.3 mm lower than in the original part). The 12 mm-class 5050 144/m strip is rejected. Gate status is unchanged: Lighting needs T-1; Electronics BLOCKED.
