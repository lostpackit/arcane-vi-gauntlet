# V4 audit — issues

Independent audit by Claude, 2026-11-14. Evidence class is marked on every item:

- **[COMPUTED]** — measured from the CAD files in this repo with the scripts in `audits/claude/scripts/`.
- **[SURROGATE SLICE]** — PrusaSlicer 2.7.2 with an X1C-like profile. **Not Bambu Studio.**
- **[ESTIMATE]** — engineering estimate, not a measurement.
- Nothing in this file is a physical test. No part was printed.

Coordinates are the source/assembled frame of `Full_Arm_Right (No Fingers).stl` (X across the hand, Y palm→back, Z cuff→fingers, mm). Left arm is the exact X-mirror.

## Root cause behind most items

V4 was produced by plane-cutting `Full_Arm_Right (No Fingers).stl`. That file is a **fused display/sizing solid**, not the functional design. The functional design is the 76-object Bambu 3MF, where the ring, cover, gauge, handle, finger base, knuckles, crystal and plates are separate parts. Cutting the fused solid faithfully reproduces its shape (C-0 below) but also reproduces everything that fusing destroyed.

| ID | Sev | Issue |
|---|---|---|
| C-1 | CRITICAL | LED chamber is sealed and the cover seat is solid in shell 08 |
| C-2 | CRITICAL | Functional parts are fused into the shells |
| C-3 | CRITICAL | Finger mount in shells 12/13 is a different revision from the printable `Fingers_Base` |
| C-4 | HIGH | Load-bearing handle is cut in half at X=211 |
| C-5 | HIGH | The "five PTFE corridor" is not the tendon path; real string holes are smaller than 4 mm |
| H-6 | HIGH | Mass and filament: about 6.2 kg of filament per arm |
| H-7 | HIGH | A 23 × 63 mm through-opening in `Glove_B1` is filled solid |
| M-8 | MEDIUM | Unkeyed planar butt seams; centreline seam runs through visible details |
| M-9 | MEDIUM | Self-intersecting faces in every shell |
| M-10 | MEDIUM | Support load and unsupported-branch warnings |
| L-11…15 | LOW | Documentation and accessory mismatches |

---

## C-0 (finding, not a defect): V4 is an exact partition of the fused source — [COMPUTED]

- All 13 right shells, inverse-transformed to the source frame: every vertex is either a source vertex (within 0.02 mm) or lies on a cut plane. Zero stray vertices. `evidence/reassembly_report.json`.
- Only 57 of 1,114,221 source vertices are absent from the shells: four slivers, 4.0 mm² total, at Y≈180, Z≈286–294.
- Sum of right shell volumes 13,960.56 cm³ = source 13,960.56 cm³.
- All 13 left shells are exact X-mirrors of the right shells (max triangle-centroid deviation 0.0 mm). `Full_Arm_Left` is an exact mirror of `Full_Arm_Right`.
- All 26 shells: watertight, consistent winding, one body, no boundary or non-manifold edges.

So the earlier mesh-validity claims are confirmed. They do not make V4 functional.

## C-1 CRITICAL — LED chamber sealed, cover seat solid (R_08 / L_08) — [COMPUTED]

Measured in the ring's own axis frame (axis tilted 1.9° from Y), h = axial height:

| Feature | Original `Circle_Light.stl` | V4 shell 08 |
|---|---|---|
| Annular trough, inner wall radius | 28.8 mm | 28.8 mm |
| Trough outer wall radius | 55.9 mm | 55.9 mm |
| Trough floor | h = −3.46 | h = −3.50 |
| Above the trough | **open** (top-down probe reaches the floor) | **solid ceiling at h = 9.81**, then solid up to h ≈ 25.5–26.7 |
| Cover volume occupied by solid | n/a | **99.7 %** of 1,842 sample points |

In shell 08 the trough is an enclosed void under about 16 mm of material: the cover (h 9.8–14.2) and the `Pressure` gauge body (h 14.0–25.9) are both part of the shell.

Consequences:
- No LED strip can be installed in a printed shell 08.
- The separately supplied `R/L_Circle_Light_Cover` STLs have nowhere to go; their seat is filled.
- README step 1 ("print shell 08 first, then dry-fit the lens") would spend about 660 g and more than a day of printing on a part that cannot take lighting. [SURROGATE SLICE]

Evidence: `evidence/led_ring_profile_ringframe.png`, `audits/claude/scripts/led4.py`, `led5.py`, `evidence/fused_parts_volume_test.json`.

Proposed correction (needs approval): shell 08 must be regenerated with `Circle_Light_Cover`, `Pressure`, `Pressure_Needle` and preferably `Circle_Light` itself excluded from the union, so the ring assembly stays a removable stack as in the 3MF.

## C-2 CRITICAL — functional parts fused into the shells — [COMPUTED]

