---
type: agent-handoff
project: arcane-vi-gauntlet
status: active
updated_date: 2026-11-25
last_agent: Copilot SDK (repository sync)
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
- **What to print: [Print queue](notes/Print_Queue_Start_Here.md)** (single source of truth). Key points: **thumb V5.3 withdrawn 11-25 (wrong-hand base): left arm prints `L_13_Knuckles_Right_V5_1`; printed R_13 V5_3 is usable; printed V5.3 bases are swapped (`L_` print = right arm)**, see [Mechanics](notes/Mechanics_Start_Here.md); left arm uses **spare R_01 / R_02 / R_05 as L_03 / L_04 / L_06**, plus `L_08 / L_09 / L_11 _SPAREMATCH`, `L_13_V5_1`, and normal L_01, L_02, L_05, L_07, L_10, L_12 (10 new left shells). **Right arm: all shells printed (owner 11-24; R_13 V5_3 was last).** L_09 SPAREMATCH printed; the other 9 new left shells are open.
- **A1 Mini (owner 11-24):** gauges, 2 pods (transparent PLA, tested, final) and thumb bases R/L printed; L_09 SPAREMATCH printed. Next: **L_07**, sled + vented cover R/L, one more thumb (status unknown).
- **Status (owner 11-24):** right arm fully printed; fingers except thumbs printed + primed; transparent parts done; left arm: spares cover 3 + L_09 done, **8 X1C shells + L_07 still to print. First Bambu estimate: L_08 + a cuff on one plate = 10 h 39 min (SUNLU, 3 walls, 3 %), so all left X1C shells may finish Fri morning (~55 h, extrapolated); see Print queue.**
- **Physical results:** T2 finger coupon PASS (11-18); both board + strip bench tests PASS (11-22); strip passes R_08 round hole, far-end JST does not (cut off). Glow-blue PETG covers FAIL (wet). Nothing else physically tested; no Bambu Studio slice by any agent (#3).
- **Materials/assembly:** **all remaining prints SUNLU matte black standard PLA, 3 walls, 3 % infill (owner 11-24; PLA Lite batch clogged both heads)**; handle = 18 mm beech rod, **cut to 249 mm** (computed by Finishing, owner to confirm on the dry stack); wooden 6 × 30 dowels; UHU Plus Schnellfest (seams, thumb dowel); UHU Poly Max (covers, electronics, buttons); no super glue near clear parts; gauges masked + painted where they should not glow.
- **Electronics:** 3 Sparkle Motion Minis, 2 BTF 160/m strips, HUAZIZ 12 × 12 × 7 LED push buttons, capacitors, flux, M2 × 8; silicone wire not yet arrived. Both board + strip sets bench-tested PASS. **Right-arm strip dry-fit done (whole 160 LEDs: lead-in 11 off, ring 112 = 2 turns, hand 24, crystal 11)**. **WLED 16 presets v3 loaded on board 1 and accepted** (Hextech Idle all blue; Shimmer; Overcharged; Calm; button-2 burst "Bring It" with Vi pink; board cool on a phone charger). Final tuning after mounting, with the wearer (owner's daughter). Still to buy: 470 Ω resistors only (+ optional multimeter). Decisions: board on sled near the ring (option A), vented cover, power bank on cuff wall, button roles B1 on/next/off, B2 Bring It. [LED Start Here](notes/LED_Wiring_Start_Here.md).
- **V4 stays NO-GO** ([audit](audits/results/FINAL_VERDICT.md)).

## Open work queue (GitHub issues)
- **Owner upload needed (checklist 2026-11-25, Main).** Use Git LFS (`.gitattributes` covers 3MF). Verify every file against the named manifest after push. Do **not** commit the local deletion of root `README.md`.
  1. `Vi_Gauntlet_V5_Print_Pack_named.zip` → replace the repo-root folder `Vi_Gauntlet_V5_Print_Pack/` with the zip's folder (same layout; correct part names #21; fixed left inserts #20; adds `0_Parts_Inventory/`). Check: its `SHA256_MANIFEST.txt`.
  2. `Repo_Upload_Issues_2_and_20.zip` → copy its `releases/` folder over the repo and run the two `git mv` lines in its `UPLOAD_STEPS.md` (R/L_08 V5_2 + mount concepts #2, fixed left inserts #20, retire R/L_08 V5_1). Check: `V5_2_SHA256_MANIFEST.txt`, `L_INSERTS_NORMALS_FIX_SHA256.txt`.
  3. `V5_4_Left_Arm_Spare_Match_v2.zip` (not the first version) → its three `*_SPAREMATCH.3mf` into `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_4_Spare_Twins/`. Check: `V5_4_Spare_Twins/V5_4_SHA256_MANIFEST.txt`.
  4. Button pod v2 → `electronics/concepts/2026-11-22_controller_placement_option_A/print/`: `Button_Pod_v2_HUAZIZ_for_18p0_beech_rod.3mf` (sha256 7425796004f8b14a396e2a5766327ba33556f17445459482982151da1e913e04, the one in use) and optionally `..._for_18p8_printed_handle.3mf` (3f067b0a2a6a792a52ef75ada5a1e22c3fb7df476628ec5d2d095cd0cf514148). Plus the Electronics conversation's sled R/L + vented cover 3MFs (that conversation has their names).
  5. Optional: V5.5 clean thumb-base reprints `R_Thumb_Base_V5_5_mirrored.3mf`, `L_Thumb_Base_V5_5_stock.3mf` → `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_5_Thumb_Fix/` (Mechanics conversation delivered them; check `V5_5_SHA256_MANIFEST.txt`).
  - Done: V5.3 thumb package (Copilot 2026-11-25, `/V5_3_Thumb_Joint/`, verified) **but V5.3 is withdrawn**; keep for history. Superseded, do not upload: `V5_4_Left_Arm_Spare_Match.zip` (v1), `L_Inserts_Normals_Fix.zip`, `V5_2_changed_files.zip`, `Vi_Gauntlet_V5_Print_Pack.zip` (unnamed).
- Print/fit: #4 ring fit with real strip, #5 finger string pull, #6 dowel fit, #7 handle, #8 gauge/cover retention, #14 thumb route, #15 supports, #16 centre seam.
- Electronics: #9 mounts vs hardware (pods printed + fitted on beech rods, final; sled v3 + cover test print pending), #10 controller pin map, #11 WLED on device, #12 firmware build, #13 current/temperature.
- Bambu Studio slice: #3.

## Pending owner decisions
- Button LEDs: always-on (one extra 5V wire + 470 Ω per LED) or not wired.
- Whether a 0.6 mm nozzle is available and whether to use a faster left-arm profile (web reports: little gain on Bambu printers; see Print queue). Fallback finish for the left arm if prints run late (Main / Finishing).
- Part labelling (owner note 2026-11-21): parts need IDs in Bambu Studio and physically. Options: marker/tape now; owner adds text in Bambu Studio; or Claude engraves IDs on hidden inner faces of the left-arm shells (geometry change, needs approval).
- Whether to flatten the lens undersides (cosmetic; they print fine as is).

## Latest actions (newest first; one short entry each)
### 2026-11-25 02:35 CET, Claude (Main sweep)
- Scheduled sweep: one new commit (Finishing right-arm glue-up guide, rod 249 mm). Linked the guide in the topic table and Deadline plan; rod length in Current state. Archived older entries verbatim. Mechanics inbox note still waits for Print queue. No new owner decisions for memory.
- Sync: PUSHED (see git log).

### 2026-11-25 01:55 CET, Claude (Main)
- Merged the Main part of the Mechanics inbox note (thumb V5.3 withdrawn; the error was Main's V5.3 build using the left-hand stock base on the right arm). Deadline plan v2 and Current state updated: L_13 = V5_1, thumb joint = key + epoxy after a wire test; V5.5 reprints added to the upload checklist. Inbox note left for Print queue (marked Main-merged). Claude project memory updated.
- Sync: PUSHED (see git log).

### 2026-11-25 01:50 CET, Claude (Mechanics)
- **Thumb V5.3 WITHDRAWN.** The stock Thumb_Base is the LEFT-hand part (mirror fit 0.013 mm); V5.3 forced it onto the right arm. The correct-hand base keys into the existing V5_1 square pocket, so no socket or dowel is needed. **Print `L_13_Knuckles_Right_V5_1`, not V5_3.** Printed V5.3 bases are swapped (`L_` = right arm), plug the stray hole. Printed R_13 V5_3 is usable (pocket intact). Files: `releases/v5/.../V5_5_Thumb_Fix/`; inbox note for Print queue and Main. **Owner upload needed:** `R/L_Thumb_Base_V5_5` 3MFs (optional reprints).
- Sync: PUSHED (see git log).

### 2026-11-25 01:45 CET, Claude (Electronics & LEDs)
- Owner confirmed: transparent-PLA pods v2 clip onto the 18 mm beech rods and work; no screws, no redesign. Stale "final pod in PETG"/"not printed" lines fixed (LED Start Here, option-A print/README, issue #9 line).
- Sync: PUSHED (see git log).

### 2026-11-25 01:40 CET, Claude (Main)
- Checked Copilot's sync at owner request: **OK.** Fast-forward only (Claude's last push `bae19da` is an ancestor of `59e164b`; no history rewritten); 14 files changed, all additions except HANDOFF header; V5.3 package added at repo root `V5_3_Thumb_Joint/`; all 4 LFS objects fetched from GitHub and SHA-256 identical to the manifest; root `README.md` intact on GitHub (its deletion exists only unstaged on the owner's PC: do not commit it). Still pending owner uploads: #2, #20, #21, V5.4 SPAREMATCH.
- Sync: PUSHED (see git log).

### 2026-11-25 00:23 UTC, Copilot SDK (repository sync)
- Fetched and fast-forwarded `main` from `493cbb9` to `744b27f`, preserving the existing local deletion of root `README.md` and the untracked `V5_3_Thumb_Joint/` folder. Remote did not change `README.md`. No local deletion was staged.
- Package backup: nine V5.3 files pushed at `1ec674df10bd95c8e6c01afe21e44066fdd49053`; all four LFS objects independently fetched and hash-checked; `git lfs fsck` passed. At the owner's request, root `README.md` was restored from HEAD. Rebased the restoration record onto `66b6a21` without conflicts; owner upload checklist and confirmed button-pod fit preserved. Push pending.

### 2026-11-25 03:00 CET, Claude (Finishing conversation)
- Wrote the right-arm glue-up guide [notes/Finishing_Assembly_Guide_Right_Arm.md](notes/Finishing_Assembly_Guide_Right_Arm.md) (+ PDF sent to owner): 4 rounds, 57 dowels, figures. **Beech rod 249 mm** (computed socket floor-to-floor 251.0; owner re-measures). Stages 5 and 9 (knuckles) wait for finger string test and thumb joint. Sled and wires before stages 7 and 10. Nothing glued or fitted yet.
- Sync: PUSHED (see git log).

### 2026-11-25 01:30 CET, Claude (Finishing conversation)
- Owner decided the paint look (spray blue, hand/dry-brush gold, clear coat maybe later) from a reference photo: logged in Decision Log + Finishing Start Here. Recommended matte white inside the LED groove/crystal well/ring trough (not black, not gold); awaiting OK. Nothing glued or painted by me.
- Sync: PUSHED (see git log).

### 2026-11-25 00:50 CET, Claude (Main)
- Updated from the repo (Print queue, Electronics, Finishing, Mechanics work since 11-22). Hygiene: merged Print queue inbox note (schedule slip) and deleted it; archived entries 2026-11-22 22:05 and older verbatim. **Deadline plan v2**: right arm glue-up Wed, left sub-assembly pipeline, fallbacks F1–F3, 7 blocking decisions (thumb fixed?, G1–G4, paint, F1 approval, wire/resistors, string test, deadline hour). Hub status refreshed.
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
