import numpy as np, trimesh, json
d = np.load('out/fullR.npz'); full = trimesh.Trimesh(d['v'], d['f'], process=False)
t = np.load('out/together.npz'); TV, TF, lab, vols, lo, hi = t['v'], t['f'], t['lab'], t['vols'], t['lo'], t['hi']
objs = json.load(open('out/3mf_objects.json'))
rng = np.random.default_rng(0)
rows = []
for c in np.argsort(-np.abs(vols)):
    if abs(vols[c]) < 100: continue   # < 0.1 cm3
    fidx = np.where(lab == c)[0]
    tri = TV[TF[fidx]]
    # sample surface points
    k = min(400, len(fidx)); sel = rng.choice(len(fidx), k, replace=False)
    u = rng.random((k,2)); s = u.sum(1) > 1; u[s] = 1 - u[s]
    p = tri[sel,0] + u[:,:1]*(tri[sel,1]-tri[sel,0]) + u[:,1:]*(tri[sel,2]-tri[sel,0])
    cp, dist, _ = trimesh.proximity.closest_point(full, p)
    inside = full.contains(p)
    v = vols[c]/1000
    # match to 3MF object by volume
    best = min(objs, key=lambda o: abs(o['volume_cm3'] - v))
    match = best['name'] if abs(best['volume_cm3'] - v) < max(0.03, 0.002*v) else '?'
    rows.append(dict(comp=int(c), vol_cm3=round(float(v),2), lo=np.round(lo[c],1).tolist(), hi=np.round(hi[c],1).tolist(), on_surface_pct=round(float((dist<0.15).mean()*100),1), inside_pct=round(float(inside.mean()*100),1), median_dist=round(float(np.median(dist)),2), name3mf=match))
    r = rows[-1]; print(f"{r['comp']:4d} {r['vol_cm3']:9.2f} surf%{r['on_surface_pct']:6.1f} in%{r['inside_pct']:6.1f} med {r['median_dist']:7.2f} {r['name3mf']:28s} lo {r['lo']} hi {r['hi']}", flush=True)
json.dump(rows, open('out/containment.json','w'), indent=1)
