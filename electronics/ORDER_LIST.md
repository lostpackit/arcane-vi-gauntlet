# LED and electronics order list — both gauntlets (Claude, 2026-11-15)

> **Status 2026-11-21:** the strip and controller choices below are superseded. Bought and received: BTF 5 mm SMD2020 160/m strip (1 m) and one Adafruit Sparkle Motion Mini; see [[electronics/HARDWARE_AS_BOUGHT]] and [[notes/LED_Wiring_Start_Here]] for current hardware and the 91-LED layout. The rest of this list is kept for history and for the parts still to order.

## Amazon order list, 2026-11-23 (Electronics conversation; owner ordering now)
Must have:
- 470 Ω resistors, 1/4 W (small assortment) — 2 per arm for always-on button LEDs from 5V.
- 2 × power bank: USB-C output 5 V ≥ 2 A, slim (~100 × 65 × 15 mm or smaller), ~5000 mAh, ideally with a low-current / always-on mode (many banks switch off at low draw). Test with the gauntlet on Calm before relying on it.
- 2 (+1 spare) × short USB-C to USB-C cable, 20–30 cm, preferably one angled plug.
- Strong self-adhesive hook-and-loop (Velcro) strips for the power banks.
- Heat-shrink assortment (resistor legs, wire joints at the button pod).
- Isopropyl alcohol 99 % (flux clean-up, surface prep before tape/glue).
- Small cable ties, 2.5 mm wide (sled strain-relief bar).
Recommended:
- Cheap digital multimeter (continuity, LED polarity, 5 V checks).
- Thin clear double-sided acrylic foam tape ("VHB" type), 5–6 mm wide, as a better hold for the strip than its factory tape on LW-PLA (plus UHU Poly Max dots, already owned).
Optional: USB-C power-bank KeepAlive module, only if the chosen bank keeps switching off.
Already have / pending: silicone wire (pending), UHU Poly Max, M2 × 8 screws, rosin flux, solder. **Owner 2026-11-23 00:27: also has USB-C cables, cable ties, isopropyl alcohol, and probably power banks (5000 or 7000 mAh; to test for low-current shut-off and size).** Still to buy: resistors, Velcro, heat shrink (if none), multimeter + VHB-type tape (recommended). **00:29: owner also has heat shrink, Velcro and clear double-sided tape → only 470 Ω resistors (+ optional multimeter) left to buy.**

This is the single list to order from. It consolidates `BOM.md`, `LED_STRIP_COMPARISON.md` and the V5.1 CAD. **Nothing has been purchased or bench-tested.** "Verified" means the product and its key specification were confirmed on a manufacturer or store page; everything else is a search term to check before buying.

## Is there an LED ring for the gauge?

**No.** The gauge light is a length of the same LED strip wrapped around the inside of the ring trough (50 pixels on the outer wall). A ready-made LED ring board is not needed and none was matched to the trough.

## LEDs per arm (V5.1)

| Zone | Pixels | Strip length |
|---|---|---|
| Ring (gauge halo) | 50 | 347 mm |
| Hand channel, including the part under the crystal | 33 | 229 mm |
| **Total** | **83** | **576 mm** |

## Order list

