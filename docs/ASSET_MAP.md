# CAD asset map

## Verified inventory (2026-11-14)

The required CAD set contains **59 files / 832,044,520 bytes**: 9 originals, 49 V4 files, and the V3 fit-validation archive. The V3 archive is 698,022 bytes. The separately committed manifest contains 61 rows; the two V1/V2 rows are intentionally excluded from this required set.

### Originals — `originals/` (9 files, 581,242,767 bytes)
- `Vi Gauntlet 3mf Project File.3mf`
- `Full_Arm_Right (No Fingers).stl`
- `Full_Arm_Left (No Fingers).stl`
- `Together For Sizing.stl`
- `Circle_Light.stl`
- `Circle_Light_Cover.stl`
- `Circle_Top_Plate_Left.stl`
- `Circle_Top_Plate_Right.stl`
- `Crystal.stl`

All nine files match their byte counts and SHA-256 values in `Claude_Vi_Gauntlet_Audit_Kit/03_INPUT_MANIFEST_SHA256.csv`. That CSV is a 10-entry audit-input manifest, not the previously referenced 61-entry asset manifest.

### V1/V2

Intentionally excluded by the user. Their absence is not an error for this upload.

### V3 — `releases/v3/Vi_Gauntlet_V3_FitValidation_Printables.zip`

One ZIP, 698,022 bytes, SHA-256 verified against `docs/ASSET_SHA256_MANIFEST.csv`. The ZIP opens and all 21 file entries decompress (1,247,730 uncompressed bytes). It contains ring and cover fit wedges, five-channel PTFE clamp base/lid, socket tolerance pins, geometry validation, design notes, generation/check scripts, hardware, and inspection previews. See `docs/UPLOAD_CAD_ASSETS.md` for the member list summary.

### V4 — `releases/v4/Vi_Gauntlet_X1C_V4_Print_Release/`

49 files, 250,103,731 bytes:
- 13 main shell STL files in `Left_Shells/`
- 13 main shell STL files in `Right_Shells/`
- 2 lighting-cover STL files
- 8 print-hardware/testing STL files
- 3 geometry-validation records
- 4 source scripts, README, and reference images

All 49 extracted V4 files match their byte counts and SHA-256 values in `docs/ASSET_SHA256_MANIFEST.csv`.

## Integrity and transfer status

- Required manifest entries: **PASS, 59/59** exact file sizes and SHA-256 (9 originals + 49 V4 + 1 V3 archive); V1/V2 excluded by request.
- V3 archive: **PASS**; `tar.exe -tf` succeeded and all 21 file entries were opened and decompressed.
- Git LFS: **46/46** assets tracked (44 STL, one 3MF, one V3 ZIP). The push acknowledged 1/1 new object; a fresh-clone targeted readback of the V3 ZIP passed at 698,022 bytes with matching SHA-256.
- Remote `main` and expected V3/manifest paths: **VERIFIED** at commit `beb157522fe4571d869ccaea186d5ceaddafaa68`.

V4 remains a digital candidate, not print-approved. See [release gates](RELEASE_GATES.md).
