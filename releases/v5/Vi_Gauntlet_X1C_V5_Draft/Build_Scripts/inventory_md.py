import json
meta=json.load(open('meta.json'))
shells=[('01','Cuff_Left_Front','V5','Cuff, front (side A)'),('02','Cuff_Left_Rear','V5','Cuff, rear (side A)'),
('03','Cuff_Right_Front','V5','Cuff, front (side B)'),('04','Cuff_Right_Rear','V5','Cuff, rear (side B)'),
('05','LightBand_Front_Left','V5','Light band, front (side A)'),('06','LightBand_Front_Right','V5','Light band, front (side B)'),
('07','LightBand_Rear_Left','V5','Light band, rear (side A), small'),('08','LightBand_Rear_RingCarrier','V5_2','Ring carrier: holds the LED ring and cover'),
('09','LightBand_Rear_Right','V5','Light band, rear (side B), small'),('10','Wrist_Left','V5_1','Wrist (side A), handle socket'),
('11','Wrist_Right','V5_1','Wrist (side B), handle socket'),('12','Knuckles_Left','V5_1','Knuckles (side A), finger slots'),
('13','Knuckles_Right','V5_1','Knuckles (side B), finger slots')]
printer={'07':'A1 Mini or X1C','09':'A1 Mini or X1C'}
inserts=[('Ring_Light_Cover_translucent','Ring light cover','Transparent PLA','A1 Mini'),
('Crystal_translucent','Crystal','Transparent PLA','A1 Mini'),
('Hand_Lens_A_translucent_81mm','Hand lens A (long, 81 mm)','Transparent PLA','A1 Mini'),
('Hand_Lens_B_translucent_46mm','Hand lens B (short, 46 mm)','Transparent PLA','A1 Mini'),
('Pressure_Gauge_Insert','Pressure gauge','Opaque PLA (any)','X1C')]
def img(b,w=150): return f'<img src="images/{b}.png" width="{w}">'
def size(b): e=meta[b+'.3mf']; return ' × '.join(map(str,e))
L=[]
a=L.append
a('# Vi Gauntlet V5 — Parts Inventory\n')
a('Checklist of every part for each arm. Tick ☐ → ☑ (or write the date) as parts come off the printer.\n')
a('- Pictures are renders of the actual print files, not photos. They show each part in its **print orientation**, so the left-arm pictures look different from the right: the left parts are mirror images.')
a('- Sizes are the print bounding box in mm.')
a('- **Left-arm naming:** left shells keep the right arm\'s side names (`L_01_Cuff_Left_Front` actually sits on the other side). Label parts as they come off the printer.')
a('- **Shell 08 must be `_V5_2`** (from the print pack). The `_V5_1` file still in the repo is superseded.')
a('- **Left inserts:** use the files from `L_Inserts_Normals_Fix.zip`, not the older ones in `7_Left_Arm`.\n')
a('**Count per arm:** 13 shells + 5 printed inserts + 1 handle = 19 printed parts, plus 57 wooden dowels and the electronics.\n')
for side,S in (('Right','R'),('Left','L')):
    a(f'---\n\n## {side} arm\n')
    a(f'### {side} shells (13) — lightweight PLA\n')
    a('| ☐ | # | Picture | File | What it is | Size (mm) | Printer |')
    a('|---|---|---|---|---|---|---|')
    for n,nm,v,desc in shells:
        b=f'{S}_{n}_{nm}_{v}'
        a(f'| ☐ | {n} | {img(b)} | `{b}` | {desc} | {size(b)} | {printer.get(n,"X1C")} |')
    a(f'\n### {side} inserts (5)\n')
    a('| ☐ | Picture | File | What it is | Size (mm) | Material | Printer |')
    a('|---|---|---|---|---|---|---|')
    for nm,desc,mat,pr in inserts:
        b=f'{S}_{nm}'
        a(f'| ☐ | {img(b,130)} | `{b}` | {desc} | {size(b)} | {mat} | {pr} |')
    a(f'\n### {side} handle and hardware\n')
    a('| ☐ | Picture | Item | Qty | Notes |')
    a('|---|---|---|---|---|')
    a(f'| ☐ | {img("Handle_OnePiece_18p8x250",130)} | Handle: `Handle_OnePiece_18p8x250` **or** 18 mm beech rod cut to 250 mm | 1 | Standard PLA/PETG, not LW-PLA. Fit into shells 10 + 11 **before** joining them |')
    a('| ☐ | | Wooden dowels 6 × 30 mm | 57 | Holes are 6.4 mm; test fit in 07/09 first |')
    a('| ☐ | | Adafruit Sparkle Motion Mini | 1 | LED controller (USB-C) |')
    a('| ☐ | | BTF 5 mm 160/m strip, 91 LEDs (ring 55 + hand 36) | ≈ 0.57 m | Cut on the copper pads only |')
    a('| ☐ | | JST-SM 3-pin pigtail (strip → board) | 1 | Red → 5V, green → 32, white → G |')
    a('| ☐ | | 12 × 12 mm tactile buttons + caps | 2 | GPIO 14 and 27 to G |')
    a('| ☐ | | USB-C power bank + short USB-C cable | 1 each | |')
    a('| ☐ | | 24 AWG silicone wire, heat shrink | — | Shared stock |')
    a(f'| ☐ | {img("Button_Pod_Handle_Clip_2x_12mm_tact_CONCEPT",110)} | Button pod (`Button_Pod_Handle_Clip_2x_12mm_tact_CONCEPT`) | 1 | **Concept**: print only once the buttons are here, and check the fit |')
    a(f'| ☐ | {img("Electronics_Sled_80x45_CONCEPT",110)} | Electronics sled (`Electronics_Sled_80x45_CONCEPT`) | 1 | **Don\'t print yet.** It was sized for the old board and needs redoing for the 32 × 20 mm Sparkle Motion Mini |')
    a('')
a('---\n\n## Shared / already done\n')
a('| ☐ | Item | Notes |')
a('|---|---|---|')
a('| ☑ | `T2_Knuckle_Slot_Forefinger_Coupon` | Printed, finger fits (2026-11-18). Test piece only |')
a('| ☐ | Fingers (stock model, both hands) | Printed separately; not part of this pack |')
a('| ☐ | 2-part epoxy (UHU Plus Schnellfest ×2) | Dowels and seams |')
a('| ☐ | UHU Poly Max (clear) | Covers, lenses, electronics. No super glue near clear parts |')
a('\n*Generated 2026-11-21 by Claude from the V5 print pack files. Renders by `Build_Scripts/inventory_render.py`.*')
open('Inventory/V5_Parts_Inventory.md','w').write('\n'.join(L)+'\n')
