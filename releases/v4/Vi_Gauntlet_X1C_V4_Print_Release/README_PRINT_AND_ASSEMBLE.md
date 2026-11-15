> **SUPERSEDED — independent audit NO-GO (2026-11-14). Do not print. Use releases/v5/.** See the [audit verdict](../../../audits/results/FINAL_VERDICT.md).

# VI GAUNTLET — V4 X1C RING-SAFE PRINT RELEASE

**This is the consolidated full-size structural shell print release, not the previous V2 prototype cuts.**

**Model:** 13 main armor pieces per arm (26 total) plus the native circular-light covers and optional printed reinforcement/string accessories. **Fingers:** deliberately **NOT modified**; continue the original finger parts you are already printing from the supplied Bambu 3MF. **Scale:** 100% throughout. **Printer:** Bambu X1 Carbon, 0.4mm nozzle, 256×256×256mm.

## What was actually fixed

- Redesigned the splits to keep the **entire existing circular-light base** intact in a SINGLE module (shell 08). The original ring source bounds, after assembly translation, are at least 10.8 mm away from every new cut plane; it is NOT separately duplicated as a mandatory print.
- Moved the wrist seam to source **Z=400mm**, eliminating the large floating islands from the previous Z=380 cut. Removed only a few tiny detached fragments created by clipping in the mid-front sections.
- Closed small clipping defects, fixed degenerate triangles, checked each of the 26 saved STLs for **positive volume, watertightness, consistent winding, a single solid, and X1C fit**. Both R/L variants pass.
- Preserved the original large STL geometry essentially exactly: summed volume of right 13 print sections differs from the right original source by less than **0.00001%** (this is a mass-properties comparison, not a functional test).
- Provided separate original/mirrored **Circle_Light_Cover** STLs; the original printed diffuser design remains separate and should be installed after LEDs. A source ring itself need not be printed again because it is part of shell 08.
- Preserved a digitally checked internal passage near the middle axis for **five 4mm OD PTFE conduits**. Sampled cut seams do not cap over this corridor. Additional two-piece PTFE clamps are supplied as optional guides.
- Added printable epoxy-keyed **internal reinforcement splines** in 65mm and 38mm sizes, with pre-arranged 18-piece batch STLs. These are *bonded* supports, not screw-in mechanical locks.

## Recommended X1C settings (starting point)

- Layer: **0.20mm**, nozzle 0.4mm, PLA (or PETG if you are comfortable tuning adhesion and bridging). **Four wall loops**, **12–15% gyroid infill**, **5 top and 5 bottom layers**.
- Import one STL at a time or group in Bambu Studio. Each STL has been **rotated for its print orientation and put at bed-level Z=0**. Re-center each object on the bed with Arrange/Center; **do not scale**.
- Use a **6–8mm brim** on large thin-walled sections. The widest shell footprint is less than 225mm, leaving room for a centered 8mm brim within the nominal bed. Check the X1C printer-specific keep-out regions.
- Preview each layer in Bambu Studio before printing. Add **tree supports (build plate only wherever possible)** for visible undersides and cantilevered decorative features; keep support material out of tube corridors, LED channels, and finger joints. Choose seam on hidden inner edge.
- Since a local Bambu Studio slicer executable was not available, **toolpath support validation and print durations are not claimed**. Digital mesh integrity and XYZ envelope validation ARE complete.

## What to print — in order

1. **Shell R_08 and/or L_08**: central circular-light rear carrier. This is a FULL FINAL shell, not a test coupon. It contains the original uncut ring geometry. Print the corresponding one separate circular-light cover and dry-fit the lens. Do not glue the lens permanently.
2. **Shell 12 and 13 on each hand**: upper hand and knuckle frame. Dry-fit the original finger-base pieces already being printed. They have not been reshaped; all geometry above source Z=400mm preserves its original contours.
3. **Shells 10/11**: upper wrist transition; then **5/6/7/9** surrounding the circular-light module 08; finally **1–4** at the cuff. Dry-assemble and tape sections before bonding.
4. **Conduit hardware**: optional two-piece 5-channel PTFE clamp + lid, seam splines as needed. Each long/short spline model can be multiplied in Bambu Studio or the batch STL used. Light-width gauges are for strip selection, not assembled parts.

## Source-coordinate join plan (mirrors apply on the left)

- Cuff: **01–04**, source Z=0–145mm, split X=211mm / Y=147mm.
- Light band: **05–09**, Z=145–310mm. Front is split X=211mm with rear split X=100/300mm, which preserves ring center section **08** (source X=100–300, Y=180–300).
- Wrist transition: **10–11**, Z=310–400mm, split X=211mm.
- Knuckle/hand housing: **12–13**, Z=400–600mm, split X=211mm.

Joint faces are planar but **not keyed with built-in bolted bosses**. Roughen mating interiors, use appropriate two-part epoxy, and bridge accessible seams on the inside with the provided **perforated splines**. Let adhesive key through the perforations. Use narrow splines on curved surfaces; do not force rigid PLA splines against tight curves or place them where they obstruct finger-string motion, ventilation, or optics. A bonded joint is permanent; choose and dry-fit any removable electronics/battery arrangement before closing large seams. Wearable strength depends on print and adhesive quality; test a representative joined seam under expected load.

## Finger-string routing and electronics

- Preserve original printed finger mechanisms. Run five **4mm OD PTFE** tubes *inside the hollow armor*, not through decorative skin or joint faces. Reference world positions in original assembled model are near **X = 194, 202.5, 211, 219.5, 228; Y=130; Z=70–470mm**. At Z=145,310,400 and X=211 the examined clipping faces left the central corridor open.
- These XYZ values are **reference assembly coordinates**, NOT print-bed coordinates. The printed section STL transformations vary. Assemble sections first; pass a temporary cord or flexible tubing through the corridor and check for snagging before bonding the final seam.
- Use the separate PTFE clamp models where they fit, anchoring the *tube ends* securely in the glove mechanism and at the accessible cuff. The source data do not define individual finger knot/tendon anchor measurements, so **end fittings and actual dynamic movement need to be tested**; DO NOT bond the entire shell shut before testing full travel.
- Wire the programmable LED strip into the source ring groove and use the ORIGINAL REMOVABLE light cover. The original cover is a separate print. Measure the actual selected LED strip width, bend radius, wires and diffuser closure first. The released shell does **not** include a controller-specific pocket, finished switch holes, or a verified 10mm strip fit. Leave a wire service loop and place the controller/battery at the reachable cuff opening on a removable mount until a specific ESP32 and LED product are purchased.

## What is and is not validated

**DONE:** 26 STL print bodies have been programmatically verified after export for 100%-scale dimensional envelope, one closed volume each, manifold edges, proper face winding. The original integrated ring base is fully inside module 08. Mirrored left geometry matches the original source's mirrored handedness (global coordinate translations differ).

**NOT POSSIBLE TO VERIFY VIRTUALLY:** exact fit of already printed finger parts; actual lighting cover snap tolerance and strip bend; mechanical strength of epoxy seams; physical finger-string pull test; actual sliced support/toolpath for your printer; final ESP32/buttons/battery integration. These require the hardware, Bambu Studio, and at least one printed fit check.

**Files:** `Right_Shells/`, `Left_Shells/`, `Lighting_Covers/`, `Print_Hardware/`, `Reference/`, `Geometry_Validation/` and `Source_Scripts/`. Original split 3MF finger objects are not duplicated; use your existing project for those.