Volume-sampling each part of the assembled reference against the fused arm (fraction of the part's volume that is solid arm):

| Part | Inside fused arm | Why it matters |
|---|---|---|
| Circle_Light_Cover | 99.8 % | diffuser, must be removable |
| Pressure, Pressure_Needle | 99.7 %, 97.8 % | gauge sits over the light |
| Glove_Light_Strip | 96.6 % | second light window (13.3 × 238 mm, back of hand) is solid |
| Crystal, Crystal_Base | 98.8 %, 99.6 % | translucent feature, now opaque and cut at X=211 |
| Handle | 99.7 % | see C-4 |
| Fingers_Base, Gold_Base_Finger, Finger_Knot ×4 | 99.6–99.9 % | see C-3 |
| Circle_Top_Plates, Under plates, Pistons, HandPalm details | fused | colour separation lost; cosmetic |
| Thumb_Base | 0.4 % | not fused (correct) |

Evidence: `evidence/fused_parts_volume_test.json`, `evidence/sections_full_vs_together.png`.

## C-3 CRITICAL — finger mount revision mismatch — [COMPUTED]

- Printable `Fingers_Base.stl` in the 3MF: 340.02 cm³, 277.8 × 94.6 × 78.0 mm.
- Finger base fused into the arm (and therefore into shells 12/13): 360.37 cm³, 277.8 × 94.6 × 79.0 mm.
- After best-fit translation, 47 % of the printable part's surface is more than 0.3 mm from the fused version and 25 % is more than 1 mm away; local differences reach about 6–12 mm (slot depths, end posts). `evidence/version_diff_sections.png`.
- The finger segments in the sizing model also do not volume-match the 3MF finger parts, and the 3MF contains `*_Middle_B_V2` parts. The fused arm appears to be an older revision than the printable set.

The fingers being printed from the 3MF were designed against the 3MF `Fingers_Base`, not against the geometry now inside shells 12/13. Whether they still seat is unknown; it cannot be claimed as preserved. I could not place the 3MF finger parts in assembled coordinates (the 3MF stores print layout only), so no finger-to-slot clearance was computed.

Proposed correction: build the knuckle region from the 3MF `Fingers_Base`, `Gold_Base_Finger` and `Finger_Knot_*` parts as separate pieces. Validate first with test T-2.

## C-4 HIGH — handle cut at mid-span — [COMPUTED] + [ESTIMATE]

- `Handle.stl` is one part in the 3MF: Ø18.8 mm × 226.8 mm, spanning X 97.9–324.6 at Y≈156, Z≈376. It is the grip that carries the gauntlet.
- In V4 it is fused into shells 10 and 11 and cut by the X=211 plane. The seam section shows a 2.8 cm² island at Y 147–165, Z 367–385: a plain butt joint of the bar.
- [ESTIMATE] A simply supported 227 mm bar with a 50 N central load sees about 2.8 N·m at the joint; a swing multiplies that several times. A glued PLA butt joint of this section is unlikely to survive that reliably. This must be confirmed or refuted by test T-3, not assumed.

Proposed correction: keep the handle as one separate part (print the 3MF `Handle.stl`, or use a 19 mm tube/dowel), or run a continuous metal or carbon rod through the bar axis.

## C-5 HIGH — tendon routing claim is wrong — [COMPUTED]

- The documented corridor (five routes at X = 194…228, Y = 130, Z = 70–470) is the middle of the arm opening, where the wearer's forearm goes. It is "unobstructed" only because it is the hand cavity. It does not connect to any finger.
- The actual string holes in the fused geometry: four bores, 3.7–3.85 × 3.3–3.4 mm, at X = 114.1, 179.4, 244.6, 308.2, running from the cavity ceiling (Z ≈ 498–500) to the finger-slot floors (Z ≈ 533), Y drifting 144.8 → 136. They lie entirely inside shells 12/13 and none is cut by a seam.
- A **4 mm OD PTFE tube does not fit a 3.4–3.8 mm bore**. The bores also print horizontally in the V4 orientation of shells 12/13, so they will come out smaller.
- No continuous fifth (thumb) bore was found. Thumb routing is unidentified.
- The 3MF contains `Ring_5X.stl` (finger pull rings), consistent with strings running a short distance from the wearer's fingers above the handle to the knuckles, not from the cuff.
- No small bores were found in the printable `Fingers_Base` at the planes sampled; whether its string holes match the fused version is unconfirmed.

Consequence: the `PTFE_FiveChannel_Clamp` parts and the cuff-entry routing do not serve the mechanism as modelled. String travel, friction and re-threading remain untested.

## H-6 HIGH — mass and filament — [SURROGATE SLICE]

0.2 mm layers, 4 walls, 5 top/bottom, 15 % gyroid, 8 mm brim, build-plate-only organic supports, PLA 1.24 g/cm³:

- 13 right shells: **6,183 g** filament, of which 761 g (12 %) is support. Finished shells about 5.4 kg per arm before fingers, electronics and adhesive.
- Both arms: about 12.4 kg.
- Heaviest: R_12 781 g, R_13 760 g, R_05 756 g, R_06 754 g, R_08 659 g.
- Time from this profile totals about 221 h per arm. That figure comes from a generic machine model and is not a Bambu estimate; treat it as an order of magnitude only.

The shells are 20–60 mm thick solids (inherited from the original glove parts), so mass is set by walls and infill. 5 kg carried on one grip is a wearability problem independent of everything else. Fewer walls and 8–10 % infill should be evaluated in Bambu Studio before any full print.

Evidence: `evidence/surrogate_slice.csv`.

## H-7 HIGH — Glove_B1 opening filled — [COMPUTED]

The printable `Glove_B1.stl` (1,674.81 cm³) has a through-opening about 23 mm wide (X 199–222) and 63 mm long (Z 272–335) in the palm-side wall. The version fused into the arm (1,730.06 cm³) is solid there. Its purpose is not determinable from geometry (access or cable opening is likely). It straddles the X=211 seam across shells 05/06 (Z < 310) and 10/11 (Z > 310). `evidence/version_diff_sections.png` (lower row).

## M-8 MEDIUM — seams — [COMPUTED]

Bonded face areas (cm²): Z=145 427; Z=310 251; Z=400 173; X=211 cuff 54, light band 58, wrist 38, knuckles 125; Y=147 36 per side; Y=180 109 per side (05|07, 06|09); X=100 72; X=300 68.

- Faces mate exactly (C-0) and areas are generous, but there is no key, pin or step anywhere. Alignment depends on hand fixturing over faces up to 400 mm across.
- Shell 08 has effectively no bonded face to 05/06 (0.1 cm² at Y=180); it hangs on 07, 09 and the Z faces.
- The X=211 seam crosses the visible centreline: crystal, crystal base, light-strip window, middle top plate, pressure gauge neighbourhood. The original design hides its joints on panel lines.
- The 2.2–2.4 mm flat splines are rigid PLA straps for curved inner walls; their fit is untested.

## M-9 MEDIUM — self-intersecting faces — [COMPUTED]

MeshLab's per-face self-intersection test flags faces in every right shell: 16–261 in most, 3,260 in R_08, 7,190 in R_05, 8,029 in R_06. The original cover also has 1,837. These are inherited from the fused source (overlapping part surfaces), not created by the cuts. PrusaSlicer sliced all parts without geometry errors, but layer previews of 05/06/08 should be checked in Bambu Studio for spurious voids or missing regions. `evidence/selfint.json`.

## M-10 MEDIUM — supports — [SURROGATE SLICE]

Support mass with build-plate-only organic supports: R_08 135 g (20 %), R_05 129 g (17 %), R_06 127 g (17 %), R_12 109 g (14 %), R_13 106 g (14 %), R_10/11 35–38 g, cuff 7–19 g. Seven shells (05, 06, 07, 08, 09, 12, 13) produced "potentially lost branch" warnings, meaning some overhangs could not be reached from the plate. Expect either supports-on-model (scarring) or unsupported regions. Bambu Studio's tree supports will differ in detail.

## LOW

- **L-11** README states a 256 × 256 × 256 mm volume. The X1C is 256 × 256 × 250. No shell is affected (tallest 177.5 mm).
- **L-12** `LED_Tape_Test_Channel_8p6mm/10p6mm` are straight 8.6/10.6 mm channels. Nothing in the gauntlet has that geometry; the ring trough is 27.1 mm wide. They validate nothing.
- **L-13** Left files keep the right arm's side names (`L_01_Cuff_Left_Front` is physically the mirrored side). Label parts when printing.
- **L-14** The 3MF has no `Circle_Top_Plate_Left/Right` (they exist only as loose STLs) and contains two different-sized pairs both named `Under_Plate_Big_A/B`.
- **L-15** Only shells 07 (100 × 165 × 65.9) and 09 (121.6 × 165 × 71.9) fit the A1 Mini, and only with a brim of 7 mm or less (165 + 2×8 = 181 mm). Every other shell needs the X1C.
- **L-16** As stored, left shells sit 3 mm from the bed edge. Re-centre before adding a brim.

## Proposed V5 direction — not started, needs owner approval

1. Rebuild from the 3MF parts, not from `Full_Arm_*`. Union only the structural glove panels (`Glove_A_*`, `Glove_Back_*`, `Glove_B1/B2`) where that removes a seam and still fits the X1C.
2. Keep separate: `Circle_Light`, `Circle_Light_Cover`, `Pressure`, `Pressure_Needle`, `Handle`, `Fingers_Base`, `Gold_Base_Finger`, `Finger_Knot_*`, `Crystal`, `Glove_Light_Strip`, plates and pistons.
3. Keep the `Glove_B1` opening.
4. Add alignment keys or dowel sockets to every merged-panel seam; move seams off the centreline where the X1C envelope allows.
5. Decide electronics pocket and button positions after tests T-1 and T-2.
