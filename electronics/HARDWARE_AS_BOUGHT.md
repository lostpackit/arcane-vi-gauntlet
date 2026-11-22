# Lighting hardware as bought (2026-11-19)

Confirmed from the owner's photos of the packaging.

| Part | Exact item | Notes |
|---|---|---|
| LED strip | BTF-LIGHTING model `HD-5V-2020-160-W-IP30-SPI`, SKU `20205V1M160L5MMRGBICW30-EU`: DC 5 V, PCB width 5 mm, 1 m, 160 LEDs/m, RGB, IP30, white PCB | Chip not named on the bag. BTF's enclosed connector card shows a 3-pin connector (+V, Data, GND), the single-data-line type WLED drives as WS281x. Confirm the pad labels on the strip itself |
| Controller | Adafruit Mini Sparkle Motion **6160** (no terminal block), seller Paradisetronic | **3 in hand** (owner, 2026-11-22, all confirmed as product 6160) |

### Product page facts (adafruit.com/product/6160, opened by Claude 2026-11-22)
- Size **31.6 × 19.8 × 7.3 mm**, with mounting holes. Sled design uses these numbers.
- USB-C power, rated 5 V 4 A, 4 A resettable fuse.
- Two level-shifted (5 V) LED outputs + 5V + GND on 0.1" pads; 2×3 pad block with 4 more GPIO + 3V + GND. GPIO numbers are not on the product page (32/33 and 14/27/25/26 come from the Adafruit guide and owner photos, recorded 2026-11-19).
- Onboard: I2S microphone, STEMMA QT, user button on GPIO 0, reset button, red LED on 12, small NeoPixel on 18, JST input port on 13. No IR receiver.
- Product page says "WLED-friendly" but does **not** say WLED is preinstalled. **Owner 2026-11-22: owner flashed board 1 with stock WLED himself (it did not come ready); now runs WLED 16.0.1, `WLED-AP` + `4.3.2.1` work.** Stock defaults seen: WS281x, GRB, length 30, GPIO reported as 1, brightness 100. Other two boards not yet checked; assume they need flashing too.

### Owner update 2026-11-21 (in chat)
Owner has: **both LED strips**, **the buttons**, **the ESP32 boards (both)**, **the capacitors**. Not yet arrived: **the additional (silicone) wire**. Buttons: **HUAZIZ LED push button 12 × 12 × 7 mm** (illuminated tact switch, through-hole; owner caliper 13.4 mm over legs, 14.64 mm over white tabs; 2026-11-22). Capacitor value not yet recorded.

## Board connections (Adafruit pinout page)

| Board pad | Goes to |
|---|---|
| 5V | strip 5V (red) |
| 32 | strip DIN (data), level-shifted on the board |
| G | strip GND, and the shared button ground |
| 14 | button A (mode), other leg to G |
| 27 | button B (action), other leg to G |
| 33 | spare second LED output |

GPIO 14 and 27 are general-purpose pins; the ADC2 note in Adafruit's guide only affects analog reads, not buttons. Avoid GPIO 0 (boot button) and 25/26 (serial).

## LED layout per arm (160 LEDs/m, pitch 6.25 mm)

| Zone | LEDs | Length | Fit (from CAD) |
|---|---|---|---|
| Ring, outer wall | 55 | 343.8 mm | wall 351.2 mm around, leaves 7.4 mm joint gap; strip 5 mm on a 13.0 mm wall |
| Hand channel incl. crystal | 36 | 225 mm | channel 232.5 mm long, 11.3 mm wide |
| **Total** | **91** | 569 mm | 1 m per arm |

WLED segments: ring `[0,55)`, hand `[55,80)`, crystal `[80,91)` (`wled/presets_144.json`). Standalone firmware defaults updated to the same layout and to pins 32 / 14 / 27.

Worst case at the listing's 0.3 W per LED: 91 x 60 mA = 5.5 A. The WLED current limit (start at 1000 mA) is required; the board's 4 A resettable fuse is a backstop, not the control.
