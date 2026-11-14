# Asset inventory

Independent audit by Claude, 2026-11-14. Repo commit audited: `2bf6e6d`.

## How the assets were obtained

`git lfs pull` failed in this session (`batch response: Resource not accessible by integration`). All 46 LFS objects were instead downloaded from the GitHub media endpoint and each file's SHA-256 was compared with the `oid` in its committed LFS pointer: **46/46 match**. Script: `audits/claude/scripts/fetch_lfs.sh`. The 13 non-LFS files of the 59-file set (validation JSON/CSV, scripts, README, PNGs) are plain Git blobs and were not separately re-hashed against `docs/ASSET_SHA256_MANIFEST.csv`.

All geometry is in **millimetres** (3MF declares `unit="millimeter"`; STL dimensions are consistent with it).

## Originals (`originals/`)

| File | Bytes (pointer) | SHA-256 (verified) | What it is |
|---|---|---|---|
| `Circle_Light.stl` | 2,484,184 | `c9496fd2ae995d1a…` | LED ring base, Ø130, open annular trough. |
| `Circle_Light_Cover.stl` | 3,106,684 | `b602b01a4c7a966e…` | Diffuser cover, Ø118.4. |
| `Circle_Top_Plate_Left.stl` | 12,759,584 | `2d82a054592aafb1…` | Decorative plate; **not present in the 3MF**. |
| `Circle_Top_Plate_Right.stl` | 12,759,784 | `6b06daa07167118a…` | Decorative plate; **not present in the 3MF**. |
| `Crystal.stl` | 1,310,584 | `b9c69d469bf709d6…` | Crystal insert. |
| `Full_Arm_Left (No Fingers).stl` | 112,726,184 | `8520f35b220a542c…` | Exact X-mirror of the right arm. |
| `Full_Arm_Right (No Fingers).stl` | 112,726,184 | `d2f0477e84abfe2c…` | One fused watertight solid, 2,254,522 triangles, 421.6 × 294.0 × 600.1 mm, 13,960.56 cm³. **Source of V4.** |
| `Together For Sizing.stl` | 130,518,084 | `e394c8f7925efe41…` | Assembled reference incl. fingers, 181 components, 475.6 × 294.1 × 872.5 mm. Parts are separate bodies; used to locate parts in assembled coordinates. |
| `Vi Gauntlet 3mf Project File.3mf` | 192,851,495 | `07f60e694fd7db84…` | Bambu Studio 2.2.1 project: 76 build items on 36 plates, print layout (not assembled). The functional design. |

## 3MF contents (parsed independently)

- 76 build items, each one mesh component; item transforms are plate placements (rotation + translation). Meshes are stored centred on their own bounding box but in assembled orientation.
- No licence, designer name or title metadata is filled in (`License`, `Designer`, `Title` empty; a numeric `DesignerUserId` is present). No process/filament settings file is embedded. All objects are assigned extruder 1.
- Per-object table with volume, size, plate and transform: `evidence/3mf_objects.json`.

