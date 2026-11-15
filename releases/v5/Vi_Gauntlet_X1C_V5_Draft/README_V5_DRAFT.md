# Vi Gauntlet V5 — DRAFT (digital only, unprinted)

Built by Claude on 2026-11-14 after owner approval of the V5 direction. **Status: draft for test printing. Not print-approved.** Nothing here has been sliced in Bambu Studio or printed. Originals were not modified; every file here is derived.

> **Where the 3MF files are.** The 33 original V5 models are in this release folder and tracked with Git LFS. Their hashes matched `V5_SHA256_MANIFEST.txt`; see `docs/ASSET_MAP.md` for transfer evidence. The V5.1 update below supersedes selected shells.

## What V5 is

The same idea as V4 (everything except the fingers fused into one solid, cut into 13 bed-sized shells per arm on the same planes and print orientations), with the functional parts kept separate so the gauntlet can be lit and held:

| Change | Detail |
|---|---|
| **Ring light opened** | The diffuser cover and the pressure gauge are no longer part of shell 08. The LED trough (27.1 mm wide, 13.3 mm deep) is open from above. Cover and gauge lift straight out along the ring axis. |
| **Cover + gauge are inserts** | `Inserts/*_Ring_Light_Cover_translucent` (print in clear/translucent PLA) and `Inserts/*_Pressure_Gauge_Insert` (gauge + needle). The gauge tail also sits in shallow pockets in shells 02 and 04. Pockets have 0.35 mm clearance per side. |
| **One-piece handle** | The handle is no longer fused and cut. Shells 10/11 have Ø19.3 mm sockets with reinforcing collars, 12.3 mm engagement each side, at least 6 mm of wall behind each. `Inserts/Handle_OnePiece_18p8x250` is a Ø18.8 × 250 mm bar. |
| **Seam dowels** | 57 dowel sockets (Ø6.4 mm, 16 mm deep each side) across all 27 shell-to-shell interfaces, for 6 × 30 mm dowels. Positions in `V5_build_log.json`. |
| **Clean meshes** | Output is 3MF. All 33 files load as manifold single parts in the slicer check. |

Not changed in this draft: seam planes, finger carrier geometry, light-strip window, crystal, palm opening, electronics pocket. See "Open items".

## Files

- `Right_Shells/`, `Left_Shells/` — 13 shells each, 3MF, already oriented for printing and centred on a 256 mm bed. Left is the exact mirror.
- `Superseded_V5_DO_NOT_PRINT/` — the original V5 versions of shells 08 and 10–13, replaced by the `_V5_1` files. History only.
- `Inserts/` — cover and gauge (R and L), handle, optional printable dowel peg.
- `Test_Coupons/T2_Knuckle_Slot_Forefinger_Coupon.3mf` — the forefinger slot of shell 13 (105 × 115 × 75 mm) for checking your printed finger before committing to shells 12/13.
- `V5_Geometry_Check.csv`, `V5_Verification.json`, `V5_build_log.json`, `V5_Surrogate_Slice_Light_Settings.csv`, `Evidence/`, `Build_Scripts/`.

## Per-shell table (right arm)

Filament is from a **PrusaSlicer surrogate** at lightweight settings (2 walls, 3 top/bottom layers, 8 % gyroid, 5 mm brim, build-plate supports), computed for **standard PLA at 1.24 g/cm³**. It is not a Bambu Studio number.

| Shell | Print size (mm) | Volume cm³ | Dowel sockets | Filament g | of which support g | Fits A1 Mini |
|---|---|---|---|---|---|---|
| 01 Cuff Left Front | 209.87 × 147.0 × 70.86 | 486.43 | 5 | 121 | 8 | no |
| 02 Cuff Left Rear | 209.97 × 147.02 × 145.0 | 961.38 | 10 | 202 | 20 | no |
| 03 Cuff Right Front | 209.4 × 147.0 × 70.86 | 485.95 | 5 | 120 | 7 | no |
| 04 Cuff Right Rear | 209.49 × 147.01 × 144.97 | 961.62 | 7 | 200 | 19 | no |
| 05 LightBand Front Left | 210.9 × 165.0 × 177.53 | 1853.66 | 14 | 498 | 133 | no |
| 06 LightBand Front Right | 210.52 × 165.0 × 177.53 | 1849.78 | 14 | 496 | 131 | no |
| 07 LightBand Rear Left | 100.0 × 165.0 × 65.91 | 442.15 | 9 | 105 | 11 | yes |
| 08 LightBand Rear RingCarrier | 200.0 × 165.0 × 83.83 | 1014.25 | 10 | 409 | 132 | no |
| 09 LightBand Rear Right | 121.61 × 165.0 × 71.87 | 597.95 | 8 | 149 | 26 | yes |
| 10 Wrist Left | 180.97 × 224.92 × 90.0 | 945.87 | 10 | 285 | 30 | no |
| 11 Wrist Right | 180.59 × 224.93 × 90.0 | 943.44 | 10 | 289 | 33 | no |
| 12 Knuckles Left | 199.75 × 199.04 × 166.22 | 1588.59 | 6 | 492 | 109 | no |
| 13 Knuckles Right | 200.12 × 199.04 × 157.7 | 1544.48 | 6 | 476 | 103 | no |

