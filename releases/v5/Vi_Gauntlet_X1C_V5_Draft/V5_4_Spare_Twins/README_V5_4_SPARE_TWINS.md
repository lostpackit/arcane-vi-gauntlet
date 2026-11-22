# Left arm from spare right shells (V5.4 "spare-match", 2026-11-22)

You have spare printed **R_05** and **R_01**. Their mirror twins on the left arm are **L_06** and **L_03**:
seam faces match within 1–2 % of their area (a sanding/filler job), and about 96–98 % of the surface is within 0.6 mm.
Only the dowel holes differ. So the left parts that meet the spares get their dowel holes moved to match them.

## Left arm parts list with the spares
| Left slot | Use | Note |
|---|---|---|
| L_03 | **spare R_01** (already printed) | |
| L_06 | **spare R_05** (already printed) | |
| L_04 | `L_04_Cuff_Right_Rear_V5_SPAREMATCH.3mf` | holes moved on its seams with L_03 and L_06 |
| L_09 | `L_09_LightBand_Rear_Right_V5_SPAREMATCH.3mf` | holes moved on its seam with L_06 |
| L_11 | `L_11_Wrist_Right_V5_1_SPAREMATCH.3mf` | holes moved on its seam with L_06 |
| L_01, L_02, L_05, L_07, L_10, L_12 | normal left files from the named print pack | |
| L_08 | `L_08_..._V5_2` (named print pack) | |
| L_13 | `L_13_Knuckles_Right_V5_3` (thumb socket) | |

Do **not** print the normal L_04, L_09 or L_11 if you use the spares, or the dowels will not line up.

What changed (computed, not printed): old holes on those seams filled, new 6.4 mm × 16 mm holes at the mirrored spare positions; every new hole sits fully in material with ≥1.2 mm walls; part sizes, outer shape and print orientation unchanged. Details: `V5_4_spare_twins_log.json`. Script: `Build_Scripts/v5_4_spare_twins.py`.

Saves about 24 h of printing (surrogate estimate for R_05 + R_01; your X1C is faster).
