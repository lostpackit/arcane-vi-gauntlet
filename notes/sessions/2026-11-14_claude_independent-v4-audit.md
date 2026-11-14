---
type: agent-session
agent: Claude (Claude Code, cloud session)
task: Independent V4 engineering audit
date: 2026-11-14
status: complete
tags: [session, audit, claude, v4]
---

# 2026-11-14 — Claude — independent V4 audit

Environment: Linux cloud workspace (2 cores, ~7 GB RAM). No printer, no hardware, **no Bambu Studio**. All results below are computed geometry checks or a labelled surrogate slice. No physical test of any kind was performed.

## Log (UTC, times approximate)

- **16:09** Cloned `main` at `2bf6e6d`. Read `AGENTS.md`, `HANDOFF.md`, `docs/AGENT_SYNC_PROTOCOL.md`, `audits/claude/CLAUDE_MASTER_PROMPT.md`, `docs/RELEASE_GATES.md`, project brief, electronics/strings notes, asset map, V4 README, project hub, test log, risk register.
- **16:10** `git lfs pull` FAILED (`batch response: Resource not accessible by integration`). The session's GitHub integration has no LFS batch access.
- **16:11** Workaround: fetched all 46 LFS objects through the `media.githubusercontent.com` endpoint and compared each file's SHA-256 with the `oid` in its committed LFS pointer. **46/46 match.** Working copies are kept outside the repo tree (`/home/claude/cad`); pointer files in the repo are untouched.
- **16:12** Unpacked the project's audit kit (prior validation JSON/CSV, build scripts). Treated as claims to verify, not evidence.
- **16:13** Per-file mesh table for every STL < 60 MB (trimesh 4/5, vertices merged): bounds, volume, watertightness, winding, components, boundary / non-manifold edges, degenerate faces. → `audits/results/GEOMETRY_REPORT.csv`.
- **16:14** Parsed the original 3MF (Bambu Studio 2.2.1 project, 76 build items on 36 plates, unit mm) including component transforms and plate assignment. → `audits/results/evidence/3mf_objects.json`.
- **16:15** Split `Together For Sizing.stl` (181 components) and matched components to 3MF objects by volume. Analysed `Full_Arm_Right (No Fingers).stl` (single watertight body, 13,960.56 cm³).
- **16:17** Cross-sections of fused arm vs assembled reference. → `audits/results/evidence/sections_full_vs_together.png`.
- **16:20** Reassembled the 13 right shells into source coordinates (inverse print rotation + translation) and compared vertex-by-vertex with the source arm. → `audits/results/evidence/reassembly_report.json`.
- **16:27** Containment test of assembled reference parts against the fused arm (surface-sample distance + inside test). Run was killed by the memory limit after the 46 largest components; those rows are reported, smaller parts were re-checked separately.
- **16:30** Bambu Studio download attempted: GitHub release host returned **403 (blocked by session network policy)**. Not retried. Installed PrusaSlicer 2.7.2 from the Ubuntu archive as a **surrogate** slicer.
- **16:33** Left/right mirror check (triangle-centroid nearest-neighbour).
- **16:34** Surrogate slice of 13 right shells + cover + hardware (first batch run failed: `/usr/bin/time` missing; rerun succeeded). Result: 6,183 g per arm incl. 761 g support; "potentially lost branch" support warnings on shells 05, 06, 07, 08, 09, 12, 13. → `audits/results/evidence/surrogate_slice.csv`.
- **16:36** Ring measured in its own axis frame: trough r 28.8–55.9 mm, 13.3 mm deep, open in the original part. **In shell 08 the trough has a solid ceiling and the cover's volume is 99.7 % solid.** → `evidence/led_ring_profile_ringframe.png`.
- **16:38** Wire notch measured (14.1 / 13.2 mm) and chamber-to-cavity passage confirmed for a 7 mm probe by voxel flood fill.
- **16:40** Printable 3MF `Fingers_Base` and `Glove_B1` compared with the versions inside the fused arm: different revisions. → `evidence/version_diff_sections.png`.
- **16:42** String-bore search: four bores 3.4–3.8 mm at X = 114.1 / 179.4 / 244.6 / 308.2, Z ≈ 498–534. No thumb bore found. The documented PTFE corridor is the arm opening.
- **16:43** MeshLab self-intersection test (first attempt failed: missing libOpenGL; installed and rerun). Flags faces in every shell.
- **16:44** Seam-face areas per shell pair (first attempt mis-clipped islands; recomputed with polygon clipping). Handle cross-section found on the X=211 seam.
- **16:45** Volume-sampling of 13 reference parts against the fused arm: everything except the thumb base is fused in. → `evidence/fused_parts_volume_test.json`.
- **16:46–16:50** Wrote `audits/results/` reports; updated `docs/RELEASE_GATES.md`, `HANDOFF.md`, hub, engineering map, decision log (pending-decision entry only), test log, risks, action log.

## Outcome

Verdict **NO-GO** for the V4 shell set. See `audits/results/FINAL_VERDICT.md`.

## Not done / failed

- Bambu Studio slice: not possible here (download blocked, HTTP 403).
- `git lfs pull`: failed; worked around and verified by hash.
- Containment scan of all 181 reference components: killed by memory limit; replaced by targeted volume tests.
- Finger-to-slot clearance with 3MF finger parts: not computed (no assembled placement available).
- Thumb mount / thumb tendon: unresolved.
- V3 archive contents: not audited.
- No CAD modified, no derived STL generated, no physical test.

## Sync

PUSHED as `4fc75b8` + `243a51f` after the owner authorised the Claude GitHub App (initial push attempt was refused with HTTP 403).