Totals per arm at these settings: **3,843 g** filament, of which 760 g is support; shells alone about 3,083 g in standard PLA. V4 at the README settings was 6,183 g and about 5,420 g.

**Lightweight PLA:** foaming LW-PLA is normally run at a reduced flow, giving roughly half to two-thirds of the mass of standard PLA for the same toolpath. On that assumption the shells would come to very roughly 1.6–2.1 kg per arm. This is an estimate; it depends on your filament's flow setting and was not sliced.

Supports are about a fifth of the filament and are concentrated in shells 05, 06, 08, 12 and 13. Re-orienting those is the next mass and time saving to look at.

## Materials

- Shells: lightweight PLA is fine.
- **Handle, dowels and finger carrier loads: use standard PLA or PETG, not LW-PLA.** Print the handle lying flat with supports, or use an 18–19 mm tube or dowel cut to 250 mm.
- Cover: clear or translucent standard PLA.

## Assembly notes

1. Dry-fit every seam with dowels before any glue. Dowel holes are modelled at 6.4 mm; foaming filament may close them up, so test one first.
2. The handle must go in **before** shells 10 and 11 are joined. It is captured between the two sockets.
3. Install the LED strip in the trough and bring the wires out through the notch into the arm cavity before fitting the cover.
4. The cover drops onto the trough rim; the gauge sits on top of it. Do not glue the gauge permanently. Use small magnets, removable adhesive or two dabs of hot glue so the light stays serviceable.
5. Most of the cover is hidden under the gauge. Light shows as a halo around the gauge edge (the cover is 118 mm across, the gauge 109 mm wide). Print the gauge in translucent filament if you want more glow.

## Verification done (computed, see `V5_Verification.json`)

- 33/33 files: watertight, consistent winding, no boundary or non-manifold edges; slicer reports manifold, single part. Two inserts contain a zero-volume speck (0.1 mm) besides the main body.
- Left shells are exact mirrors (0.0 mm deviation).
- Trough: top-down probes at five radii × 72 angles reach the floor everywhere; nothing sits above it.
- Cover and gauge: zero overlap with the arm when seated and when lifted 1–40 mm along the ring axis.
- Handle: zero overlap with the arm as placed; none of the old fused handle remains; 6.1–8.6 mm wall behind each socket floor.
- Dowel sockets: none intersect each other; each is surrounded by at least 1.5 mm of solid (4.5 mm on the seam face).
- All parts fit 256 × 256 × 250.

## Open items — do not treat V5 as finished

1. **Shells 12/13 are on hold.** The finger carrier inside them is still the older revision (audit issue C-3). Print the T2 coupon and try your finger on it first.
2. **Light-strip window and crystal** are still fused solid. Lighting them needs a channel cut under each; not done.
3. **Electronics**: no controller, button or battery mounts yet. Planned for the cuff after the LED hardware is chosen.
4. **Seam planes** are unchanged from V4, so the centre seam still crosses the visible top details.
5. **Thumb**: mount and string route not addressed.
6. **No Bambu Studio slice, no physical test.** Gates in `docs/RELEASE_GATES.md` still apply.

## Suggested first prints

1. `R_Ring_Light_Cover_translucent` + the original `Circle_Light.stl` (audit test T-1) on the A1 Mini, to settle the LED strip choice.
2. `T2_Knuckle_Slot_Forefinger_Coupon` on the A1 Mini, with one of your printed fingers.
3. `R_09` (A1 Mini) and `R_07`, small shells that share a doweled seam with 08, to test dowel fit in your LW-PLA.
4. Then `R_08_LightBand_Rear_RingCarrier_V5_1`.

---

# V5.1 update — hand light strip and crystal (2026-11-15, owner-approved)

