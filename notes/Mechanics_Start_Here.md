---
type: start-here
tags: [mechanics, fingers, strings, thumb, handle, dowels, start-here]
updated: 2026-11-22
---

# Mechanics: Start Here (fingers, strings, thumb, handle, dowels)

Owned by the **Mechanics** conversation ([[Conversation_Starters]]). Any shell CAD change needs owner approval. Never record a print, fit or test as done unless the owner said so.

## Status (2026-11-22)
| Item | State | Evidence |
|---|---|---|
| Finger fit in knuckle slot | **PASS (physical, 11-18):** printed finger fits the T2 coupon | [[04_Test_Log]], issue #5 |
| Finger **string pull / curl test** | **NOT DONE.** Coupon bore was filled by supports; no cord pull, free return, force or travel reported | issue #5 (open) |
| Real string bores | 4 bores, 3.3-3.85 mm, in shells 12/13, printing horizontally so they close up. PTFE 4 mm OD does not fit | `audits/results/ISSUES.md` C-5 |
| Thumb joint V5.3 | **Digital PASS only.** Socket in R/L_13 + one 6.4 x 16 mm dowel hole; base has the matching hole. Overlap 0, ~15.4 cm2 contact. **Not printed, not load-tested** | `releases/v5/.../V5_3_Thumb/README_V5_3_THUMB.md`, issue #14 |
| Thumb string route | **UNRESOLVED.** No thumb bore exists; owner has not said whether the thumb is string-actuated | issue #14 |
| Dowel fit in LW-PLA (6.4 mm sockets) | Untested | issue #6 |
| Handle fit and load | Untested | issue #7 |

## Next physical tests (owner)
1. Finger string test on the T2 coupon or a real knuckle shell: clear the bore (3.5 mm drill), pass a 0.8-1.5 mm cord, check free return, full curl and release, note pull force and travel.
2. One dowel dry-fit in a printed LW-PLA socket (any seam).
3. Thumb: after printing R_13_V5_3 and a thumb base, dry-fit without glue and check it seats, the dowel enters both holes, and the thumb clears the fingers.
4. Handle through both sockets before shells 10/11 are joined.

## Open decisions for owner
- Is the thumb string-actuated or fixed?
- Handle: printed PLA/PETG or 18 mm beech rod.
