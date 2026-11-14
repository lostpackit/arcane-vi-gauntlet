# WLED (preferred) — setup for Claude to validate

The file [presets.json](presets.json) is a **starter example, not an exported tested WLED backup**. Install supported WLED on two ESP32-class controllers, one per gauntlet. Configure 5 V WS2812-compatible RGB output, reference GPIO16, provisional 39 LEDs and ~1500 mA software LED current limit in **Config → LED Preferences**. Configure 2 pushbuttons on reference GPIO25/26; actual GPIOs depend on selected board. Back up settings before preset import.

**Presets**: 1 idle breathe, 2 charge/wipe, 3 chase, 4 surge, 5 sustained flash/strobe, 6 violet sparks. Three proposed segments: [0,21) ring, [21,35) hand, [35,39) crystal. IDs 21–25 are button-action API macros.

**WLED Time & Macros button mapping**:
- A short → 21 (`{"ps":"1~6~"}`); A long → 22 (`{"on":"t"}`).
- B short → 23 (`{"bri":"w~32"}`); B double → 24 (`{"ps":5}`); B long → 25 (`{"ps":6}`).

**Check against installed firmware**: `/json/eff` for effect IDs, `/json/state` for segment fields, and current WLED macro syntax. WLED's **button 0** may have special 5s/10s hold behavior (AP/reset); verify button slot mapping, never hold long enough to trigger it. Import presets through WLED UI or `/edit` after backup. These presets **do not** configure GPIO or button actions automatically.

WLED flash preset 5 remains strobing until mode changes. For one-shot flash-and-resume, test a WLED playlist/usermod or the separate [standalone Arduino reference](../firmware/README.md). Do not claim the WLED JSON reproduces custom choreography exactly until tested behind the diffuser.

Official docs: https://kno.wled.ge/features/presets/ ; https://kno.wled.ge/features/macros/ ; https://kno.wled.ge/interfaces/json-api/

## 144 LEDs/m layout (Claude, 2026-11-14)

[presets_144.json](presets_144.json) is `presets.json` with only the segment bounds remapped for the recommended strip: ring `[0,50)`, hand `[50,84)`, crystal `[84,93)`. Set LED count 93 and the current limit to 1000 mA to start. Effect IDs, speeds and macros are unchanged and equally untested. For a ring-only build, set LED count 50 and delete the hand and crystal segments. Speeds tuned for 21 pixels may look slower on 50 and will need adjusting on the device.
