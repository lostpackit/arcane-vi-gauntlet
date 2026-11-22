---
type: context-pack
tags: [electronics, leds, wled, start-here]
updated: 2026-11-22
---

# LEDs and wiring: start here

Context pack for any agent (or new conversation) working on the gauntlet LEDs. Read [[HANDOFF]] and [[AGENTS]] first, then this note.

## Owner constraints (do not re-litigate)
- USB-C power only. **No USB-A.**
- **No perfboard or breadboard.** Wires solder straight to the board pads.
- Phone control through **WLED**.
- Amazon.de preferred. **Say plainly when a link or page can't be opened.** Never describe a listing that wasn't actually read.
- No shell geometry changes without owner approval.

## Hardware: received vs ordered (2026-11-21)
| Item | Status | Notes |
|---|---|---|
| Adafruit Sparkle Motion Mini (#6160) | **3 in hand** (owner, 2026-11-22) | 31.6 × 19.8 × 7.3 mm, USB-C 5 V 4 A fused. Not WLED-preinstalled: board 1 flashed by owner with stock **WLED 16.0.1**; flash the others via install.wled.me |
| BTF-LIGHTING 5 mm SMD2020 strip, 160 LEDs/m, IP30 | **2 in hand** (1 m each) | 6.25 mm pitch, 5 V, JST-SM 3-pin. Confirmed on strip: red +5V, green data (middle pad), white GND; input end = factory cable with the product tag |
| JST-SM pigtail, 3 wires | Came with strip | Soldered to board 1 (5V/32/G), checked from photos 2026-11-22 |
| Buttons, capacitors | In hand (owner, 2026-11-21) | Part numbers / values not yet recorded |
| 24 AWG silicone wire | Not yet arrived | |
| BTF JST-SM 3-pin pairs (20), heat shrink, USB-C power banks + C-to-C cables, flux | Status not recorded | See [[electronics/ORDER_LIST]] |

Details: [[electronics/HARDWARE_AS_BOUGHT]].

## Board connections (verified against Adafruit guide and owner photos)
- Large edge pads: **5V, 32, 33, G**. Strip: **red → 5V, green → 32, white → G** (confirm against the strip's printed 5V/DIN/GND).
- Back pads: **14, 27** (buttons, each to **G**), also 25, 26, 3V, G.
- The two white JST-SH sockets are **not** for LEDs: the 4-pin is STEMMA QT I²C, the 3-pin is a GPIO13 input port. Leave them empty.

## WLED gotchas (found 2026-11-22)
- **GPIO 32 locked by AudioReactive** in stock WLED (default mic pins SD 32 / WS 15 / SCK 14, which also blocks button pin 14). Fix per Adafruit's Mini Sparkle Motion guide: Config → Usermods → AudioReactive: type SPH0654, SD 9, WS 10, SCK 23; save; reboot; then set LED GPIO 32. Every freshly flashed board.
- **Uncut strip on the bench:** with WLED length shorter than the strip, pixels past the length lit up on their own (stayed on with WLED off and after a power-cycle; likely boot-time noise; unconfirmed) and sit outside the current limiter. Keep length = physical LEDs (160) and limit with segment 0 instead. Not an issue once the strip is cut.

## Layout per arm (91 LEDs)
- Ring: 55 LEDs (index 0–54), 343.8 mm in a 351.2 mm wall.
- Hand: 36 LEDs (55–90), 225 mm in a 232.5 mm channel. Crystal = last 11 (80–90).
- Firmware: `LED_PIN 32`, `MODE_PIN 14`, `ACTION_PIN 27`, `LIMIT_MA 1000` ([[electronics/firmware/README]]). WLED presets: `electronics/wled/presets_144.json` (ring [0,55), hand [55,80), crystal [80,91)).

## Strip routing (owner decision 2026-11-22)
- **One continuous strip per arm** from the ring into the hand channel, no cut between ring and hand (owner's call; physical turn into the notch slot still to be checked on printed R_08).
- **Near end** (owner's term) = strip input end: keeps its **factory JST connector**, which passes out through the ring's exit hole and plugs into the ESP32 pigtail in the cavity. No connector sits inside the trough.
- **Far end**: cut the strip to about 100 LEDs *before* threading (leading end must be bare; the far-end factory connector stays on the ~60-LED spare offcut), run once around the trough **outer wall** (LEDs facing inward), through the notch slot into the hand channel, then trim at the crystal end in place on the copper pads.
- LEDs hidden in the slot are set off in WLED; zone counts (ring / gap / hand / crystal) to be recounted after the physical fit.
- ESP32 pigtail soldered by owner 2026-11-22 (red/green/white); pad check against silkscreen done from photos: red 5V, green 32, white G, 33 empty.
- Don't stick the strip down until the bench test passes. Each arm needs its own 1 m reel.

## Next steps (in order)
1. **Bench test board 1 (2026-11-22): first light, R/G/B (GRB), rainbow PASS on all 160.** Still to record: **heat test** (length 160 + segment 0–91, max 1000 mA, solid white full, USB-C charger; touch-check strip start / board / joints / JST at 5 and 10 min). Details in [[04_Test_Log]].
2. Mirror results to GitHub issues #10–#13 (not yet done).
3. Update [[electronics/WIRING]] fully for the Sparkle Motion Mini (it still reflects older plans).
4. Redesign the electronics sled for the 32 × 20 mm board (current concept is 80 × 45 for the old board); validate button pod with the real switches (#9).
5. Owner decision pending: "breathing all the time, button triggers an effect then returns to breathing" (durations and button mapping).
6. Check WLED effect IDs on the device (IDs 13/15 in the presets may be wrong).

## Related
[[electronics/README]] · [[electronics/EFFECTS]] · [[electronics/CODE_AND_WLED_REVIEW]] · [[electronics/LED_STRIP_COMPARISON]] · [[03_Decision_Log]] · [[05_Risks_and_Blockers]]
