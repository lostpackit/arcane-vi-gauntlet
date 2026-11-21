# 2026-11-20 Claude — A1 Mini translucent parts + left-insert normals fix

- Owner set up A1 Mini with translucent glow-in-the-dark blue PETG for LED covers; asked which parts to print.
- Translucent set (all fit 180 mm bed): R/L Ring_Light_Cover (118.3 x 118.4 x 8.8 mm), R/L Crystal (65.1 x 37.2 x 5.6), R/L Hand_Lens_A (81.4 x 13.3 x 1.6), R/L Hand_Lens_B (46.4 x 13.3 x 1.6).
- FINDING: all five Left inserts (Ring cover, Crystal, Lens A, Lens B, Pressure Gauge) have inverted face winding (signed volume negative) — mirror without winding flip. Right inserts and Left shells are positive.
- FIX: faces inverted only (no vertex change); volumes now equal Right counterparts, extents match. Delivered as /home/claude/out/L_Inserts_Normals_Fix.zip (LFS upload blocked) + releases/v5/.../L_INSERTS_NORMALS_FIX_SHA256.txt. Owner/Copilot to replace Inserts/L_*.3mf.
- Note given: glow filament is abrasive; Bambu lists PLA Glow under hardened-steel nozzle only for A1 mini. Print one ring cover first and check light transmission with the strip.
- No physical or slicer test performed by Claude.

## 2026-11-21
- Owner switched cover material: glow-blue PETG failed (wet: stringing/popping). Using GiantArm transparent PLA (190–220 °C); tests at 205 °C frosted / 220 °C clearer on Lens B.
- Dowels: wooden 6×30 (printed peg = fallback). Handle: printed PLA/PETG or 18 mm beech rod (NOT 20 mm; sockets 19.3). Glue: UHU Plus Schnellfest epoxy (dowels/seams), UHU Poly Max clear (covers/electronics), no CA near clear parts.
- L vs R translucent inserts are mirror images and not identical (best rigid fit deviation: lens A ≤0.16 mm, crystal ≤0.30, ring cover ≤0.49) → print L files for left.
- Lens bottom tilted 0.02–0.05 mm (inherited); within first layer, prints fine. Offered to flatten if wanted.
- Generated parts inventory with renders: releases/v5/Vi_Gauntlet_X1C_V5_Draft/Inventory/V5_Parts_Inventory.md (+39 PNG renders); scripts Build_Scripts/inventory_*.py. Uses print-pack files (08 = V5_2) and fixed L inserts.
