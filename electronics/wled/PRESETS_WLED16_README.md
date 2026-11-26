# WLED 16 presets: whole strip, both arms (2026-11-22; v4 sound looks 2026-11-26)

File: `presets_wled16_whole_strip.json`. Built by Claude from the owner's right-arm dry-fit (160 LEDs) and owner's style decisions. Effect IDs checked against WLED v16.0.1 source (`wled00/FX.h`). Loaded on a board 2026-11-22 (owner video): v1 had the **Overlay flag in the wrong field** (`o1`; WLED 16 uses `o2` = check2 for Lightning/Glitter overlay), so the idle lightning layer blacked out the hand shafts. Fixed in v2 of this file. **v3:** in WLED 16 every segment has its own pixel buffer and the default blend mode "top" replaces the layers below, black included, so layered effects need **blend mode stencil (`bm`: 16, black = see-through)** with the effect's own Overlay off (`FX_fcn.cpp` segblend). Idle lightning: speed 90 → a strike every 0–16 s (avg ~8 s; `mode_lightning`: delay = random(255−speed)×100 ms). Replaces `presets.json` / `presets_144.json` (old strip, 91 LEDs).

Segments (WLED index from the board end): lead-in 0–10 off · ring 11–122 · (123–124 dark) · hand 125–148 · crystal 149–159.

| ID | Name | What it does |
|---|---|---|
| 1 | **Hextech Idle** (boot preset, all blue) | ring Breathe cyan/blue · hand Running soft cyan pulses · crystal Heartbeat ice-blue · rare faint Lightning overlay in the hand |
| 2 | **Shimmer** | ring + crystal Glitter (Ocean palette, white glitter) · hand Running |
| 3 | **Overcharged** | ring fast Running + white Glitter overlay · hand constant Lightning · crystal fast Heartbeat white |
| 4 | **Calm** | Pacifica everywhere, brightness 90 (battery saver) |
| 5 | **Misfit Toys** (sound, v4) | dim blue base everywhere + on top: ring **Gravcenter** (bass shockwave bursting both ways from the ring middle, falling peak dot) · hand **Puddlepeak** ("paint bombs": a splash lands on each beat) · crystal **Pixels** in gold ("firelight" sparks, brighter when louder) |
| 6 | **Playground** (sound, v4) | ring dim **Pacifica** undercurrent + **Plasmoid** haze (Ocean) that only shows where the music is loud · hand **Ripple Peak** (a drop ripples out on each beat) · crystal **Midnoise** (ice-blue glow swelling from the centre with the vocal) |
| 10 | **Bring It** (playlist) | 11 charge 1.2 s → 12 discharge 1.6 s → restores the look that was running (end = 255) |
| 11 | Bring It 1 charge | ring Meteor spinning fast · hand Running fast toward the crystal · crystal dimmed |
| 12 | Bring It 2 discharge | ring Starburst **Vi pink** + cyan + white · hand Lightning · crystal Sparkle Dark (pink, white flashes) |
| 20 | Next look | cycles presets 1 → 6 (v4; was 1 → 4) |
| 21 | Off | off |

Vi pink appears **only** in Bring It (owner).

## Sound looks (v4, 2026-11-26)
The onboard mic (TDK ICS-43434, underside of the board at the USB-C end, sound hole to the label side) works with the AudioReactive settings below (owner clap test with Gravimeter, 2026-11-26). Effect IDs and how each one draws checked in v16.0.1 `FX.cpp` (Gravcenter 156, Puddlepeak 144, Pixels 128, Plasmoid 133, Ripple Peak 148, Midnoise 135; palettes `* Color 1` 2, `* Color Gradient` 4, Ocean 9). Each audio effect is a stencil layer (`bm` 16) over a dim base, so the arm never goes fully dark when it is quiet. In silence the sound layers draw nothing.
- **Misfit Toys** (Pusha T & Mako, Arcane S1): hard-hitting rap over electronic production, written around the "misfit toy" energy of Ekko and the Firelights. Look: punchy and beat-driven.
- **Playground** (Bea Miller, Arcane S1 ep. 1 "Welcome to the Playground"): slinky, smoky invitation into the Undercity. Look: slow haze and drops, swelling glow.
- Colours stay hextech blue / cyan / ice / white; one gold accent (Misfit Toys crystal sparks, matches the gold paint). No pink.
- Needed per board: Config → Usermods → AudioReactive **Enabled**, mic **SPH0654**, SD 9 / WS 10 / SCK 23, **AGC Normal**. Sensitivity per segment: Gravcenter/Plasmoid "Sensitivity"/"# of pixels" slider; Puddlepeak/Ripple Peak react to beat peaks.
- To keep them out of the button cycle: edit preset 20 to `1~4~`.
- Not yet tested on the board (as of 2026-11-26); mic will hear less inside the shell (see cover sound-hole idea).

## Load and set up (per board)
1. WLED → Config → Security & Updates → **Restore presets** → choose the JSON file → upload. (Back up first with "Backup presets" if you want the old ones.)
2. Config → LED Preferences: Length **160**, GPIO **32**, limiter **1000 mA**; **Buttons**: button 0 = GPIO **14**, type Pushbutton; button 1 = GPIO **27**, Pushbutton. Defaults: **Apply preset 1 at boot**, turn LEDs on after power up. Save.
3. Config → Time & Macros → **Button actions**: button 0 push **20**, long press **21**; button 1 push **10**. Save.
4. Never hold button 1 (GPIO 14, WLED button 0) longer than 5 s: WLED opens its setup Wi-Fi at 5 s and **factory-resets at 10 s** (`button.cpp`).
5. If the hand pulses run toward the ring instead of the crystal, tick **Reverse** on that segment and re-save the preset.
