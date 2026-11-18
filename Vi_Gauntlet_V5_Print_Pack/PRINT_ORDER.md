# Vi Gauntlet V5 — print pack and print order

Complete set of current files, one folder per printing step. Built by Claude, 2026-11-17. Every file matches the checksums in the repo (`SHA256_MANIFEST.txt` here).

**Status: draft, unprinted.** Nothing has been sliced in Bambu Studio or printed. Steps 1–2 are the tests; only carry on to the big shells if they pass.

Filament figures are from a stand-in slicer at 2 walls, 8 % gyroid, standard PLA. Lightweight PLA will come out roughly half to two-thirds of that.

## Materials

| Parts | Material |
|---|---|
| All shells (01–13) | Lightweight PLA |
| Ring cover, crystal, hand lenses | Clear or translucent standard PLA |
| Gauge | Any PLA (translucent gives more glow) |
| Handle | Standard PLA or PETG, **not** lightweight PLA |
| Button pod, electronics sled | Standard PLA or PETG |

## Step 1 — Test prints (A1 Mini) — `1_Test_Prints_A1_Mini/`

| File | Size (mm) | ≈ g | What it tells you |
|---|---|---|---|
| `R_Ring_Light_Cover_translucent` | 118 × 118 × 9 | 27 | Diffusion and fit of the light cover. This is the real cover; keep it |
| `T2_Knuckle_Slot_Forefinger_Coupon` | 105 × 115 × 75 | 121 | Does a printed forefinger seat and curl? Throwaway test piece |
| `OPTIONAL_Circle_Light_original_standin.stl` | 130 × 130 × 25 | 78 | Cheap stand-in for the ring trough to test the LED strip before printing shell 08. Skip it if you'd rather print shell 08 directly |

## Step 2 — Right arm, ring section — `2_Right_Arm_Ring_Section/`

| Order | File | Size (mm) | Printer | ≈ g |
|---|---|---|---|---|
| 1 | `R_07_LightBand_Rear_Left_V5` | 100 × 165 × 66 | A1 Mini (brim ≤ 7 mm) or X1C | 105 |
| 2 | `R_09_LightBand_Rear_Right_V5` | 122 × 165 × 72 | A1 Mini (brim ≤ 7 mm) or X1C | 149 |
| 3 | `R_08_LightBand_Rear_RingCarrier_V5_2` | 200 × 165 × 84 | X1C | 409 |

Before printing 08: try 6 × 30 mm dowels in the sockets of 07 and 09. If they're tight in lightweight PLA, adjust before going on.

## Step 3 — Right arm inserts — `3_Right_Arm_Inserts/`

| File | Size (mm) | Printer | ≈ g | Material |
|---|---|---|---|---|
| `R_Pressure_Gauge_Insert` | 109 × 185 × 33 | X1C | 50 | any PLA |
| `R_Crystal_translucent` | 65 × 37 × 6 | A1 Mini | 4 | translucent |
| `R_Hand_Lens_A_translucent_81mm` | 81 × 13 × 1.6 | A1 Mini | 2 | translucent |
| `R_Hand_Lens_B_translucent_46mm` | 46 × 13 × 1.6 | A1 Mini | 1 | translucent |
| `Handle_OnePiece_18p8x250` | 250 × 19 × 19 | X1C | 23 | standard PLA/PETG; **print twice** (one per arm) |

## Step 4 — Right arm wrist — `4_Right_Arm_Wrist/`

| File | Size (mm) | Printer | ≈ g |
|---|---|---|---|
| `R_10_Wrist_Left_V5_1` | 181 × 225 × 90 | X1C | 285 |
| `R_11_Wrist_Right_V5_1` | 181 × 225 × 90 | X1C | 289 |

The handle goes into its sockets **before** 10 and 11 are joined; it is trapped between them.

## Step 5 — Right arm light band front and cuff — `5_Right_Arm_LightBand_Front_and_Cuff/`

| File | Size (mm) | Printer | ≈ g |
|---|---|---|---|
| `R_05_LightBand_Front_Left_V5` | 211 × 165 × 178 | X1C | 498 |
| `R_06_LightBand_Front_Right_V5` | 211 × 165 × 178 | X1C | 496 |
| `R_01_Cuff_Left_Front_V5` | 210 × 147 × 71 | X1C | 121 |
| `R_02_Cuff_Left_Rear_V5` | 210 × 147 × 145 | X1C | 202 |
| `R_03_Cuff_Right_Front_V5` | 209 × 147 × 71 | X1C | 120 |
| `R_04_Cuff_Right_Rear_V5` | 209 × 147 × 145 | X1C | 200 |

05 and 06 are the biggest and tallest parts; check the support preview in Bambu Studio first.

## Step 6 — Right arm knuckles — `6_Right_Arm_Knuckles_AFTER_FINGER_TEST/`

| File | Size (mm) | Printer | ≈ g |
|---|---|---|---|
| `R_12_Knuckles_Left_V5_1` | 200 × 199 × 166 | X1C | 489 |
| `R_13_Knuckles_Right_V5_1` | 200 × 199 × 158 | X1C | 475 |

Only after the step 1 finger coupon passes.

## Step 7 — Left arm — `7_Left_Arm/`

Same parts mirrored (`L_` files): repeat steps 2–6 in the same order. The left cover, gauge, crystal and lenses are here too. Use the second handle print.

Left shells keep the right arm's side names (`L_01_Cuff_Left_Front` is physically on the other side). Label parts as they come off the printer.

## Step 8 — Electronics mounts — `8_Electronics_Mounts_CONCEPT/`

Print once the hardware has arrived, and check against it: `Button_Pod_Handle_Clip_2x_12mm_tact_CONCEPT` (7 g, snaps onto the handle, holds two 12 × 12 mm switches) and `Electronics_Sled_80x45_CONCEPT` (9 g, tray for controller and level shifter). One of each per arm.

## Optional — `9_Optional/`

`Dowel_Peg_5p9x30_optional`: printable dowel if you don't have wooden 6 × 30 mm dowels (57 per arm).

## Totals per arm (stand-in slicer, standard PLA)

Shells about 3,840 g including about 760 g of supports; inserts and handle about 80 g. Lightweight PLA for the shells brings the finished shells to very roughly 1.6–2.1 kg per arm.
