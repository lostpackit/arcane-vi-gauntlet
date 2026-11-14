# Upload original CAD and V1–V4 assets — corrected instructions

**Correction (2026-11-14):** An earlier version of this page referred to `Arcane_Vi_Gauntlet_GitHub_Ready_Repository.zip`. That file was never provided. A single ~945 MB archive could not be reliably delivered, so the CAD import package is now **six separately downloadable ZIPs**, each with paths ready to extract into this existing repository. See the ChatGPT project conversation for the downloads.

## Download all six archives
1. `Arcane_Vi_Gauntlet_Assets_01_Original_3MF.zip` — original Bambu 3MF.
2. `Arcane_Vi_Gauntlet_Assets_02_Original_Arms.zip` — left and right full-arm reference STLs.
3. `Arcane_Vi_Gauntlet_Assets_03_Original_Lights.zip` — circle, covers, plates, crystal and sizing STL.
4. `Arcane_Vi_Gauntlet_Assets_04_V1.zip` — V1 redesign archive.
5. `Arcane_Vi_Gauntlet_Assets_05_V2.zip` — V2 redesign archive.
6. `Arcane_Vi_Gauntlet_Assets_06_V3_V4.zip` — V3 archive and extracted V4 release (including 26 main shells).

Also download `Arcane_Vi_Gauntlet_Assets_SHA256.csv` for file integrity checks. The six ZIPs contain only `originals/` and `releases/` subfolders; **they do not replace** `AGENTS.md`, `HANDOFF.md`, Obsidian notes or other repository documentation.

## Recommended: automated Windows import

From the **existing clone** (not a new Git repository), with Git and Git LFS installed:

```powershell
git clone https://github.com/lostpackit/arcane-vi-gauntlet.git
cd arcane-vi-gauntlet
git lfs install

# Place all six ZIPs and the SHA256 CSV in the same download folder.
.\tools\Import-ViGauntletAssets.ps1 -SourceFolder "$env:USERPROFILE\Downloads"

git status
git add originals releases
git lfs ls-files
git commit -m "Import original CAD references and V1-V4 design assets"
git pull --rebase origin main
git push origin main
```

If you already cloned, **skip `git clone`** and open PowerShell in your existing clone. The import script validates all 61 file hashes against the supplied CSV **before** copying; it refuses to overwrite any different existing files.

If you prefer manual extraction, extract **all six ZIPs directly into the root of the existing clone**, preserving the `originals/` and `releases/` paths. Verify hashes using the CSV or `Get-FileHash -Algorithm SHA256` before pushing.

## Git LFS and synchronization checks
- The GitHub connector cannot transfer binary assets through Git LFS; push from your local machine.
- Confirm `git lfs ls-files` lists all STL, 3MF and ZIP files before committing. Ordinary Git objects above 100 MB are rejected by GitHub.
- Check Git LFS quota/storage/bandwidth before uploading approximately 1.3 GB of uncompressed CAD assets.
- Other agents may push notes and `HANDOFF.md` while you work. Preserve local edits, rebase/pull safely, and **never force-push**.
- After pushing, verify `originals/` and `releases/v4/` exist on GitHub, compare hashes, and update `HANDOFF.md` with the confirmed state.

**V4 is NOT approved for full wearable printing** until the independent CAD, actual Bambu Studio slicer, lighting, tendon and assembly acceptance gates pass. See [release gates](RELEASE_GATES.md) and [agent synchronization](AGENT_SYNC_PROTOCOL.md).
