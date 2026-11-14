# Claude review request — electronics package and V5 integration

1. Read all files under `electronics/`, current `HANDOFF.md`, `audits/results/ELECTRONICS_FIT.md` and V5 README.
2. **Mechanical**: reconcile ring trough, removable cover, crystal and 238 mm hand strip with V5. Find controller/bank/button pockets, accessible wiring, and paths clear of handle, dowels, fingers and all tendon/string routes. No CAD edits without owner approval.
3. **BOM**: verify real product datasheets/widths, bare 8/10 mm ring strip vs ~2.7 mm accent, controller board selection (ESP32-WROOM-32 or XIAO ESP32-S3), button dimensions, 5 V bank rating and shifter pinout. Mark each APPROVE/CHANGE/BLOCKED; no purchase assumed.
4. **Electrical**: calculate worst-case current, wire voltage drop, fuse and connector ratings; verify actual board 5 V/USB power path, ground, /OE, level shift, capacitor, bank auto-off and skin/thermal safety.
5. **WLED**: validate `wled/presets.json` against target version and `/json/eff`, macro/button mapping, segment bounds, sustained flash behavior, optional two-arm sync and 1500 mA software current limit. Bench-test before calling it verified.
6. **Arduino alternative**: compile `firmware/src/main.cpp` using PlatformIO; review 2-button debounce/long/double, flash-resume and six effect visuals, current limitations and millis rollover. This is NOT WLED.
7. **Tests**: recommend smallest LED strip sample, T-1 cover test, 3–5 pixel breadboard, measured current/temperature, glove button ergonomics and final in-gauntlet wiring test.
8. Update Obsidian session log, `HANDOFF.md`, engineering gate evidence and proposed V5 CAD requirements. **Keep lighting/electronics BLOCKED** until real hardware fit, current and function are tested. Preserve V5 and originals.
