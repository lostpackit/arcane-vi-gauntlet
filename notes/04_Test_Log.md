---
type: validation-log
tags: [testing, validation]
---

# Validation and print test log

**No independently verified physical build, complete Bambu Studio slice, finger-string test or LED fit test has been recorded in this repository.** Do not convert earlier digital claims into PASS without rerunning checks.

For each test, add a separate note from [[templates/Validation_Template]] or append a row here with date, part, printer/material/profile, method, observed evidence, PASS/FAIL/UNKNOWN/BLOCKED, and the associated commit.

| Date | Test | Status | Evidence |
|---|---|---|---|
| 2026-11-14 | Required asset size/SHA-256 verification | PASS (59/59) | [[docs/ASSET_MAP]]; `docs/ASSET_SHA256_MANIFEST.csv`; 9 originals + 49 V4 + 1 V3 ZIP; V1/V2 excluded |
| 2026-11-14 | V3 archive structure/content | PASS | `tar.exe -tf` listed 21 file entries; every entry opened/decompressed, 1,247,730 bytes total |
| 2026-11-14 | Remote commit and asset visibility | PASS | `origin/main` equals `beb157522fe4571d869ccaea186d5ceaddafaa68`; GitHub listings show the required asset paths |
| 2026-11-14 | Git LFS configuration and inventory | PASS | 46 assets tracked (44 STL, 1 3MF, 1 V3 ZIP); V3 resolves to `filter=lfs`; push reported 1/1 new LFS object uploaded |
| 2026-11-14 | Targeted remote V3 LFS readback | PASS | Fresh shallow clone fetched only the V3 ZIP; 698,022 bytes and SHA-256 `99647f63cfc4dabf5b05703b74c5e41d67fa37251cc6009c32a497d519323315` matched |
| 2026-11-14 | V4 independent release audit (Claude; CAD analysis + surrogate slice, no physical test) | DONE — verdict NO-GO | `audits/results/FINAL_VERDICT.md`, `audits/results/ISSUES.md` |
| 2026-11-14 | LFS asset re-verification by Claude (46 objects vs pointer SHA-256) | PASS (46/46) | `audits/results/INVENTORY.md` |
| 2026-11-14 | 26 shells: watertight / single body / mirror / reassembly to source | PASS (computed) | `audits/results/GEOMETRY_REPORT.csv`, `audits/results/evidence/reassembly_report.json` |
| 2026-11-14 | Shell 08 LED chamber and cover seat | FAIL (computed): chamber sealed, cover volume 99.7 % solid | `audits/results/evidence/led_ring_profile_ringframe.png` |
| 2026-11-14 | Finger base revision, fused arm vs printable 3MF | FAIL (computed): 25 % of surface > 1 mm apart | `audits/results/evidence/version_diff_sections.png` |
| 2026-11-14 | Surrogate slice, PrusaSlicer 2.7.2 X1C-like profile (NOT Bambu Studio) | INFO: 6,183 g per arm incl. 761 g support | `audits/results/evidence/surrogate_slice.csv` |
| 2026-11-14 | Full X1C slicer check | NOT RUN | [[docs/RELEASE_GATES]] |
| 2026-11-14 | V5 draft: 33 files closed-solid / mirror / open trough / cap lift-out / handle sockets / dowel sockets | PASS (computed) | `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_Verification.json` |
| 2026-11-14 | V5 draft surrogate slice, lightweight settings (PrusaSlicer, NOT Bambu Studio) | INFO: 3,843 g per arm incl. 760 g support, standard PLA | `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_Surrogate_Slice_Light_Settings.csv` |
| 2026-11-14 | V5 physical prints (T-1, T2 coupon, dowel fit) | NOT RUN | owner to print |
| 2026-11-14 | LED strip and ring fit | BLOCKED (hardware) — CAD measured: trough 27.1 mm wide × 13.3 mm deep; physical test T-1 proposed | `audits/results/ELECTRONICS_FIT.md` |
| 2026-11-14 | Original finger mount and tendon travel | NOT RUN physically — digital findings in ISSUES C-3, C-5; test T-2 proposed | `audits/results/FINAL_VERDICT.md` |
| 2026-11-14 | V5 draft model SHA-256 manifest | PASS (33/33, local) | `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_SHA256_MANIFEST.txt`; 82,500,770 bytes; LFS remote readback pending |

Also update [[docs/RELEASE_GATES]] and [[HANDOFF]] after every test.
