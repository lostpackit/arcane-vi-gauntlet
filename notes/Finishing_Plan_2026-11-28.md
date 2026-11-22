---
type: plan
tags: [finishing, glue, paint, assembly, schedule]
updated: 2026-11-22
owner: Finishing conversation
---

# Finishing plan to 2026-11-28 (glue-up, paint, final assembly)

Written Sun 2026-11-22 22:30 CET by the Finishing conversation. **Nothing here has been glued, painted or tested.** Seam list comes from `V5_build_log.json` (27 interfaces per arm, 57 dowels; left arm has the same topology, mirrored). Cure times are from UHU data sheets found on the web 2026-11-22 (links at the end); paint times are typical rattle-can values, **check the can**.

## 1. Reality check on the deadline
Minimum chain from "last structural seam glued" to "ready for final assembly": epoxy final strength 12 h -> fill/sand/prime (1 day, primer needs a night) -> colour coats with masking (about 1.5 days) -> paint hard-dry about 24 h. So for a whole-arm finish landing on Sat 11-28 the **last shell must be glued by Tue 11-24 evening.**
- Right arm (about 65 % printed): feasible if the remaining shells are confirmed and printed in the next 1-2 days.
- Left arm (10 shells not started, about 150 h surrogate): **cannot make the whole-arm chain.** Use the pipeline in section 4 (finish each sub-assembly as its shells come off, join painted sub-assemblies last). If prints still run late, fallback order: (1) both arms working, (2) right arm fully painted, (3) left arm primed + painted as far as time allows. This is a Print queue / Main question; flagged in HANDOFF.

## 2. Gates to answer in the owner's dry-fit (before any glue)
| Gate | Question | Why it matters |
|---|---|---|
| G1 | With the arm dry-assembled on dowels, can the 1 m strip be pushed through the hand channel tunnels from the open end? Which shells carry the channel? | If yes: strip goes in **after paint**, no overspray on LEDs. If no: strip goes in before the seams it crosses are glued, and the channel + strip must be masked for painting. |
| G2 | With the arm assembled, can you reach the sled posts (M2 x 8) and plug the strip JST from the cuff opening? | If no: sled + board go in before the rear band is joined to the front band. |
| G3 | Do the primed fingers still press into their slots (slot pieces overlap up to 0.15 mm)? Does a crystal / lens / cover test piece still fit a 0.3 mm gap with one coat of primer? | Paint adds about 0.05-0.15 mm per surface and can jam press fits. Mask or sand pockets, ledges and slots. |
| G4 | Do 6 x 30 dowels go into LW-PLA sockets (6.4 mm holes) without force? Print queue notes the foam can close holes. | Ream before glue, not after. |

## 3. Glue-up sub-assemblies and what must be in first
Epoxy: UHU Plus Schnellfest (pot life about 5 min, so **one seam per mix**, tape or clamp 20 min, handle after 60 min, full strength 12 h). Dry-fit every seam first. Coat both faces and dowel ends; keep squeeze-out out of the hand channel, lens ledges, crystal well and cover seat (wipe at once; tape those edges first).

