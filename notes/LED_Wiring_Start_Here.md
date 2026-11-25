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
| BTF-LIGHTING 5 mm SMD2020 strip, 160 LEDs/m, IP30 | **2 in hand** (1 m each) | 6.25 mm pitch, 5 V, JST-SM 3-pin. Confirmed on strip: red +5V, green data (middle pad), white GND; input end = factory cable with the product tag. **Bare cut pads between every LED** (can cut at any LED; pads short if strip touches itself or metal) |
| JST-SM pigtail, 3 wires | Came with strip | Soldered to board 1 (5V/32/G), checked from photos 2026-11-22 |
| Buttons | In hand | **HUAZIZ LED push button 12 × 12 × 7 mm** (illuminated tact switch, through-hole legs; 13.4 mm over legs, 14.64 mm over tabs). Use two **diagonally opposite** legs for the switch. Built-in LED optional (2 more wires + resistor) |
| Capacitors | In hand (owner, 2026-11-21) | Value not yet recorded |
| 24 AWG silicone wire | Not yet arrived | |
| Solid rosin flux (tin) | In hand (owner photo 2026-11-22) | Use on board joints |
| Heat shrink, Velcro, clear double-sided tape, USB-C cables, cable ties, IPA | In hand (owner, 2026-11-23); power banks 5000/7000 mAh probably in hand | Still to buy: **470 Ω resistors** (+ optional multimeter), see [[electronics/ORDER_LIST]] |

Details: [[electronics/HARDWARE_AS_BOUGHT]].

