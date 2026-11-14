import sys, numpy as np, trimesh, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
def load(p):
    d = np.load(p); return trimesh.Trimesh(d['v'], d['f'], process=False), d
full, _ = load('out/fullR.npz'); tog, td = load('out/together.npz')
def segs(m, origin, normal, axes):
    s = trimesh.intersections.mesh_plane(m, normal, origin)
    return s[:, :, axes] if len(s) else np.zeros((0,2,2))
cuts = [('Z',z) for z in (40,100,145,200,260,310,350,376,400,440,480,520,560,590)] + [('X',x) for x in (211,150,280)] + [('Y',y) for y in (130,155,200,240)]
fig, axs = plt.subplots(4, 6, figsize=(36, 24)); axs = axs.ravel()
for ax, (a, val) in zip(axs, cuts):
    n = {'X':[1,0,0],'Y':[0,1,0],'Z':[0,0,1]}[a]; o = np.array(n, float)*val
    axes = {'X':[1,2],'Y':[0,2],'Z':[0,1]}[a]
    ax.add_collection(LineCollection(segs(tog, o, n, axes), colors='tab:orange', linewidths=0.5))
    ax.add_collection(LineCollection(segs(full, o, n, axes), colors='k', linewidths=0.8))
    ax.set_title(f'{a}={val}  black=Full_Arm_Right  orange=Together', fontsize=11); ax.autoscale(); ax.set_aspect('equal'); ax.grid(alpha=.3)
for ax in axs[len(cuts):]: ax.axis('off')
plt.tight_layout(); plt.savefig('out/sections_full_vs_together.png', dpi=60)
