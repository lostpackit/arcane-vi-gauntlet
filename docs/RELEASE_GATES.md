# Engineering release gates

**V4 status: NOT APPROVED for full production. Independent audit verdict (Claude, 2026-11-14): NO-GO.** See `audits/results/FINAL_VERDICT.md`. Statuses below marked "computed" come from CAD analysis; no Bambu Studio slice and no physical test has been done.

| Gate | Required evidence | Current status |
|---|---|---|
| Source fidelity | Compare original 3MF objects/transforms with derived full-arm meshes | **FAIL** (2026-11-14, Claude, computed) — V4 equals the fused arm exactly, but the fused arm is not the 3MF functional design: parts fused, `Fingers_Base`/`Glove_B1` are different revisions. `audits/results/ISSUES.md` C-0, C-2, C-3, H-7 |
| Source licensing | Verify permission to privately store/share originals | UNKNOWN — 3MF has no licence/designer metadata (Claude, 2026-11-14) |
| Mesh integrity | Independently check watertightness, intersections, volume, and component counts | PASS (computed, Claude 2026-11-14) with caveat — 26/26 watertight, single body, volumes match; self-intersecting faces in every shell (ISSUES M-9). `audits/results/GEOMETRY_REPORT.csv` |
| X1C fit | Bambu Studio orientations, brim/support footprint and machine keep-outs | UNKNOWN — envelope incl. 8 mm brim fits (computed); Bambu Studio keep-outs not checked |
| Toolpaths | Actual slicing, overhangs, supports, adhesion, collision and estimates | UNKNOWN — PrusaSlicer surrogate slice only (6.18 kg/arm, 0.76 kg support); **no Bambu Studio slice**. `audits/results/PRINTABILITY.md` |
| Seams | All 13 sections per arm mate and can be aligned | UNKNOWN — faces mate exactly (computed); no keys, alignment unproven (ISSUES M-8) |
| Strength | Representative printed seam and adhesive tests | UNKNOWN — no physical test; handle is cut at X=211 (ISSUES C-4) |
| Finger mounting | Original finger bases fit V4 sections 12/13 | **FAIL** (computed) — mount in shells 12/13 is a different revision from printable `Fingers_Base` (ISSUES C-3); physical fit untested |
| Tendons | Five routes, full travel, replaceability and acceptable friction | **FAIL** (computed) — documented corridor is the arm opening; real bores are 4 × 3.4–3.8 mm, no thumb route found, 4 mm PTFE does not fit (ISSUES C-5) |
| Lighting | Exact LED strip width, thickness, bend radius, cover closure and removal | **FAIL** (computed) — shell 08 LED chamber sealed, cover seat solid (ISSUES C-1). Original ring trough 27.1 × 13.3 mm measured; strip fit pending test T-1 |
| Electronics | ESP32, buttons, battery, wiring, strain relief and safe charging | BLOCKED — no hardware; plan in `audits/results/ELECTRONICS_FIT.md` |
| Wearability | Hand clearance, comfort, articulation, safe edges | UNKNOWN — about 5.4 kg of shell per arm (surrogate slice) on one grip (ISSUES H-6) |
| End-to-end | One assembled side with functioning lights and fingers | BLOCKED |

Record PASS only with evidence. FAIL, UNKNOWN, and BLOCKED are not PASS. Physical validation cannot be replaced by a digital render.

## V5 draft (2026-11-14)

`releases/v5/Vi_Gauntlet_X1C_V5_Draft/` is a **draft** and is **not approved**. Computed checks pass for mesh integrity, envelope, open LED trough, cover/gauge removal, handle sockets and dowel sockets (`V5_Verification.json`). Every gate that needs Bambu Studio or a physical test is still UNKNOWN or BLOCKED for V5. Finger mounting and Tendons remain unresolved (shells 12/13 on hold).
