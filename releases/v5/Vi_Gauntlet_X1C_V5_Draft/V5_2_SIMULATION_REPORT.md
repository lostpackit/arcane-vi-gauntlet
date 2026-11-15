# V5.2 digital simulation report (Claude, 2026-11-15)

**What this is:** computed checks on the model files, standing in for print and fit tests that cannot be done here. **Nothing was printed, wired or sliced in Bambu Studio.** A pass here means "no problem found in the geometry", not "proven on hardware".

## 1. Models re-checked from the repository

- The 13 right shells were loaded from the repo (shell 08 from the V5.2 build), returned to assembled coordinates and compared with the verified build: maximum deviation **0.0 mm**.
- Left shells are exact mirrors (checked at build).

## 2. Assembly simulation

| Check | Result |
|---|---|
| Shell-to-shell interference, all 78 pairs | none |
| 13 shells joined | one connected body, no gaps or overlaps in volume |
| Cover (seated 0.25 mm below its modelled height) | interference 0.0 mm³ |
| Gauge | interference 0.0 mm³ |
| Crystal | interference 0.0 mm³, minimum gap 0.15 mm |
| Hand lens A, B | interference 0.0 / 0.0 mm³ |
| Handle, 250 mm | interference 0.0 mm³, minimum gap 0.25 mm |
| 57 dowels, 6 × 30 mm | interference 0.0 mm³, minimum gap 0.2 mm; no socket shallower than 15 mm per side |
| Cover against gauge | 1.93 mm³ contact (they touch by design) |

## 3. LED strip fit, modelled as solids

| Strip | Model | Result |
|---|---|---|
| Ring | 7.2 × 2.2 mm band on the trough outer wall, joint gap at the notch | interference 0.0 mm³; **5.56 mm** clear below the cover |
| Hand | 229 × 7.2 × 2.2 mm (33 LEDs) on the channel floor | interference 0.0 mm³; **2.0 mm** below the lens |

- Trough outer wall fitted as a circle: radius 55.87 mm, residual 0.01 mm.
- **Correction:** the deepened channel is 232.5 mm long, so the hand strip is **33 LEDs, not 34**. A 34-LED strip modelled at 236 mm collided with the channel ends. Per-arm total is **83** (ring 50 + hand 33).

## 4. Wire path

Largest sphere that can pass, with cover and gauge in place:

| Route | V5.1 | V5.2 |
|---|---|---|
| Ring trough → hand LED channel | **2.0 mm** (too small for three wires) | **4.0 mm** |
| Ring trough → arm cavity | 11.0 mm | 11.0 mm |

V5.2 fix: a 9 mm wide wire slot at trough-floor level through the notch into the channel. It removes 3 mm³ of leftover shelf in shell 08 only.

## 5. Finger fit (audit issue C-3)

The finger parts that touch the knuckle block are the finger core (first segment) and the slot "piece". Both are the same geometry in the 3MF you are printing and in the assembled reference: printable finger core vs the three assembled core segments, in cm³: fore 288.88 / 288.85, little 274.95 / 274.91, ring 305.64 / 305.62, middle 305.13 / 305.37 (0.24 apart, so possibly a small revision); the slot pieces match to 0.03 cm³ or better. Sampling their surfaces against V5.1 shells 12/13 in assembled position:

| Finger | Core: surface inside shell | Core: typical running gap | Slot piece: deepest overlap |
|---|---|---|---|
| fore | 0.0 % | 1.8 mm | 0.03 mm |
| middle | 0.0 % | 0.82 mm | 0.13 mm |
| ring | 0.1 % | 0.83 mm | 0.08 mm |
| little | 0.1 % | 0.84 mm | 0.15 mm |

- Cores clear the shells with about 0.8–1.8 mm running gap. Slot pieces overlap by at most 0.15 mm, a snug press fit as designed.
- So the fingers being printed should seat in V5.1 shells 12/13. The printable 3MF `Fingers_Base` is a different revision of the base, but the fingers match the base that is fused into the shells.
- Limits: volume match is strong evidence, not proof, that the printed cores are identical; hinge action, string pull and the armour plates were not simulated. The coupon print is still the confirmation.

## 6. Print simulation (PrusaSlicer surrogate, lightweight settings, standard PLA)

| Part | Filament g | of which support g |
|---|---|---|
| R_08_LightBand_Rear_RingCarrier_V5_2 | 409.0 | 131.7 |
| R_10_Wrist_Left_V5_1 | 284.5 | 29.5 |
| R_11_Wrist_Right_V5_1 | 288.6 | 33.4 |
| R_12_Knuckles_Left_V5_1 | 489.1 | 109.1 |
| R_13_Knuckles_Right_V5_1 | 475.0 | 104.4 |
| R_Crystal_translucent | 3.9 | 0.3 |
| R_Hand_Lens_A_translucent_81mm | 1.9 | 0.0 |
| R_Hand_Lens_B_translucent_46mm | 1.1 | 0.0 |
| R_Ring_Light_Cover_translucent | 27.4 | 2.8 |
| Button_Pod_Handle_Clip_2x_12mm_tact_CONCEPT | 7.2 | 0.0 |
| Electronics_Sled_80x45_CONCEPT | 8.8 | 0.0 |

All 11 parts sliced without geometry errors. Unsupported-branch warnings (build-plate-only supports): R_08_LightBand_Rear_RingCarrier_V5_2, R_12_Knuckles_Left_V5_1, R_13_Knuckles_Right_V5_1.

## 7. What simulation cannot tell you

Real filament behaviour (LW-PLA foaming, dowel-hole shrinkage, warping), layer adhesion and strength, the true strip dimensions and bend behaviour, light diffusion and hot spots, current and temperature, hinge and string action, comfort and weight in the hand. Those stay as open GitHub issues.
