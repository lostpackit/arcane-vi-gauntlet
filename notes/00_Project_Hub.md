---
type: dashboard
project: arcane-vi-gauntlet
status: active
tags: [arcane, vi, 3d-printing, dashboard]
---

# Arcane Vi Gauntlet — Project Hub

> **Start here in Obsidian.** The repository root is the vault. Read [[HANDOFF]] and [[AGENTS]] before doing any work.

## Live navigation
- [[HANDOFF|Current agent handoff]] — latest verified state, blockers and next action
- [[AGENTS|Mandatory agent operating rules]]
- [[docs/AGENT_SYNC_PROTOCOL|After-action synchronization protocol]]
- [[docs/PROJECT_BRIEF|Project requirements]]
- [[docs/RELEASE_GATES|Print-release acceptance gates]]
- [[docs/ELECTRONICS_AND_STRINGS|LED and tendon constraints]]
- [[docs/ASSET_MAP|CAD asset manifest]]
- [[docs/OBSIDIAN_SETUP|Vault setup]]
- [[audits/claude/CLAUDE_MASTER_PROMPT|Claude independent audit]]

- [[electronics/README|Electronics design pack]] — BOM, effects, wiring, WLED presets, alternative ESP32 code; **Claude review required**
- [[electronics/REVIEW_CHECKLIST|Electronics review checklist]]

## Start Here notes (one per workstream)
- **[[Deadline_Plan_2026-11-28|Deadline plan to 2026-11-28]]** (Main)
- [[Conversation_Starters|Topic conversations: who owns what]]
- [[Print_Queue_Start_Here|Print queue to 2026-11-28]]
- [[Mechanics_Start_Here|Mechanics: fingers, strings, thumb, handle, dowels]]
- [[Finishing_Start_Here|Finishing: glue-up, paint, final assembly]]
- [[LED_Wiring_Start_Here|LEDs, wiring, WLED, firmware]]
- Printing: [[releases/v5/Vi_Gauntlet_X1C_V5_Draft/PRINT_ORDER|Print order]] and [[releases/v5/Vi_Gauntlet_X1C_V5_Draft/Inventory/V5_Parts_Inventory|Parts inventory]]
- Inbox from chat-only AIs: `notes/inbox/` (merge at session start)

## Knowledge notes
- [[01_Engineering_Map|Design and engineering map]]
- [[02_Agent_Roles|Agent responsibilities]]
- [[03_Decision_Log|Decision log]]
- [[04_Test_Log|Validation and print test log]]
- [[05_Risks_and_Blockers|Risks and blockers]]
- [[Action_Log|Milestone index]]
- [[sessions/README|Per-agent session logs]]

## Current status (2026-11-25)
**Deadline 2026-11-28: both gauntlets working and painted.** Plan v2: [[Deadline_Plan_2026-11-28]]. Current state in [[HANDOFF]].

**Printing:** right arm **all 13 shells printed** (R_13 V5_3 last, 11-24). Left arm: spares R_01/R_02/R_05 as L_03/L_04/L_06 + L_09 printed; 8 X1C shells + L_07 to go (≈55 h on the first Bambu estimate). All remaining prints SUNLU standard PLA, 3 walls, 3 %. Handles = beech rod. [[Print_Queue_Start_Here]].

**Electronics:** both board + strip bench tests PASS; right strip dry-fit counted; WLED 16 presets v3 accepted. [[LED_Wiring_Start_Here]].

**Finishing / mechanics:** nothing glued or painted; finger string test and thumb dry-fit still to do. **Thumb V5.3 withdrawn (11-25): key + square pocket of V5_1, left arm prints L_13 V5_1.** [[Finishing_Plan_2026-11-28]] · [[Mechanics_Start_Here]].

**Independent audit (Claude, 2026-11-14): NO-GO for the V4 shell set.** Shell 08 seals the LED chamber, the handle is cut, and the finger mount is a different revision from the printable base. Start with [[audits/results/FINAL_VERDICT]] and [[audits/results/ISSUES]]. Four small test prints are proposed.

**History:** V5's 33 models remain in Git LFS, with superseded shells separated for history. Original/V3/V4 asset verification is recorded in [[docs/ASSET_MAP]]; V1/V2 were intentionally excluded.

## Agent reminder
After **every** project action, record the result in your own dated session note and update [[HANDOFF]]. Push at completed atomic checkpoints. A local edit is not a cross-agent update until committed and pushed.

**Topic conversations and ownership:** [[Conversation_Starters]] · Finishing: [[Finishing_Start_Here]]
