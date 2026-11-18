# CLAUDE MASTER PROMPT — VI GAUNTLET V4 INDEPENDENT ENGINEERING AUDIT

You are acting as an **independent, skeptical 3D-printing/CAD/manufacturing engineer**. Your job is to audit, and if needed repair, a redesigned 3D-printed *Arcane/Vi-style wearable gauntlet* for a Bambu Lab X1 Carbon (X1C). This is **not** a request to affirm the previous assistant's work. Assume every previous claim is **unverified until you reproduce it from the actual source and output geometry**.

## Goal and project history

The user's original project is a highly detailed gauntlet from a Bambu-compatible **3MF project with many separately printable objects**. The user wants to reduce assembly effort and visible seams by combining non-finger parts into larger, stronger prints while retaining:

1. All **original separately printed finger components** and their intended cable/string actuation. Fingers are already being printed; do not change their mating geometry without compelling evidence and explicit identification of required replacement parts.
2. The original **fixed/nonmotorized knuckle arrangement**. Motorized knuckles are on hold; any needed finger-string movement must still work.
3. A visually accurate, wearable, full-scale exterior.
4. **Animated addressable LED lighting**, not static lighting. Original circular light geometry and a removable diffuser/cover must work; LED wiring must reach an accessible controller/battery/switch location. The user has **not yet chosen or purchased** the LED strip or ESP32/controller, so actual strip width, bend radius, current draw and dimensions must not be fabricated.
5. Accessibility for threading/replacing finger strings, LEDs and electronics, and a comfortable way to wear/remove the gauntlet.
6. A reliable printable result on the user's **Bambu Lab X1 Carbon, 0.4-mm nozzle**, build volume nominally 256 × 256 × 256 mm, with no uniform downscaling of completed fingers.

The first attempt cut a fused full-arm STL into 8 sections per side but crossed the circular ring and suffered mesh defects. V2 repaired meshes and added prototype pins/splines but left functional interfaces unresolved. V3 tested PTFE corridor ideas and lighting profiles. **V4** changes the partition to **13 shell pieces per arm (26 total)** to keep the full ring base inside shell **08**, and provides separate covers, bonded reinforcement splines and optional five-channel PTFE clamps.

V4's claimed accomplishments are **not proof of assembly or functionality**: its saved-file report claims 26 watertight, positive-volume single bodies fitting the X1C nominal volume; preservation of essentially all original mesh volume; and an uncut ring base. A previous candidate corridor for five 4-mm-OD PTFE tubes was sampled only at selected locations. V4 still uses **permanently bonded planar shell joints** (not integrated removable mechanical locks), and it does **not** model an actual selected LED/controller/button/battery arrangement. The previous assistant did **not** run Bambu Studio slicing and did **not** prove finger actuation or physical LED cover fit.

## Inputs (locally available, or request them if missing)

**Original source / authoritative design:**
- `Vi Gauntlet 3mf Project File.3mf` — reference layout, individual fingers, glove shells, circular light components. Inspect the 3MF ZIP/XML metadata, per-object meshes and **object transforms / build plate placements**, not just screenshots.
- `Full_Arm_Right (No Fingers).stl` and `Full_Arm_Left (No Fingers).stl` — complete fused shell reference geometry, **not automatically evidence of a functional, serviceable assembly**.
- `Together For Sizing.stl` — reference only; verify scale/role before using it as an assembly source.
- `Circle_Light.stl`, `Circle_Light_Cover.stl`, `Circle_Top_Plate_Left.stl`, `Circle_Top_Plate_Right.stl`, `Crystal.stl` — source light pieces.

**Candidate design under audit:**
- `Vi_Gauntlet_X1C_V4_Print_Release.zip` — contains `Right_Shells/`, `Left_Shells/`, `Lighting_Covers/`, `Print_Hardware/`, `Reference/`, `Geometry_Validation/`, `Source_Scripts/`, and the V4 assembly README. Extract it completely.

