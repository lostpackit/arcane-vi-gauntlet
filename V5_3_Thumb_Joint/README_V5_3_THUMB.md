> **WITHDRAWN 2026-11-25 (Claude, Mechanics):** V5.3 was built on the stock Thumb_Base, which is the LEFT-hand part, forced onto the right shell. Socket and dowel holes are wrong. Do not print `L_13_..._V5_3`; print `L_13_Knuckles_Right_V5_1`. The printed V5.3 bases are swapped (L_ file = right hand). See [V5_5_Thumb_Fix/README_V5_5_THUMB_FIX.md](../releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_5_Thumb_Fix/README_V5_5_THUMB_FIX.md).

# V5.3 thumb joint: R/L shell 13 + thumb base with dowel

Owner-approved 2026-11-22. Replaces `R_13_Knuckles_Right_V5_1` and `L_13_Knuckles_Right_V5_1`, and the stock `Thumb_Base`.

| File | Printer | Material | Notes |
|---|---|---|---|
| `R_13_Knuckles_Right_V5_3.3mf` | X1C | LW-PLA as other shells; 3 walls recommended | Same size and print orientation as V5.1; adds the thumb socket + one 6.4 mm dowel hole (16 mm deep) |
| `L_13_Knuckles_Right_V5_3.3mf` | X1C | same | Exact mirror of the right |
| `R_Thumb_Base_V5_3_dowel.3mf` | A1 Mini or X1C | **Standard PLA or PETG**, 4 walls, ~30 % infill (load-bearing) | Same as stock Thumb_Base, same print orientation, plus one 6.4 mm dowel hole (16 mm deep) |
| `L_Thumb_Base_V5_3_dowel.3mf` | A1 Mini or X1C | same | Mirror of the right |

What changed (computed, not physically tested):
- Before: the stock thumb base touched shell 13 on only ~2.6 cm² and overlapped it by ~6.6 cm³, so it could not seat.
- After: socket with 0.25 mm clearance; zero overlap; ~15.4 cm² of the base sits within 0.3 mm of the socket (~6× the glue area) and the socket locks it against twisting.
- One 6 × 30 mm wooden dowel: 16 mm hole in the shell + 16 mm hole in the base. Only one spot has enough solid material all round (~50 mm in the base, ~57 mm in the shell along the dowel), so it is one dowel, not two.
- The base slides into the socket along one direction, roughly straight out from the side of the hand (the dowel sets the direction).

Assembly: dry-fit first. Then epoxy (UHU Plus Schnellfest) the dowel into the shell hole, coat socket + dowel end, push the base on fully, hold or tape 10 min, leave overnight before loading the thumb.

Build: `Build_Scripts/v5_3_thumb.py`; numbers in `V5_3_thumb_build_log.json`.
