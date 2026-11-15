> **Current order list:** [ORDER_LIST.md](ORDER_LIST.md). The sections below are historical.

# Bill of materials — candidates for two gauntlets (not order-ready)

| Part | Quantity total | Proposed specification | Status / verification |
|---|---:|---|---|
| ESP32 | 2 | ESP32-WROOM-32 DevKit **reference**; XIAO ESP32-S3 is an alternate requiring different pins/WLED build | Select only after board footprint/power review |
| Ring LEDs | ~0.70 m + spare | Bare IP30, 5 V, addressable WS2812-compatible **RGB**, 8 or 10 mm PCB, ~60 LED/m; ~351 mm/arm | Ring T-1 fit, diffuser, bend, pad/wire clearance |
| Hand LEDs | ~0.48 m + spare | Narrow ~2.7 mm 5 V addressable RGB strip discussed earlier; ~238 mm/arm | No V5 mounting/channel confirmed |
| Crystal LEDs | ~8 pixels | 4 small addressable 5 V RGB pixels/arm (provisional) | V5 crystal geometry not final |
| Momentary switches | 4 | 2 per arm, normally open, thumb reachable with gloves | Ergonomics and button pods unverified |
| Level shifter | 2 | 74AHCT125 at 5 V or Adafruit Pixel Shifter #6066 after datasheet/pinout review | Verify actual module, power and IO |
| Data resistor | 2 | 330–470 Ω at first pixel DIN | Bench test |
| Bulk capacitor | 2 | 1000 µF, ≥10 V, across LED 5 V/GND, observe polarity | Physical mounting |
| Power banks | 2 | Protected commercial 5 V USB, ≥3 A sustained output, 5000–10000 mAh, low-current mode | Weight, size, auto-off, temperature |
| Fuse and holder | 2 | Inline 3 A fuse on +5 V close to bank | Match cable/connector ratings |
| 5 V distribution | 2 | Insulated USB power breakout/distribution rated ≥3 A | No USB/VIN back-feed |
| Detachable LED connectors | ≥4 pairs | Keyed/polarized 3-pin, rated for branch current | Ring/hand/crystal serviceability |
| Wire | As measured | 20–22 AWG power, 26–28 AWG signal, strain relief/heat-shrink | Measure lengths and voltage drop |
| Mounts | 2 sets | Removable controller and bank sled, accessible disconnect | Design around V5 handle and tendons |

**Power budget estimate**: 39 RGB pixels × 60 mA ≈ **2.34 A per arm** at worst-case full white, plus ESP32. This is a *conservative estimate*, not measured. WLED prototype current-limit target ~1.5 A/arm (software estimate only); physical fuse, rated wiring and meter tests remain mandatory. Do not mix RGBW and RGB protocols on an unverified single data chain. Use separate 5 V banks for the arms. No bare LiPo against skin; no charging while worn.

**Procurement hold**: Claude must verify real datasheets, actual 8/10 mm ring strip and ~2.7 mm hand strip dimensions, controller/power fit, LED channel, cover closure and V5 wiring access before approving a sample order. **No components have been bought.**

## Claude review — 2026-11-14 (LED strip selection; nothing purchased)

See [LED_STRIP_COMPARISON](LED_STRIP_COMPARISON.md). Earlier rows are kept as written; this section records the review outcome.

| Part | Review | Proposed change |
|---|---|---|
| Ring LEDs | **CHANGE** | BTF-LIGHTING Ultra-Narrow WS2812B 3535, 144 LEDs/m, 7.2 mm, IP30: **50 px per ring** on the trough outer wall. Fallback: WS2812B 5050 60/m 10 mm (21 px). The 5050 144/m strip is rejected (about 12 mm in a 13.0 mm wall). |
| Hand LEDs | **CHANGE / BLOCKED on CAD** | Same 7.2 mm 144/m strip, 34 px. The ~2.7 mm accent strip is not needed (window is 13.3 mm wide). V5 has no channel yet. |
| Crystal LEDs | **CHANGE / BLOCKED on CAD** | Same strip, 9 px. V5 has no pocket yet. |
| Strip quantity | — | 2 m of the 7.2 mm strip (1 m per arm = 93 of 144 LEDs), plus 1 m of 60/m 10 mm as fallback and bench sample. |
| Power budget | **CHANGE** | 93 px per arm; worst case 5.6 A at the manufacturer's 0.3 W/LED. WLED current limit is mandatory; start at 1000 mA per arm. 3 A fuse unchanged. |
| Power bank, fuse, shifter, resistor, capacitor, connectors, wire | APPROVE as specified | No change from the strip choice. |
| ESP32 board | OPEN | Either board drives 93 px. Choice depends on mount size and soldering; pin map must follow the chosen board. |
| Momentary switches | OPEN | Size and position wait for the handle-area button pod design. |

Remaining before any "order-ready" mark: T-1 ring fit with a real sample, colour order, measured current and 30-minute temperature.

## Update 2026-11-15 (Claude)

Consolidated order list: [ORDER_LIST](ORDER_LIST.md). With V5.1 the hand strip also lights the crystal, so the per-arm count is **84 pixels** (ring 50 + hand channel 34), not 93, and no separate crystal LEDs are needed. No LED ring board is used for the gauge.

**2026-11-15 (V5.2):** per-arm count corrected to **83** (ring 50 + hand 33). See [ORDER_LIST](ORDER_LIST.md).
