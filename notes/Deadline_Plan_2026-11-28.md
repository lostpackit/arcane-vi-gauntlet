---
type: plan
owner_conversation: Main
tags: [deadline, schedule, coordination]
updated: 2026-11-25
version: 2
---

# Deadline plan: both gauntlets working and painted by Sat 2026-11-28 (v2, 2026-11-25 00:45)

Owned by **Main** ([[Conversation_Starters]]). Topic details live in each topic's notes; this page only sequences them. v1 (2026-11-22) assumed the right arm printed by Mon night; it finished Tue 23:36, so v2 re-plans from Wed 11-25. Nothing below is a physical result unless the owner reported it.

## Where we are (Wed 11-25 00:45)
- **Right arm: all 13 shells printed** (R_13 V5_3 last, Tue 23:36). Not glued. Thumb bases R+L, gauges ×2, pods ×2 (final), all clear parts printed. Handles = beech rod.
- **Left arm:** L_03/L_04/L_06 (spares) + L_09 printed. **8 X1C shells + L_07 (A1) to go.** First real Bambu estimate (L_08 + cuff, SUNLU PLA, 3 walls, 3 %) = 10 h 39 min, so the X1C queue ≈ 55 h → **last left shell (L_13) about Fri 08:00** if the 0.51 ratio holds (one data point; L_05/L_12/L_13 are support-heavy and may run longer). Order and times: [[Print_Queue_Start_Here]].
- **Electronics:** both boards + strips bench PASS; right-arm strip dry-fit counted; WLED 16 presets v3 accepted (final tuning with the wearer after mounting). To buy: 470 Ω resistors (button LEDs). Silicone wire: arrival not recorded.
- **Mechanics:** finger string-pull test (#5) **not yet done**; thumb joint printed but not dry-fitted; R_13/L_13 have **no thumb string hole** (so the thumb is fixed this build unless drilled).
- **Finishing:** nothing glued or painted; gates G1–G4 (dry-fit questions) and the paint system still open ([[Finishing_Plan_2026-11-28]]).

## Critical path now
1. **Right arm must be glued Wed** (it is a day behind the Finishing calendar), so it can be primed Thu and painted Thu–Fri.
2. **Left arm** follows the Finishing **sub-assembly pipeline**: glue → fill → prime → paint each sub-assembly as its shells arrive, join the painted pieces on masked bare seam faces. The knuckles (L_12 Thu night, L_13 Fri morning) are the last and tightest.
3. **Finger string test before any knuckle glue** (both arms).

## Day by day
| Day | X1C (Print queue) | A1 Mini | Right arm (Finishing + Mechanics) | Left arm | Electronics |
|---|---|---|---|---|---|
| **Wed 25** | L_08+L_01 (→ ~11:00), L_02 (→ ~15:00), L_10 (→ ~21:00), L_05 overnight | **L_07**, then sled + vented cover R/L | **Morning: dry-fit gates G1–G4, finger string test, thumb base dry-fit in R_13.** Then glue: cuff, rear band (sled first if G2 = no), front band, wrist with **beech rod in**, thumb base + dowel epoxy. Knuckles last (after string test). Cure overnight | Glue cuff sub-assembly (L_01/L_02 + spares R_01/R_02) once L_02 is off | Load presets on board 2; rename both APs; buy 470 Ω resistors; wire buttons if wire is in |
| **Thu 26** | L_11 (→ ~13:00), L_12 (→ ~23:00), L_13 overnight | Spare / reprints | Fill + sand seams, **prime** (night to dry) | Rear band (L_08+L_07+L_09) + front band (L_05+spare R_05): glue, fill; prime cuff | Prepare left board + strip on the bench |
| **Fri 27** | L_13 done ~08:00; **buffer for one failed print** | — | **Colour coats** + masking; gauges painted; evening: strip, board, pod, power bank in; **first in-arm power-up + heat check** | Prime/paint bands + cuff; wrist (L_10+L_11) glue in the morning with rod; knuckles glue as soon as L_13 is off | Right install (evening) |
| **Sat 28** | — | — | Covers, lenses, crystal, gauge on; fingers strung; **wear test with the wearer**, WLED tuning | Join painted sub-assemblies; knuckles: fallback finish if needed; strip, board, pod; covers/lenses; fingers | Left install; both arms tested; power banks charged |

## Fallbacks (Main's recommendation, owner to approve)
- **F1, approve now:** if L_12/L_13 land Friday, the **left knuckles get a simpler finish** (primer + one colour + dry-brush, no clear coat) so they are dry by Saturday.
- **F2, planned anyway:** left electronics install on Saturday morning.
- **F3, only if a Bambu estimate for L_05, L_12 or L_13 is over about 11 h:** slice that part at 0.28 mm layers (keep 3 walls on L_13 for the thumb socket). Print queue to apply.
- If the X1C loses a plate (failure/clog): print queue reorders so the knuckles still finish first; the left cuff can be glued and painted last because it is the least detailed.

## Decisions blocking this plan (owner)
| # | Decision | Needed by | Topic |
|---|---|---|---|
| 1 | **Thumb fixed this build?** R_13/L_13 were printed without a string hole. Yes = glue it in its pose; no = Mechanics designs a drill guide today | Wed (before thumb epoxy) | Mechanics |
| 2 | **Dry-fit answers G1–G4** (strip through channel with arm assembled? sled reachable? primed fits? dowels fit?) | Wed morning (before right glue-up) | Finishing |
| 3 | **Paint system and colours on hand** (primer/filler, colours, masking, clear?) | Wed (shopping) / Thu (priming) | Finishing |
| 4 | **Approve fallback F1** for the left knuckles | Thu | Main |
| 5 | **Silicone wire here?** If not, buy 22/26 AWG locally Wed; plus 470 Ω resistors | Wed | Electronics |
| 6 | **Finger string test result** (#5) | Before knuckle glue (Wed right, Fri left) | Mechanics |
| 7 | What time on Sat 28 it must be ready | Now | Main |
| — | Non-blocking: owner LFS uploads (#2, #20, #21, V5.3, V5.4); part labelling (marker) | — | Print queue |

Related: [[HANDOFF]] · [[Print_Queue_Start_Here]] · [[Finishing_Plan_2026-11-28]] · [[LED_Wiring_Start_Here]] · [[Mechanics_Start_Here]]
