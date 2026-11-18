# CLAUDE INDEPENDENT AUDIT — QUICK START

## Status in one sentence
V4's 26 shell STLs passed the previous assistant's **saved-mesh and nominal envelope checks**, but the combined wearable is NOT yet certified for all full-scale prints: slicer previews, real finger routing/anchors, LED channel/cover fit, long-term seam strength, and electronic integration need independent verification.

## Recommended approach: Claude Code with local files (best for STL/3MF)

1. Make a **ViGauntlet_Audit** folder on your Windows PC.
2. Place the following **original files, unchanged**, in its `input` folder:
   - `Vi_Gauntlet_X1C_V4_Print_Release.zip` (candidate)
   - `Vi Gauntlet 3mf Project File.3mf` (original multi-part reference)
   - `Full_Arm_Right (No Fingers).stl` and `Full_Arm_Left (No Fingers).stl` (source full-arm reference)
   - `Circle_Light.stl`, `Circle_Light_Cover.stl`, `Circle_Top_Plate_Left.stl`, `Circle_Top_Plate_Right.stl`, `Crystal.stl`
   - `Together For Sizing.stl` (optional reference)
3. Extract this small **Claude_Vi_Gauntlet_Audit_Kit.zip** into the top-level `ViGauntlet_Audit` folder.
4. Open `ViGauntlet_Audit` in VS Code with **Claude Code** (or another Claude environment that can execute geometry scripts on local files and access slicer outputs).
5. Paste the complete text in `01_CLAUDE_MASTER_PROMPT.md` into Claude Code. Ask it to use `input/`, create all results under `audit_output/`, and *not* alter originals.
6. Have Claude produce a **NO-GO / CONDITIONAL GO / GO** report with actual measurements and saved audit files. If it can't run a slicer, YOU can use Bambu Studio on the X1C profile and send back screenshots/estimated print times so Claude can audit those results.

Example Windows PowerShell commands from the working folder:

```powershell
New-Item -ItemType Directory -Force -Path .\input, .\audit_output | Out-Null
Expand-Archive -Path '.\input\Vi_Gauntlet_X1C_V4_Print_Release.zip' -DestinationPath '.\audit_output\v4_extracted' -Force
# Do not unpack the 3MF and assume it is one STL: it is a ZIP/XML assembly with transformations.
```

## Alternate: Claude.ai chat (less reliable for native CAD)

Anthropic lists PDF, standard documents, and images among its native supported upload formats; **STL, 3MF and ZIP aren't listed as standard document formats**. Although Claude.ai chat may accept large attachments, that does **not** guarantee it can parse CAD meshes or do a full CAD review. You can attach `01_CLAUDE_MASTER_PROMPT.md`, the preview image, CSV/JSON reports, and try the V4 / 3MF files. Require Claude to first demonstrate that it genuinely extracted the mesh and read the 3MF geometry, otherwise use Claude Code locally. Do **not** accept an audit based only on the preview, README or validation JSON.

## File package contents
- `01_CLAUDE_MASTER_PROMPT.md`: self-contained independent review assignment.
- `02_ACCEPTANCE_GATES.csv`: explicit criteria and existing evidence status.
- `03_INPUT_MANIFEST_SHA256.csv`: checksums of original artifacts for tamper/accidental mismatch checks.
- `04_CLAUDE_REPORT_TEMPLATE.md`: structured report to request.
- `Existing_Validation/` and `Existing_Build_Scripts/`: prior V4 records; **not** independent validation.
- `Reference/V4_Shell_Layout.png`: visualization only; not proof of fit.

The large V4 ZIP, original 3MF and source STLs are supplied **separately**, not duplicated in this small kit. You need the actual files for meaningful verification.

## Stop/go standard
Don't start all the large shells just because Bambu Studio shows green placement or because a mesh is closed. Demand an exact cover mating test, successful finger/string routing, realistic sliced parts and a viable assembly/maintenance plan. You may print **targeted validation coupons** while the full build is on HOLD.