| # | Glue step (right-arm numbering; left identical) | Seams | Must already be done / installed |
|---|---|---|---|
| 1 | **Cuff**: 01+02 and 03+04 (Y147), then halves together (X211) | 1-2, 3-4, 1-3, 2-4 | Nothing electronic. Decide the Velcro patch on the cuff wall (apply after paint on a masked bare patch). |
| 2 | **Rear band**: 08+07 (X100), 08+09 (X300) | 7-8, 8-9 | Dowel test on 07/09 (G4). **Sled glued under the ring on 08** (UHU Poly Max, bare plastic, sled test-fitted first) if G2 = no. Exit hole 16 x 12 mm kept clear. |
| 3 | **Front band**: 05+06 (X211), then front to rear band (Y180: 5-7, 6-9) | 5-6, 5-7, 6-9 | Sled/board decision from G2. Board wires (5V/32/G pigtail, buttons on 14/27/G, USB-C cable) routed into the cavity before the front band closes over them. |
| 4 | **Band + cuff** (Z145) | 1-5, 2-5, 2-7, 2-8, 3-6, 4-6, 4-8, 4-9 | Cuff and band finished (steps 1-3). Cuff stays open for the power bank, so nothing else needed. |
| 5 | **Wrist**: 10+11 (X211), then wrist to band (Z310) | 10-11, 5-10, 6-11, 7-10, 8-10, 8-11, 9-11 | **Handle (Ø18.8 printed, or 18 mm beech rod) seated in both sockets first**; it is trapped. **Button wires laid along the inside** to the handle area (service loop, pod end free) before 10/11 close. Wires that cross a seam go in before that seam closes. |
| 6 | **Knuckles**: 12+13 (X211), then to wrist (Z400) | 12-13, 10-12, 11-13 | Finger fit + string-pull test passed (issue #5), **thumb base dowel-epoxied into 13 and cured overnight**, string path agreed. Strip route through the seam (G1) done if G1 = no. |

Not glued, ever: ring cover, hand lenses, crystal (lift-out, UHU Poly Max dots only, **after** the strip is in and tested); gauge (sits on the cover, held with removable putty or two hot-glue dots, see README).

## 4. Pipeline for the late arm
Do not wait for the whole arm. As each sub-assembly's shells come off the printer: glue it (section 3), fill, sand, prime, paint it, then join the painted sub-assemblies at Z145 / Z310 / Z400 with epoxy on **masked, bare** seam faces and dowel holes (paint on a joint face weakens it and tightens the dowel fit). Touch up the joint line afterwards. Cost: visible seams need a final touch-up coat. The centre X211 seam runs across visible top details, so glue the two halves **before** painting wherever both halves exist.

## 5. Cure and dry reference (20 degrees C)
| Product | Working time | Hand-firm | Full strength | Notes |
|---|---|---|---|---|
| UHU Plus Schnellfest (data sheet) | about 5 min (some packs say 2 min: check yours) | 20 min | 12 h; 60 min is functional strength | Min. cure 2 h at 5 C, 60 min at 20 C, 30 min at 25 C. Heat speeds it; keep LW-PLA under about 45 C. |
| UHU Poly Max (variant not recorded) | Glasklar Express: skin 10-15 min, working about 2 h | Power Transparent: about 30 min | about 4 h on thin films; 2 mm per 24 h through-cure | Paintable after cure. Check your tube. |
| Filler/putty, primer, colour, clear (typical, unverified) | recoat 10-15 min or after 1 h (per can) | touch-dry 15-30 min | handle 12-24 h, hard 3-7 days | LW-PLA foam soaks primer: expect 2-3 filler coats; sand between. |

## 6. Paint system and masking (proposal, needs owner OK)
- Same-brand spray family: filler primer, colour, clear. Test on a hidden scrap or the failed glow-blue PETG cover first (foam surface, thin coats, no heat gun).
- Mask or keep out of the paint: ring cover, lenses, crystal, gauge glow windows, finger slots, crystal well and lens ledges (0.3 mm gaps), cover seat, dowel holes (plug with toothpicks), seam faces for late joins, Velcro patch, sled posts.
- Gauges: transparent PLA, paint the areas that should not glow on the outside; leave the window clear; fit after paint.
- Peel tape when paint is touch-dry; score the edge first.

## 7. Calendar (right arm firm only if its prints finish as assumed; left arm as printed)
| Day | Right arm | Left arm |
|---|---|---|
| Sun 11-22 | Dry-fit on dowels; strip thread test (G1); answer G1-G4 | - |
| Mon 11-23 | Glue steps 1-3 as shells allow (one seam per mix); order paint and supplies | First shells print; glue sub-assemblies as they finish |
| Tue 11-24 | Glue steps 4-6, handle + thumb dowel; **last structural glue** | Glue sub-assemblies, fill/sand |
| Wed 11-25 | Fill, sand, prime (night to dry) | Prime what is glued |
| Thu 11-26 | Colour coats + masking | Colour sub-assemblies |
| Fri 11-27 | Clear coat, unmask; electronics (strip, board, pod), test | Join painted sub-assemblies; electronics |
| Sat 11-28 | Lenses, crystal, cover, gauge, power bank, final check | Same, if shells arrived on time |

## 8. Final assembly and wear check (per arm)
1. Paint hard-dry (about 24 h); masks off. 2. Strip in (whole 1 m, ring twice, then hand channel), far-end plug already removed, no pad touching metal or itself. 3. Board on sled (M2 x 8), strip JST plugged, buttons wired, WLED AP SSID renamed. 4. **Power-up test before anything is bonded over the strip**, 10 min, feel for heat under the cover. 5. Lenses, crystal, cover (Poly Max dots), gauge. 6. Power bank on Velcro, USB-C cable. 7. Button pod snapped on. 8. Fingers + strings, thumb. 9. Wear check: strap fit, nothing rubs wires, buttons reachable.

## Open decisions for the owner
1. Paint system (section 6) and colours. 2. Which right-arm shells are still unprinted. 3. Velcro patch location. 4. Fallback priority if prints run late (section 1). 5. Which UHU Poly Max variant you have.

Sources: UHU Plus Schnellfest data sheet (media.hornbach.de/hb/technicaldatasheet/as.46147721.pdf); UHU Poly Max Glasklar Express data sheet (image.hagebau.de/pdf/2000000000023153.pdf); toom.de listing for Poly Max Power Transparent. Related: [[Finishing_Start_Here]] · [[LED_Wiring_Start_Here]] · [[Print_Queue_Start_Here]]
