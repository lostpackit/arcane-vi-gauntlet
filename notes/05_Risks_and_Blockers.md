---
type: risk-register
tags: [risk, blockers]
---

# Risks and blockers

| Risk | Status | Required next evidence |
|---|---|---|
| V3 LFS object remote availability | VERIFIED | Fresh-clone targeted readback matched the manifest size and SHA-256; internal member hashes remain unknown |
| V3 archive member hashes | UNKNOWN | Manifest covers the V3 ZIP container only; its 21 internal files are not individually listed |
| V4 printability and support requirements | UNKNOWN | Bambu Studio actual slice |
| Finger mounting and five string paths | UNKNOWN | Assembly geometry and physical travel |
| Circular LED groove width/depth and diffuser clearance | BLOCKED | Measure channel and real LED strip |
| Electronics and battery mounting/access | BLOCKED | Selected parts and dimensions |
| Bonded seam strength and serviceability | UNKNOWN | Test coupons and mechanical review |
| Third-party source license | UNKNOWN | Provenance and terms |
| **Shell 08 LED chamber sealed, cover seat solid** | OPEN — CRITICAL (Claude audit C-1) | Regenerate 08 without cover/gauge fused; test T-1 |
| **V4 cut from fused display solid, not 3MF functional parts** | OPEN — CRITICAL (C-2) | Owner decision on V5 direction |
| **Finger mount revision differs from printable Fingers_Base** | OPEN — CRITICAL (C-3) | Test T-2 |
| Handle cut at X=211 | OPEN — HIGH (C-4) | Test T-3 / one-piece handle |
| Tendon corridor claim invalid; bores 3.4–3.8 mm; thumb route unknown | OPEN — HIGH (C-5) | Test T-2; owner confirms tendon layout |
| Mass about 5.4 kg of shell per arm (surrogate slice) | OPEN — HIGH (H-6) | Bambu Studio slice at lighter settings |
| Glove_B1 23 × 63 mm opening filled | OPEN — HIGH (H-7) | Restore in V5 |
| Bambu Studio slice still not run by any agent | OPEN | Run on owner's machine |
| Claude cloud session cannot upload Git LFS objects (download and normal push work) | OPEN (tooling) — LFS storage host blocked by session network policy | Owner uploads CAD delivered as zip |
| V5 remote LFS object availability | UPLOAD ACKNOWLEDGED; SAMPLED READBACK PASS (2/33) | Push reported all 33 objects; fresh-clone readback verified one insert and one shell. Remaining objects were not individually read back |
| V5 draft unprinted; dowel and insert clearances untested in LW-PLA | OPEN | Print R_09/R_07 and inserts first |
| V5 shells 12/13 still carry the older finger carrier | OPEN — hold | T2 coupon with a printed finger |
| V5 supports about 20 % of filament | OPEN | Re-orient 05/06/08/12/13 |
| V5.1 3MF files (shells 08, 10–13, crystal, lenses) not yet in the repo | CLOSED 2026-11-15 — uploaded (`030b461`), verified 16/16; superseded files moved to `Superseded_V5_DO_NOT_PRINT/` | Owner/Copilot: upload from `V5_1_changed_files.zip`, verify manifest, remove superseded `_V5` files |
| V5.2 shell 08, mount concepts and fixed left inserts not yet in the repo | OPEN — owner upload from `Repo_Upload_Issues_2_and_20.zip` | GitHub issues #2, #20 |
| Left inserts (ring cover, crystal, lenses, gauge) had inverted normals | FIXED in files 2026-11-20; awaiting upload | issue #20 |
| Repo 3MFs all named `geometry_0` (parts indistinguishable in Bambu) | FIXED in delivered named print pack; repo copies pending upload | issue #21 |
| X1C-printed right shells (plates 21, 27) not identified | OPEN: owner to read part sizes in Bambu or measure; compare to inventory sizes | Test Log 2026-11-21 |
| Electronics sled concept sized for old board (80 × 45) | OPEN | Redesign for 32 × 20 mm Sparkle Motion Mini |
| LED bench test not yet run | OPEN | Board + strip in WLED, 10 min full-white heat check (covers are PLA) |
| Remaining work is tracked as GitHub issues #2–#16 and #20 | INFO | Use the issue list as the queue |

For current priority and ownership, see [[HANDOFF]]. Record any newly discovered risk there **after the action**.
