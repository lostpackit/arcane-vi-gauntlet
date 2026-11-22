---
type: concept
date: 2026-11-22
status: concept for owner review (not print-approved, nothing printed)
tags: [electronics, sled, button-pod, wiring]
---

# Controller placement, option A (owner decision 2026-11-22)

Concept renders computed from `originals/Full_Arm_Right (No Fingers).stl` (assembled coordinates, mm) and Adafruit's own 3D model of the Sparkle Motion Mini (github.com/adafruit/Adafruit_CAD_Parts, "6160 Sparkle Motion Mini"). **No shell geometry was changed.** Left arm = mirror.

| File | Shows |
|---|---|
| `view_inside.png` | Right arm, near half cut away: sled + board, pod, bank, wire routes |
| `view_close.png` | Close-up from below at the ring |
| `placement_side.png` | Lengthwise section with assumed forearm/fist and clearance |
| `placement_cross.png` | Cross-section at the sled |
| `parts.png` | Sled (exploded with board and screws) and button pod |

## Numbers (computed)
- **Exit hole** from the LED ring trough into the arm: about 16 × 12 mm opening at Z 255–271, X 205–217, running up ~20 mm to the trough floor (Y ≈ 250).
- **Bore ceiling** under the ring is a ridge: Y 230.8 on the centreline, ~222 at ±10 mm, ~211 at ±40 mm (rays from the bore).
- **Sled**: 36 (along arm) × 26 mm, top face generated from the actual ceiling (glue face, UHU Poly Max), flat underside at Y 218.1 (≥ 2 mm material everywhere), 4 posts Ø5.8 × 4.5 mm on the board's M2.5 hole pattern (Adafruit .brd: holes at 2.54/2.54, 27.94/2.667, 2.54/17.145, 27.94/17.08 mm; board 30.48 × 19.75 mm), 2.2 mm pilots for M2.5 self-tapping screws, cable-tie bar at the pad end. ~6.9 cm³. Overlap with the shell: 0 mm³. Entirely on shell 08.
- **Board**: module side up (toward the sled), labels/USB-C facing down, USB-C end toward the cuff, pad end 9 mm short of the exit hole. Lowest point Y 208.6.
- **Button pod**: rebuild of `Mounts_CONCEPT` pod (C-clip on the Ø18.8 handle, two 12 × 12 mm tact pockets), shown at X 262–288 next to the fist, pad facing down/back. Overlap with the shell: 0 mm³. Final spot and angle set by the owner's thumb.
- **Power bank**: example 100 × 65 × 15 mm on the cuff side wall (X 92.5–107.5, Z 45–145); not chosen yet.
- **Wire routes** kept ≥ 3 mm off the shell: LED lead ~5 cm, USB-C ~18 cm, button wires ~20 cm (add slack).

## Assumptions (not measured)
- Forearm envelope: ellipse 100 × 84 mm at the cuff opening tapering to 66 × 48 mm at Z 330, centred X 211, Y 140→150; fist box X 165–258, Y 112–200, Z 330–425 around the handle. With this, the board hangs **≈ 32 mm** above the forearm. Even resting on the bore floor (Y ≈ 56), a forearm would need to be over ~14 cm thick to reach the board.
- Thumb position on the handle is not known; the pod is adjustable by design.
- Renders use the original fused arm; V5 differences in this area (opened trough, hand slot) do not touch the bore ceiling.

## Update 2026-11-22 15:45 CET: sled v3 + vented cover
Owner asked for a cover over the board (vented) and has M2 × 8 screws. Sled v3: posts Ø5 with 1.7 mm pilots (screws from the board side), two outer posts for the cover, sled 34 mm wide, flat underside Y 215.8, PCB bottom Y 211.6, cover bottom Y 203.6. Overlaps with shell, board and each other: 0. Images: `sled_v3_exploded.png`, `sled_v3_inside.png`, `print/print_orient.png`.
