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
| Anything | [Project Hub](notes/00_Project_Hub.md), then this file |
| Printing V5 parts | **[Print queue to 2026-11-28](notes/Print_Queue_Start_Here.md)**, [Print order](releases/v5/Vi_Gauntlet_X1C_V5_Draft/PRINT_ORDER.md), [Parts inventory](releases/v5/Vi_Gauntlet_X1C_V5_Draft/Inventory/V5_Parts_Inventory.md) |
| LEDs, wiring, WLED, firmware | [LED_Wiring_Start_Here](notes/LED_Wiring_Start_Here.md) |
| Why something was decided | [Decision log](notes/03_Decision_Log.md) |
| What has been tested | [Test log](notes/04_Test_Log.md), [Release gates](docs/RELEASE_GATES.md) |

## Current state (2026-11-22 21:35)
- **DEADLINE 2026-11-28: BOTH gauntlets working (fingers, LEDs) and painted** (owner). Print time is the critical path. Owner plans a full dry-fit before any glue.
- **What to print: [Print queue](notes/Print_Queue_Start_Here.md)** (single source of truth). Key points: R_13 = `R_13_Knuckles_Right_V5_3` (thumb socket); left arm uses **spare R_01 / R_02 / R_05 as L_03 / L_04 / L_06**, plus `L_08 / L_09 / L_11 _SPAREMATCH`, `L_13_V5_3`, and normal L_01, L_02, L_05, L_07, L_10, L_12 (10 new left shells). **Right-arm shells still to print: not yet confirmed by owner.**
- **A1 Mini plate tonight (owner):** both pressure gauges in **transparent PLA** (standing on end, 3 mm brim, tree supports) + **button pod v2** fit test. Thumb bases (`*_Thumb_Base_V5_3_dowel`, standard/clear PLA, 4 walls) later, before knuckle assembly. A1 Mini also takes L_07, L_09_SPAREMATCH, one more thumb, sled/cover.
- **Status (owner):** fingers except thumbs printed + primed; one more thumb needed; all transparent parts printed; right arm ~65 % printed and dry-fitting with dowels; left arm shells not started (spares cover 3).
- **Physical results:** T2 finger coupon PASS (11-18); both board + strip bench tests PASS (11-22); strip passes R_08 round hole, far-end JST does not (cut off). Glow-blue PETG covers FAIL (wet). Nothing else physically tested; no Bambu Studio slice by any agent (#3).
- **Materials/assembly:** shells LW-PLA; handle printed PLA/PETG or 18 mm beech rod; wooden 6 × 30 dowels; UHU Plus Schnellfest (seams, thumb dowel); UHU Poly Max (covers, electronics, buttons); no super glue near clear parts; gauges masked + painted where they should not glow.
- **Electronics:** 3 Sparkle Motion Minis, 2 BTF 160/m strips, **HUAZIZ 12 × 12 × 7 LED push buttons** (pod v2 sized for them), capacitors, flux, M2 × 8; silicone wire not yet arrived. Decisions: continuous strip ring→hand, whole 1 m per arm, ring wrapped twice, board on sled near the ring (option A), power bank on cuff wall. [LED Start Here](notes/LED_Wiring_Start_Here.md).
- **V4 stays NO-GO** ([audit](audits/results/FINAL_VERDICT.md)).

## Open work queue (GitHub issues)
- **Owner upload needed:** #2 (V5.2 shell 08 + mount concepts), #20 (fixed left inserts), #21 (3MF object names; use `Vi_Gauntlet_V5_Print_Pack_named.zip`), the V5.3 thumb files (`V5_3_Thumb_Joint.zip`: R/L_13 V5_3, R/L thumb base; retire R/L_13 V5_1), and V5.4 spare-match left files (`V5_4_Left_Arm_Spare_Match_v2.zip`: L_08/L_09/L_11 SPAREMATCH). Files in `Repo_Upload_Issues_2_and_20.zip` from Claude; steps in its `UPLOAD_STEPS.md`. Claude's session cannot upload LFS.
- Print/fit: #4 ring fit with real strip, #5 finger string pull, #6 dowel fit, #7 handle, #8 gauge/cover retention, #14 thumb route, #15 supports, #16 centre seam.
- Electronics: #9 mounts vs hardware (sled v3 + cover + pod concept done 2026-11-22, test print pending), #10 controller pin map, #11 WLED on device, #12 firmware build, #13 current/temperature.
- Bambu Studio slice: #3.

## Pending owner decisions
- Lighting behaviour: "breathing all the time, button triggers an effect, then back to breathing" (durations and button mapping).
- Right-arm shells still to print (needed for the X1C schedule) and whether a 0.6 mm nozzle is available.
- Button LEDs: wire the HUAZIZ buttons' built-in LEDs (2 wires + resistor each) or not.
- Part labelling (owner note 2026-11-21): parts need IDs in Bambu Studio and physically. Options: marker/tape now; owner adds text in Bambu Studio; or Claude engraves IDs on hidden inner faces of the left-arm shells (geometry change, needs approval).
- Whether to flatten the lens undersides (cosmetic; they print fine as is).

## Latest actions (newest first; one short entry each)
### 2026-11-22 21:35 CET, Claude (print/vault session)
- "Update the vault": hygiene check: HANDOFF was 128 lines, so entries up to 2026-11-22 09:20 moved verbatim to `notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-22.md`; Current state rewritten; inbox empty. Since 20:45: two transparent gauges fit one A1 Mini plate standing; owner plate = 2 gauges + pod; button pod v2 for HUAZIZ LED buttons (`electronics/concepts/.../scripts/pod_export_v2.py`, 3MFs LFS-pending, sent in chat). Files: Print Queue, LED Start Here, Hardware as bought, print/README.
- Next: owner confirms right shells left + 0.6 nozzle → X1C plate schedule to 11-28.
- Sync: PUSHED (see git log).

### 2026-11-22 20:45 CET, Claude (print/vault session)
- New `notes/Print_Queue_Start_Here.md`: left-arm list with spares, small parts, A1 Mini assignments. Gauge: R and L identical shape (mirror-symmetric ≤0.22 mm), 185 mm long so A1 Mini only standing diagonally; plate layout with both thumb bases verified (2D, 32 mm clearance). Right-arm remaining shells still to be confirmed by owner. Sync: PUSHED.

### 2026-11-22 18:55 CET, Claude (print/vault session)
- Third spare is R_02 (owner correction): becomes L_04. Rebuilt spare-match set v2: L_08 (V5_2), L_09, L_11 with relocated holes; L_04 SPAREMATCH withdrawn. One R_02 hole toward L_09 has no partner (insufficient material). Left arm now needs 10 new shells. Sync: PUSHED.

### 2026-11-22 18:00 CET, Claude (print/vault session)
- Owner accidentally printed spare R_05 and R_01. Computed: they are mirror twins of L_06 / L_03 (seam faces within ~2 %); built `L_04/L_09/L_11_*_SPAREMATCH` with dowel holes moved to match the spares (all holes fully in material). Left arm list: `V5_4_Spare_Twins/README_V5_4_SPARE_TWINS.md`. Saves ~24 h (surrogate). Not printed.
- Sync: PUSHED (see git log).

### 2026-11-22 17:30 CET, Claude (print/vault session)
- Built V5.3 thumb joint (owner-approved): R/L_13 socket (0.25 mm clearance, swept along the insertion direction) + one 6.4 mm × 16 mm dowel hole; R/L thumb base with matching hole, original print pose. Overlap 0, contact ~15.4 cm² (was ~2.6). Only one dowel spot has full material. Files delivered as `V5_3_Thumb_Joint.zip`; docs/log/manifest in `releases/v5/.../V5_3_Thumb/`; script `Build_Scripts/v5_3_thumb.py`. Not printed or load-tested.
- Next: owner answers on remaining right shells and 0.6 mm nozzle; then plate-by-plate print queue to 2026-11-28.
- Sync: PUSHED (see git log).

### 2026-11-22 17:20 CET, Claude (print/vault session)
- **Thumb joint finding (computed):** printable `Thumb_Base` placed on V5.1 shell 13 touches only ~2.6 cm² (within 0.5 mm) and **collides with the shell by ~6.6 cm³** at its inner end, so it cannot seat as modelled. Cutting a 0.25 mm-clearance socket into R_13 (removes ~7 cm³) raises the nesting contact to ~18.5 cm² (≈7×); the cut adds one through-opening (genus 18→19), location and wall thickness not yet checked (run killed by memory). Proposal to owner: socket in R_13/L_13 + 2 × 6 mm wooden dowels + UHU Plus Schnellfest. **Needs owner approval (geometry change).** Evidence: `/home/claude/thumbstudy/sections.png` (session workspace). Issue #14.
- Schedule check: surrogate slice ≈151 h per arm of shells (PrusaSlicer light profile; owner X1C runs faster, e.g. plate 21 6.7 h); left arm + rest of right ≈ the whole time to 2026-11-28 with no margin. Asked owner what "ready" must include.
- Sync: PUSHED (see git log).

### 2026-11-22 16:50 CET, Claude (print/vault session)
- "Update the vault": hygiene check (HANDOFF 102 lines OK, inbox empty). Recorded fit checks on printed R_08 (near-end JST passes exit hole but not into trough; bare strip passes round hole; far-end JST does not fit, cut before threading), print history 2026-11-21, geometry_0 naming fix (#21). LED Start Here far-end note aligned with the whole-1-m decision. Files: Test Log, Risks, LED Start Here, session note `2026-11-20_claude_a1-mini-translucent-parts.md`.
- Next: identify X1C plates 21/27 by size; owner uploads #2/#20/#21.
- Sync: PUSHED (see git log).

### 2026-11-22 16:35 CET, Claude (LED session, afternoon)
- Option A placement study from the original right arm + Adafruit's board model: exit hole under the ring 16 × 12 mm, sled glued to the ridged ceiling behind it, ~28 mm to an average forearm (assumed). Sled v3 (M2 × 8 into posts; nuts rejected: too close to pads), vented cover, button pod fit-test files for 18.8 printed handle and 18 mm beech rod. Recorded owner decisions. Open: pod buttons + handle type, dry-fit count, power bank model, WIRING.md rewrite. **Owner/Copilot: upload the 5 concept .3mf files (LFS) to the concept `print/` folder; Claude cannot push LFS.**
- Sync: PUSHED (see git log).

### 2026-11-22 09:45 CET, Claude (LED bench session)
- Hygiene check (stale items fixed, incl. "Project instructions empty" below and entry times). Bench test board 1 + strip: owner flashed stock WLED 16.0.1; AudioReactive remapped (mic 9/10/23) to free GPIO 32; pigtail solder joints checked from photos (5V/32/G correct; stray strand removed); **first light, colour order, rainbow PASS**. Pixels past WLED length light up on their own (not WLED-driven); bench workaround length 160 + segment 0–91. Parts in hand recorded.
- Files: Test Log, HARDWARE_AS_BOUGHT, LED Start Here, ORDER_LIST banner, `notes/sessions/2026-11-21_claude_led-bench-test.md`. Merged with the parallel 09:10/09:20 session (continuous-strip decision kept).
- Next: heat-test result; wire-routing plan for owner review; WIRING.md rewrite; sled for 31.6 × 19.8 mm board (stand-alone part).
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
