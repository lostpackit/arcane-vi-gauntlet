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

## Knowledge notes
- [[01_Engineering_Map|Design and engineering map]]
- [[02_Agent_Roles|Agent responsibilities]]
- [[03_Decision_Log|Decision log]]
- [[04_Test_Log|Validation and print test log]]
- [[05_Risks_and_Blockers|Risks and blockers]]
- [[Action_Log|Milestone index]]
- [[sessions/README|Per-agent session logs]]

## Current status
**V5 draft exists (Claude, 2026-11-14, owner-approved direction):** [[releases/v5/Vi_Gauntlet_X1C_V5_Draft/README_V5_DRAFT]]. Unprinted; start with the small test prints listed there.

**Independent audit (Claude, 2026-11-14): NO-GO for the V4 shell set.** Shell 08 seals the LED chamber, the handle is cut, and the finger mount is a different revision from the printable base. Start with [[audits/results/FINAL_VERDICT]] and [[audits/results/ISSUES]]. Four small test prints are proposed.

**V5 CAD payload:** 33 3MF models (13 shells per arm, six inserts, one finger-slot coupon; 82,500,770 bytes) are on remote `main` under `releases/v5/Vi_Gauntlet_X1C_V5_Draft/`. All 33 match the supplied SHA-256 manifest; Git LFS acknowledged 33/33 uploads. Fresh-clone readback of one insert and one shell matched their hashes. V5 is unprinted and not print-approved.

**V5.1 additions:** 16 revised shell and insert models match the V5.1 SHA-256 manifest locally; their archive contents were readable. Git LFS acknowledged all 16 uploads and all 16 were independently downloaded and hash-checked. Superseded V5 shells remain for history, not printing. No Bambu Studio slice or physical tests are implied.

**V4 is a digital candidate, not cleared for full printing.** The required set contains 9 originals, 49 V4 files, and the V3 fit-validation ZIP. All 59 required files pass exact byte-size and SHA-256 checks against [[docs/ASSET_SHA256_MANIFEST]]. V1/V2 are intentionally excluded. The V3 ZIP opens and contains 21 fit-validation/support files. All 46 LFS assets are tracked; the V3 object was pushed and fetched from a fresh clone with matching size/SHA-256. Commit `beb157522fe4571d869ccaea186d5ceaddafaa68` is verified on remote `main`. No verified LED-strip dimensions or end-to-end physical assembly test.

## Agent reminder
After **every** project action, record the result in your own dated session note and update [[HANDOFF]]. Push at completed atomic checkpoints. A local edit is not a cross-agent update until committed and pushed.