| # | Item | Qty | Specification to check | Where | Status |
|---|---|---|---|---|---|
| 1 | LED strip, BTF-LIGHTING Ultra-Narrow WS2812B | 2 m (2 × 1 m or 1 × 2 m) | 3535 LEDs, **144 LEDs/m, 7.2 mm**, 5 V, IP30, white PCB | https://www.btf-lighting.com/products/ultra-narrow-ws2812b-addressable-rgbic-led-strip (variant "3535 144LEDs 7.2mm IP30") | Product verified on manufacturer page; ships from China, buyer handles customs. Not found on Amazon.de |
| 2 | Fallback/bench strip, BTF-LIGHTING WS2812B | 1 m | 5050, **60 LEDs/m, 10 mm**, 5 V, IP30 | Amazon.de, BTF-LIGHTING store | Listing not individually verified |
| 3 | ESP32 controller board | 1 pack of 3 | **AZDelivery 3 × ESP32 NodeMCU Dev Kit C, WROOM-32, CP2102, USB-C, pins soldered** (matches the reference wiring and firmware pins) | https://www.amazon.de/AZDelivery-Development-Anschluss-kompatibel-inklusive/dp/B0D8WBG557 | **Chosen 2026-11-17.** Listing found by search, not opened; check "3 ×", USB-C and soldered pins |
| 4 | Level shifter | 2 + spare | 74AHCT125 (DIP-14 or breakout) | Amazon.de: `74AHCT125` | Not verified |
| 5 | Tactile switches with caps | 4 + spares | **12 × 12 mm tactile switch ("Taster 12x12 mit Kappe")**, to fit the handle button pod | Amazon.de: `Taster 12x12mm mit Kappe` | Not verified; pod is a concept sized from catalogue dimensions |
| 6 | Power bank | 2 | 5 V, **with a USB-A output port**, at least 2.4 A, 5,000–10,000 mAh, low-current mode ("Kleinstrom") | Amazon.de | Not verified |
| 7 | Inline fuse holder + 3 A fuses | 2 + spare fuses | Blade or 5×20 mm, 3 A | Amazon.de: `Sicherungshalter Flachsicherung` | — |
| 8 | Electrolytic capacitor | 2 + spares | 1000 µF, 10 V or higher | Amazon.de: `Elko 1000uF 16V` | — |
| 9 | Resistors | assortment | 330–470 Ω | Amazon.de: `Widerstand Sortiment` | — |
| 10 | 3-pin connectors | 6+ pairs | JST-SM 3-pin with leads | Amazon.de: `JST SM 3 Pin Stecker Buchse` | — |
| 11 | Silicone wire | 1 set | 22 AWG (power), 26 AWG (signal) | Amazon.de: `Silikonkabel 22AWG Set` | — |
| 12 | **USB-A** plug with bare leads | 2 + spare | USB-A male to open wires, 5 V power | Amazon.de: `USB A Stecker offene Enden Kabel` | Changed 2026-11-17: a bare USB-C plug gets no power from most USB-C power banks (they only switch on when they detect a device) |
| 13 | Heat-shrink tubing | 1 set | — | Amazon.de | — |
| 14 | Wooden dowels | 120 | 6 × 30 mm | Amazon.de / Baumarkt: `Holzdübel 6x30` | 57 per arm |
| 15 | ~~Small magnets~~ | — | **Dropped 2026-11-15.** The gauge has no flat contact area for magnets; it is glued to the cover and the cap is held with removable putty (item 17) | — | Not needed |
| 16 | Clear or translucent PLA | 1 spool | For cover, hand lenses, crystal | — | — |

## Not to buy

12 V or 24 V pixel strips, silicone-sleeved (IP65/IP67) strips, the 5050 144 LEDs/m strip (about 12 mm wide), bare LiPo cells, an LED ring board.

## Settings that go with this list

WLED: 83 LEDs, WS281x, colour order GRB (confirm on the sample), current limit 1000 mA, segments ring `[0,50)`, hand `[50,73)`, crystal `[73,83)`; presets in `wled/presets_144.json`. Standalone firmware: default build is the same 83-pixel layout.

## First things to do when parts arrive

1. Bench test 3–5 pixels of the strip with the controller, fuse and capacitor.
2. Seat 50 pixels in a printed ring (shell 08 or the stand-in `Circle_Light.stl`) with the cover on.
3. Measure current at the 1000 mA limit and temperature after 30 minutes.

## Update 2026-11-15 (V5.2 simulation)

- Hand strip is **33 LEDs** (the deepened channel is 232.5 mm long), so each arm is **83 LEDs**. Strip quantity is unchanged (1 m per arm).
- Items 5 and 3: concept mounts now exist in `releases/v5/Vi_Gauntlet_X1C_V5_Draft/Mounts_CONCEPT/`: a clip-on handle pod for **two 12 × 12 mm tactile switches** and an 80 × 45 mm electronics sled with zip-tie slots. If you want to use the pod as drawn, buy 12 × 12 mm tactile switches with caps instead of panel-mount buttons. The sled takes either controller board.
- Add: hook-and-loop tape (sled and power bank to the cuff wall), small zip ties, removable mounting putty (gauge cap).