| Group | Objects |
|---|---|
| Glove structure (10) | Glove_A_Left1 (917.56 cm³), Glove_A_Left2 (1626.19 cm³), Glove_A_Right1 (977.08 cm³), Glove_A_Right2 (1642.46 cm³), Glove_Back_LeftA (994.85 cm³), Glove_Back_LeftB (650.16 cm³), Glove_Back_RightA (1036.53 cm³), Glove_Back_RightB (646.12 cm³), Glove_B1 (1674.81 cm³), Glove_B2 (663.09 cm³) |
| Lighting | Circle_Light (119.15 cm³), Circle_Light_Cover (45.32 cm³), Glove_Light_Strip (3.61 cm³), Crystal (5.87 cm³), Crystal_Base (48.93 cm³), Under_Crystal (7.07 cm³), Pressure (110.22 cm³), Pressure_Needle (0.51 cm³) |
| Grip and tendon hardware | Handle (61.78 cm³), Ring_5X (1.96 cm³) |
| Finger carrier | Fingers_Base (340.02 cm³), Gold_Base_Finger (71.73 cm³), Finger_Knot_Fore (56.63 cm³), Finger_Knot_Middle (56.22 cm³), Finger_Knot_Ring (56.22 cm³), Finger_Knot_Little (56.5 cm³) |
| Plates / pistons / details | Under_Plate_Big_A (263.98 cm³), Under_Plate_Big_A (257.42 cm³), Under_Plate_Big_B (274.84 cm³), Under_Plate_Big_B (264.28 cm³), Under_Plate_Small (234.68 cm³), Middle_Top_Plate (132.24 cm³), Small_Top_Plate_Left (38.35 cm³), Small_Top_Plate_Right (38.38 cm³), Piston_Left (235.53 cm³), Piston_Right (215.35 cm³), Piston_Right_Detail (33.45 cm³), HandPalm_Detail_1 (80.37 cm³), HandPalm_Detail_2 (49.98 cm³) |
| Fingers and thumb (37 objects) | ForeFinger_Detail (4.6), Forefinger (288.88), Forefinger_Base_A (22.6), Forefinger_Base_B (15.2), Forefinger_Middle_A (17.8), Forefinger_Middle_B_V2 (13.58), Forefinger_Piece (19.15), Forefinger_Tip (35.27), LittleFinger_Detail (4.71), Little_Finger (274.95), Little_Finger_Piece (18.02), Little_Finger_Tip (38.62), Littlefinger_Base_A (21.09), Littlefinger_Base_B (14.26), Littlefinger_Middle_A (16.33), Littlefinger_Middle_B_V2 (12.61), MiddleFinger_Detail (4.48), Middle_Finger (305.13), Middle_Finger_Piece (18.81), Middle_Finger_Tip (48.01), Middlefinger_Base_A (23.04), Middlefinger_Base_B (15.13), Middlefinger_Middle_A (18.34), Middlefinger_Middle_B_V2 (13.83), RingFinger_Detail (4.5), Ring_Finger (305.64), Ring_Finger_Piece (18.68), Ring_Finger_Tip (45.32), Ringfinger_Base_A (23.05), Ringfinger_Base_B (15.32), Ringfinger_Middle_A (18.48), Ringfinger_Middle_B_V2 (13.17), Thumb (178.47), Thumb_Base (113.66), Thumb_Middle_A (36.26), Thumb_Middle_B (23.82), Thumb_Tip (48.43) |

Glove structure total: 10,828.85 cm³. The fused arm is 13,960.56 cm³; the difference is the plates, pistons, lighting parts, handle and finger carrier that were unioned in.

Notes:
- `Under_Plate_Big_A/B` appear twice with different geometry (263.98/274.84 cm³ and 257.42/264.28 cm³).
- `Fingers_Base` (340.02 cm³) and `Glove_B1` (1,674.81 cm³) differ from the versions inside the sizing model and fused arm (360.37 and 1,730.06 cm³). See ISSUES C-3 and H-7.
- `*_Middle_B_V2` finger parts indicate the 3MF is a later revision than the sizing/full-arm STLs.

## Releases

- **V1, V2:** intentionally excluded by the owner; not audited.
- **V3** `releases/v3/Vi_Gauntlet_V3_FitValidation_Printables.zip`: pointer hash verified (698,022 bytes). Contents were **not** audited in this session.
- **V4** `releases/v4/Vi_Gauntlet_X1C_V4_Print_Release/`: 13 right + 13 left shells, 2 covers, 8 hardware/test STLs (all LFS, hashes verified), 3 validation records, 4 scripts, README, 5 PNGs. Per-file metrics in `GEOMETRY_REPORT.csv`.

## Prior validation records checked

| Claim (V4 README / JSON) | Independent result |
|---|---|
| 26 shells watertight, single body, consistent winding | Confirmed |
| Print sizes in `Print_Size_Check.csv` | Confirmed to 0.01 mm |
| Right shell volume sum equals source within 0.00001 % | Confirmed (13,960.56 vs 13,960.56 cm³) |
| Left = mirrored right | Confirmed exact |
| Ring base at least 10.8 mm from every cut plane | Consistent with measured ring extents; not the relevant question (see C-1) |
| "Original printed diffuser remains separate and should be installed after LEDs" | **False for the shell as built**: cover volume is 99.7 % solid in shell 08 |
| "Preserved internal passage for five 4 mm PTFE conduits" | **Misleading**: the passage is the arm opening; real string bores are 3.4–3.8 mm and elsewhere |
| Fingers "have not been reshaped" | Finger parts untouched, but the mount they attach to is a different revision from the printable one |

