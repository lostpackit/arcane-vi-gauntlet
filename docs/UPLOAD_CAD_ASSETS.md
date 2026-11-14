# Upload the original models and V1–V4 releases

The GitHub connector can publish documentation but is not a Git LFS transfer client. The large STL, 3MF and ZIP assets must be pushed from a machine with Git LFS installed.

## Recommended: full staged archive
Download `Arcane_Vi_Gauntlet_GitHub_Ready_Repository.zip` from the ChatGPT project conversation and extract it. This is the complete staged directory containing CAD assets and release files. **Use the GitHub repository as the destination**, not a new repository.

In Windows PowerShell (Git and Git LFS required):
```powershell
git clone https://github.com/lostpackit/arcane-vi-gauntlet.git
cd arcane-vi-gauntlet
git lfs install
# Copy only originals/ and releases/ from the extracted staged directory
# into this cloned repository, preserving the directory structure.
git add originals releases
git lfs ls-files
git commit -m "Import original CAD references and V1-V4 design assets"
git push origin main
```

Before committing, ensure `git lfs ls-files` lists the large STL/3MF/ZIP files. GitHub rejects ordinary Git objects above 100 MB. Git LFS has separate storage/bandwidth limits; check account quota before upload.

If using the smaller scaffold and split archives instead, follow `docs/QUICK_START.md` in the downloadable scaffold to stage and hash-check the assets.

## Post-upload checks
1. Browse `originals/` and `releases/v4/` on GitHub.
2. Confirm CAD files are LFS pointers in Git history, with downloadable LFS objects.
3. Compare file sizes and SHA-256 values against the supplied asset manifest.
4. Do not call V4 production-ready until independent acceptance gates pass.