## Board connections (verified against Adafruit guide and owner photos)
- Large edge pads: **5V, 32, 33, G**. Strip: **red → 5V, green → 32, white → G** (confirm against the strip's printed 5V/DIN/GND).
- Back pads: **14, 27** (buttons, each to **G**), also 25, 26, 3V, G.
- The two white JST-SH sockets are **not** for LEDs: the 4-pin is STEMMA QT I²C, the 3-pin is a GPIO13 input port. Leave them empty.

## WLED gotchas (found 2026-11-22)
- **GPIO 32 locked by AudioReactive** in stock WLED (default mic pins SD 32 / WS 15 / SCK 14, which also blocks button pin 14). Fix per Adafruit's Mini Sparkle Motion guide: Config → Usermods → AudioReactive: type SPH0654, SD 9, WS 10, SCK 23; save; reboot; then set LED GPIO 32. Every freshly flashed board.
- **Uncut strip on the bench:** with WLED length shorter than the strip, pixels past the length lit up on their own (stayed on with WLED off and after a power-cycle; likely boot-time noise; unconfirmed) and sit outside the current limiter. Keep length = physical LEDs (160) and limit with segment 0 instead. Not an issue once the strip is cut.

## Layout per arm: whole strip, 160 LEDs (owner dry-fit 2026-11-22, right arm)
WLED index 0 = first LED after the board's plug (input end). Owner counted from the far end (= WLED 159).
| Zone | WLED index | Count | Owner's far-end count |
|---|---|---|---|
| Lead-in inside the gauntlet (probably hidden) | 0–10 | 11 | 150–160 |
| Ring (gauge), two turns | 11–122 | 112 | 38–149 |
| Turn into the hand channel (hidden; soft twist is fine) | 123–124 | 2 | 36–37 |
| Long shaft, Lens A | 125–136 | 12 | 24–35 |
| Under the top plate (hidden) | 137–138 | 2 | 22–23 |
| Short shaft, Lens B | 139–146 | 8 | 14–21 |
| Under the crystal base front (hidden) | 147–148 | 2 | 12–13 |
| Crystal | 149–159 | 11 | 1–11 |
Proposed WLED segments: lead `[0,11)` off; ring `[11,123)`; hand `[125,149)` (hidden LEDs inside it don't matter, owner); crystal `[149,160)`. Ring split per turn (~56 each) to be confirmed when installed. The older 91-LED layout and the CAD-estimate figure `hand_crystal_layout.png` are superseded by these counts.
- Firmware pins unchanged: data GPIO 32, buttons 14 / 27, WLED limit 1000 mA.

## Strip routing (owner decision 2026-11-22)
- **Hand channel + crystal layout (dry-fit guide):** `electronics/concepts/2026-11-22_controller_placement_option_A/hand_crystal_layout.png`. Strip lies flat, LEDs up; from the ring: LEDs 1–13 under Lens A, 14–16 hidden (top plate), 17–24 Lens B, 25–27 hidden (crystal base front), 28–36 light the crystal; the strip's end lands at the channel end. Twist 90° in the notch slot.
- **One continuous strip per arm** from the ring into the hand channel, no cut between ring and hand (owner's call; physical turn into the notch slot still to be checked on printed R_08).
- **Near end** (owner's term) = strip input end: keeps its **factory JST connector**, which passes out through the ring's exit hole and plugs into the ESP32 pigtail in the cavity. No connector sits inside the trough.
- **Far end**: the far-end factory JST **does not fit** the opening toward the hand channel (owner fit check 2026-11-22), so it is cut off before threading and stays on the offcut; the leading end must be bare. The bare strip passes the round hole. Thread once (or twice, see below) around the trough **outer wall** (LEDs facing inward), through the notch slot into the hand channel, then trim at the crystal end in place. (The earlier "cut at ~100 LEDs" note is superseded by the whole-1-m decision below.)
- LEDs hidden in the slot are set off in WLED; zone counts (ring / gap / hand / crystal) to be recounted after the physical fit.
- ESP32 pigtail soldered by owner 2026-11-22 (red/green/white); pad check against silkscreen done from photos: red 5V, green 32, white G, 33 empty.
- Don't stick the strip down until the bench test passes. Each arm needs its own 1 m reel.
- **Owner decision 2026-11-22 (re-confirmed 21:47): use the WHOLE 1 m strip per arm, do not cut LEDs off; ring wrapped twice**. Only the far-end factory plug/cable is removed (it does not fit the opening). Estimate: ring 2 turns ≈ 112 + slot ≈ 3 + hand 36 ≈ 151 of 160; where the last LEDs land is checked in the dry-fit (two rows on the outer wall; ~110 ring + ~36 hand/crystal ≈ 146 LEDs). Dry-fit on R_08 pending; the 91-LED layout below is superseded once the fit is confirmed and LEDs recounted.

## Next steps (in order)
1. **Bench test board 1: DONE, PASS (2026-11-22).** First light, R/G/B (GRB), rainbow on all 160; 10+ min at 91 LEDs / 1000 mA full white: everything warm, no restarts. Restarts seen earlier were the strip's bare pads shorting when coiled. Details in [[04_Test_Log]]. Still open: heat with the strip enclosed under the cover (do at first in-arm power-up). **Board 2 + strip 2: PASS (owner, 2026-11-22).** Both boards still named `WLED-AP`: rename (Config → WiFi Setup → AP SSID) before powering both at once.
2. Mirror results to GitHub issues #10–#13 (not yet done).
3. **Dry-fit** the double ring wrap on printed R_08; count LEDs per turn → set WLED segments (ring / hand / crystal).
4. **Placement (option A) concept done 2026-11-22:** [[electronics/concepts/2026-11-22_controller_placement_option_A/README]]. Test-print sled (R/L) and cover; hold the sled against printed shell 08 before gluing. Button pod: **v2** (`print/Button_Pod_v2_HUAZIZ_for_18p8_printed_handle` / `..._18p0_beech_rod`) has pockets for the HUAZIZ buttons (island + leg/solder channel + bottom wire exit; glue with Poly Max). **DONE 2026-11-24: 2 pods v2 printed in transparent PLA, clipped onto the 18 mm beech rods, fit fine (owner). Final, no redesign.** Pods have no screws (clip only); screws are for the sled and cover only. **Snip the two plastic locating pegs off the button underside flush before gluing** (they sit on the island edge; owner photos 2026-11-24).
5. Update [[electronics/WIRING]] fully for the Sparkle Motion Mini and option A (wire lengths ~5 / 18 / 20 cm + slack; keep strip pads apart and off metal; insulate the strip end where the far-end plug was removed).
6. Lighting decided 2026-11-22: B1 = on / next look (hold = off), B2 = "Bring It" burst 3–4 s; default all blue; Vi pink only in the burst.
7. **Presets v3 loaded on board 1, accepted (2026-11-22); load the same file on board 2.** `electronics/wled/presets_wled16_whole_strip.json` + `PRESETS_WLED16_README.md` (IDs checked in WLED 16.0.1 source). Load on both boards, set buttons 14/27 and button actions, tune speeds by eye.

## Related
[[electronics/README]] · [[electronics/EFFECTS]] · [[electronics/CODE_AND_WLED_REVIEW]] · [[electronics/LED_STRIP_COMPARISON]] · [[03_Decision_Log]] · [[05_Risks_and_Blockers]]
