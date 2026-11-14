import numpy as np, trimesh, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
t = np.load('out/together.npz'); TV, TF, lab, lo, hi = t['v'], t['f'], t['lab'], t['lo'], t['hi']
def comp(c): 
    f = TF[lab==c]; return trimesh.Trimesh(TV, f, process=False)
light = comp(49); cover = comp(48)
print('light bounds', light.bounds.round(2).tolist()); print('cover bounds', cover.bounds.round(2).tolist())
cx = (light.bounds[0,0]+light.bounds[1,0])/2; cz = (light.bounds[0,2]+light.bounds[1,2])/2
ccx = (cover.bounds[0,0]+cover.bounds[1,0])/2; ccz = (cover.bounds[0,2]+cover.bounds[1,2])/2
print('light centre x,z', round(cx,2), round(cz,2), 'cover centre', round(ccx,2), round(ccz,2))
s8 = np.load('out/asm_R_08.npz'); shell = trimesh.Trimesh(s8['v'], s8['f'], process=False)
# full-res originals
ol = trimesh.load('cad/originals/Circle_Light.stl', force='mesh'); oc = trimesh.load('cad/originals/Circle_Light_Cover.stl', force='mesh')
print('orig light bounds', ol.bounds.round(2).tolist(), 'orig cover', oc.bounds.round(2).tolist())
fig, axs = plt.subplots(2, 2, figsize=(22, 14))
for ax, ang in zip(axs.ravel(), (0, 45, 90, 135)):
    a = np.radians(ang); dirv = np.array([np.cos(a), 0, np.sin(a)]); nrm = np.array([-np.sin(a), 0, np.cos(a)])
    o = np.array([cx, 0, cz])
    for m, col, lw in ((shell,'k',1.0), (cover,'tab:blue',0.9), (light,'tab:orange',0.5)):
        s = trimesh.intersections.mesh_plane(m, nrm, o)
        if len(s):
            r = (s - o) @ dirv; y = s[:,:,1]
            ax.add_collection(LineCollection(np.stack([r, y], -1), colors=col, linewidths=lw))
    ax.set_xlim(-72, 72); ax.set_ylim(226, 262); ax.set_aspect('equal'); ax.set_xticks(np.arange(-70, 71, 5)); ax.set_yticks(np.arange(226, 263, 2)); ax.grid(alpha=.4)
    ax.set_title(f'Radial section through ring axis at {ang} deg (black = V4 shell 08, blue = cover, orange = original Circle_Light); r mm vs assembled Y mm')
plt.tight_layout(); plt.savefig('out/led_ring_profile.png', dpi=75)
np.savez('out/ring_center.npz', c=np.array([cx, cz]))
