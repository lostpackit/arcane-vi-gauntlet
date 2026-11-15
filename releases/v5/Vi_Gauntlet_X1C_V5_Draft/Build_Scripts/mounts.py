"""Concept mounts for the LED hardware. Stand-alone printed parts; no shell changes."""
import sys; sys.path.insert(0, '/home/claude/scripts')
import numpy as np, trimesh, manifold3d as m3, json, os
from v5_lib import *
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True); spec = {}
C = m3.Manifold.cylinder; B = m3.Manifold.cube
# ---- 1. button pod: snap-on C-clip for the 18.8 mm handle + pad for two 12 x 12 mm tactile switches
HR, GAP, WALL, LEN = 9.4, 0.25, 2.8, 26.0
clip = C(LEN, HR + GAP + WALL, HR + GAP + WALL, 96) - C(LEN + 2, HR + GAP, HR + GAP, 96).translate((0, 0, -1))
mouth = B((40, 15.0, LEN + 2)).translate((-40, -7.5, -1))              # 15 mm snap opening on the -X side
clip = clip - mouth
PADW, PADT = 30.0, 9.0                                                   # tangential width, radial thickness
x0 = HR + GAP + WALL - 1.2
pad = B((PADT + 1.2, PADW, LEN)).translate((x0, -PADW / 2, 0))
SW, SWD = 12.5, 4.2                                                      # switch pocket (12 x 12 body + clearance), depth
pockets = []
for yc in (-7.45, 7.45):
    pockets.append(B((SWD + 0.1, SW, SW)).translate((x0 + PADT + 1.2 - SWD, yc - SW / 2, (LEN - SW) / 2)))       # open to the outer face
    pockets.append(B((PADT, 9.0, 3.0)).translate((x0 + 1.6, yc - 4.5, -1)).translate((0, 0, 0)))                    # lead/wire slot out the end face
    pockets.append(B((PADT - SWD - 1.4, 9.0, (LEN - SW) / 2 + 3.5)).translate((x0 + 1.6, yc - 4.5, -0.5)))          # joins pocket floor to the slot
pod = (clip + pad) - m3.Manifold.batch_boolean(pockets, m3.OpType.Add) - C(LEN + 2, HR + GAP, HR + GAP, 96).translate((0, 0, -1))
pod = pod.decompose(); pod.sort(key=lambda q: -q.volume()); pod = pod[0]
t = to_tm(pod); t.apply_translation([128 - (t.bounds[0][0] + t.bounds[1][0]) / 2, 128 - (t.bounds[0][1] + t.bounds[1][1]) / 2, -t.bounds[0][2]]); t.export(f'{OUT}/Button_Pod_Handle_Clip_2x_12mm_tact_CONCEPT.3mf')
spec['button_pod'] = dict(handle_d=18.8, clip_inner_d=2 * (HR + GAP), clip_wall=WALL, snap_opening=15.0, length=LEN, switch_pocket=[SW, SW, SWD], size=[round(float(x), 1) for x in t.extents], volume_cm3=round(pod.volume() / 1000, 2), watertight=bool(t.is_watertight))
# ---- 2. electronics sled: flat tray with rim, zip-tie slots, for controller + level shifter; fixes with hook-and-loop
L, W, T, RIM = 80.0, 45.0, 2.4, 5.0
sled = B((L, W, T)) + (B((L, W, T + RIM)) - B((L - 3.2, W - 3.2, RIM + 1)).translate((1.6, 1.6, T)))
cuts = []
for x in (10, 30, 50, 70):
    for y in (4.0, W - 7.0): cuts.append(B((6.0, 3.0, T + 2)).translate((x - 3, y, -1)))         # zip-tie slots
cuts.append(B((14.0, 3.2, RIM + 2)).translate((L / 2 - 7, -1, T)))                              # cable exits in the rim
cuts.append(B((14.0, 3.2, RIM + 2)).translate((L / 2 - 7, W - 2.2, T)))
cuts.append(B((3.2, 12.0, RIM + 2)).translate((-1, W / 2 - 6, T)))                              # USB access at one end
sled = sled - m3.Manifold.batch_boolean(cuts, m3.OpType.Add)
t2 = to_tm(sled); t2.apply_translation([128 - L / 2, 128 - W / 2, 0]); t2.export(f'{OUT}/Electronics_Sled_80x45_CONCEPT.3mf')
spec['electronics_sled'] = dict(size=[L, W, T + RIM], inner=[L - 3.2, W - 3.2], zip_slots=8, volume_cm3=round(sled.volume() / 1000, 2), watertight=bool(t2.is_watertight))
json.dump(spec, open(f'{OUT}/mounts_spec.json', 'w'), indent=1); print(json.dumps(spec, indent=1))
# fit checks
h = C(60, HR, HR, 96).translate((0, 0, -15)); print('pod vs handle interference mm3:', round((pod ^ h).volume(), 3), '| min gap', round(pod.min_gap(h, 3.0), 2))
sw = [B((12.0, 12.0, 12.0)).translate((x0 + PADT + 1.2 - SWD + 0.05, yc - 6.0, (LEN - 12.0) / 2)) for yc in (-7.45, 7.45)]
print('pod vs two 12x12 switch bodies interference mm3:', [round((pod ^ s_).volume(), 3) for s_ in sw], '| wall between pockets mm:', round(2 * 7.45 - SW, 2), '| wall under pocket to handle bore mm:', round(x0 + PADT + 1.2 - SWD - (HR + GAP), 2))
