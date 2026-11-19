# Lighting hardware as bought (2026-11-19)

Confirmed from the owner's photos of the packaging.

| Part | Exact item | Notes |
|---|---|---|
| LED strip | BTF-LIGHTING model `HD-5V-2020-160-W-IP30-SPI`, SKU `20205V1M160L5MMRGBICW30-EU`: DC 5 V, PCB width 5 mm, 1 m, 160 LEDs/m, RGB, IP30, white PCB | Chip not named on the bag. BTF's enclosed connector card shows a 3-pin connector (+V, Data, GND), the single-data-line type WLED drives as WS281x. Confirm the pad labels on the strip itself |
| Controller | Adafruit Mini Sparkle Motion **6160** (no terminal block), seller Paradisetronic | 1 received, 1 outstanding |

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
