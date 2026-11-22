# Left arm from spare right shells (V5.4 "spare-match", updated 2026-11-22)

Spare printed right shells: **R_01, R_02, R_05**. Their mirror twins on the left arm:

| Spare | Becomes | Seam-face match (area mismatch) |
|---|---|---|
| R_01 | **L_03** | 0.2–1.7 % |
| R_02 | **L_04** | 0.6–1.8 % |
| R_05 | **L_06** | 0.2–2.0 % |

The spares meet each other correctly (they are real neighbours on the right arm). Only the dowel holes toward the new left parts differ, so those new parts get their holes moved:

## Left arm parts list
| Left slot | Use |
|---|---|
| L_03, L_04, L_06 | **spares R_01, R_02, R_05** (already printed) |
| L_08 | `L_08_LightBand_Rear_RingCarrier_V5_2_SPAREMATCH.3mf` (1 hole moved, seam with L_04) |
| L_09 | `L_09_LightBand_Rear_Right_V5_SPAREMATCH.3mf` (holes moved on seams with L_06 and L_04; fits the A1 Mini) |
| L_11 | `L_11_Wrist_Right_V5_1_SPAREMATCH.3mf` (holes moved, seam with L_06) |
| L_01, L_02, L_05, L_07, L_10, L_12 | normal left files from the named print pack |
| L_13 | `L_13_Knuckles_Right_V5_3` (thumb socket) |

**Do not print** the normal L_03, L_04, L_06, L_08, L_09 or L_11. Use the earlier `L_04_..._SPAREMATCH` from the first version of this zip: no longer needed (spare R_02 replaces it).

One hole of spare R_02 (toward L_09) has no partner: there was not enough material in L_09 there. Leave that hole empty, or glue a short dowel stub in flush; the L_04–L_09 seam still has one dowel plus epoxy.

All moved holes: 6.4 mm × 16 mm, fully in material, walls ≥ 1.2 mm; old holes filled; sizes, outer shape, print orientation unchanged (computed, not printed). Log: `V5_4_spare_twins_log.json`. Script: `Build_Scripts/v5_4_spare_twins.py`.
