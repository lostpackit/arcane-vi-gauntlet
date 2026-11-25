# V5.5 thumb fix: the stock Thumb_Base is left-handed (2026-11-25)

Computed by Claude (Mechanics) after the owner's dry-fit photos of 2026-11-25. **Not printed or fitted by any agent.**

## Finding
- The printable `Thumb_Base` in `originals/Vi Gauntlet 3mf Project File.3mf` is the **left-hand** base. Mirrored, it matches the right-arm base in `Together For Sizing.stl` to a median of 0.013 mm. Without mirroring, no rigid fit exists.
- V5.3 (2026-11-22) forced the unmirrored (left) base onto the **right** shell 13. The collision it found, the socket it cut and the dowel hole it placed all come from that impossible pose. **V5.3 is withdrawn.**
- The V5.3 base files are swapped: `R_Thumb_Base_V5_3_dowel` is the left-hand shape and `L_Thumb_Base_V5_3_dowel` is the right-hand shape.
- **The original design already fits.** Shell 13 V5_1 has a tapered square key pocket. The correct-hand base's key sits inside it with clearance on every section from x = 338 to 329. About 28 cm² of the base is within 0.5 mm of the shell, and the overlap is a 0.35 cm³ skin, i.e. nominal contact. No socket or dowel is needed.

## Printed parts (owner has these)
| Printed part | Is actually | Use on | Stray V5.3 hole |
|---|---|---|---|
| `L_Thumb_Base_V5_3_dowel` | right-hand base | **RIGHT arm** | 6.4 × 16 mm blind hole whose mouth is on the **outer** face (points away from the hand). Plug: glue a 6 mm dowel stub, cut flush, sand, fill |
| `R_Thumb_Base_V5_3_dowel` | left-hand base | **LEFT arm** | same, mirrored |
| `R_13_Knuckles_Right_V5_3` (printed) | usable | right arm | Key pocket **intact** (sections match V5_1). With the correct base: overlap 0.30 cm³, about 19 cm² within 0.5 mm. Extra V5.3 cavity above the key and the V5.3 shell dowel hole (mouth near the upper edge of the base) are not filled by the base: dry-fit first, then fill the visible part with a dowel stub and epoxy putty. **Keep the key pocket clean.** |

## What to print
- **L_13: print `L_13_Knuckles_Right_V5_1`** (named print pack `7_Left_Arm/`, also in the repo via LFS), **not** `L_13_..._V5_3`. V5.3 changed only the thumb socket and hole, so the seams with L_11 SPAREMATCH and L_12 are identical.
- Optional clean reprints (no stray hole), A1 Mini, standard PLA, 4 walls: `R_Thumb_Base_V5_5_mirrored.3mf` (right arm) and `L_Thumb_Base_V5_5_stock.3mf` (left arm; identical to the stock 3MF base). Same print pose as the stock base. Hashes: `V5_5_SHA256_MANIFEST.txt`. **LFS upload pending** (delivered in chat).

## Assembly (both arms)
Dry-fit: push the base straight onto the side of the hand (along −X), key into the square pocket, and check that it sits without rocking. Then glue it with UHU Plus Schnellfest on the key and the contact faces. No dowel.

## Possible thumb string route (issue #14, to check with a wire)
Next to the key pocket, shell 13 has a 3.8 × 5.4 mm slanted bore. A line through its centre passes through the correct-pose base without touching material, which suggests that the base has a matching hole. Push a 1 mm wire through before gluing to see whether it is a string path.

Evidence: `thumb_v5_5_finding.png`, `printed_R13_V5_3_with_correct_base.png`. Script: `Build_Scripts/v5_5_thumb_fix.py`.
