---
type: agent-handoff
project: arcane-vi-gauntlet
status: active
updated_date: 2026-11-24
last_agent: Claude
sync_state: pushed
tags:
  - handoff
  - agents
  - vi-gauntlet
---

# Cross-agent handoff: READ FIRST

> The authoritative current state for every agent and every AI conversation. Read [AGENTS.md](AGENTS.md) first.
> **Keep this file short (target under 120 lines).** It holds the current state and the last few actions only. Detail goes in `notes/sessions/`; older entries move **verbatim** to `notes/handoff_archive/`. See "Context continuity" in AGENTS.md.

## Start here by topic
| Working on | Read |
|---|---|
| Anything | [Project Hub](notes/00_Project_Hub.md), then this file; **who owns what: [Conversation starters](notes/Conversation_Starters.md)** |
| Printing V5 parts | **[Print queue to 2026-11-28](notes/Print_Queue_Start_Here.md)**, [Print order](releases/v5/Vi_Gauntlet_X1C_V5_Draft/PRINT_ORDER.md), [Parts inventory](releases/v5/Vi_Gauntlet_X1C_V5_Draft/Inventory/V5_Parts_Inventory.md) |
| Glue-up, paint, final assembly | **[Finishing plan](notes/Finishing_Plan_2026-11-28.md)**, [Finishing Start Here](notes/Finishing_Start_Here.md) |
| LEDs, wiring, WLED, firmware | [LED_Wiring_Start_Here](notes/LED_Wiring_Start_Here.md) |
| Why something was decided | [Decision log](notes/03_Decision_Log.md) |
| What has been tested | [Test log](notes/04_Test_Log.md), [Release gates](docs/RELEASE_GATES.md) |

