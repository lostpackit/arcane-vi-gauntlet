# V4 printability

Independent audit by Claude, 2026-11-14.

**What this is and is not.** Geometry numbers are computed from the STLs. Filament, support and time numbers come from **PrusaSlicer 2.7.2 with an X1C-like profile** (`audits/claude/scripts/x1c_surrogate.ini`), because Bambu Studio could not be obtained in this environment (download blocked by network policy, HTTP 403). **No Bambu Studio slice was run. Nothing was printed.** The X1C-fit and Toolpaths gates therefore stay UNKNOWN.

## Summary

- All 26 shells are closed, single-body solids and fit the X1C envelope with an 8 mm brim (largest footprint with brim 197 × 241 mm, tallest part 177.5 mm against a 250 mm Z limit).
- Printing them is feasible. Printing them **now is not advisable**: shells 08, 10/11 and 12/13 carry functional defects (ISSUES C-1, C-3, C-4, C-5) and together account for about 3.2 kg of filament per arm.
- Per arm: about 6.2 kg of filament including 0.76 kg of supports, at 4 walls / 15 % gyroid.

## Per-shell table (right arm; left is the exact mirror)

| Shell | Print size X×Y×Z (mm) | With 8 mm brim | Volume cm³ | Orientation (verified) | Filament g | Support g | Fits A1 Mini |
|---|---|---|---|---|---|---|---|
| R_01_Cuff_Left_Front | 209.872 × 147.0 × 70.861 | 225.9x163.0 | 488.996 | Z=145 face down | 202 | 7 | no |
| R_02_Cuff_Left_Rear | 209.974 × 147.017 × 145.0 | 226.0x163.0 | 969.67 | Z=145 face down | 340 | 19 | no |
| R_03_Cuff_Right_Front | 209.402 × 146.999 × 70.861 | 225.4x163.0 | 488.52 | Z=145 face down | 202 | 7 | no |
| R_04_Cuff_Right_Rear | 209.489 × 147.01 × 144.974 | 225.5x163.0 | 968.215 | Z=145 face down | 338 | 17 | no |
| R_05_LightBand_Front_Left | 210.898 × 165.0 × 177.53 | 226.9x181.0 | 1860.842 | Y=180 face down | 756 | 129 | no |
| R_06_LightBand_Front_Right | 210.518 × 165.0 × 177.528 | 226.5x181.0 | 1856.963 | Y=180 face down | 754 | 127 | no |
| R_07_LightBand_Rear_Left | 100.0 × 165.0 × 65.906 | 116.0x181.0 | 446.768 | Y=180 face down, outer skin up | 168 | 9 | yes |
| R_08_LightBand_REAR_RING_CARRIER | 200.0 × 165.0 × 93.505 | 216.0x181.0 | 1171.885 | Y=180 face down, ring face up | 659 | 135 | no |
| R_09_LightBand_Rear_Right | 121.611 × 165.0 × 71.872 | 137.6x181.0 | 602.051 | Y=180 face down, outer skin up | 233 | 25 | yes |
| R_10_Wrist_Upper_Left | 180.972 × 224.917 × 90.0 | 197.0x240.9 | 984.767 | as modelled, Z=310 face down | 494 | 35 | no |
| R_11_Wrist_Upper_Right | 180.588 × 224.928 × 90.0 | 196.6x240.9 | 982.655 | as modelled, Z=310 face down | 496 | 38 | no |
| R_12_Knuckles_Left | 199.754 × 199.038 × 166.222 | 215.8x215.0 | 1591.672 | X=211 face down | 781 | 109 | no |
| R_13_Knuckles_Right | 200.117 × 199.044 × 157.705 | 216.1x215.0 | 1547.556 | X=211 face down | 760 | 106 | no |

Totals for 13 shells: 6,183 g filament, 761 g of it support. Cover: 56 g. Hardware: clamp base 10 g, lid 8 g, spline batches 46 g and 23 g.

