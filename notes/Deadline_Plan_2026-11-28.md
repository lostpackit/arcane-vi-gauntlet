---
type: plan
owner_conversation: Main
tags: [deadline, schedule, coordination]
updated: 2026-11-22
---

# Deadline plan: both gauntlets working and painted by Sat 2026-11-28

Owned by **Main** ([[Conversation_Starters]]). Topic details live in each topic's Start Here note; this page only sequences them.
Assumptions (owner to correct): both printers run around the clock; owner works on it in the evenings; "done" = Friday 27 night, Saturday 28 is buffer and final test.

## Critical path
**X1C print time.** Remaining right shells (not yet confirmed, probably ~5) + 8 left shells + handles ≈ **110–120 X1C hours** at current settings (estimate: surrogate slices × 0.68, the ratio seen on plate 21). X1C time available until Thursday 26 night ≈ **96 h**. So the left arm must print faster (0.6 mm nozzle / 0.28–0.32 mm layers / 2 walls / ~8 % infill), or something moves to the A1 Mini, or finishing is compressed.

Second risk: **paint cure time** on the left arm (glued Friday morning, painted Friday). Third: **silicone wire not arrived** (blocks electronics install).

## Day by day
| Day | X1C | A1 Mini | Electronics & LEDs | Mechanics | Finishing |
|---|---|---|---|---|---|
| **Sun 22** (tonight) | Next right shell overnight. If it is R_13, **only after the thumb-string decision** (see decisions) | 2 clear gauges + pod v2 fit test | Rename the boards' AP SSIDs | — | — |
| **Mon 23** | Last right shells (long one overnight). Decide faster profile for the left | Thumb bases R+L + extra thumb (day); **L_07** overnight | Dry-fit the double ring wrap on R_08, count LEDs per turn; pod v2 fit check with real buttons | **Finger string test** on coupon/R_12 (#5); one dowel fit test (#6); handle decision | Full **dry-fit of the right arm**; buy primer/filler/paint; test the paint stack on a lit scrap clear part |
| **Tue 24** | Right finished → **left long shells** (L_05, L_08, L_12, L_13) start | **L_09_SPAREMATCH** overnight; sled R/L + cover | Wire arrives? Solder strip lead + buttons into PETG pod; WLED segments; update WIRING | Right thumb: dry-fit, then epoxy base + dowel (overnight) | **Right glue-up** in sub-assemblies (sled glued under the ring **before** closing that area); cure overnight |
| **Wed 25** | Left shells | Final pods (PETG) ×2; spares/reprints | Left board + strip prepared on the bench | String the right fingers | Right: fill seams, sand, **prime**; base coat in the evening |
| **Thu 26** | **Last left shells must finish tonight** | Buffer / reprints | Right: thread strip (ring + hand channel), sled + board + pod, power bank; **first in-arm power-up + heat check** | Right fingers adjusted | Right: details, masking, clear parts (gauges painted), covers/lenses on **after** the strip; left dry-fit as parts arrive |
| **Fri 27** | Buffer for one failed print | — | — | Left thumb epoxy (morning), string left fingers | **Left glue-up morning**, fill/sand midday, **prime + paint** afternoon/evening (thin coats, fast-dry) |
| **Sat 28** | — | — | Left: strip, board, pod, power-up; both arms final test, power banks charged | Final finger check | Left touch-ups; cover/lenses on; **wear test** |

Fallbacks if the X1C slips past Thursday: (1) left arm painted in a simpler scheme (one base colour + dry-brush), (2) strip and electronics in the left arm Saturday morning instead of Friday, (3) the least visible left shell printed at the coarsest settings.

## Decisions blocking the plan (owner)
| # | Decision | Blocks | Topic |
|---|---|---|---|
| 1 | **Thumb: string-actuated or fixed?** If strings, R_13/L_13 need a thumb bore **before** they are printed | R_13 / L_13 printing | Mechanics |
| 2 | **Which right shells are still left to print?** | X1C schedule | Print queue |
| 3 | **Faster left-arm profile:** 0.6 mm nozzle available? Accept coarser layers? | Left arm fitting in time | Print queue |
| 4 | **Handle: printed or 18 mm beech rod?** | Handle prints, pod variant, wrist assembly | Mechanics |
| 5 | **Silicone wire ETA** (if not here by Tue, buy 24–26 AWG locally) | Electronics install | Electronics |
| 6 | **Paint scheme and paint on hand** (primer, colours, filler, masking) | Priming Wed | Finishing |
| 7 | When exactly on the 28th it must be ready, and owner's available hours per day | Whole schedule | Main |
| 8 | Button LEDs wired or not; default look / effect list / burst length | Not blocking the build (set in WLED any time) | Electronics |
| 9 | Part labelling (marker now, or engraved left shells) | Avoiding mix-ups | Print queue |

Related: [[HANDOFF]] · [[Print_Queue_Start_Here]] · [[LED_Wiring_Start_Here]] · [[Mechanics_Start_Here]] · [[Finishing_Start_Here]]
