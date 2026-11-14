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
