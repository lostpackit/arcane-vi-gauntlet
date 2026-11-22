# WLED 16 presets: whole strip, both arms (2026-11-22)

File: `presets_wled16_whole_strip.json`. Built by Claude from the owner's right-arm dry-fit (160 LEDs) and owner's style decisions. Effect IDs checked against WLED v16.0.1 source (`wled00/FX.h`). **Not yet loaded on a board.** Replaces `presets.json` / `presets_144.json` (old strip, 91 LEDs).

Segments (WLED index from the board end): lead-in 0–10 off · ring 11–122 · (123–124 dark) · hand 125–148 · crystal 149–159.

| ID | Name | What it does |
|---|---|---|
| 1 | **Hextech Idle** (boot preset, all blue) | ring Breathe cyan/blue · hand Running soft cyan pulses · crystal Heartbeat ice-blue · rare faint Lightning overlay in the hand |
| 2 | **Shimmer** | ring + crystal Glitter (Ocean palette, white glitter) · hand Running |
| 3 | **Overcharged** | ring fast Running + white Glitter overlay · hand constant Lightning · crystal fast Heartbeat white |
| 4 | **Calm** | Pacifica everywhere, brightness 90 (battery saver) |
| 10 | **Bring It** (playlist) | 11 charge 1.2 s → 12 discharge 1.6 s → restores the look that was running (end = 255) |
| 11 | Bring It 1 charge | ring Meteor spinning fast · hand Running fast toward the crystal · crystal dimmed |
| 12 | Bring It 2 discharge | ring Starburst **Vi pink** + cyan + white · hand Lightning · crystal Sparkle Dark (pink, white flashes) |
| 20 | Next look | cycles presets 1 → 4 |
| 21 | Off | off |

Vi pink appears **only** in Bring It (owner).

## Load and set up (per board)
1. WLED → Config → Security & Updates → **Restore presets** → choose the JSON file → upload. (Back up first with "Backup presets" if you want the old ones.)
2. Config → LED Preferences: Length **160**, GPIO **32**, limiter **1000 mA**; **Buttons**: button 0 = GPIO **14**, type Pushbutton; button 1 = GPIO **27**, Pushbutton. Defaults: **Apply preset 1 at boot**, turn LEDs on after power up. Save.
3. Config → Time & Macros → **Button actions**: button 0 push **20**, long press **21**; button 1 push **10**. Save.
4. Never hold button 1 (GPIO 14, WLED button 0) longer than 5 s: WLED opens its setup Wi-Fi at 5 s and **factory-resets at 10 s** (`button.cpp`).
5. If the hand pulses run toward the ring instead of the crystal, tick **Reverse** on that segment and re-save the preset.
