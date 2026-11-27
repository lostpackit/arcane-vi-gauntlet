---
type: decision-log
tags: [decisions]
---

# Decision log

Append decisions with date, agent, alternatives, rationale, evidence, and affected files. **Do not silently rewrite old decisions.**

## Established
- **2026-11-14 / prior project work:** Keep original manually string-actuated fingers; defer motorized knuckles.
- **2026-11-14 / prior project work:** Require animated addressable LEDs and wearable effect buttons, not just static light.
- **2026-11-14 / prior project work:** V4 uses 13 sections per arm; light ring preserved within one structural section; reinforcement splines and separate light cover.
- **2026-11-14 / repository coordination:** Keep source files immutable and repository private until model rights are verified.
- **2026-11-14 / multi-agent coordination:** GitHub `main` + repository-root Obsidian vault + `HANDOFF.md` are the shared record. All agents update handoff and dated logs after every action.

## Owner decisions
- **2026-11-27 / Owner:** The original [3MF project file](../originals/Vi%20Gauntlet%203mf%20Project%20File.3mf) was the reference guide; only its fingers remain correct for this project. Use the original model only as a finger reference, not as the current design for the rest of the gauntlet. This direction does not replace physical finger-mount or tendon tests. Evidence: owner instruction; [[docs/ASSET_MAP]].
- **2026-11-14 / Owner:** APPROVED the V5 direction below and asked for a lighter build (cosplay use, lightweight PLA). Clarified intent: fuse everything except the fingers into one solid and cut it into bed-sized shells; functional parts (light cover, gauge, handle) may stay separate where needed for LEDs and strength. First result: `releases/v5/Vi_Gauntlet_X1C_V5_Draft/` (draft, unprinted).
- **2026-11-14 / Claude (independent audit):** PROPOSED (since approved, see above) — stop treating `Full_Arm_* (No Fingers).stl` as the V4/V5 source. Rebuild from the 3MF functional parts, merging only structural glove panels, keeping ring, cover, gauge, handle, finger carrier, crystal and light strip as separate parts. Alternatives: (a) patch V4 by regenerating only shells 08, 10/11, 12/13; (b) print the original 3MF as designed. Rationale and evidence: `audits/results/ISSUES.md`, `audits/results/FINAL_VERDICT.md`. No CAD has been changed.

See [[docs/DECISIONS_AND_HISTORY]] and [[HANDOFF]].

