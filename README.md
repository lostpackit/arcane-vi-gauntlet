# Arcane Vi Gauntlet — X1C Redesign

**Status: V4 independently audited NO-GO. Current work is the V5.1 draft in `releases/v5/Vi_Gauntlet_X1C_V5_Draft/`, approved for test prints only.**

Private engineering repository for adapting the multi-part *Arcane* Vi gauntlets to a Bambu Lab **X1 Carbon** (0.4 mm nozzle; nominal 256 × 256 × 256 mm build volume).

## Goals
- Build a matched left/right pair with **fewer larger structural prints**, less hand assembly, and a clean exterior.
- Keep the **original fingers** (already printing) compatible and manually string-actuated. No motorized knuckles in this revision.
- Support animated addressable LEDs, wearable effect-selection buttons, and a serviceable controller/power system.
- Preserve the circular lighting ring, cover/diffuser, electronics accessibility, finger-string routing, and repair access.
- Do not assume a 10 mm LED strip fits until its measured width, thickness, bend radius, and wiring are checked.

## Design history
| Version | What changed | Status |
|---|---|---|
| V1 | Initial eight-section per arm cut | Superseded concept |
| V2 | Mesh repairs and dowel socket prototypes | Superseded prototype |
| V3 | Light-ring and PTFE channel fit coupons | Fit-test concept |
| V4 | 13 shell sections per arm; light ring in one section; separate cover and reinforcement splines | **Independent audit: NO-GO** |
| V5 | Draft with separate lighting inserts, handle and dowel sockets | Superseded in part by V5.1 |
| V5.1 | Revised hand light channel, crystal well and selected shells | Draft; test prints only |

Earlier checks reported watertight STL meshes and nominal X1C bed fit, but **a closed mesh is not proof of a printable, mechanically sound or wearable design**. There has been no independently verified Bambu Studio slicing, complete finger travel, lighting fit, strength or physical assembly.

## Obsidian knowledge base and cross-agent handoff
The **repository root is an Obsidian vault**. Open the cloned repository folder in Obsidian and start at [Project Hub](notes/00_Project_Hub.md). The live state shared by Claude, ChatGPT, Codex, Copilot, Hermes and other agents is [HANDOFF.md](HANDOFF.md).

**All agents must follow [AGENTS.md](AGENTS.md)**: read the handoff before acting; **after every action, successful or failed**, update the handoff and a dated session log; commit and push at atomic checkpoints. Read [agent sync protocol](docs/AGENT_SYNC_PROTOCOL.md) and [Obsidian setup](docs/OBSIDIAN_SETUP.md). This is a workflow requirement, not an automatic background synchronization service.

**If you are uploading CAD files now:** documentation changes may have been pushed since you cloned. Run `git pull --rebase origin main` before your asset push (first preserve/commit any local changes; never discard them).

## Read first
- [Engineering acceptance gates](docs/RELEASE_GATES.md)
- [Build requirements](docs/PROJECT_BRIEF.md)
- [Electronics and finger string constraints](docs/ELECTRONICS_AND_STRINGS.md)
- [Claude independent review](audits/claude/CLAUDE_MASTER_PROMPT.md)
- [V4 audit verdict](audits/results/FINAL_VERDICT.md)
- [V5.1 draft and print set](releases/v5/Vi_Gauntlet_X1C_V5_Draft/README_V5_DRAFT.md)
- [Current electronics order list](electronics/ORDER_LIST.md)
- [CAD asset upload instructions](docs/UPLOAD_CAD_ASSETS.md)

## CAD storage and build workflow
The original, V3, V4, V5 and V5.1 CAD assets are in the repository using **Git LFS** for STL, 3MF, and ZIP objects. V1 and V2 were intentionally excluded. See the [asset map](docs/ASSET_MAP.md) and [asset instructions](docs/UPLOAD_CAD_ASSETS.md). Do not commit generated G-code.

**Original 3MF reference:** [Vi Gauntlet 3mf Project File.3mf](originals/Vi%20Gauntlet%203mf%20Project%20File.3mf) is the original model used as a guide. The owner states that only the fingers remain correct for this project: use this file **only as a finger reference**, not as the current design for the rest of the gauntlet. Finger mounting and tendon compatibility still require the checks in the [handoff](HANDOFF.md).

Keep this repository **private** until the third-party model license and redistribution permissions are established. Nothing here grants rights to *Arcane* or third-party source meshes.

## Release rule
A GO verdict requires independent source fidelity, actual X1C slicer/toolpath review, confirmed joins, finger attachment and tendon travel, removable LED cover/LED fit, electrical access, safety, and representative physical fit tests. Until then, **hold full armor production** and print only targeted tests/fingers from the original 3MF.
