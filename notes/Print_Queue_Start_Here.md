---
type: start-here
tags: [printing, schedule, start-here]
updated: 2026-11-24
---

# Print queue: start here (deadline 2026-11-28, both arms working + painted)

Owned by the **Print queue** conversation. Everything under "Status" is the owner's report; nothing here was seen by Claude except the photos of the right arm (2026-11-22).

## Status (owner reports, to 2026-11-24 23:51)
- **Right arm: all shells printed.** R_13 = `R_13_Knuckles_Right_V5_3` (thumb socket) was the last print, finishing Tue 11-24 23:36. R_06 (plain/palm side, mirror of R_05) was the other late one.
- Fingers except thumbs printed + primed; **one more thumb: status not reported**. Transparent parts done. **Thumb bases (R and L `*_Thumb_Base_V5_3_dowel`) printed.**
- **Gauges (transparent PLA) and 2 button pods (transparent PLA) printed and tested fine; the transparent pods are final** (no PETG pods).
- **Handles: 18 mm beech rod, not printed** (owner 11-24).
- **Left arm:** spares R_01 / R_02 / R_05 = L_03 / L_04 / L_06 (printed). **L_09 SPAREMATCH printed (11-24).** Nothing else printed.
- **Material (owner decision 11-24):** bad batch of PLA Lite clogged both heads, so print times from those prints are not usable. From now on **SUNLU matte black standard PLA** (4 spools in hand, same-day delivery for more) unless PETG is needed. Profile: **3 walls, 3 % infill** (owner compared PLA vs PLA Lite: little weight difference).

## Left arm (10 new shells; 3 slots filled by spare right shells)
| Slot | Print / use | Printer | Status |
|---|---|---|---|
| L_01 | `L_01_Cuff_Left_Front_V5` | X1C | to print |
| L_02 | `L_02_Cuff_Left_Rear_V5` | X1C | to print |
| L_03 / L_04 / L_06 | **spare R_01 / R_02 / R_05** (no L_03/04/06 file exists) | — | done |
| L_05 | `L_05_LightBand_Front_Left_V5` | X1C | to print |
| L_07 | `L_07_LightBand_Rear_Left_V5` (plain file) | A1 Mini | to print (next A1 plate) |
| L_08 | `L_08_LightBand_Rear_RingCarrier_V5_2_SPAREMATCH` | X1C | to print |
| L_09 | `L_09_LightBand_Rear_Right_V5_SPAREMATCH` | A1 Mini | **done** |
| L_10 | `L_10_Wrist_Left_V5_1` | X1C | to print |
| L_11 | `L_11_Wrist_Right_V5_1_SPAREMATCH` | X1C | to print |
| L_12 | `L_12_Knuckles_Left_V5_1` | X1C | to print |
| L_13 | `L_13_Knuckles_Right_V5_3` (thumb socket) | X1C | to print |
Files: `Vi_Gauntlet_V5_Print_Pack_named.zip` (plain files, correct part names), `V5_4_Left_Arm_Spare_Match_v2.zip` (SPAREMATCH), `V5_3_Thumb_Joint.zip` (R/L_13 V5_3, thumb bases). Repo copies are LFS pointers or missing (see HANDOFF "Owner upload needed").

## X1C schedule from Tue 11-24 23:55 (order follows the Finishing pipeline: rear band, cuff, front band, wrist, knuckles)
Hours = PrusaSlicer surrogate (2 walls, 8 %, standard PLA, supports included) and "×0.68" (Main's ratio from plate 21). **No Bambu Studio estimate exists yet for any left shell.** Assumes plates are swapped only 07:00-23:30.
| # | Plate | Surrogate h | ×0.68 h | Ends (surrogate) | Ends (×0.68) |
|---|---|---|---|---|---|
| 1 | L_08 | 16.1 | 10.9 | Wed 16:01 | Wed 10:51 |
| 2 | L_02 | 7.9 | 5.4 | Wed 23:55 | Wed 16:14 |
| 3 | L_01 | 4.8 | 3.3 | Thu 11:48 | Wed 19:30 |
| 4 | L_05 | 19.6 | 13.3 | Fri 07:24 | Thu 08:49 |
| 5 | L_10 | 11.2 | 7.6 | Fri 18:36 | Thu 16:26 |
| 6 | L_11 | 11.4 | 7.8 | Sat 06:00 | Fri 00:11 |
| 7 | L_12 | 19.3 | 13.1 | Sun 02:18 | Fri 20:07 |
| 8 | L_13 | 18.7 | 12.7 | Mon 01:42 | Sat 08:50 |
**Verdict:** total 109 h (surrogate) or 74 h (×0.68) against ~96 h to Sat 24:00 and ~48 h to Thu night. Even the optimistic column leaves no time for glue and paint on the last shells (Finishing needs the last glue by about Tue). The left arm will be a sub-assembly pipeline with a fallback finish; see the Finishing plan. **Needed to replace guesses:** the real Bambu Studio time of L_08 on SUNLU with the 3-wall, 3 % profile.

## A1 Mini queue
1. **L_07** (plain file, ~6 h guess, brim ≤ 7 mm), next.
2. Sled R/L + vented cover (Electronics conversation files; fit-check the sled on printed R_08 first). No estimate yet.
3. One more thumb (stock finger model), if not printed.
All A1 plates in SUNLU unless the design says PETG.

## Multiples and speed
- Nothing pairs on an X1C plate: cuffs are 210 mm wide, bands 200-225 mm. Only handles could have ridden along (now beech rod). Multiples do not shorten time; the only gain is fewer plate swaps and no idle gap overnight.
- Levers (web research 2026-11-23): layers 0.24-0.28 mm; grid or cross hatch instead of gyroid plus infill combination; keep 3 walls on L_13 (thumb socket); tree or hybrid supports on the build plate only; compare normal vs tree estimate per plate. A 0.6 mm nozzle gave little or no gain in Bambu Lab user reports; standard PLA removes LW-PLA's flow limit. **Orientation:** start from the file's own pose; keep supports out of string bores, thumb socket, dowel holes and visible faces (the T2 coupon's bore filled with support).
- Do not start a long plate unattended on filament suspected bad.

## Small parts
| Part | Status |
|---|---|
| Ring covers, crystals, lenses (both arms) | done |
| Gauges ×2, pods ×2 (transparent PLA) | done, tested (owner) |
| Thumb bases R + L | done |
| Sled + vented cover R/L | to print (A1) |
| Handles | beech rod (not printed) |
