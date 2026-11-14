# CAD asset upload and verification

## Verified asset state (2026-11-14)

Assets are already present and organized in this existing clone. **Do not download, extract, or run the importer again.**

- `originals/`: 9 files (one 3MF and eight STLs), 581,242,767 bytes; all 9 match `docs/ASSET_SHA256_MANIFEST.csv` by byte size and SHA-256.
- `releases/v4/Vi_Gauntlet_X1C_V4_Print_Release/`: 49 files, 250,103,731 bytes, including 13 main shell STLs per arm.
- `releases/v3/Vi_Gauntlet_V3_FitValidation_Printables.zip`: 698,022 bytes.
- V1 and V2: intentionally excluded.
- V3 archive has 21 readable fit-validation/support entries; the V3 ZIP size and SHA-256 match the manifest.
- `docs/ASSET_SHA256_MANIFEST.csv` contains 61 rows; the 59 required entries (9 originals, 49 V4, 1 V3 ZIP) pass exact size/SHA-256 checks. The two V1/V2 rows are intentionally excluded.
- Combined required CAD payload: 59 files, 832,044,520 bytes. The separately included manifest is 9,281 bytes.
- Prior checkpoint: 45 original/V4 LFS objects were acknowledged as uploaded and passed local `git lfs fsck`. The newly added V3 ZIP requires its own push and targeted remote readback.

See [asset map](ASSET_MAP.md) for per-file structure and verified scope.

## Git LFS, stage, commit, and push

From the existing repository clone:

```powershell
git lfs version
git lfs install --local
git check-attr filter -- "originals/Vi Gauntlet 3mf Project File.3mf" "originals/Full_Arm_Left (No Fingers).stl"
git add originals releases/v4
git lfs ls-files
git status --short
```

Confirm all 44 STL files, the 3MF, and the V3 ZIP (46 LFS files total) are listed by Git LFS. The V3 ZIP must resolve to `filter=lfs`. Do not stage the separate `Claude_Vi_Gauntlet_Audit_Kit/` unless it is intentionally part of a separately reviewed change.

Before pushing, fetch and preserve any concurrent changes. Never force-push or discard local work:

```powershell
git fetch origin
git status --short --branch
# If origin/main advanced, reconcile safely without discarding staged assets or other agents' changes.
git commit -m "Upload original CAD and V4 release assets"
git push origin main
```

Prior-checkpoint note: The preceding 45-object upload and directory visibility were verified, but a direct LFS readback was not performed then. This note is superseded for the current task; the V3 object must be pushed and read back.

**Current upload status (2026-11-14):** The older remote-readback paragraph above reflects a prior checkpoint and is superseded. The local manifest validates all 59 required files, including extracted V4 and the V3 ZIP; V1/V2 are intentionally excluded. The V3 object has not yet been pushed or remotely read back. Issue #1 must remain open until that LFS object and the final commit are remotely verified.

V4 is **NOT approved for full wearable printing**. No asset-upload check substitutes for the independent CAD, Bambu Studio, assembly, lighting, tendon, or physical-fit release gates. See [release gates](RELEASE_GATES.md) and [agent synchronization](AGENT_SYNC_PROTOCOL.md).
