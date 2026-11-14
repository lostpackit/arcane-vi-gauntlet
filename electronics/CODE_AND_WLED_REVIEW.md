# Lighting code, WLED and hardware review (Claude, 2026-11-14)

**Review by reading only.** Nothing was compiled, flashed, imported into WLED or wired. Items marked "verify" depend on the installed toolchain or WLED version.

## Standalone firmware (`firmware/src/main.cpp`)

Logic is sound overall: non-blocking loop, debounce, short/long/double press, and unsigned `millis()` arithmetic that survives rollover. Issues, most important first:

| # | Severity | Finding | Fix |
|---|---|---|---|
| F1 | High (likely build failure) | `Button a{MODE_PIN}` brace-initialises a struct that has default member initialisers. That only compiles as C++14 or later. PlatformIO's stock `espressif32` Arduino core has historically built as gnu++11. Verify by compiling. | Add a constructor `Button(int p):pin(p){}`, or set `build_unflags = -std=gnu++11` and `build_flags = -std=gnu++17` in `platformio.ini`. |
| F2 | High with 93 px | No current limit. Flash at the top brightness step drives all pixels near half-white: roughly 2.4 A with 93 pixels, close to the 3 A fuse (about 1.0 A with 39). | Lower `BRIGHT[]` for the 93-pixel layout, or cap flash intensity; measure with a meter. WLED's limiter does this properly. |
| F3 | Medium | Pixel counts and timings are tuned for 21/14/4. With ring 50 the chase takes about 3.3 s per turn instead of 1.4 s and the 5-pixel tail shrinks from 86° to 36°. | If the 144/m strip is used: `RING=50, HAND=34, CRYSTAL=9`, scale the step time (about 27 ms) and tail length (about 12 px). |
| F4 | Low | `sinf(t*0.0028f)` loses float precision after several hours of one effect, giving a slightly uneven breath. | Use `t % period` before converting to float. |
| F5 | Low | Pin map is for an ESP32-WROOM DevKit (16/25/26). A XIAO board has none of those pins. | Change the three constants to match the board bought. |
| F6 | Info | Mode cycling correctly skips FLASH; flash returns to the previous effect after 350 ms. | — |

## WLED presets (`wled/presets.json`, `wled/presets_144.json`)

| # | Severity | Finding | Fix |
|---|---|---|---|
| W1 | High | Button A cycles `"1~6~"`, which includes preset 5, the **sustained strobe**. The design says flash is only on B double-press. | Renumber so the cycle excludes the strobe: e.g. sparks → 5, flash → 7, cycle `"1~5~"`, B double → 7. |
| W2 | High (safety) | A sustained full-ring strobe is a photosensitivity risk in a crowd and is the highest-current preset. | Make it a short burst (see W3) and keep its brightness low. |
| W3 | Medium | One-shot flash-and-resume: WLED can do "flash, then go to a fixed preset" with a playlist, but not "return to whatever was running". | Playlist: strobe for about 0.4 s, end preset = idle breathing. If exact resume matters, use the standalone firmware. |
| W4 | Medium (verify) | "Energy chase" uses effect 13 and "Power surge" uses 15. From memory of the WLED effect list, 13 is Theater (marching dots) and 15 is Running, neither of which is a single rotating highlight with a trail or a burst-and-decay. | On the device open `/json/eff` and pick by name: a chase/comet/meteor-type effect for the chase, a fade/breathe variant at high speed for the surge. Do not trust IDs from this file. |
| W5 | Low (verify) | `"bri":"w~32"` (wrap-around brightness step) and `"on":"t"` look valid for current WLED; confirm on the installed version. | — |
| W6 | Info | Presets do not set LED count, pins, colour order or the current limit. Those are in Config → LED Preferences. Use 93 LEDs, 1000 mA, WS281x, GRB (confirm). | — |
| W7 | Info | Holding WLED button 0 for more than 5 s opens the setup access point. | Put on/off on a long press of about 1 s and avoid long holds, or use button slots 1 and 2. |

## Hardware and wiring (`WIRING.md`, `BOM.md`)

The scheme is electrically conventional and I found no error in it: fused 5 V bank, common ground, 74AHCT125 with /OE low, 330–470 Ω at the first pixel, 1000 µF across the LED rail, zones fed in parallel, buttons to ground with pull-ups.

Points to settle on the bench:
- **Do not power the board from USB and the bank at once** unless the board's schematic shows a diode between USB 5 V and the 5 V pin.
- A USB-A port on a small power bank is often limited to about 2.4 A; with the 1000 mA limit that is fine.
- Tie the unused 74AHCT125 inputs to ground.
- The chain is ring → hand → crystal; the lead between zones can be 20–30 cm. If the far zones flicker, feed their data from a second shifter gate.
- Board choice, button pod and mounts are still open (see `REVIEW_CHECKLIST.md`).

## Recommendation

Use **WLED** for the build: it has the current limiter, live tuning from a phone and no compile step. Fix W1–W3 in the preset file when the device is on the bench, and choose effects by name (W4). Keep the standalone sketch as a fallback, after F1–F3.