**Audit kit:** current prompt, existing validation reports/scripts (for understanding provenance, not as authoritative verification), acceptance gate CSV and report template.

If the files or a functioning geometry/slicing tool are absent, distinguish **NOT CHECKED** from **PASS**; do not invent visual/mesh observations.

## Mandatory independent work, in priority order

### A. Inventory and reconstruct the assembly
- Enumerate the original 3MF objects by name, quantity, size, and role (fingers, tendon anchors, hand shell, ring, cover, fasteners, cosmetic plates, etc.). Identify **which features are active vs decorative**.
- Establish and document a **single common coordinate frame**. The V4 STL parts were reoriented for printing; use the supplied build scripts/transform records to reverse them before comparing to the assembled reference. Do not overlay print-bed-oriented STLs and conclude they do not fit.
- Create a labeled exploded view plus assembly/reconstruction overlays (right and left). Check that all required original features remain present. Detect missing geometry, extra intrusions, seams through mounting points, trapped internal pieces and inaccessible cavities.
- Check mirrored handedness and that any asymmetric finger interfaces remain on the correct side.

### B. Mesh integrity and slicer compatibility
- Independently re-load **all 26 shell STLs** from disk and compute triangle count, watertightness, manifold edges, normals/winding, signed volume, number of connected components, AABB bounds and minimum feature thickness. Report results for **each filename** in a CSV/table.
- Look for self-intersections, unintended internal walls, tiny loose islands, inverted internal faces and errors hidden by a watertightness check. Verify no vital small geometry was silently dropped during repairs.
- Verify each oriented part's actual placement and **usable Bambu X1C bed** fit, allowing realistic brim/support clearance and printer keep-outs. The 256-mm cube alone is insufficient.
- If Bambu Studio, OrcaSlicer or equivalent **actual slicer** is available, slice every shell using the X1C 0.4-mm profile, realistic PLA settings (starting proposal: 0.20-mm layer, 4 walls, 12–15% gyroid and 5 top/bottom layers); report support burden, print viability, estimated filament/time, seam appearance and overhangs. Export or capture slicer previews. No slicer = **NOT VERIFIED**, not PASS.

### C. Confirm fit of the pieces and structural joints
- Virtually reassemble the 13 original-scale pieces for each hand; check mating face alignment, gaps, overlaps and internal collisions **after inverse orientation transforms**. Compare reassembled outer surface against source full-arm geometry; overall volume preservation alone is insufficient.
- Evaluate whether **flat epoxy-bonded seams and loose splines** will align strongly and accurately in a heavy wearable prop. Check accessible bonding area, seam loading, print layer orientation and whether reinforcement splines actually fit on interior surfaces without occupying LED/tendon passages. Verify if the existing model has any reliable mechanical keys/registration. Recommend/implement improved joints if needed.
- Ensure the wearer can put on/take off the assembled gauntlet, flex the wrist as intended and access batteries/controller/string ends **after** bonding. If significant access is blocked, do not approve.

### D. Finger operation — critical and non-negotiable
- Inspect the **original 3MF finger bases, mounts, hinges, anchors and tendon attachment paths**. Check the V4 hand/knuckle shells 12/13 against the finger parts already being printed: correct scale, mounting holes/clearances, attachment orientation and range of motion.
- Verify that **five separate string conduits** can physically run from the intended actuation point to the correct individual finger attachments with no closed solid walls, pinch points, forbidden bends, snagging, rubbing, or blocked maintenance access.
- V4 describes a candidate 5 × 4-mm-OD PTFE tube corridor near source coordinates X≈194, 202.5, 211, 219.5, 228 mm; Y≈130 mm; Z≈70–470 mm. Treat these as a **hypothesis**. Test the **full 3D route**, not just selected cross-sections. Check tube outside diameter, real tube/cord clearance, guide mounting, end anchoring, and routing through every seam. If anchor hardware is absent, propose explicit printable fixes.
- Model/animate finger travel if feasible, or provide an honest physical test requirement; do **not** certify moving fingers from a static clearance measurement.

