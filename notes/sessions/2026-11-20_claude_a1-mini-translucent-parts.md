# 2026-11-20 Claude — A1 Mini translucent parts + left-insert normals fix

- Owner set up A1 Mini with translucent glow-in-the-dark blue PETG for LED covers; asked which parts to print.
- Translucent set (all fit 180 mm bed): R/L Ring_Light_Cover (118.3 x 118.4 x 8.8 mm), R/L Crystal (65.1 x 37.2 x 5.6), R/L Hand_Lens_A (81.4 x 13.3 x 1.6), R/L Hand_Lens_B (46.4 x 13.3 x 1.6).
- FINDING: all five Left inserts (Ring cover, Crystal, Lens A, Lens B, Pressure Gauge) have inverted face winding (signed volume negative) — mirror without winding flip. Right inserts and Left shells are positive.
- FIX: faces inverted only (no vertex change); volumes now equal Right counterparts, extents match. Delivered as /home/claude/out/L_Inserts_Normals_Fix.zip (LFS upload blocked) + releases/v5/.../L_INSERTS_NORMALS_FIX_SHA256.txt. Owner/Copilot to replace Inserts/L_*.3mf.
- Note given: glow filament is abrasive; Bambu lists PLA Glow under hardened-steel nozzle only for A1 mini. Print one ring cover first and check light transmission with the strip.
- No physical or slicer test performed by Claude.