## Current state (2026-11-25 00:45, Main)
- **DEADLINE 2026-11-28: BOTH gauntlets working (fingers, LEDs) and painted** (owner). **Plan v2: [Deadline_Plan_2026-11-28](notes/Deadline_Plan_2026-11-28.md)**. Critical path now: **right arm glue-up Wed 11-25** (a day behind), left arm via the sub-assembly pipeline as shells arrive (last left shell L_13 ≈ Fri 08:00 on the first Bambu estimate), **finger string test before any knuckle glue**. Nothing glued or painted yet.
- **What to print: [Print queue](notes/Print_Queue_Start_Here.md)** (single source of truth). Key points: R_13 = `R_13_Knuckles_Right_V5_3` (thumb socket); left arm uses **spare R_01 / R_02 / R_05 as L_03 / L_04 / L_06**, plus `L_08 / L_09 / L_11 _SPAREMATCH`, `L_13_V5_3`, and normal L_01, L_02, L_05, L_07, L_10, L_12 (10 new left shells). **Right arm: all shells printed (owner 11-24; R_13 V5_3 was last).** L_09 SPAREMATCH printed; the other 9 new left shells are open.
- **A1 Mini (owner 11-24):** gauges, 2 pods (transparent PLA, tested, final) and thumb bases R/L printed; L_09 SPAREMATCH printed. Next: **L_07**, sled + vented cover R/L, one more thumb (status unknown).
- **Status (owner 11-24):** right arm fully printed; fingers except thumbs printed + primed; transparent parts done; left arm: spares cover 3 + L_09 done, **8 X1C shells + L_07 still to print. First Bambu estimate: L_08 + a cuff on one plate = 10 h 39 min (SUNLU, 3 walls, 3 %), so all left X1C shells may finish Fri morning (~55 h, extrapolated); see Print queue.**
- **Physical results:** T2 finger coupon PASS (11-18); both board + strip bench tests PASS (11-22); strip passes R_08 round hole, far-end JST does not (cut off). Glow-blue PETG covers FAIL (wet). Nothing else physically tested; no Bambu Studio slice by any agent (#3).
- **Materials/assembly:** **all remaining prints SUNLU matte black standard PLA, 3 walls, 3 % infill (owner 11-24; PLA Lite batch clogged both heads)**; handle = 18 mm beech rod; wooden 6 × 30 dowels; UHU Plus Schnellfest (seams, thumb dowel); UHU Poly Max (covers, electronics, buttons); no super glue near clear parts; gauges masked + painted where they should not glow.
- **Electronics:** 3 Sparkle Motion Minis, 2 BTF 160/m strips, HUAZIZ 12 × 12 × 7 LED push buttons, capacitors, flux, M2 × 8; silicone wire not yet arrived. Both board + strip sets bench-tested PASS. **Right-arm strip dry-fit done (whole 160 LEDs: lead-in 11 off, ring 112 = 2 turns, hand 24, crystal 11)**. **WLED 16 presets v3 loaded on board 1 and accepted** (Hextech Idle all blue; Shimmer; Overcharged; Calm; button-2 burst "Bring It" with Vi pink; board cool on a phone charger). Final tuning after mounting, with the wearer (owner's daughter). Still to buy: 470 Ω resistors only (+ optional multimeter). Decisions: board on sled near the ring (option A), vented cover, power bank on cuff wall, button roles B1 on/next/off, B2 Bring It. [LED Start Here](notes/LED_Wiring_Start_Here.md).
- **V4 stays NO-GO** ([audit](audits/results/FINAL_VERDICT.md)).

## Open work queue (GitHub issues)
- **Owner upload needed:** #2 (V5.2 shell 08 + mount concepts), #20 (fixed left inserts), #21 (3MF object names; use `Vi_Gauntlet_V5_Print_Pack_named.zip`), the V5.3 thumb files (`V5_3_Thumb_Joint.zip`: R/L_13 V5_3, R/L thumb base; retire R/L_13 V5_1), and V5.4 spare-match left files (`V5_4_Left_Arm_Spare_Match_v2.zip`: L_08/L_09/L_11 SPAREMATCH). Files in `Repo_Upload_Issues_2_and_20.zip` from Claude; steps in its `UPLOAD_STEPS.md`. Claude's session cannot upload LFS.
- Print/fit: #4 ring fit with real strip, #5 finger string pull, #6 dowel fit, #7 handle, #8 gauge/cover retention, #14 thumb route, #15 supports, #16 centre seam.
- Electronics: #9 mounts vs hardware (sled v3 + cover + pod concept done 2026-11-22, test print pending), #10 controller pin map, #11 WLED on device, #12 firmware build, #13 current/temperature.
- Bambu Studio slice: #3.

## Pending owner decisions
- Button LEDs: always-on (one extra 5V wire + 470 Ω per LED) or not wired.
- Whether a 0.6 mm nozzle is available and whether to use a faster left-arm profile (web reports: little gain on Bambu printers; see Print queue). Fallback finish for the left arm if prints run late (Main / Finishing).
- Part labelling (owner note 2026-11-21): parts need IDs in Bambu Studio and physically. Options: marker/tape now; owner adds text in Bambu Studio; or Claude engraves IDs on hidden inner faces of the left-arm shells (geometry change, needs approval).
- Whether to flatten the lens undersides (cosmetic; they print fine as is).

## Latest actions (newest first; one short entry each)
### 2026-11-25 00:50 CET, Claude (Main)
- Updated from the repo (Print queue, Electronics, Finishing, Mechanics work since 11-22). Hygiene: merged Print queue inbox note (schedule slip) and deleted it; archived entries 2026-11-22 22:05 and older verbatim. **Deadline plan v2**: right arm glue-up Wed, left sub-assembly pipeline, fallbacks F1–F3, 7 blocking decisions (thumb fixed?, G1–G4, paint, F1 approval, wire/resistors, string test, deadline hour). Hub status refreshed.
- Sync: PUSHED (see git log).

### 2026-11-25 00:25 CET, Claude (Print queue conversation)
- Owner sliced L_08 + a left cuff on one X1C plate: **10 h 39 min** (first Bambu estimate; about 0.51 of the surrogate). Rescaled schedule: left X1C shells done about Fri 08:10 if the ratio holds. Corrected "nothing pairs": pairing works for L_08 + a cuff. Print Queue, Test Log, Decision Log, Risks and the Main inbox note updated.
- Sync: PUSHED (see git log).

### 2026-11-24 23:55 CET, Claude (Print queue conversation)
- Hygiene check: HANDOFF 102 lines OK, inbox empty; fixed stale "draft, unprinted" in PRINT_ORDER and a status banner in the inventory. Recorded owner reports: right arm all printed, gauges + 2 transparent pods tested and final, thumb bases printed, L_09 SPAREMATCH printed, handles = beech rod, material switch to SUNLU standard PLA (3 walls, 3 %). **Finding:** X1C needs 74-109 h for the 8 left shells vs ~96 h to Sat 24:00 (surrogate, not Bambu); rewrote `notes/Print_Queue_Start_Here.md` with an ordered schedule (L_08, L_02, L_01, L_05, L_10, L_11, L_12, L_13). Nothing sliced by Claude. Main note in `notes/inbox/`.
- Next: owner sends Bambu time for L_08; starts L_08 on the X1C and L_07 on the A1 Mini.
- Sync: PUSHED (see git log).

### 2026-11-24 00:45 CET, Claude (Electronics & LEDs)
- Order list 2026-11-23 (`electronics/ORDER_LIST.md`): only 470 Ω resistors (+ optional multimeter) left to buy. Button locating pegs (owner photos): snip flush before gluing into pod v2; no CAD change (noted in option-A print/README).
- Sync: PUSHED (see git log).

### 2026-11-22 23:30 CET, Claude (Electronics & LEDs)
- Right-arm LED dry-fit counts recorded and mapped to WLED segments; WLED 16 preset file `electronics/wled/presets_wled16_whole_strip.json` (v3) built, loaded on board 1 and accepted by owner after two source-checked fixes (overlay flag is `o2`; layered segments need blend mode stencil `bm`:16). Board cool. Owner decisions: default all blue, Vi pink only in "Bring It", tune after mounting with the wearer. Next: load board 2, rename APs, print sled/cover, power bank, resistors, wire buttons when wire arrives.
- Sync: PUSHED (see git log).

### 2026-11-22 22:20 CET, Claude (Main)
- Took the Main role. Hygiene: merged Mechanics inbox note (Hub status refreshed, Mechanics/Finishing/Conversation_Starters linked) and deleted it; archived entries 18:55 and older verbatim to `HANDOFF_SNAPSHOT_2026-11-22`. New **`notes/Deadline_Plan_2026-11-28.md`**: day-by-day plan across printing, electronics, mechanics, finishing + 9 blocking decisions (thumb string before R_13 prints; right shells left; faster left profile; handle; wire ETA; paint; deadline hour).
- Sync: PUSHED (see git log).

### 2026-11-22 22:35 CET, Claude (Finishing conversation)
- Hygiene check: HANDOFF 113 lines, inbox empty, Start Here notes within a page; no fixes needed. Wrote `notes/Finishing_Plan_2026-11-28.md` (glue-up order from the seam graph, prerequisites, UHU cure times from data sheets, dry-fit gates G1-G4, paint/masking proposal, calendar). **Finding:** whole-arm finish for 11-28 needs the last shell glued by Tue 11-24; left arm cannot, so it uses a sub-assembly pipeline. Nothing glued or painted; paint system not yet chosen.
- Next: owner dry-fit answers G1-G4 and the open decisions; Main/Print queue to see the schedule risk.
- Sync: PUSHED (see git log).

### 2026-11-22 22:30 CET, Claude (Mechanics conversation)
- Read-only status + hygiene check. Finger string pull test (#5) still not reported; thumb V5.3 digital PASS only (not printed or load-tested); thumb string route unresolved (#14). New `notes/Mechanics_Start_Here.md`; Hub is stale, left `notes/inbox/2026-11-22_claude-mechanics_hub-stale.md` for Main. No CAD changed.
- Sync: PUSHED (see git log).

Older entries: [snapshot 2026-11-22](notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-22.md), [snapshot 2026-11-21](notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-21.md), [archive 2026-11](notes/handoff_archive/HANDOFF_ARCHIVE_2026-11.md).

## Entry template
```markdown
### YYYY-MM-DD HH:MM, <agent>
- Action / result (PASS / FAIL / UNKNOWN / BLOCKED, with facts):
- Files / evidence:
- Next:
- Sync: LOCAL / PUSHED <sha> / UNSYNCED <reason>
```
