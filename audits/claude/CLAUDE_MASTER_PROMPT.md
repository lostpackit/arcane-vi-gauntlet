# Independent Claude Code engineering audit

You are conducting an **independent, adversarial engineering audit**, not a confirmation of prior claims. Work from the repository's original CAD assets and V4 release. **Do not assume the existing mesh-validation reports prove print readiness.**

## Goal
Determine whether the V4 left/right gauntlets can be reliably printed on a Bambu Lab X1 Carbon (0.4 mm nozzle), assembled, worn, operated with the existing manually string-actuated fingers, and equipped with animated LED lighting and wearable effect controls.

## Required process
1. Inventory source 3MF, original STLs, V1–V4 releases, scripts and prior validation reports. Record file hashes and units.
2. Independently parse the 3MF multi-object geometry and transforms; compare against the derived fused arm STLs. Identify any lost internal features or mounting interfaces.
3. For each V4 STL, measure bounds, volume, watertightness, connected components, self-intersections, degenerate faces and orientation. Supply a per-file table and reproducible commands.
4. Verify seam mating/alignment for all 13 sections on each arm; assess adhesive-only seam strength, reinforcement splines and assembly access.
5. Import/slice in Bambu Studio with actual X1C settings. Verify build-plate constraints, supports, collisions, overhangs, bridging and print estimates. **Do not claim slicer validation if Bambu Studio was not run.**
6. Compare original fingers to V4 mounts, and trace all five proposed tendon/PTFE routes from control entry to the fingertips; assess string travel, repairability and wear.
7. Measure the ring/cover channel for candidate LED strips. Determine exact usable width/depth/circumference and bend constraints. No unverified assumption that 10 mm strips fit.
8. Develop a feasible ESP32, battery, buttons and wiring service plan with actual part dimensions and electrical safety considerations. Identify measurements blocked by unpurchased hardware.
9. Identify minimum physical test prints (light ring coupon, finger attachment, seam strength coupon, tendon path) and acceptance criteria.
10. Produce a verdict: PASS, FAIL, UNKNOWN, or BLOCKED for each gate in `docs/RELEASE_GATES.md`, with evidence paths and priority fixes.

## Deliverables
- `audits/results/INVENTORY.md`
- `audits/results/GEOMETRY_REPORT.csv`
- `audits/results/ISSUES.md` (severity, reproducible evidence, proposed fix)
- `audits/results/PRINTABILITY.md`
- `audits/results/ELECTRONICS_FIT.md`
- `audits/results/FINAL_VERDICT.md`
- Recommended V5 changes, **only** if justified by findings.

Distinguish computed geometry checks, actual slicer observations, and physical tests. Do not invent evidence, CAD dimensions, or test results. Do not modify source originals.