Full mesh metrics for all 44 STLs: `GEOMETRY_REPORT.csv`. Slice breakdown: `evidence/surrogate_slice.csv`.

## Checks performed

| Check | Result | Class |
|---|---|---|
| Watertight, consistent winding, single body, no boundary/non-manifold edges (26 shells) | all pass | computed |
| Degenerate (zero-area) faces after vertex merge | 0–55 per shell (R_08 55, R_10 54, R_11 20, R_13 10) | computed |
| Self-intersecting faces (MeshLab) | present in all shells; 05/06/08 have thousands | computed |
| Left = mirror of right | exact | computed |
| Shells reassemble to the source solid | exact, 4 mm² of slivers lost | computed |
| Print orientation and Z=0 seating as stated in README | confirmed for all 13 | computed |
| Envelope vs 256 × 256 × 250 with 8 mm brim | all fit | computed |
| X1C keep-out zones (front-left cutter/purge area), plate type limits | **not checked** — needs Bambu Studio | — |
| Slicing completes without geometry errors | yes, all 13 shells + cover + hardware | surrogate |
| Support demand | 7–135 g per shell | surrogate |
| Unreachable overhangs with build-plate-only supports | warnings on 05, 06, 07, 08, 09, 12, 13 | surrogate |
| Bridging / overhang quality, seam placement, first-layer adhesion | **not assessable without a real slice preview and a print** | — |

## Print risks, in order of filament at stake

1. **R/L_08 (659 g each).** Functionally dead as modelled: sealed LED chamber, fused cover (C-1). In the V4 orientation the chamber ceiling is a 27 mm annular internal bridge over a void that cannot be reached to clear supports. Do not print.
2. **R/L_12, 13 (about 770 g each).** Finger-base revision mismatch (C-3). String bores of 3.4–3.8 mm lie horizontal in this orientation and will close up. 14 % support. Do not print before test T-2.
3. **R/L_05, 06 (about 755 g each).** Tallest parts (177.5 mm) standing on the Y=180 face, which touches the bed only over roughly X < 100 mm; the palm-side arch is carried on about 129 g of supports. Highest self-intersection counts. Affected by H-7. Print only after a Bambu Studio preview and after the seam layout is settled.
4. **R/L_10, 11 (about 495 g each).** Largest footprint (181 × 225 mm; 197 × 241 with brim, about 7.5 mm bed margin). Contain the cut handle halves as 113 mm horizontal cantilevers about 57 mm above the bed (C-4). Do not print before the handle decision.
5. **R/L_01–04 (200–340 g each), 07, 09 (170–230 g).** Lowest risk; cosmetic fusing only. Still worth holding, because a V5 seam layout may move the Z=145 and X=211 planes.

## Settings notes for the eventual Bambu Studio run

- The README's 4 walls / 15 % gyroid gives about 5.4 kg of finished shell per arm. Compare 3 walls / 10 % and 2 walls / 8 % in Bambu Studio for mass before committing.
- Left shells are stored 3 mm from the bed edge; centre them before adding a brim.
- On the A1 Mini, shells 07 and 09 need a brim of 7 mm or less.
- Record per-part filament, time and support from Bambu Studio in `notes/04_Test_Log.md`; those numbers replace the surrogate values here.

## Reproduce

```
python3 -I audits/claude/scripts/geom.py <cad-root> geom_basic.csv        # mesh table
python3 -I audits/claude/scripts/bigstl.py "<Full_Arm_Right...stl>" fullR.npz
python3 -I audits/claude/scripts/reassemble.py                              # shells vs source
python3 -I audits/claude/scripts/selfint.py                                 # MeshLab self-intersections
prusa-slicer --export-gcode --load audits/claude/scripts/x1c_surrogate.ini --center 128,128 --dont-arrange -o out.gcode part.stl
python3 -I audits/claude/scripts/gstat.py out.gcode                         # grams by feature type
```
Scripts use working paths under `out/` and `cad/`; adjust to your checkout.
