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

## Current state (2026-11-22)
- **DEADLINE: ready to wear by 2026-11-28: BOTH gauntlets working (fingers, LEDs) and painted** (owner, 2026-11-22). Print time is the critical path. Owner status 2026-11-22: all fingers except thumbs printed + primed (drying), probably one more thumb to print; all transparent parts printed; right gauntlet ~65 % printed; left gauntlet not started (except fingers, crystals, LED parts); nothing glued, full dry-fit planned first. R_13 not yet printed: **print `R_13_Knuckles_Right_V5_3` (thumb socket + dowel), not V5_1**; thumb base to be reprinted from `R_Thumb_Base_V5_3_dowel` (standard PLA/PETG).
- **V4: NO-GO** ([audit verdict](audits/results/FINAL_VERDICT.md)). Do not print V4 shells.
- **Print set: V5 / V5.1 / V5.2** in `releases/v5/Vi_Gauntlet_X1C_V5_Draft/`. Shell 08 must be `_V5_2`. Not print-approved by release gates; owner is test-printing.
- **Physical results:** T2 finger coupon PASS (2026-11-18). **Right arm partly printed** (owner photo + print history 2026-11-21: shell 08 with ring cover seated; A1 Mini printed ring cover ×2, crystals and lenses; X1C plates 21 and 27 of the owner's project of Claude files, shells not yet identified because every file was named geometry_0, now fixed in the named print pack). Glow-blue PETG covers FAIL (wet); covers now GiantArm transparent PLA.
- **Materials/assembly:** shells LW-PLA; handle printed PLA/PETG or 18 mm beech rod; wooden 6 × 30 mm dowels (57 per arm); UHU Plus Schnellfest epoxy for seams; UHU Poly Max for covers/electronics; no super glue near clear parts.
- **Electronics:** in hand: 3 Sparkle Motion Minis (6160), 2 BTF 5 mm 160/m strips, buttons, capacitors, rosin flux, M2 × 8 screws; silicone wire not yet arrived. **Both board + strip sets bench-tested PASS (2026-11-22)** (WLED 16.0.1, GPIO 32, GRB, 1 A limit, heat OK). Owner decisions 2026-11-22: one continuous strip ring→hand, **whole 1 m per arm with the ring wrapped twice** (dry-fit on R_08 pending), **board near the ring (option A)**, board on a sled with M2 × 8 screws and a vented cover, power bank Velcroed to the cuff wall, button pod snaps onto the handle after assembly. Concept renders + test-print 3MFs (sled R/L, cover, pod) in `electronics/concepts/2026-11-22_controller_placement_option_A/`; not printed. Details: [LED Start Here](notes/LED_Wiring_Start_Here.md).
- **No Bambu Studio slice by any agent** (issue #3). Only owner prints are physical evidence.

## Open work queue (GitHub issues)
- **Owner upload needed:** #2 (V5.2 shell 08 + mount concepts), #20 (fixed left inserts), #21 (3MF object names; use `Vi_Gauntlet_V5_Print_Pack_named.zip`), the V5.3 thumb files (`V5_3_Thumb_Joint.zip`: R/L_13 V5_3, R/L thumb base; retire R/L_13 V5_1), and V5.4 spare-match left files (`V5_4_Left_Arm_Spare_Match_v2.zip`: L_08/L_09/L_11 SPAREMATCH). Files in `Repo_Upload_Issues_2_and_20.zip` from Claude; steps in its `UPLOAD_STEPS.md`. Claude's session cannot upload LFS.
- Print/fit: #4 ring fit with real strip, #5 finger string pull, #6 dowel fit, #7 handle, #8 gauge/cover retention, #14 thumb route, #15 supports, #16 centre seam.
- Electronics: #9 mounts vs hardware (sled v3 + cover + pod concept done 2026-11-22, test print pending), #10 controller pin map, #11 WLED on device, #12 firmware build, #13 current/temperature.
- Bambu Studio slice: #3.

## Pending owner decisions
- Lighting behaviour: "breathing all the time, button triggers an effect, then back to breathing" (durations and button mapping).
- Part labelling (owner note 2026-11-21): parts need IDs in Bambu Studio and physically. Options: marker/tape now; owner adds text in Bambu Studio; or Claude engraves IDs on hidden inner faces of the left-arm shells (geometry change, needs approval).
- Whether to flatten the lens undersides (cosmetic; they print fine as is).

## Latest actions (newest first; one short entry each)
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

### 2026-11-22 09:20, Claude
- Owner decision: continuous strip ring→hand; near end keeps factory connector to ESP32 pigtail (owner soldered pigtail to board). Far end cut before threading. Recorded in Decision Log + LED_Wiring_Start_Here. Next: bench test, then physical turn check. Sync: PUSHED.

### 2026-11-22 09:10, Claude
- Owner photo: strip test-placed in R_08 ring trough; JST connector lies in the trough. Confirmed plan: no connectors in the ring; solder wires at strip ends, exit via hole, connector in cavity. Added to LED_Wiring_Start_Here. Sync: PUSHED.

### 2026-11-21 23:35, Claude
- Bug: all Claude 3MFs show as "geometry_0" in Bambu. Fixed object names (= file name) in a new `Vi_Gauntlet_V5_Print_Pack_named.zip` (geometry unchanged). Repo copies need replacing (issue #21). Owner confirmed X1C plates ("Vi Gauntlet right 3mf_reaggranged") are his project built from Claude's files; plates 21/27 shells still unidentified. Sync: PUSHED.

### 2026-11-21 22:36 CET, Claude
- Claude Project "Arcane Gauntlets": added start-here pointer doc; V4 verdict doc marked historical. Project instructions were empty then; owner has since set them (checked 2026-11-21 22:40). Sync: PUSHED b67fae9.

### 2026-11-21 22:32 CET, Claude
- Added vault hygiene check at every session start (AGENTS.md rule 5a); owner trigger: "clean up the vault". Sync: PUSHED.

### 2026-11-21 22:29 CET, Claude
- Action: Compacted this handoff (was 296 lines). Full previous text archived verbatim at [HANDOFF_SNAPSHOT_2026-11-21](notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-21.md). Added "Context continuity" rules to AGENTS.md and the sync protocol, inbox capture for chat-only AIs (`notes/inbox/`), and a paste-in instruction for other AI tools (`docs/AI_CONTEXT_INSTRUCTIONS.md`).
- Next: owner uploads #2/#20; LED bench test in a new conversation starting from LED_Wiring_Start_Here.
- Sync: PUSHED (see git log).

### 2026-11-21 22:26 CET, Claude
- Vault brought current: Project Hub, Decision Log (owner decisions since V5), Test Log, Risks; new `notes/LED_Wiring_Start_Here.md`.

### 2026-11-21 22:17, Claude
- Parts inventory with renders pushed (`Inventory/V5_Parts_Inventory.md`). Retried LFS push of 9 3MFs: still blocked by session network policy. Nothing half-pushed; zip + steps delivered; commented on #2 and #20.

### 2026-11-20, Claude
- Found inverted normals in all five left inserts; fixed copies delivered (hashes in `L_INSERTS_NORMALS_FIX_SHA256.txt`). Session note: `notes/sessions/2026-11-20_claude_a1-mini-translucent-parts.md`.

### 2026-11-19, Claude
- Hardware received and recorded (`electronics/HARDWARE_AS_BOUGHT.md`); firmware/presets set to 91 LEDs, pins 32/14/27.

### 2026-11-18, Copilot SDK
- Backed up local print-pack/source folders to the repo and verified LFS readback of the new objects. Detail in the archive snapshot and `notes/sessions/2026-11-18_copilot-sdk_*`.

Older entries: [snapshot 2026-11-21](notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-21.md), [archive 2026-11](notes/handoff_archive/HANDOFF_ARCHIVE_2026-11.md).

## Entry template
```markdown
### YYYY-MM-DD HH:MM, <agent>
- Action / result (PASS / FAIL / UNKNOWN / BLOCKED, with facts):
- Files / evidence:
- Next:
- Sync: LOCAL / PUSHED <sha> / UNSYNCED <reason>
```
