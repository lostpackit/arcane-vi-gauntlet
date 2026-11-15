# WLED (preferred) — setup for Claude to validate

The primary layout is [presets_144.json](presets_144.json) for **83 LEDs per arm** at 144 LEDs/m. [presets.json](presets.json) is the **35-LED fallback** at 60 LEDs/m. Both are starter examples, not exported, tested WLED backups. Install supported WLED on two ESP32-class controllers, one per gauntlet. Configure 5 V WS2812-compatible RGB output, reference GPIO16 and an appropriate software LED current limit in **Config → LED Preferences**. Configure 2 pushbuttons on reference GPIO25/26; actual GPIOs depend on selected board. Back up settings before preset import.

**Fallback segments**: [0,21) ring, [21,31) hand, [31,35) crystal. IDs 21–25 are button-action API macros. See the preset fixes below for current button behavior.

**WLED Time & Macros button mapping**:
- A short → 21; A long → 22.
- B short → 23; B double → 24; B long → 25.

**Check against installed firmware**: `/json/eff` for effect IDs, `/json/state` for segment fields, and current WLED macro syntax. WLED's **button 0** may have special 5s/10s hold behavior (AP/reset); verify button slot mapping, never hold long enough to trigger it. Import presets through WLED UI or `/edit` after backup. These presets **do not** configure GPIO or button actions automatically.

The current one-shot flash playlist returns to idle, not the previously running effect. See the separate [standalone Arduino reference](../firmware/README.md). Do not claim the WLED JSON reproduces custom choreography exactly until tested behind the diffuser.

Official docs: https://kno.wled.ge/features/presets/ ; https://kno.wled.ge/features/macros/ ; https://kno.wled.ge/interfaces/json-api/

## 144 LEDs/m layout (Claude, 2026-11-14)

[presets_144.json](presets_144.json) uses the V5.1 recommended strip: 83 LEDs, ring `[0,50)`, hand `[50,73)`, crystal `[73,83)` (the crystal is lit by the end of the hand strip). Set the current limit to 1000 mA to start. Effect IDs, speeds and macros are untested. For a ring-only build, set LED count 50 and delete the hand and crystal segments. Speeds tuned for 21 pixels may look slower on 50 and will need adjusting on the device.

## Preset fixes (Claude, 2026-11-14) — applied to both preset files, untested on a device

- Button A now cycles presets **1–5** (`"1~5~"`): 1 idle, 2 charging, 3 chase, 4 surge, 5 arcane sparks. The strobe is no longer in the cycle.
- Preset **7** is the strobe at reduced brightness; preset **8** is a playlist that runs it for 0.4 s and then loads preset 1 (idle). Button B double-press calls 8. WLED cannot return to "whatever was running"; the standalone firmware can.
- Button B long-press calls preset 5.
- **Macro mapping to enter in Time & Macros:** A short → 21, A long → 22, B short → 23, B double → 24, B long → 25 (unchanged numbers).
- **Still to do on the device:** effect IDs 13 (chase) and 15 (surge) were not changed because they cannot be confirmed without the installed version's `/json/eff`. Choose a comet/chase-type effect for preset 3 and a fast fade/breathe for preset 4 by name, then re-save those presets.
