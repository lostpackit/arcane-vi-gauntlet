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
- Git LFS: 46 total model/archive objects tracked. Push acknowledged the new V3 object (1/1, 698 KB); a fresh-clone targeted readback returned 698,022 bytes and SHA-256 `99647f63cfc4dabf5b05703b74c5e41d67fa37251cc6009c32a497d519323315`, matching the manifest/pointer. Local `git lfs fsck` passed.

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

**Current upload status (2026-11-14):** All 59 required files pass manifest size/SHA-256 checks; V1/V2 are intentionally excluded. Commit `beb157522fe4571d869ccaea186d5ceaddafaa68` is verified on GitHub `main`; the V3 LFS object was fetched from a fresh cache and its size/SHA-256 match. Issue #1 is eligible for closure after the factual completion summary is posted.

V4 is **NOT approved for full wearable printing**. No asset-upload check substitutes for the independent CAD, Bambu Studio, assembly, lighting, tendon, or physical-fit release gates. See [release gates](RELEASE_GATES.md) and [agent synchronization](AGENT_SYNC_PROTOCOL.md).
