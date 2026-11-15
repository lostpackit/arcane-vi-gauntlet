import sys; sys.path.insert(0,'/home/claude/scripts')
import numpy as np, trimesh, json, warnings; warnings.filterwarnings('ignore')
from v5_lib import *
t = tog(); lo, hi, vols = t['lo'], t['hi'], t['vols']
K = trimesh.util.concatenate([trimesh.Trimesh(np.load(f'/home/claude/out/v51_asm_{i}.npz')['v'], np.load(f'/home/claude/out/v51_asm_{i}.npz')['f'], process=False) for i in (11, 13)])
objs = json.load(open('/home/claude/out/3mf_objects.json'))
print('3MF thumb objects:', [(o['name'], o['volume_cm3']) for o in objs if 'humb' in o['name']])
sel = [c for c in range(len(vols)) if abs(vols[c]) > 3000 and hi[c][0] > 350 and lo[c][0] > 300 and lo[c][2] > 400 and lo[c][2] < 560]
print('candidate comps', len(sel)); res = []
for c in sorted(sel, key=lambda c: lo[c][2]):
    v = vols[c]/1000; best = min(objs, key=lambda o: abs(o['volume_cm3']-v)); nm = best['name'][:-4] if abs(best['volume_cm3']-v) < max(0.03, 0.002*v) else '(no exact 3MF match)'
    tm = comp_tm(c); p, _ = trimesh.sample.sample_surface(tm, 4000, seed=7); ins = K.contains(p); _, dist, _ = trimesh.proximity.closest_point(K, p)
    r = dict(comp=int(c), part=nm, volume_cm3=round(float(v),2), lo=lo[c].round(1).tolist(), hi=hi[c].round(1).tolist(), inside_pct=round(100*float(ins.mean()),1), max_penetration_mm=round(float(dist[ins].max()),2) if ins.any() else 0.0, touching_pct=round(100*float((dist[~ins]<0.2).mean()),1), min_gap_mm=round(float(dist[~ins].min()),2))
    res.append(r); print(r, flush=True)
json.dump(res, open('/home/claude/out/thumb_fit.json','w'), indent=1)