## Owner decisions since V5 (appended 2026-11-21 by Claude from chat record)
- **2026-11-15 / Owner:** Approved cutting the hand LED strip channel and crystal slot (V5.1).
- **2026-11-17–19 / Owner:** LEDs: BTF-LIGHTING 5 mm SMD2020 160 LEDs/m strip (ultra-narrow 3535 out of stock). Layout per arm 91 LEDs: ring 55, hand 36 (crystal = last 11). Controller: Adafruit Sparkle Motion Mini (ESP32, WLED, USB-C). **USB-C only, no USB-A. No perfboard/breadboard.** Phone control via WLED. Data GPIO 32, buttons GPIO 14 / 27 to G, 1000 mA limit. Connectors: BTF JST-SM 3-pin pairs. Evidence: [[electronics/HARDWARE_AS_BOUGHT]], [[electronics/ORDER_LIST]].
- **2026-11-19 / Owner:** 1000 µF capacitor ordered as optional insurance; fit only if bench test shows flicker/resets.
- **2026-11-20 / Owner:** Shell 08 printed in regular opaque PLA (only covers/lenses/crystal need to be translucent).
- **2026-11-20 / Owner:** Light covers, crystal, lenses: glow-in-the-dark blue PETG **rejected** (wet: stringing/popping); now **GiantArm transparent PLA** (190–220 °C), frosted vs clearer chosen by Lens B test. Glow green PETG not used (tint + abrasive).
- **2026-11-21 / Owner:** Seam dowels: wooden 6 × 30 mm (printed peg = fallback). Handle: printed PLA/PETG or 18 mm beech rod cut to 250 mm (not 20 mm; sockets 19.3 mm). Glue: UHU Plus Schnellfest 2-K epoxy for dowels/seams; UHU Poly Max (clear) for covers/electronics; no super glue near clear parts.
- **Pending owner decision:** lighting behaviour "breathing all the time, button triggers an effect then returns to breathing" (durations and button mapping not chosen).
- **2026-11-22 / Owner:** LED strip runs **continuously from ring to hand** (no ring/hand cut). Near (input) end keeps the factory JST connector, mated to the ESP32 pigtail outside the ring; far end cut before threading. Pending physical check of the turn into the notch slot. Details: [[LED_Wiring_Start_Here]].
- **2026-11-22 / Owner:** Use the **whole 1 m strip per arm** for a richer ring: wrap the ring outer wall **twice** (two rows, shallow spiral) instead of cutting to 91 LEDs; no crystal doubling. Subject to a dry-fit on printed R_08 (rows below the cover seat, exit into the hand slot). Far-end factory connector still cut off before threading. Details: [[LED_Wiring_Start_Here]].
- **2026-11-22 / Owner:** Controller location **option A**: each Sparkle Motion Mini sits **near the ring** (in the arm cavity by the ring's exit), so the soldered JST pigtail plugs straight into the strip; only the USB-C cable runs back to the power bank in the cuff; button wires run from the handle. Exact spot and sled to be shown to owner from CAD.
- **2026-11-22 / Owner:** Board mounting: Sparkle Motion Mini on a printed **sled glued under the ring**, fixed with the owner's **M2 × 8 screws**, with a **perforated (vented) cover** to protect it (owner's idea). **Power bank Velcroed to the cuff wall.** **Button pod snaps onto the handle after assembly.** Concept files: [[electronics/concepts/2026-11-22_controller_placement_option_A/README]].
- **2026-11-22 / Owner:** Deadline 2026-11-28: both gauntlets complete, working and painted.
- **2026-11-22 / Owner:** Approved V5.3 thumb joint: socket in R_13/L_13 + dowel; thumb base reprinted with matching hole (old printed base was a poor print anyway). Files: `releases/v5/.../V5_3_Thumb/`.
- **2026-11-22 / Owner:** Reprint both pressure gauges in transparent PLA and paint the areas that should not glow (more light from the ring shows through). Gauge sits directly on the ring cover over the LEDs.
- **2026-11-22 / Owner:** A1 Mini plate = 2 transparent gauges + button pod fit test; thumb bases printed later.
- **2026-11-22 / Owner:** Button roles (2 buttons per arm): **button 1 = power on + cycle through effects**, **button 2 = a 'Hextech power-up explosion' burst**, then back to the normal look. Effects, burst length and button-LED wiring (always-on via 470 Ω from 5V proposed) still to confirm.
- **2026-11-22 21:47 / Owner (re-confirmed):** **No cutting LEDs off: the whole 1 m strip is used in each arm** (ring wrapped twice, then the hand channel and crystal). Only the far-end factory plug is removed because it does not fit. Any agent planning a strip layout must start from 160 LEDs per arm.
- **2026-11-22 22:39 / Owner:** Lighting style: **blue and cyan with white flashes, plus some Vi pink**; button-2 burst lasts **3–4 s**; owner wants a **lightning effect in the hand shafts**. Animation storyboard proposed by Claude (WLED 16.0.1 effects checked in source: Breathe 2, Running 15, Sparkle Dark 21, Lightning 57, Meteor 76, Glitter 87, Starburst 89, Heartbeat 100, Pacifica 101, Flow 110); preset file after owner approval.
- **2026-11-22 22:44 / Owner:** Default look **all blue** (no pink). **Vi pink only in the button-2 burst**, which is named **"Bring It"** (cocky name wanted). Owner likes the glitter and the rest of the storyboard; the pink cycle look becomes "Shimmer" (blue + white glitter). Presets: `electronics/wled/presets_wled16_whole_strip.json`.
- **2026-11-22 23:27 / Owner:** Presets accepted as they are; **final effect tuning after everything is mounted, with the wearer (owner's daughter) watching**. Button pod position/angle to be set by the wearer's thumb.
- **2026-11-24 00:39 / Owner:** HUAZIZ button locating pegs get **snipped off** rather than adding holes to the button pod; no pod CAD change.
- **2026-11-24 / Owner:** **Material change:** all remaining prints in **SUNLU matte black standard PLA** (4 spools in hand, same-day delivery) unless PETG is needed; shells no longer LW-PLA (PLA Lite batch clogged both heads; weight difference at 3 walls / 3 % infill is small). Profile **3 walls, 3 % infill**. Time estimates from the clogged prints are not usable.
- **2026-11-24 / Owner:** **Handles: 18 mm beech rod**, not printed.
- **2026-11-24 / Owner:** **Button pods: the transparent-PLA pods (printed and tested) are final**; no PETG pods.
- **2026-11-25 / Owner:** plans to print **L_08 (SPAREMATCH) together with a left cuff on one X1C plate** (Bambu estimate 10 h 39 min); the other left cuff follows. L_01 and L_02 are the cuffs still needed (spares R_01/R_02 = L_03/L_04).
- **2026-11-25 / Owner:** Paint look (reference photo: blue recessed panels, raised gold frames, gold dial/knuckle caps/joints): **prime, spray blue over the visible surfaces, then hand-brush / dry-brush the gold** on frames and trim; the hand-painted look is accepted over a perfect finish. Parts not blue or gold (undersides, leather areas) get minimal paint. Overall clear coat: maybe, decide later. Gloss vs satin not answered yet. LED groove / crystal well / ring trough interior colour: open (Claude recommends matte white, see Finishing Start Here).
- **2026-11-25 01:38 / Owner:** Pods v2 (transparent PLA) **clipped onto the 18 mm beech rod handles; fit confirmed, no redesign or changes**. Pods need no screws.
- **2026-11-26 06:50 / Owner:** Add two **sound-reactive looks inspired by Arcane songs "Misfit Toys" and "Playground"** in Arcane/hextech colours, on top of the existing presets (v4: presets 5 and 6). Claude default, not an owner decision yet: both added to the Next-look cycle (1 → 6); one gold accent, no pink.
- **2026-11-26 14:24 / Owner:** Print the board sled now (R + L) with **cover v3.1** (Claude added two mic sound holes after the mic test passed; sled itself unchanged).
- **2026-11-27 / Owner:** Right arm only for the 11-28 deadline (left arm skipped, owner clarified after a typo). Sled and board missed before the final join; decided to mount them **Saturday morning**, glued with **UHU Plus Schnellfest epoxy** (Claude proposal accepted: overhead hold; supersedes Poly Max for the sled only), after the blue paint. Finger gold and finger epoxy assembly also Saturday; LED wiring tonight comes first.
