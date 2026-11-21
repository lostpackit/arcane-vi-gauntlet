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

## Current status
**Current print set: V5 / V5.1 / V5.2** (shell 08 = `_V5_2`): [[releases/v5/Vi_Gauntlet_X1C_V5_Draft/README_V5_DRAFT]], print order [[releases/v5/Vi_Gauntlet_X1C_V5_Draft/PRINT_ORDER]], **parts checklist [[releases/v5/Vi_Gauntlet_X1C_V5_Draft/Inventory/V5_Parts_Inventory]]**. Owner is nearly done printing the right arm (2026-11-21); finger coupon passed. No Bambu Studio slice by any agent.

**LEDs / electronics: start at [[LED_Wiring_Start_Here]].** Hardware partly received (Sparkle Motion Mini ×1, BTF 160/m strip); bench test next.

**Independent audit (Claude, 2026-11-14): NO-GO for the V4 shell set.** Shell 08 seals the LED chamber, the handle is cut, and the finger mount is a different revision from the printable base. Start with [[audits/results/FINAL_VERDICT]] and [[audits/results/ISSUES]]. Four small test prints are proposed.

**History:** V5's 33 models remain in Git LFS, with superseded shells separated for history. Original/V3/V4 asset verification is recorded in [[docs/ASSET_MAP]]; V1/V2 were intentionally excluded.

## Agent reminder
After **every** project action, record the result in your own dated session note and update [[HANDOFF]]. Push at completed atomic checkpoints. A local edit is not a cross-agent update until committed and pushed.
