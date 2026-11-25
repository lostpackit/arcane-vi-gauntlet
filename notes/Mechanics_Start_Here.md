---
type: start-here
tags: [mechanics, fingers, strings, thumb, handle, dowels, start-here]
updated: 2026-11-25
---

# Mechanics: Start Here (fingers, strings, thumb, handle, dowels)

Owned by the **Mechanics** conversation ([[Conversation_Starters]]). Any shell CAD change needs owner approval. Never record a print, fit or test as done unless the owner said so.

## Thumb (2026-11-25): read [V5.5 thumb fix](../releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_5_Thumb_Fix/README_V5_5_THUMB_FIX.md)
- **The stock `Thumb_Base` is the LEFT-hand part.** V5.3 forced it onto the right arm, so **V5.3 is withdrawn**.
- **L_13: print `L_13_Knuckles_Right_V5_1`, not V5_3.**
- The printed V5.3 bases are swapped: the **`L_` print goes on the RIGHT arm** and the **`R_` print on the LEFT arm**. Plug each one's stray outer-face hole with a dowel stub, cut it flush and fill. Clean V5.5 reprint files are available (LFS pending).
- Printed R_13 V5_3 is usable: the key pocket is intact. Fill the leftover V5.3 cavity and shell dowel hole where they show after the dry-fit.
- Joint = tapered key in the square pocket + UHU Plus Schnellfest. **No thumb dowel.**

## Status
| Item | State | Evidence |
|---|---|---|
| Finger fit in knuckle slot | **PASS (physical, 11-18)** | [[04_Test_Log]], #5 |
| Finger string pull / curl test | **NOT DONE.** Needed before knuckle glue | #5 |
| Real finger string bores | 4 bores, 3.3-3.85 mm, in shells 12/13 | `audits/results/ISSUES.md` C-5 |
| Thumb base fit | Computed: correct-hand base keys into the pocket. Not dry-fitted with the correct base yet | V5.5 README, #14 |
| Thumb string route | Lead: a 3.8 x 5.4 mm slanted bore beside the key pocket that lines up with the correct-pose base. Check with a wire | #14 |
| Dowel fit (seams) | Right arm assembled on dowels (owner photos 11-22) | [[04_Test_Log]] |
| Handle | 18 mm beech rod (owner 11-24); fit not reported | #7 |

## Next physical checks (owner)
1. Right arm: `L_` thumb-base print onto R_13, key into the square pocket. Does it sit without rocking? Where are gaps visible?
2. A 1 mm wire through the bore beside the key pocket: does it come out through the base? (thumb string or fixed)
3. Finger string test before any knuckle glue (#5).

## Open decisions for owner
- Thumb string-actuated or fixed (step 2 decides).
- Reprint clean bases or plug the printed ones.
