# V4 independent audit — final verdict

Independent audit by Claude, 2026-11-14, on commit `2bf6e6d`.

## Verdict: NO-GO for printing the V4 shell set

V4 is a geometrically clean, printable cut of the wrong source. It was cut from the fused display solid (`Full_Arm_* (No Fingers).stl`) instead of the functional 3MF parts. As a result the LED chamber is sealed, the diffuser seat is solid, the load-bearing handle is cut in half, and the finger mount is a different revision from the printable finger base. Printing the full set would consume about 6.2 kg of filament per arm (surrogate slice) and yield a gauntlet that cannot be lit and may not accept the fingers.

**GO** for the four small test prints below. They cost a few hundred grams and settle the open questions.

## Basis of evidence

| Class | Used for |
|---|---|
| Computed from CAD (this audit) | all geometry, fidelity, LED chamber, string bores, seam areas |
| Surrogate slice (PrusaSlicer 2.7.2, X1C-like profile) | filament, supports, slicing completes |
| Bambu Studio slice | **not run** (could not be obtained here) |
| Physical print / fit / load test | **none** |

## Release gates

| Gate | Status | Evidence / reason |
|---|---|---|
| Source fidelity | **FAIL** | V4 ↔ fused arm is exact (ISSUES C-0). Fused arm ↔ 3MF functional design is not: parts fused (C-2), `Fingers_Base` and `Glove_B1` are different revisions (C-3, H-7). |
| Source licensing | UNKNOWN | 3MF carries no licence or designer metadata. Not resolvable from files. |
| Mesh integrity | PASS (computed), with caveat | 26/26 watertight, single body, consistent winding, zero boundary/non-manifold edges, volumes match. Caveat: self-intersecting faces in every shell (M-9). |
| X1C fit | UNKNOWN | Envelope with 8 mm brim fits (computed). Bambu Studio keep-outs not checked. |
| Toolpaths | UNKNOWN | Surrogate slice only. Supports 7–135 g per shell; unsupported-branch warnings on 7 shells (M-10). |
| Seams | UNKNOWN | Mating faces are exact (computed). No keys; alignability and spline fit unproven (M-8). |
| Strength | UNKNOWN | No physical test. Handle butt joint is predicted to be inadequate (C-4, estimate). |
| Finger mounting | **FAIL** | Mount geometry in shells 12/13 is not the printable `Fingers_Base` (C-3). Actual finger fit untested. |
| Tendons | **FAIL** | Documented five-route corridor is the arm opening, not a tendon path. Four 3.4–3.8 mm bores found; no thumb route identified; 4 mm PTFE does not fit (C-5). Travel untested. |
| Lighting | **FAIL** | Shell 08 chamber sealed, cover seat solid (C-1). Original ring part measures 27.1 × 13.3 mm trough; 8/10 mm strip fit supported by CAD, pending T-1. |
| Electronics | BLOCKED | No hardware selected; no mounting geometry exists. Plan in `ELECTRONICS_FIT.md`. |
| Wearability | UNKNOWN | About 5.4 kg of shell per arm on one grip is a concern (H-6). No fit test. |
| End-to-end | BLOCKED | Depends on all of the above. |

## What would waste the most filament if printed now

| Part (each arm) | Filament | Why it would be wasted |
|---|---|---|
| 08 ring carrier | 659 g | cannot take LEDs or the cover |
| 12 + 13 knuckles | 1,541 g | finger mount revision, string bores |
| 10 + 11 wrist | 990 g | handle cut at the seam |
| 05 + 06 light band front | 1,510 g | filled `Glove_B1` opening; seam layout likely to change |

The README's print order starts with shell 08, then 12/13. Those are exactly the parts that should not be printed.

## Minimal physical test plan

Ordered by value per gram. A1 Mini where it fits, to keep the X1C free.

| # | Print | Printer | What it settles | Pass criteria |
|---|---|---|---|---|
| **T-1** | Original `Circle_Light.stl` (lay flat, trough up) + `Circle_Light_Cover.stl`, exactly as supplied, at 100 %. Cover in the intended diffuser filament. | A1 Mini (Ø130 fits 180) | Lighting gate: real trough size, cover fit, strip fit, diffusion | Trough ≥ 26.5 mm wide and ≥ 12.8 mm deep as printed; a sample 10 mm (or 8 mm) bare strip seats on the outer wall with wires out through the notch; cover seats fully and can be removed by hand; no hot spots through the cover at working brightness |
| **T-2** | One finger: its base parts from the 3MF as you are already printing them, plus the 3MF `Fingers_Base.stl` printed once as designed (278 × 95 × 78; X1C). Optional: a knuckle-slot coupon cut from R_13 (forefinger slot, about 70 × 115 × 105 mm) to compare. The coupon is a derived test file and needs your OK before I generate it. | X1C (base), A1 Mini (finger parts, coupon) | Finger mounting and tendon gates | Finger base seats and hinges on the 3MF `Fingers_Base` without filing; a 0.8–1.5 mm cord passes the string bore and returns freely; full curl and release by pulling the cord with the finger ring; note pull force and travel. Then repeat on the V4 coupon and record the differences |
| **T-3** | Handle decision coupon: two Ø18.8 × 50 mm stubs butt-bonded with the intended epoxy, versus one solid Ø18.8 × 100 mm bar, both printed in the orientation they would have in the shell | A1 Mini | Strength gate for the grip | Bonded bar carries at least 3× the finished gauntlet weight at mid-span on a 100 mm support span without cracking. If it does not, the handle must be one piece or rod-reinforced |
| **T-4** | Seam coupon: two 60 × 40 × 25 mm blocks at shell settings, butt-bonded; one pair plain, one pair with a short spline | A1 Mini | Seams / strength gates | Joint survives a firm hand bend; failure, if forced, occurs in the print and not at the glue line; note whether the spline sits flat |

Not recommended as tests: the `LED_Tape_Test_Channel` coupons (no matching feature) and the PTFE clamp (not on the real tendon path).

Before any of this is released for full printing, slice the candidate parts in Bambu Studio with the real X1C profile and record supports, time and filament per part.

## Decisions needed from the owner

1. Approve or reject the V5 direction: rebuild from the 3MF functional parts, merging only structural glove panels (details in `ISSUES.md`, last section). No CAD has been changed.
2. Approve generating the T-2 knuckle-slot coupon STL (derived file under a new `releases/tests/` path; originals untouched).
3. Handle approach after T-3: one-piece printed handle, tube/dowel, or through-rod.
4. Confirm the intended tendon layout (finger rings to knuckle bores, thumb included or not).

## Limits of this audit

- No Bambu Studio, no printer, no hardware. Slicer numbers are from a different slicer with a generic machine model; times especially are indicative only.
- 3MF finger parts could not be placed in assembled coordinates, so finger-to-slot clearance was not computed.
- Thumb mount and thumb tendon path were not resolved.
- V3 archive contents were not audited. V1/V2 were excluded by the owner.
- Left arm was verified as an exact mirror and not analysed separately beyond that.
- Minimum wall thickness and min-feature analysis were not run; the shells are thick solids and this was judged low priority against the functional defects.
