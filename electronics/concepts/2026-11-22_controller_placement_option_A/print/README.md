# Print files (concept, 2026-11-22)

> **The five .3mf files are not in the repo yet.** They are Git LFS files and Claude's session cannot upload LFS (proxy blocks the LFS storage host). They were delivered to Erich in the chat on 2026-11-22; to add them, upload them with LFS from a normal checkout (or have Copilot do it) into this `print/` folder. They can also be regenerated from `../scripts/` (pod_export.py, build_v3.py + export_sled.py) with the original arm STL and Adafruit's 6160 model.

## Button pod: fit-test print

Status: **test print for the clip fit only.** The button pockets (12.5 × 12.5 × 4.2 mm, from the Mounts_CONCEPT pod) are not yet checked against the owner's actual buttons; they will be updated once the button type is known.

| File | Handle | Clip bore | Snap opening |
|---|---|---|---|
| `Button_Pod_for_18p8_printed_handle.3mf` | printed handle Ø18.8 | 19.3 mm | 15.0 mm |
| `Button_Pod_for_18p0_beech_rod.3mf` | beech rod Ø18 | 18.5 mm | 14.4 mm |

Snaps onto the handle after assembly (no need to fit it before shells 10/11 are joined). Already oriented: clip upright, flat on the bed.

## Filament and Bambu Studio settings (recommendation, not sliced by Claude)
- **PETG** (standard). It flexes open over the rod without cracking. Not LW-PLA. PLA works for a first fit test but may crack after repeated snapping.
- 0.4 mm nozzle, 0.16–0.20 mm layers, **4 wall loops**, 4 top / 4 bottom layers, 30 % gyroid infill.
- **Supports off** (the button windows bridge 12.5 mm; the wire slots open onto the bed). Brim off, or 3 mm if PETG corners lift.
- Keep the orientation in the file: the C-ring is printed as stacked rings, so it flexes along its layers rather than across them.
- About 8 cm³ (~10 g PETG).

## Sled (v3) and vented board cover

Owner has **M2 × 8 screws** (plus nuts). Design uses the screws only:
- **Board**: 4 × M2 × 8 go up through the board's corner holes (head on the label side) and **thread straight into 1.7 mm pilot holes in the posts**. Unscrew 4 screws and the board comes off; the sled stays glued.
- **Cover**: 2 × M2 × 8 from below through the cover tabs into the two outer posts. Floor and side walls are slotted for air; both ends open for USB-C and the wires.
- **Why not nuts on the board:** an M2 nut is 4.6 mm across corners, wider than the 4.0 mm clear ring around each mounting hole, and would sit within ~0.2 mm of the 5V, GND and 3.3V pads next to the holes (Adafruit board file). Screw heads (3.8 mm) stay inside the clear ring. Keep the nuts as a fix if a thread ever strips.

| File | Notes |
|---|---|
| `Sled_Right_Arm_M2_CONCEPT.3mf` | Glue face shaped to the right arm's ceiling under the ring (computed from the original arm). 34 × 26 × 36 mm, ~10.6 cm³ |
| `Sled_Left_Arm_M2_CONCEPT.3mf` | Exact mirror for the left arm |
| `Board_Cover_vented_both_arms_CONCEPT.3mf` | Symmetric, fits either arm. 35 × 30 × 11 mm, ~1.7 cm³ |

Print settings (recommendation, not sliced by Claude):
- **Sled**: standard **PETG or PLA** (not LW-PLA: the screws thread into it). Printed standing on its end as in the file, so the glue face is a clean side wall. 0.2 mm layers, **4 walls** (posts come out solid), 25 % infill, brim 5 mm. Supports off; if the horizontal posts droop, switch on tree supports (build plate only).
- **Cover**: PLA or PETG, flat as in the file, 0.2 mm, 3 walls, supports off.
- **Before gluing**: hold the sled up against the printed shell 08 under the ring, board end toward the cuff. The glue face should sit flush on the ridge; sand lightly if a print artefact holds it off. Glue with UHU Poly Max.
- Clearance (computed): cover bottom ~28 mm above an average forearm (assumed size).


## Button pod v2 for the owner's buttons (2026-11-22, Claude print/vault session)
Owner's buttons: **HUAZIZ LED push button 12 × 12 × 7 mm** (illuminated tact switch, through-hole legs). Owner caliper: 13.4 mm across the legs, 14.64 mm across the white side tabs.
- `Button_Pod_v2_HUAZIZ_for_18p8_printed_handle.3mf` / `Button_Pod_v2_HUAZIZ_for_18p0_beech_rod.3mf` (script `../scripts/pod_export_v2.py`; 3MFs LFS-pending, delivered in chat).
- Pocket 15.2 × 13.8 × 4.5 mm (body), 2.6 mm channel round a 7.6 mm centre island, 5 mm deep, for the legs and solder joints; wire exit to the pod's bottom end. Clip unchanged. Pad 10.7 mm thick (v1: 7.2), pod 32 × 33 × 26 mm, ~9 cm³.
- Assembly: solder wires to the switch legs (and the LED legs if the button lights are wanted), route out the bottom slot, dab of UHU Poly Max on the island, press the button in.
- Not printed or fitted. Black-body height not measured (pocket assumes ≈4.5 mm; if taller, the button simply stands further proud).