> **File status:** the 16 new `.3mf` files (shells 08, 10, 11, 12, 13 for both arms, crystal and hand-lens inserts) match `V5_1_SHA256_MANIFEST.txt`; see `HANDOFF.md` for remote sync status. Superseded V5 shells are retained for history but **must not be printed**. Shells 01–07 and 09 and the other inserts are unchanged.

## What changed

Inspection of the fused solid showed the original design already contains an **LED channel under the hand light strip** (about 11.3 mm wide, 2.2 mm deep) and a **light well under the crystal**. Both were sealed. V5.1 opens them:

| Change | Detail |
|---|---|
| Hand lens freed | The 13.3 × 238 mm light-strip insert is no longer fused. Its slot is open to the outside where nothing sits over it. |
| LED channel deepened | Channel under the lens is now 4.2 mm deep (was 2.2) over a 10.5 mm width, 11.3 mm wide at the top. 4.6–6.6 mm of wall remains to the hand cavity. Straight and unobstructed for its whole length. |
| Channel reaches the ring | The channel runs on toward the ring's wire notch, so the ring strip and the hand strip can be one data chain with the joint at the notch. |
| Crystal freed | The crystal is a lift-out insert (0.3 mm clearance). The well beneath it is open down to the LED channel, so **the hand strip lights the crystal**; no separate crystal LEDs. |
| Dowel sockets | Identical positions to V5, so any V5 shells already printed still mate. |

## New inserts (print in clear or translucent standard PLA)

- `*_Hand_Lens_A_translucent_81mm` — sits between the ring and the top plate.
- `*_Hand_Lens_B_translucent_46mm` — sits between the top plate and the crystal base.
- `*_Crystal_translucent`.

The lens is only fitted where it is visible. Under the top-plate bridge and under the crystal base the slot is left as an open tunnel for the strip.

## LED layout per arm with the 7.2 mm 144 LEDs/m strip

Ring 50 + hand channel 34 = **84 pixels** (replaces the earlier 93). The last 11 hand pixels sit under the crystal well. WLED segments: ring `[0,50)`, hand `[50,73)`, crystal `[73,84)`.

## Fitting notes

1. Feed the strip into the channel from an open section and push it through the two tunnels (22 mm under the top plate, about 18 mm under the front of the crystal base). Do this before bonding anything over it.
2. The lens rests on ledges about 1.0 mm wide each side. Fix it with a few dots of clear glue or thin double-sided tape; it carries no load.
3. LEDs sit about 2 mm below a 1.6 mm lens, so individual pixels will be visible as soft dots at 144 LEDs/m. A frosted or thicker lens print softens this.
4. The centre seam (X = 211) runs along the channel. Channel floor at the seam is 4.6 mm or more.
5. The crystal rests on a narrow rim (about 12 % of its underside). Glue dots are enough.

## Verification (computed; `V5_1_Verification.json`)

- 39/39 built files are closed manifold single parts within the X1C envelope; left = exact mirror.
- Only shells 08, 10, 11, 12, 13 differ from V5 (−0.8 to −4.8 cm³ each).
- Crystal: zero overlap seated and lifted 1–25 mm. Lens segments A and B: zero overlap seated; lift-out clear (one 0.3 mm³ contact at 3 mm).
- Channel: 11.3 mm wide, 4.2 mm deep at 12 stations; 234 mm clear straight run.
- Channel under the crystal is open to the outside through the crystal pocket at three stations.
- No dowel socket has lost its surrounding wall.

Still unprinted and unsliced in Bambu Studio. Shells 12/13 remain on hold for the finger test.

---

## Current print set (as of 2026-11-15) — 13 shells per arm

Each folder (`Right_Shells/`, `Left_Shells/`) now holds exactly one file per shell:

| Shell | File (right arm; left is the same with `L_`) | Version |
|---|---|---|
| 01–07, 09 | `R_0x_..._V5.3mf` | V5 (unchanged) |
| 08 ring carrier | `R_08_LightBand_Rear_RingCarrier_V5_1.3mf` | V5.1 |
| 10, 11 wrist | `R_10_Wrist_Left_V5_1.3mf`, `R_11_Wrist_Right_V5_1.3mf` | V5.1 |
| 12, 13 knuckles | `R_12_Knuckles_Left_V5_1.3mf`, `R_13_Knuckles_Right_V5_1.3mf` | V5.1 — **on hold until the finger coupon test** |

Inserts: ring cover, gauge, handle, crystal, hand lens A and B (both arms), optional dowel peg. Test coupon: T2 finger slot.
