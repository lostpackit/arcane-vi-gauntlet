---
type: agent-handoff
project: arcane-vi-gauntlet
status: active
updated_date: 2026-11-21
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
| Printing V5 parts | [Print order](releases/v5/Vi_Gauntlet_X1C_V5_Draft/PRINT_ORDER.md), [Parts inventory](releases/v5/Vi_Gauntlet_X1C_V5_Draft/Inventory/V5_Parts_Inventory.md) |
| LEDs, wiring, WLED, firmware | [LED_Wiring_Start_Here](notes/LED_Wiring_Start_Here.md) |
| Why something was decided | [Decision log](notes/03_Decision_Log.md) |
| What has been tested | [Test log](notes/04_Test_Log.md), [Release gates](docs/RELEASE_GATES.md) |

## Current state (2026-11-21)
- **V4: NO-GO** ([audit verdict](audits/results/FINAL_VERDICT.md)). Do not print V4 shells.
- **Print set: V5 / V5.1 / V5.2** in `releases/v5/Vi_Gauntlet_X1C_V5_Draft/`. Shell 08 must be `_V5_2`. Not print-approved by release gates; owner is test-printing.
- **Physical results:** T2 finger coupon PASS (2026-11-18). Owner nearly done printing the **right arm** (2026-11-21). Glow-blue PETG covers FAIL (wet); covers now GiantArm transparent PLA.
- **Materials/assembly:** shells LW-PLA; handle printed PLA/PETG or 18 mm beech rod; wooden 6 × 30 mm dowels (57 per arm); UHU Plus Schnellfest epoxy for seams; UHU Poly Max for covers/electronics; no super glue near clear parts.
- **Electronics:** Sparkle Motion Mini (1 of 2 received), BTF 5 mm 160/m strip received, 91 LEDs per arm, data GPIO 32, buttons 14/27, WLED. Bench test not yet run. Rest of parts being ordered.
- **No Bambu Studio slice by any agent** (issue #3). Only owner prints are physical evidence.

## Open work queue (GitHub issues)
- **Owner upload needed:** #2 (V5.2 shell 08 + mount concepts), #20 (fixed left inserts). Files in `Repo_Upload_Issues_2_and_20.zip` from Claude; steps in its `UPLOAD_STEPS.md`. Claude's session cannot upload LFS.
- Print/fit: #4 ring fit with real strip, #5 finger string pull, #6 dowel fit, #7 handle, #8 gauge/cover retention, #14 thumb route, #15 supports, #16 centre seam.
- Electronics: #9 mounts vs hardware (sled must be redone for 32 × 20 mm board), #10 controller pin map, #11 WLED on device, #12 firmware build, #13 current/temperature.
- Bambu Studio slice: #3.

## Pending owner decisions
- Lighting behaviour: "breathing all the time, button triggers an effect, then back to breathing" (durations and button mapping).
- Part labelling (owner note 2026-11-21): parts need IDs in Bambu Studio and physically. Options: marker/tape now; owner adds text in Bambu Studio; or Claude engraves IDs on hidden inner faces of the left-arm shells (geometry change, needs approval).
- Whether to flatten the lens undersides (cosmetic; they print fine as is).

## Latest actions (newest first; one short entry each)
### 2026-11-21 22:50, Claude
- Claude Project "Arcane Gauntlets": added start-here pointer doc; V4 verdict doc marked historical. Project instructions still empty: owner to paste `docs/AI_CONTEXT_INSTRUCTIONS.md`. Sync: PUSHED.

### 2026-11-21 22:45, Claude
- Added vault hygiene check at every session start (AGENTS.md rule 5a); owner trigger: "clean up the vault". Sync: PUSHED.

### 2026-11-21 22:35, Claude
- Action: Compacted this handoff (was 296 lines). Full previous text archived verbatim at [HANDOFF_SNAPSHOT_2026-11-21](notes/handoff_archive/HANDOFF_SNAPSHOT_2026-11-21.md). Added "Context continuity" rules to AGENTS.md and the sync protocol, inbox capture for chat-only AIs (`notes/inbox/`), and a paste-in instruction for other AI tools (`docs/AI_CONTEXT_INSTRUCTIONS.md`).
- Next: owner uploads #2/#20; LED bench test in a new conversation starting from LED_Wiring_Start_Here.
- Sync: PUSHED (see git log).

### 2026-11-21 22:30, Claude
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
