---
type: context-pack
tags: [electronics, leds, wled, start-here]
updated: 2026-11-21
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
| Adafruit Sparkle Motion Mini (#6160) | 1 received, 2nd pending from seller | ESP32-MINI-1, USB-C, WLED preinstalled |
| BTF-LIGHTING 5 mm SMD2020 strip, 160 LEDs/m, IP30 | Received | 6.25 mm pitch, 5 V, JST-SM 3-pin (red +5 V, green data, white GND) |
| JST-SM pigtail with bare ends | 1 came with strip | Enough for the bench test |
| BTF JST-SM 3-pin pairs (20) | Ordering | Second arm + spares |
| 12 × 12 mm tactile buttons + caps, 24 AWG silicone wire, heat shrink, USB-C power banks + short C-to-C cables, 1000 µF cap (optional), flux | Ordering | See [[electronics/ORDER_LIST]] |

Details: [[electronics/HARDWARE_AS_BOUGHT]].

## Board connections (verified against Adafruit guide and owner photos)
- Large edge pads: **5V, 32, 33, G**. Strip: **red → 5V, green → 32, white → G** (confirm against the strip's printed 5V/DIN/GND).
- Back pads: **14, 27** (buttons, each to **G**), also 25, 26, 3V, G.
- The two white JST-SH sockets are **not** for LEDs: the 4-pin is STEMMA QT I²C, the 3-pin is a GPIO13 input port. Leave them empty.

## Layout per arm (91 LEDs)
- Ring: 55 LEDs (index 0–54), 343.8 mm in a 351.2 mm wall.
- Hand: 36 LEDs (55–90), 225 mm in a 232.5 mm channel. Crystal = last 11 (80–90).
- Firmware: `LED_PIN 32`, `MODE_PIN 14`, `ACTION_PIN 27`, `LIMIT_MA 1000` ([[electronics/firmware/README]]). WLED presets: `electronics/wled/presets_144.json` (ring [0,55), hand [55,80), crystal [80,91)).

## Strip routing (owner decision 2026-11-22)
- **One continuous strip per arm** from the ring into the hand channel, no cut between ring and hand (owner's call; physical turn into the notch slot still to be checked on printed R_08).
- **Near end** (owner's term) = strip input end: keeps its **factory JST connector**, which passes out through the ring's exit hole and plugs into the ESP32 pigtail in the cavity. No connector sits inside the trough.
- **Far end**: cut the strip to about 100 LEDs *before* threading (leading end must be bare; the far-end factory connector stays on the ~60-LED spare offcut), run once around the trough **outer wall** (LEDs facing inward), through the notch slot into the hand channel, then trim at the crystal end in place on the copper pads.
- LEDs hidden in the slot are set off in WLED; zone counts (ring / gap / hand / crystal) to be recounted after the physical fit.
- ESP32 pigtail soldered by owner 2026-11-22 (red/green/white); pad check against silkscreen (5V / 32 / G) pending.
- Don't stick the strip down until the bench test passes. Each arm needs its own 1 m reel.

## Next steps (in order)
1. **Bench test** one board + strip: solder pigtail to 5V/32/G, USB-C power, join `WLED-AP`, open `4.3.2.1`. Config → LED Preferences: GPIO 32, WS281x, 160 LEDs, max current 500 mA, GRB. Test solid red, then rainbow. Run 10 min full white and check heat by touch (covers are PLA, softens around 55–60 °C).
2. Record result in [[04_Test_Log]], [[HANDOFF]] and GitHub issues #10–#13.
3. Update [[electronics/WIRING]] fully for the Sparkle Motion Mini (it still reflects older plans).
4. Redesign the electronics sled for the 32 × 20 mm board (current concept is 80 × 45 for the old board); validate button pod with the real switches (#9).
5. Owner decision pending: "breathing all the time, button triggers an effect then returns to breathing" (durations and button mapping).
6. Check WLED effect IDs on the device (IDs 13/15 in the presets may be wrong).

## Related
[[electronics/README]] · [[electronics/EFFECTS]] · [[electronics/CODE_AND_WLED_REVIEW]] · [[electronics/LED_STRIP_COMPARISON]] · [[03_Decision_Log]] · [[05_Risks_and_Blockers]]
