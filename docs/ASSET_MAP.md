# CAD asset map

## Local inventory (2026-11-14)

The following files are present in the working tree and the remote commit. GitHub `main` and local `HEAD` match at `91f7233aceca2251a1f136ffff24f0524421176c`; GitHub directory listings confirm the originals and both V4 shell directories.

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

### V3

No V3 fit-validation assets were found in the repository. `releases/v3/` is absent. This remains a blocker for completing the asset upload and closing GitHub Issue #1.

### V4 — `releases/v4/Vi_Gauntlet_X1C_V4_Print_Release/`

49 files, 250,103,731 bytes:
- 13 main shell STL files in `Left_Shells/`
- 13 main shell STL files in `Right_Shells/`
- 2 lighting-cover STL files
- 8 print-hardware/testing STL files
- 3 geometry-validation records
- 4 source scripts, README, and reference images

The available CSV refers to an absent `Vi_Gauntlet_X1C_V4_Print_Release.zip`; it does not provide hashes for the extracted V4 files. V4 SHA-256 verification is therefore incomplete.

## Integrity and transfer status

- Original assets: **PASS, 9/9 hashes and byte counts** against the available audit-kit manifest.
- V3 assets: **MISSING**.
- V4 extracted-file hashes: **NOT VERIFIED**; no applicable hashes are available.
- Git LFS: version 3.7.1 installed/configured; all 45 STL/3MF assets are LFS-tracked. The push reported **45/45 LFS objects uploaded (828 MB)**; local `git lfs fsck` passed. GitHub API shows pointer blobs (132–134 bytes), as expected. Direct remote binary readback was not attempted because the instruction prohibits downloading.
- Remote main ref and expected directories: **VERIFIED**. Remote object upload acknowledged; independent retrieval remains untested.

V4 remains a digital candidate, not print-approved. See [release gates](RELEASE_GATES.md).
