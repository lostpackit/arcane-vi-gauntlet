import sys; sys.path.insert(0, '/home/claude/scripts')
import numpy as np, trimesh, json
from v5_lib import *
t = tog(); lo, hi, vols = t['lo'], t['hi'], t['vols']
K = trimesh.util.concatenate([trimesh.Trimesh(np.load(f'/home/claude/out/v51_asm_{i}.npz')['v'], np.load(f'/home/claude/out/v51_asm_{i}.npz')['f'], process=False) for i in (12, 13)])
fb3 = trimesh.load('/home/claude/out/placed_Fingers_Base.stl', force='mesh')
objs = json.load(open('/home/claude/out/3mf_objects.json')); res = []
cols = {'little': (80, 150), 'ring': (150, 212), 'middle': (212, 277), 'fore': (277, 350)}
def test(tm, body, zmax=None):
    p, _ = trimesh.sample.sample_surface(tm, 6000, seed=5)
    if zmax: p = p[p[:, 2] < zmax]
    ins = body.contains(p); _, dist, _ = trimesh.proximity.closest_point(body, p)
    pen = dist[ins]; out = dist[~ins]
    return dict(points=len(p), inside_pct=round(100 * float(ins.mean()), 1), max_penetration_mm=round(float(pen.max()), 2) if len(pen) else 0.0, p95_penetration_mm=round(float(np.percentile(pen, 95)), 2) if len(pen) else 0.0, touching_pct=round(100 * float((out < 0.15).mean()), 1) if len(out) else 0.0, near_gap_median_mm=round(float(np.median(out[out < 3])), 2) if (out < 3).any() else None)
for fname, (x0, x1) in cols.items():
    sel = [c for c in range(len(vols)) if abs(vols[c]) > 3000 and x0 < (lo[c][0] + hi[c][0]) / 2 < x1 and hi[c][2] > 505 and 500 < lo[c][2] < 600 and hi[c][0] - lo[c][0] < 80]
    for c in sorted(sel, key=lambda c: lo[c][2]):
        v = vols[c] / 1000; best = min(objs, key=lambda o: abs(o['volume_cm3'] - v)); nm = best['name'][:-4] if abs(best['volume_cm3'] - v) < max(0.03, 0.002 * v) else ('finger core segment 1' if v > 100 else 'armor plate (older rev)')
        if 'Knot' in nm: continue
        tm = comp_tm(c); a = test(tm, K, zmax=605); b = test(tm, fb3, zmax=605)
        res.append(dict(finger=fname, comp=int(c), part=nm, volume_cm3=round(v, 2), vs_V5_1_knuckle_shells=a, vs_3MF_Fingers_Base=b))
        print(f"{fname:6s} {nm:26s} Z {lo[c][2]:.0f}-{hi[c][2]:.0f} | V5.1 shells: inside {a['inside_pct']:5.1f}% maxpen {a['max_penetration_mm']:.2f} p95 {a['p95_penetration_mm']:.2f} touching {a['touching_pct']:5.1f}% near-gap med {a['near_gap_median_mm']} | 3MF base: inside {b['inside_pct']:5.1f}% maxpen {b['max_penetration_mm']:.2f} p95 {b['p95_penetration_mm']:.2f}", flush=True)
json.dump(res, open('/home/claude/out/finger_fit.json', 'w'), indent=1)
