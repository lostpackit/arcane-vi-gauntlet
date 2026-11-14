import json, numpy as np, trimesh, sys
from scipy.spatial import cKDTree
objs = {o['name']: o for o in json.load(open('out/3mf_objects.json'))}
t = np.load('out/together.npz'); TV, TF, lab, lo, hi = t['v'], t['f'], t['lab'], t['lo'], t['hi']
full = None
def placed(name, comp, zalign='center'):
    d = np.load('out/cache3mf/'+objs[name]['files'][0].split('/')[-1]+'.npz'); m = trimesh.Trimesh(d['v'], d['f'], process=False)
    cm = (lo[comp]+hi[comp])/2; off = cm - (m.bounds[0]+m.bounds[1])/2
    if zalign == 'lo': off[2] = lo[comp][2] - m.bounds[0][2]
    if zalign == 'hi': off[2] = hi[comp][2] - m.bounds[1][2]
    m.apply_translation(off); return m
def cluster(pts, r=3.0):
    if not len(pts): return []
    tr = cKDTree(pts); import scipy.sparse.csgraph as cg
    g = tr.sparse_distance_matrix(tr, r, output_type='coo_matrix'); n, l = cg.connected_components(g, directed=False)
    out = []
    for k in range(n):
        p = pts[l==k]
        if len(p) >= 8: out.append((len(p), p.min(0).round(1).tolist(), p.max(0).round(1).tolist()))
    return sorted(out, key=lambda x:-x[0])
for name, comp in (('Fingers_Base.stl', 98), ('Glove_B1.stl', 81), ('Thumb_Base.stl', 168)):
    ref = trimesh.Trimesh(TV, TF[lab==comp], process=False)
    best = None
    for za in ('center','lo','hi'):
        m = placed(name, comp, za)
        p, fi = trimesh.sample.sample_surface(m, 40000, seed=1)
        _, d1, _ = trimesh.proximity.closest_point(ref, p)
        score = (d1 > 0.3).mean()
        if best is None or score < best[0]: best = (score, za, m, p, d1)
    score, za, m, p, d1 = best
    q, _ = trimesh.sample.sample_surface(ref, 40000, seed=2); _, d2, _ = trimesh.proximity.closest_point(m, q)
    print(f'=== {name}: 3MF vol {m.volume/1000:.2f} vs sizing-model comp {comp} vol {ref.volume/1000:.2f}; best z-align {za}')
    print(f' 3MF surface not present in sizing version (>0.3mm): {100*(d1>0.3).mean():.1f}% max {d1.max():.2f}')
    for c in cluster(p[d1>0.3])[:14]: print('   3MF-only feature cluster', c)
    print(f' sizing surface not present in 3MF version (>0.3mm): {100*(d2>0.3).mean():.1f}% max {d2.max():.2f}')
    for c in cluster(q[d2>0.3])[:14]: print('   sizing-only feature cluster', c)
    m.export(f'out/placed_{name}')
    np.savez(f'out/diff_{name}.npz', p3mf=p[d1>0.3], psz=q[d2>0.3])
