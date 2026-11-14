---
type: agent-session
agent: Claude (Claude Code, cloud session)
task: V5 draft build after owner approval
date: 2026-11-14
status: complete
tags: [session, v5, claude, cad]
---

# 2026-11-14 — Claude — V5 draft build

Owner approved the V5 direction in chat (about 18:21 UTC) and asked for a lighter build: cosplay use, lightweight PLA. Owner also connected the Claude GitHub App. No Bambu Studio and no printer in this session; nothing was physically tested.

## Log (UTC, times approximate)

- **18:22** `git push origin main` now succeeds: audit commits `4fc75b8`, `243a51f` are on GitHub. `git lfs pull` now works too.
- **18:25** Loaded the fused arm into manifold3d: valid solid, 13,960.56 cm³. Cover, gauge, needle, handle from the original parts load as valid solids.
- **18:27** Probed how the parts sit in the arm. Found: light-strip window and crystal sit in shallow recesses over a 7–8 mm wall with no LED channel behind them; the `Glove_B1` opening is covered outside by the under plates (so it is an inner pocket, not an external port); the original handle ends sit on Ø9 pegs on wall bosses.
- **18:29** First build: cover and gauge removed by scaled tools. FAILED verification: a 0.04–0.07 mm film remained over the trough and the gauge still collided slightly when lifted (scaling a non-convex shape does not give a true clearance).
- **18:31** Dowel placement returned zero sockets (margin test bug); fixed; then improved to cover every shell pair.
- **18:40** Second build: true 0.35 mm in-plane clearance (union of shifted copies) swept along the ring axis, plus an explicit annular air column for the trough. Verification passes: trough open at all probes, cover and gauge lift out with zero overlap.
- **18:42** Handle sockets: first version only reached 2.6 mm into the wall once the bosses were accounted for. Redesigned with added collars and deeper sockets: 12.3 mm engagement, 6.1–8.6 mm wall left.
- **20:55** STL export re-check FAILED: after vertex merge, most shells showed 1–46 tiny non-manifold edges (sub-0.5 mm kissing faces from the boolean output). A MeshLab repair attempt was destructive (one shell lost most of its volume) and was discarded; files rebuilt.
- **21:05** Switched output to 3MF, which keeps the valid indexed topology. 33/33 files now pass: watertight, no boundary or non-manifold edges, slicer check reports manifold single part.
- **21:10** Added T2 finger-slot coupon cut from the V5 arm.
- **21:15–21:40** Surrogate slice (PrusaSlicer 2.7.2) at lightweight settings: 3,843 g per arm incl. 760 g support in standard PLA, against 6,183 g for V4 at README settings. Seven shells still give unsupported-branch warnings.
- **21:45** Copied to `releases/v5/Vi_Gauntlet_X1C_V5_Draft/`, wrote README, updated handoff and notes.
- **22:17** Push FAILED on the LFS upload: `github-cloud.s3.amazonaws.com` is blocked by the session network policy (403). Not retried by another route. Commit redone without the binaries; 3MF files delivered to the owner as a zip with a SHA-256 manifest in the repo.

## Result

`releases/v5/Vi_Gauntlet_X1C_V5_Draft/` — 26 shells, 6 inserts, 1 test coupon, verification records, build scripts. Status: DRAFT, unprinted.

## Not done

Finger carrier revision (shells 12/13 on hold), light-strip and crystal lighting channels, electronics mounts, seam-plane relocation, thumb route, support-reducing re-orientation, Bambu Studio slicing, any physical test.

## Sync

Docs, records and scripts PUSHED. The 33 `.3mf` files are NOT in the repo; owner must add them from the delivered zip (see `HANDOFF.md`).
