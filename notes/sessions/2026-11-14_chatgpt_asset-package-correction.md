---
type: agent-session
date: 2026-11-14
agent: ChatGPT
task: asset-package-correction
status: complete-when-verified
tags: [agents, github, cad, handoff]
---

# Correct missing CAD import archive reference

## User report
The GitHub upload instructions named `Arcane_Vi_Gauntlet_GitHub_Ready_Repository.zip`, but that file had never been provided.

## Actions and evidence
1. Confirmed the missing filename in `docs/UPLOAD_CAD_ASSETS.md`.
2. Located all source STL/3MF files and V1–V4 ZIPs in the project working environment.
3. Attempted to package one ~945 MB archive; delivery failed because the generated archive was too large.
4. Built six smaller ZIP archives, each with ready-to-extract `originals/` and `releases/` paths, plus a 61-file SHA256 manifest.
5. Verified each archive's ZIP CRC and checked that the V4 package includes 13 right and 13 left armor shell STLs.
6. Replaced the nonexistent-file instruction with six-part download guidance and added a PowerShell importer that verifies all hashes before copying and refuses to overwrite conflicting files.
7. Updated `HANDOFF.md` for the next agent and the user. **No CAD binaries have been pushed to GitHub by this action.**

## Blockers
- User must download and push the CAD assets using Git LFS.
- V4 is not independently print-approved.
- GitHub LFS quota/bandwidth may apply.

## Next
User imports six ZIPs using `tools/Import-ViGauntletAssets.ps1`, commits and pushes, then an agent verifies remote asset presence/hashes and begins the independent audit.
