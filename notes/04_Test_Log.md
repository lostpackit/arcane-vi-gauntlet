---
type: validation-log
tags: [testing, validation]
---

# Validation and print test log

**No independently verified physical build, complete Bambu Studio slice, finger-string test or LED fit test has been recorded in this repository.** Do not convert earlier digital claims into PASS without rerunning checks.

For each test, add a separate note from [[templates/Validation_Template]] or append a row here with date, part, printer/material/profile, method, observed evidence, PASS/FAIL/UNKNOWN/BLOCKED, and the associated commit.

| Date | Test | Status | Evidence |
|---|---|---|---|
| 2026-11-14 | Required asset size/SHA-256 verification | PASS (59/59) | [[docs/ASSET_MAP]]; `docs/ASSET_SHA256_MANIFEST.csv`; 9 originals + 49 V4 + 1 V3 ZIP; V1/V2 excluded |
| 2026-11-14 | V3 archive structure/content | PASS | `tar.exe -tf` listed 21 file entries; every entry opened/decompressed, 1,247,730 bytes total |
| 2026-11-14 | Remote commit and asset visibility | PASS | `origin/main` equals `dced43625bce1d00b3e94133496f9cfdac463682`; GitHub lists the V5 model paths |
| 2026-11-14 | Git LFS configuration and inventory | PASS | 79 assets tracked (44 STL, 34 3MF, 1 ZIP); push reported 33/33 new V5 objects uploaded |
| 2026-11-14 | Targeted remote V3 LFS readback | PASS | Fresh shallow clone fetched only the V3 ZIP; 698,022 bytes and SHA-256 `99647f63cfc4dabf5b05703b74c5e41d67fa37251cc6009c32a497d519323315` matched |
| 2026-11-14 | V4 independent release audit (Claude; CAD analysis + surrogate slice, no physical test) | DONE — verdict NO-GO | `audits/results/FINAL_VERDICT.md`, `audits/results/ISSUES.md` |
| 2026-11-14 | LFS asset re-verification by Claude (46 objects vs pointer SHA-256) | PASS (46/46) | `audits/results/INVENTORY.md` |
| 2026-11-14 | 26 shells: watertight / single body / mirror / reassembly to source | PASS (computed) | `audits/results/GEOMETRY_REPORT.csv`, `audits/results/evidence/reassembly_report.json` |
| 2026-11-14 | Shell 08 LED chamber and cover seat | FAIL (computed): chamber sealed, cover volume 99.7 % solid | `audits/results/evidence/led_ring_profile_ringframe.png` |
| 2026-11-14 | Finger base revision, fused arm vs printable 3MF | FAIL (computed): 25 % of surface > 1 mm apart | `audits/results/evidence/version_diff_sections.png` |
| 2026-11-14 | Surrogate slice, PrusaSlicer 2.7.2 X1C-like profile (NOT Bambu Studio) | INFO: 6,183 g per arm incl. 761 g support | `audits/results/evidence/surrogate_slice.csv` |
| 2026-11-14 | Full X1C slicer check | NOT RUN | [[docs/RELEASE_GATES]] |
| 2026-11-14 | V5 draft: 33 files closed-solid / mirror / open trough / cap lift-out / handle sockets / dowel sockets | PASS (computed) | `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_Verification.json` |
| 2026-11-14 | V5 draft surrogate slice, lightweight settings (PrusaSlicer, NOT Bambu Studio) | INFO: 3,843 g per arm incl. 760 g support, standard PLA | `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_Surrogate_Slice_Light_Settings.csv` |
| 2026-11-14 | LED strip comparison for V5 ring (CAD + manufacturer specs; no hardware) | DONE — recommend 7.2 mm 3535 144/m, 50 px; 12 mm 144/m rejected | `electronics/LED_STRIP_COMPARISON.md` |
| 2026-11-15 | V5.1 hand channel / crystal well: closed solids, lens and crystal lift-out, channel size, dowels unchanged | PASS (computed) | `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_1_Verification.json` |
| 2026-11-15 | V5.1 model transfer integrity | PASS locally (16/16) | `V5_1_SHA256_MANIFEST.txt`; 43,283,814 bytes; copied SHA-256 values match and every 3MF archive entry was readable. See [[HANDOFF]] for remote status. |
| 2026-11-15 | V5.1 remote LFS readback | PASS (16/16) | Asset commit `030b461ea3a0ca205c045aa3de6da7a0f3b803f9`; path-filtered fetch to an empty independent cache, all SHA-256 values matched the manifest; `git lfs fsck` passed. |
| 2026-11-15 | V5.2 digital assembly, LED-strip, wire-path and finger-fit simulation | PASS (computed); wire link fixed 2 → 4 mm; hand strip corrected to 33 LEDs | `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_2_SIMULATION_REPORT.md` |
| 2026-11-18 | T2 knuckle-slot coupon (owner print) | **PASS: finger fits.** Orientation changed by owner; supports filled the string bore. Part heavy at default slicer settings | owner report in chat; GitHub issue #5 |
| 2026-11-20 | Glow-in-the-dark blue PETG for covers (owner, A1 Mini) | **FAIL: wet filament, stringing and popping after 2 tries.** Switched to transparent PLA | owner report in chat |
| 2026-11-22 | **Board 2 + strip 2 bench test** | **PASS (owner report):** "lights up and does the things" (WLED set up as board 1; effects work). AP SSID still default `WLED-AP` (owner renames later). No separate heat test (same design as board 1) | owner in chat 12:29 |
| 2026-11-22 | Board 2: JST pigtail soldered (rosin flux used) | **PASS (photo check):** top: white→G, green→32, red→5V, 33 empty; underside joints smooth/shiny, 33 pad tinned but separate; cleaned 12:18: clear gaps either side of 33, solder ball gone. OK to power | owner photos 12:13, 12:15, 12:18 |
| 2026-11-22 | **Bench step 10: heat test**, 91 LEDs solid white, brightness 255, WLED limit 1000 mA (est. 1000 mA), USB-C phone charger, strip flat in open air, ~14 min | **PASS (touch only, no thermometer):** strip start, board, solder joints, JST all "warm" at 5 and 10 min, as owner expected; no restarts (uptime 18 min 53 s at end). Not yet tested enclosed under the PLA cover | owner in chat + screenshots 10:16, 10:30 |
| 2026-11-22 | Bench step 10c: reboot isolation | Board alone (strip unplugged) shaken: no reboot. Strip plugged in, coiled with loops crossing, shaken: **reboot**. Working theory: bare copper cut pads (5V/DIN/GND, between **every** LED on this strip, owner close-up 09:57) of crossing loops, or the far-end plug, bridging 5V–GND momentarily. **Confirmed 10:11:** strip laid with no crossings, far-end plug clear, shaken + JST wiggled: no restarts. Cause = strip pads shorting against each other when coiled. Joints and JST OK | owner in chat + photo 09:56 |
| 2026-11-22 | Bench step 10: heat test (91 LEDs, 1000 mA, USB-C charger) | **INTERRUPTED ~09:41:** owner moved the strip and it turned off and back on. Board rebooted (segments lost; Info uptime 2 min 45 s at 09:43). Suspects: momentary 5V–GND short on strip side (bare pads / far-end JST near metal screws) or tug on USB-C / joints | owner in chat |
| 2026-11-22 | Bench step 10 setup: length 91, max PSU 1000 mA, USB-C charger | **INFO:** first 91 white; LEDs 92–160 stayed warm yellow. Cause: WS281x pixels hold their last colour while powered; after the soft reboot WLED no longer sends data past LED 91. Those latched pixels are outside the brightness limiter. Power-cycle did NOT clear it (09:29). 09:32: WLED power OFF → 92–160 stay yellow; Info: Total LEDs 91, one segment, est. 1000 mA. So WLED is not driving them; likely boot-time data-line noise latched by unaddressed pixels (unconfirmed). Workaround: length 160 + segment 0 stop 91. **09:38: workaround PASS, 92–160 dark** | owner photos 09:25, 09:29, screenshots 09:30–09:31 |
| 2026-11-22 | Bench step 9: Rainbow effect, all 160 LEDs, powered from computer USB | **PASS:** all LEDs correct, no flicker or dead pixels to the far end | owner in chat 02:19 |
| 2026-11-22 | Bench step 8: colour order (WLED Solid red / green / blue) | **PASS:** all three correct, GRB confirmed for the BTF 2020 strip | owner in chat 02:17 |
| 2026-11-22 | **Bench step 7: first light** (board 1 + full 1 m strip, USB-C, WLED 16.0.1, ABL 500 mA) | **PASS:** whole strip lights warm yellow (WLED default) end to end; no heat/smell reported | owner in chat 02:16 |
| 2026-11-22 | Bench step 6b: rework check | **PASS (visual, pending tug test):** stray strand gone, SMD caps clear; three joints fully wet their pads, no bridges, 33 pad empty; joints frosty (typical of lead-free) with rosin residue; a few loose specks near the 33 pad to brush off | owner photo 02:13 |
| 2026-11-22 | Bench step 6: pigtail soldered to board 1 (through-hole, wires from top) | **REWORK before power (photo review):** placement correct (red 5V, green 32, white G, 33 empty), no bridges seen. Found a stray thin strand lying across the two SMD capacitors next to the 32 joint, touching toward the GPIO 26 hole; 32 and G joints look dull/grainy; wire stubs untrimmed; red insulation looks heat-deformed at 5V | owner photos 02:04 (top + 2 bottom) |
| 2026-11-22 | Bench step 5: pigtail plug test | **PASS:** 3-wire pigtail (no extra power wires) mates with input-end plug; colours line up straight through (red-red, green-green, white-white) | owner in chat 00:49 |
| 2026-11-22 | Bench step 4: strip input end and wire colours (visual, no multimeter) | **PASS (visual):** arrows point away from the factory cable end that carries the product tag = input end. At the pads: red on the pad marked +5V (strip edge), green on the middle (data) pad, white on the opposite (GND) pad. Matches vault (red 5V, green data, white GND) | owner close-up photo 00:47 |
| 2026-11-22 | Bench step 3a/3: AR mic remapped to 9/10/23, then LED prefs set | **PASS (config saved):** WS281x RGB, GRB, 160 LEDs, GPIO 32, ABL on, max PSU 500 mA, 55 mA/LED, per-output limiter off, global brightness factor 100 % | owner screenshots 00:39 and 00:41 (second shows Data GPIO 32, start 0, length 160, not reversed, skip 0; RMT 1/8 used) |
| 2026-11-22 | Bench step 3: set LED GPIO 32 in stock WLED 16.0.1 | **BLOCKED (resolved by 3a):** GPIO 32 shown as reserved by usermod (AudioReactive default mic pins). Fix: remap AR mic to 9/10/23 per Adafruit guide | owner in chat |
| 2026-11-22 | Bench A: board 1 on USB-C alone, WLED check | **PASS:** owner flashed stock WLED 16.0.1 (board was not preinstalled); `WLED-AP` joined, `4.3.2.1` UI loads. Stock LED defaults: WS281x, GRB, 30 LEDs, GPIO 1 | owner in chat |
| 2026-11-22 | Controller count (owner report) | 3 × Adafruit 6160 in hand | owner in chat; [[electronics/HARDWARE_AS_BOUGHT]] |
| 2026-11-21 | Parts received (owner report) | Both LED strips, buttons, both ESP32 boards, capacitors in hand; silicone wire not yet arrived | owner report in chat; [[electronics/HARDWARE_AS_BOUGHT]] |
| 2026-11-21 | Left vs right translucent inserts congruence (computed) | INFO: mirror images, not identical (best fit ≤0.16 mm lens A, ≤0.30 crystal, ≤0.49 ring cover); print L files for left | session note 2026-11-20 |
| 2026-11-14 | V5 physical prints (T-1, T2 coupon, dowel fit) | NOT RUN | owner to print |
| 2026-11-14 | LED strip and ring fit | BLOCKED (hardware) — CAD measured: trough 27.1 mm wide × 13.3 mm deep; physical test T-1 proposed | `audits/results/ELECTRONICS_FIT.md` |
| 2026-11-14 | Original finger mount and tendon travel | NOT RUN physically — digital findings in ISSUES C-3, C-5; test T-2 proposed | `audits/results/FINAL_VERDICT.md` |
| 2026-11-14 | V5 draft model SHA-256 manifest | PASS (33/33) | `releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_SHA256_MANIFEST.txt`; 82,500,770 bytes |
| 2026-11-14 | V5 targeted remote LFS readback | PASS (2/33 sampled) | Fresh clone retrieved `Dowel_Peg_5p9x30_optional.3mf` (2,884 bytes) and `R_01_Cuff_Left_Front_V5.3mf` (1,641,461 bytes); both SHA-256 values matched the manifest |

Also update [[docs/RELEASE_GATES]] and [[HANDOFF]] after every test.