### E. Ring, LEDs, wiring and serviceability — critical and non-negotiable
- Verify that original `Circle_Light.stl` geometry is genuinely retained in ring carrier section 08, *and* that `Circle_Light_Cover.stl` can be installed/removed **after the rest of the shell has been assembled**. Confirm reference-frame alignment, snap geometry, clearances, and any ring/cover interference.
- Measure groove width/depth **along the full intended LED strip route**, minimum bend radius and available wire exit. Test 8-mm vs 10-mm strip feasibility **only from geometry**, preserving a clearance margin. Do not infer from a single screenshot or from an unrelated generic LED channel test model.
- Reserve an identifiable wire pathway from ring to the cuff with strain relief and removable service access. Do not drill through tendon mounts or through exterior decoration.
- There is no chosen LED strip, ESP32 or battery yet. Mark electrical fit, power/thermal safety, animations and button mounting **BLOCKED ON HARDWARE SELECTION** if necessary; recommend minimum dimensions and a practical controller/button/power wiring architecture without presenting hypothetical fit as verified. LED and battery should remain replaceable.

### F. Final assembly, human fit and print economics
- Verify actual wearer fit and source-vs-finger scale assumptions, including glove opening/straps and hand access. Identify exact wearer measurements required for a physical fit approval.
- Provide a build order that avoids trapping strings, LED covers, wiring or fasteners. Distinguish removable vs permanent joins and document repair procedure.
- Compare V4 print-count, estimated time, filament, support wastage, alignment complexity and structural risk with the original 3MF plate layout. The user values **saving time, material and assembly labor**, not simply reducing the number of named parts.
- Recommend a minimal but targeted **first-print validation plan** (e.g., ring carrier + matching cover, tendon/knuckle mating coupon, representative seam test, LED-width coupon) before printing both arms. Specify measurable pass/fail tolerances.

## Required output and truthfulness rules

1. **Start with a clear verdict:** `NO-GO`, `CONDITIONAL GO FOR SPECIFIED TEST PRINTS ONLY`, or `GO FOR FULL ARMOR PRINTING` and exactly what evidence supports it. Do not give blanket approval if a critical function is unverified.
2. Give a **gate-by-gate audit** using `PASS / FAIL / NOT CHECKED / NEEDS HARDWARE` for: files, assembly coordinate reconstruction, each STL, practical bed fit, slicer preview, joints, finger compatibility, complete string routing, light-cover removal, LED channel, wiring, electrical enclosure, wearability.
3. Include a **part-by-part table** with filename, dimensions, topology, support/print concerns, and estimated print time/material (estimate only with actual slicer).
4. List problems ranked **BLOCKER / MAJOR / MINOR**, showing the exact file and geometric location/measurement where possible; add screenshots or section views as evidence.
5. If you can modify CAD safely, **fix any blocker**, save corrected STLs/3MF/STEP (if possible), independently re-check them, and provide a **changelog** and `v5` revision with traceable source scripts. Never overwrite the original inputs. Never call modified files final until your own gates pass.
6. Give a concise **print order** and an exact **minimum test-print list**, with what each test proves and what a failed fit implies.
7. Tell the user plainly what can only be established by an actual X1C print, test assembly, or selected hardware. **Never fabricate a Bambu Studio result, physical fit, LED-strip dimension, or movement test.**

You have permission to be critical of the previous assistant's conclusions. Favor an actionable failure report over a flattering but unsupported approval. The objective is to prevent wasting filament and time while getting a strong, attractive, wearable gauntlet with working finger strings and animated LEDs.

**Begin by opening the supplied models and V4 ZIP, reading the manifest, and reporting exactly which files you can actually parse. Then perform the technical review without waiting for permission to inspect or write non-destructive corrected copies.**
