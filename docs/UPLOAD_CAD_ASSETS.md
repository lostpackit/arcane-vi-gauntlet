# CAD asset upload and verification

## Current local state (2026-11-14)

Assets are already present and organized in this existing clone. **Do not download, extract, or run the importer again.**

- `originals/`: 9 files (one 3MF and eight STLs), 581,242,767 bytes. All 9 match the available `Claude_Vi_Gauntlet_Audit_Kit/03_INPUT_MANIFEST_SHA256.csv` by size and SHA-256.
- `releases/v4/Vi_Gauntlet_X1C_V4_Print_Release/`: 49 files, 250,103,731 bytes, including 13 main shell STLs per arm.
- V1 and V2: intentionally excluded.
- V3 fit-validation assets: not found; the missing V3 set prevents full completion.
- The requested 61-entry `Arcane_Vi_Gauntlet_Assets_SHA256.csv` is unavailable. The audit-kit CSV also references an absent V4 ZIP and does not hash the extracted V4 files.
- Combined existing originals and V4 payload: 58 files, 831,346,498 bytes. Remote commit and LFS object availability are pending until a successful push and verification.

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

Confirm all 44 STL files and the 3MF (45 LFS files total) are listed by Git LFS. The three original files larger than 100 MB must be LFS pointers, not ordinary Git blobs. Do not stage the separate `Claude_Vi_Gauntlet_Audit_Kit/` unless it is intentionally part of a separately reviewed change.

Before pushing, fetch and preserve any concurrent changes. Never force-push or discard local work:

```powershell
git fetch origin
git status --short --branch
# If origin/main advanced, reconcile safely without discarding staged assets or other agents' changes.
git commit -m "Upload original CAD and V4 release assets"
git push origin main
```

After a successful push, verify the remote commit, browse expected files on GitHub, confirm LFS pointers in the commit and confirm remote LFS objects can be fetched/read. If authentication, quota, or permissions block this, report the exact failure and leave the issue open.

V4 is **NOT approved for full wearable printing**. No asset-upload check substitutes for the independent CAD, Bambu Studio, assembly, lighting, tendon, or physical-fit release gates. See [release gates](RELEASE_GATES.md) and [agent synchronization](AGENT_SYNC_PROTOCOL.md).
