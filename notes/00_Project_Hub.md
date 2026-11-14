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

## Knowledge notes
- [[01_Engineering_Map|Design and engineering map]]
- [[02_Agent_Roles|Agent responsibilities]]
- [[03_Decision_Log|Decision log]]
- [[04_Test_Log|Validation and print test log]]
- [[05_Risks_and_Blockers|Risks and blockers]]
- [[Action_Log|Milestone index]]
- [[sessions/README|Per-agent session logs]]

## Current status
**V4 is a digital candidate, not cleared for full printing.** The required set contains 9 originals, 49 V4 files, and the V3 fit-validation ZIP. All 59 required files pass exact byte-size and SHA-256 checks against [[docs/ASSET_SHA256_MANIFEST]]. V1/V2 are intentionally excluded. The V3 ZIP opens and contains 21 fit-validation/support files. All 46 LFS assets are tracked; the V3 object was pushed and fetched from a fresh clone with matching size/SHA-256. Commit `beb157522fe4571d869ccaea186d5ceaddafaa68` is verified on remote `main`. No verified LED-strip dimensions or end-to-end physical assembly test.

## Agent reminder
After **every** project action, record the result in your own dated session note and update [[HANDOFF]]. Push at completed atomic checkpoints. A local edit is not a cross-agent update until committed and pushed.