## Update 2026-11-17 — list re-checked

The list is still valid. Changes folded into the table above: the controller is now a specific board (item 3), buttons are 12 × 12 mm tactile switches for the handle pod (item 5), and magnets are dropped (item 15). Added:

| # | Item | Qty | Why |
|---|---|---|---|
| 17 | Removable mounting putty | 1 pack | Holds the gauge-and-cover cap |
| 18 | Hook-and-loop tape, self-adhesive | 1 roll | Electronics sled and power bank to the cuff wall |
| 19 | Small zip ties | 1 pack | Boards onto the sled |
| 20 | Clear glue or thin clear double-sided tape | 1 | Hand lenses, crystal, gauge to cover |

**Must-have to light one ring on the bench:** items 1 (or 2), 3, 4, 6, 7, 8, 9, 11, 12. Everything else can wait until parts are printed.

## Update 2026-11-17 (late) — gaps found while drawing the wiring

| # | Item | Qty | Why |
|---|---|---|---|
| 21 | Perfboard ("Lochrasterplatine"), small | 2–3 | The 74AHCT125 is a bare chip; it, the resistor and the capacitor need something to sit on |
| 22 | 14-pin DIP socket | 2 + spare | So the shifter chip plugs in and is not soldered directly |
| 23 | Dupont jumper wires (female-female and female-male) + small breadboard | 1 set | First bench test without soldering to the ESP32 |
| 24 | Soldering iron, solder, multimeter | if not already owned | Strip joints, power wiring, and the current/temperature test |

Items 6 and 12 changed: power comes from a **USB-A** port through a USB-A pigtail. Do not power the ESP32 from USB and the power bank at the same time.

## Revision 2026-11-17 (night) — PROPOSED, replaces items 3, 4, 7, 9, 12, 21, 22, 23 and the USB-A change

Owner objections: wants USB-C, not USB-A; a perfboard/breadboard build has no clear home inside the glove; the 7.2 mm ultra-narrow strip is out of stock.

**Controller: Adafruit Sparkle Motion Mini** (ADA6160, or ADA6314 with pre-soldered terminal block), 2 + 1 spare. ESP32 module, WLED-friendly, **USB-C power input up to 5 V 4 A with a 4 A resetting fuse**, two **level-shifted** LED outputs, 32.3 × 19.7 × 12.4 mm, 5.1 g, mounting holes. It replaces: the AZDelivery ESP32 pack, the 74AHCT125, perfboard, DIP socket, inline fuse holder, USB pigtail and breadboard. Power: ordinary USB-C to USB-C cable from a USB-C power bank. Not on Amazon.de; European sellers found: Opencircuit (NL), robot-domestici (IT), Pimoroni (UK/EU), The Pi Hut (UK). Stock varies.

Still needed: 1000 µF capacitor at the strip (recommended), silicone wire, heat-shrink, 3-pin JST connectors, two 12 × 12 mm tactile switches per arm, short USB-C to USB-C cable per arm, USB-C power bank with low-current mode.

**LED strip:** any 5 V WS2812B, IP30, **width 10 mm or less**, 144–160 LEDs/m fits both the ring wall (about 13.0 mm high) and the hand channel (11.3 mm wide) with no CAD change; the LED count is a WLED setting. Candidates seen in search, stock not verified: BTF-LIGHTING WS2812B 2020 5 mm 160/m; TOPXCDZ WS2812B 3535 8 mm 144/m. Fallback that is widely stocked: BTF-LIGHTING WS2812B 5050 60/m 10 mm (21 + 15 LEDs per arm, more stepped animation).

Firmware/WLED pin map and the sled concept must be updated to this board once the owner confirms.
