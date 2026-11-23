---
type: agent-handoff
project: arcane-vi-gauntlet
status: active
updated_date: 2026-11-22
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

## Current state (2026-11-22 21:35)
- **DEADLINE 2026-11-28: BOTH gauntlets working (fingers, LEDs) and painted** (owner). **Plan: [Deadline_Plan_2026-11-28](notes/Deadline_Plan_2026-11-28.md)**. Critical path: X1C time (~110–120 h needed vs ~96 h to Thu night at current settings). Owner plans a full dry-fit before any glue.
- **What to print: [Print queue](notes/Print_Queue_Start_Here.md)** (single source of truth). Key points: R_13 = `R_13_Knuckles_Right_V5_3` (thumb socket); left arm uses **spare R_01 / R_02 / R_05 as L_03 / L_04 / L_06**, plus `L_08 / L_09 / L_11 _SPAREMATCH`, `L_13_V5_3`, and normal L_01, L_02, L_05, L_07, L_10, L_12 (10 new left shells). **Right-arm shells still to print: not yet confirmed by owner.**
- **A1 Mini plate tonight (owner):** both pressure gauges in **transparent PLA** (standing on end, 3 mm brim, tree supports) + **button pod v2** fit test. Thumb bases (`*_Thumb_Base_V5_3_dowel`, standard/clear PLA, 4 walls) later, before knuckle assembly. A1 Mini also takes L_07, L_09_SPAREMATCH, one more thumb, sled/cover.
- **Status (owner):** fingers except thumbs printed + primed; one more thumb needed; all transparent parts printed; right arm ~65 % printed and dry-fitting with dowels; left arm shells not started (spares cover 3).
- **Physical results:** T2 finger coupon PASS (11-18); both board + strip bench tests PASS (11-22); strip passes R_08 round hole, far-end JST does not (cut off). Glow-blue PETG covers FAIL (wet). Nothing else physically tested; no Bambu Studio slice by any agent (#3).
- **Materials/assembly:** shells LW-PLA; handle printed PLA/PETG or 18 mm beech rod; wooden 6 × 30 dowels; UHU Plus Schnellfest (seams, thumb dowel); UHU Poly Max (covers, electronics, buttons); no super glue near clear parts; gauges masked + painted where they should not glow.
- **Electronics:** 3 Sparkle Motion Minis, 2 BTF 160/m strips, HUAZIZ 12 × 12 × 7 LED push buttons, capacitors, flux, M2 × 8; silicone wire not yet arrived. Both board + strip sets bench-tested PASS. **Right-arm strip dry-fit done (whole 160 LEDs: lead-in 11 off, ring 112 = 2 turns, hand 24, crystal 11)**. **WLED 16 presets v3 loaded on board 1 and accepted** (Hextech Idle all blue; Shimmer; Overcharged; Calm; button-2 burst "Bring It" with Vi pink; board cool on a phone charger). Final tuning after mounting, with the wearer (owner's daughter). Still to buy: 470 Ω resistors only (+ optional multimeter). Decisions: board on sled near the ring (option A), vented cover, power bank on cuff wall, button roles B1 on/next/off, B2 Bring It. [LED Start Here](notes/LED_Wiring_Start_Here.md).
- **V4 stays NO-GO** ([audit](audits/results/FINAL_VERDICT.md)).

## Open work queue (GitHub issues)
- **Owner upload needed:** #2 (V5.2 shell 08 + mount concepts), #20 (fixed left inserts), #21 (3MF object names; use `Vi_Gauntlet_V5_Print_Pack_named.zip`), the V5.3 thumb files (`V5_3_Thumb_Joint.zip`: R/L_13 V5_3, R/L thumb base; retire R/L_13 V5_1), and V5.4 spare-match left files (`V5_4_Left_Arm_Spare_Match_v2.zip`: L_08/L_09/L_11 SPAREMATCH). Files in `Repo_Upload_Issues_2_and_20.zip` from Claude; steps in its `UPLOAD_STEPS.md`. Claude's session cannot upload LFS.
- Print/fit: #4 ring fit with real strip, #5 finger string pull, #6 dowel fit, #7 handle, #8 gauge/cover retention, #14 thumb route, #15 supports, #16 centre seam.
- Electronics: #9 mounts vs hardware (sled v3 + cover + pod concept done 2026-11-22, test print pending), #10 controller pin map, #11 WLED on device, #12 firmware build, #13 current/temperature.
- Bambu Studio slice: #3.

## Pending owner decisions
- Button LEDs: always-on (one extra 5V wire + 470 Ω per LED) or not wired.
- Right-arm shells still to print (needed for the X1C schedule) and whether a 0.6 mm nozzle is available.
- Part labelling (owner note 2026-11-21): parts need IDs in Bambu Studio and physically. Options: marker/tape now; owner adds text in Bambu Studio; or Claude engraves IDs on hidden inner faces of the left-arm shells (geometry change, needs approval).
- Whether to flatten the lens undersides (cosmetic; they print fine as is).

## Latest actions (newest first; one short entry each)
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

### 2026-11-22 22:05 CET, Claude (Electronics & LEDs conversation)
- Owner set up topic conversations: **Main** (renamed "LED review"), **Electronics & LEDs** (this one), **Print queue**, **Finishing** (glue-up + painting), optional **Mechanics**. Ownership + starter prompts: `notes/Conversation_Starters.md`; new `notes/Finishing_Start_Here.md`; AGENTS.md concurrency rule; Claude Project start-here doc updated.
- Sync: PUSHED (see git log).

### 2026-11-22 21:50 CET, Claude (LED session)
- Owner re-confirmed: **whole 1 m strip per arm, no LEDs cut off** (only the far-end plug removed). Decision Log, LED Start Here and the new hand/crystal layout figure (`electronics/concepts/2026-11-22_controller_placement_option_A/hand_crystal_layout.png`) corrected; Claude memory updated. Owner button roles recorded (B1 on/cycle, B2 Hextech burst).
- Sync: PUSHED (see git log).

### 2026-11-22 21:40 CET, Claude (LED session)
- Merge note: this session also sent the owner a "pod v2" at 17:30 with the **same file names** but different pockets (12.6 square + tab cross slots, leg cavity with pillar). **Superseded:** the canonical v2 is the print session's (`scripts/pod_export_v2.py`, already on the A1 plate). Owner: discard the 17:30 copies. Noted in the concept print/README. Claude project memory updated.
- Sync: PUSHED (see git log).

### 2026-11-22 21:35 CET, Claude (print/vault session)
- "Update the vault": hygiene check: HANDOFF was 128 lines, so entries up to 2026-11-22 09:20 moved verbatim to `notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-22.md`; Current state rewritten; inbox empty. Since 20:45: two transparent gauges fit one A1 Mini plate standing; owner plate = 2 gauges + pod; button pod v2 for HUAZIZ LED buttons (`electronics/concepts/.../scripts/pod_export_v2.py`, 3MFs LFS-pending, sent in chat). Files: Print Queue, LED Start Here, Hardware as bought, print/README.
- Next: owner confirms right shells left + 0.6 nozzle → X1C plate schedule to 11-28.
- Sync: PUSHED (see git log).

### 2026-11-22 20:45 CET, Claude (print/vault session)
- New `notes/Print_Queue_Start_Here.md`: left-arm list with spares, small parts, A1 Mini assignments. Gauge: R and L identical shape (mirror-symmetric ≤0.22 mm), 185 mm long so A1 Mini only standing diagonally; plate layout with both thumb bases verified (2D, 32 mm clearance). Right-arm remaining shells still to be confirmed by owner. Sync: PUSHED.

Older entries: [snapshot 2026-11-22](notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-22.md), [snapshot 2026-11-21](notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-21.md), [archive 2026-11](notes/handoff_archive/HANDOFF_ARCHIVE_2026-11.md).

## Entry template
```markdown
### YYYY-MM-DD HH:MM, <agent>
- Action / result (PASS / FAIL / UNKNOWN / BLOCKED, with facts):
- Files / evidence:
- Next:
- Sync: LOCAL / PUSHED <sha> / UNSYNCED <reason>
```
