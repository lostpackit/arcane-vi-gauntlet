# LED and electronics order list — both gauntlets (Claude, 2026-11-15)

This is the single list to order from. It consolidates `BOM.md`, `LED_STRIP_COMPARISON.md` and the V5.1 CAD. **Nothing has been purchased or bench-tested.** "Verified" means the product and its key specification were confirmed on a manufacturer or store page; everything else is a search term to check before buying.

## Is there an LED ring for the gauge?

**No.** The gauge light is a length of the same LED strip wrapped around the inside of the ring trough (50 pixels on the outer wall). A ready-made LED ring board is not needed and none was matched to the trough.

## LEDs per arm (V5.1)

| Zone | Pixels | Strip length |
|---|---|---|
| Ring (gauge halo) | 50 | 347 mm |
| Hand channel, including the part under the crystal | 34 | 236 mm |
| **Total** | **84** | **583 mm** |

## Order list

| # | Item | Qty | Specification to check | Where | Status |
|---|---|---|---|---|---|
| 1 | LED strip, BTF-LIGHTING Ultra-Narrow WS2812B | 2 m (2 × 1 m or 1 × 2 m) | 3535 LEDs, **144 LEDs/m, 7.2 mm**, 5 V, IP30, white PCB | https://www.btf-lighting.com/products/ultra-narrow-ws2812b-addressable-rgbic-led-strip (variant "3535 144LEDs 7.2mm IP30") | Product verified on manufacturer page; ships from China, buyer handles customs. Not found on Amazon.de |
| 2 | Fallback/bench strip, BTF-LIGHTING WS2812B | 1 m | 5050, **60 LEDs/m, 10 mm**, 5 V, IP30 | Amazon.de, BTF-LIGHTING store | Listing not individually verified |
| 3 | ESP32 controller board | 2 + 1 spare | ESP32-WROOM-32 DevKit (matches the reference wiring and firmware pins) **or** Seeed XIAO ESP32-C3/S3 (smaller, different pins) | Amazon.de: `ESP32 DevKit WROOM-32` or `Seeed XIAO ESP32C3` | Board choice still open; either runs WLED |
| 4 | Level shifter | 2 + spare | 74AHCT125 (DIP-14 or breakout) | Amazon.de: `74AHCT125` | Not verified |
| 5 | Momentary push buttons | 4 + spares | Normally open, momentary ("Taster"), about 12 mm | Amazon.de: `Drucktaster 12mm Taster Schließer` | Size waits for the button-pod design |
| 6 | Power bank | 2 | 5 V, at least 2.4 A output, 5,000–10,000 mAh, low-current mode ("Kleinstrom") | Amazon.de | Not verified |
| 7 | Inline fuse holder + 3 A fuses | 2 + spare fuses | Blade or 5×20 mm, 3 A | Amazon.de: `Sicherungshalter Flachsicherung` | — |
| 8 | Electrolytic capacitor | 2 + spares | 1000 µF, 10 V or higher | Amazon.de: `Elko 1000uF 16V` | — |
| 9 | Resistors | assortment | 330–470 Ω | Amazon.de: `Widerstand Sortiment` | — |
| 10 | 3-pin connectors | 6+ pairs | JST-SM 3-pin with leads | Amazon.de: `JST SM 3 Pin Stecker Buchse` | — |
| 11 | Silicone wire | 1 set | 22 AWG (power), 26 AWG (signal) | Amazon.de: `Silikonkabel 22AWG Set` | — |
| 12 | USB-C plug with bare leads | 2 | 5 V power pigtail | Amazon.de: `USB-C Stecker offenes Ende` | — |
| 13 | Heat-shrink tubing | 1 set | — | Amazon.de | — |
| 14 | Wooden dowels | 120 | 6 × 30 mm | Amazon.de / Baumarkt: `Holzdübel 6x30` | 57 per arm |
| 15 | Small magnets (optional) | 12 | 6 × 2 mm, to hold the gauge over the light cover | Amazon.de | Needs magnet pockets (not yet in CAD) |
| 16 | Clear or translucent PLA | 1 spool | For cover, hand lenses, crystal | — | — |

## Not to buy

12 V or 24 V pixel strips, silicone-sleeved (IP65/IP67) strips, the 5050 144 LEDs/m strip (about 12 mm wide), bare LiPo cells, an LED ring board.

## Settings that go with this list

WLED: 84 LEDs, WS281x, colour order GRB (confirm on the sample), current limit 1000 mA, segments ring `[0,50)`, hand `[50,73)`, crystal `[73,84)`; presets in `wled/presets_144.json`. Standalone firmware: default build is the same 84-pixel layout.

## First things to do when parts arrive

1. Bench test 3–5 pixels of the strip with the controller, fuse and capacitor.
2. Seat 50 pixels in a printed ring (shell 08 or the stand-in `Circle_Light.stl`) with the cover on.
3. Measure current at the 1000 mA limit and temperature after 30 minutes.
