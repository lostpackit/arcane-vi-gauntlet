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
