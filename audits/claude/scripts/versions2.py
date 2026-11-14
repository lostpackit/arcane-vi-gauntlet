import json, numpy as np, trimesh, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from scipy.spatial import cKDTree
t = np.load('out/together.npz'); TV, TF, lab = t['v'], t['f'], t['lab']
d = np.load('out/fullR.npz'); full = trimesh.Trimesh(d['v'], d['f'], process=False)
res = {}
for name, comp in (('Fingers_Base.stl', 98), ('Glove_B1.stl', 81)):
    m = trimesh.load(f'out/placed_{name}', force='mesh'); ref = trimesh.Trimesh(TV, TF[lab==comp], process=False)
    p, _ = trimesh.sample.sample_surface(m, 6000, seed=3)
    q, _ = trimesh.sample.sample_surface(ref, 60000, seed=4); tr = cKDTree(q)
    T = np.zeros(3)
    for it in range(60):   # trimmed translation-only ICP
        dd, ii = tr.query(p + T); keep = dd < np.percentile(dd, 60)
        step = (q[ii[keep]] - (p[keep] + T)).mean(0); T += step
        if np.linalg.norm(step) < 1e-4: break
    m.apply_translation(T); print(name, 'ICP translation refine', T.round(3), 'median resid', np.median(tr.query(p+T)[0]).round(3))
    p2, _ = trimesh.sample.sample_surface(m, 40000, seed=5); _, d1, _ = trimesh.proximity.closest_point(ref, p2)
    print('  after refine: 3MF surface >0.3mm from sizing version: %.1f%%, >1mm: %.1f%%' % (100*(d1>0.3).mean(), 100*(d1>1).mean()))
    m.export(f'out/placed_{name}'); res[name] = m
def seg(m, n, o, axes):
    s = trimesh.intersections.mesh_plane(m, n, o); return s[:,:,axes] if len(s) else np.zeros((0,2,2))
fig, axs = plt.subplots(2, 3, figsize=(30, 18)); axs = axs.ravel()
views = [('Fingers_Base.stl','Z',545,[0,1]),('Fingers_Base.stl','Z',575,[0,1]),('Fingers_Base.stl','Y',150,[0,2]),('Glove_B1.stl','X',211,[1,2]),('Glove_B1.stl','Z',310,[0,1]),('Glove_B1.stl','Y',45,[0,2])]
for ax,(name,a,val,axes) in zip(axs,views):
    n = {'X':[1,0,0],'Y':[0,1,0],'Z':[0,0,1]}[a]; o = np.array(n,float)*val
    ax.add_collection(LineCollection(seg(full,n,o,axes), colors='k', linewidths=1.6))
    ax.add_collection(LineCollection(seg(res[name],n,o,axes), colors='tab:red', linewidths=0.9))
    b = res[name].bounds; ax.set_xlim(b[0][axes[0]]-8, b[1][axes[0]]+8); ax.set_ylim(b[0][axes[1]]-8, b[1][axes[1]]+8)
    ax.set_aspect('equal'); ax.grid(alpha=.4); ax.set_title(f'{a}={val}: black = Full_Arm_Right (V4 source), red = printable 3MF {name}', fontsize=13)
plt.tight_layout(); plt.savefig('out/version_diff_sections.png', dpi=60)
