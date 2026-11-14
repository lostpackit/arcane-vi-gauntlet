import numpy as np, trimesh, matplotlib, json
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
t = np.load('out/together.npz'); lo, hi = t['lo'], t['hi']
ol = trimesh.load('cad/originals/Circle_Light.stl', force='mesh', process=False); ol.merge_vertices()
oc = trimesh.load('cad/originals/Circle_Light_Cover.stl', force='mesh', process=False); oc.merge_vertices()
ol.apply_translation(lo[49] - ol.bounds[0]); oc.apply_translation(lo[48] - oc.bounds[0])
print('placement residual light', np.abs(ol.bounds[1]-hi[49]).max().round(3), 'cover', np.abs(oc.bounds[1]-hi[48]).max().round(3))
s8 = np.load('out/asm_R_08.npz'); shell = trimesh.Trimesh(s8['v'], s8['f'], process=False)
n = ol.principal_inertia_vectors[np.argmax(ol.principal_inertia_components)]; n = n*np.sign(n[1])
c = ol.center_mass
# cover axis
nc = oc.principal_inertia_vectors[np.argmax(oc.principal_inertia_components)]; nc = nc*np.sign(nc[1])
print('ring axis', n.round(4), 'cover axis', nc.round(4), 'angle between deg', round(float(np.degrees(np.arccos(min(1,abs(n@nc))))),3))
print('ring COM', c.round(2), 'cover COM', oc.center_mass.round(2), 'cover COM radial offset from ring axis', round(float(np.linalg.norm((oc.center_mass-c) - ((oc.center_mass-c)@n)*n)),3))
u = np.cross(n, [0,0,1]); u /= np.linalg.norm(u); w = np.cross(n, u)
def prof(m, ang):
    a = np.radians(ang); d = np.cos(a)*u + np.sin(a)*w; nr = np.cross(n, d)
    s = trimesh.intersections.mesh_plane(m, nr, c)
    if not len(s): return np.zeros((0,2,2))
    return np.stack([(s-c)@d, (s-c)@n], -1)
fig, axs = plt.subplots(3, 2, figsize=(24, 21))
for ax, ang in zip(axs.ravel(), (0, 30, 60, 90, 120, 150)):
    for m, col, lw in ((shell,'k',1.4), (oc,'tab:blue',1.0), (ol,'tab:orange',0.6)):
        ax.add_collection(LineCollection(prof(m, ang), colors=col, linewidths=lw))
    ax.set_xlim(-70, 70); ax.set_ylim(-16, 16); ax.set_aspect('equal'); ax.set_xticks(np.arange(-70, 71, 5)); ax.set_yticks(np.arange(-16, 17, 1)); ax.grid(alpha=.4)
    ax.set_title(f'Ring-frame radial section {ang} deg: black=V4 shell 08, blue=cover (as placed in sizing model), orange=original Circle_Light. r vs axial h (mm, 0 = ring centre of mass)')
plt.tight_layout(); plt.savefig('out/led_ring_profile_ringframe.png', dpi=70)
# numeric: collect distinct vertices of the light profile at several angles
for ang in (0, 90):
    p = prof(ol, ang).reshape(-1,2); p = p[p[:,0]>0]
    key = np.unique(np.round(p,2), axis=0)
    print('light profile verts ang', ang, len(key)); 
    # cluster into corner list sorted by r
    for q in key[np.argsort(key[:,0])][:400:1]:
        pass
    np.save(f'out/light_prof_{ang}.npy', key)
    p = prof(oc, ang).reshape(-1,2); p = p[p[:,0]>0]; np.save(f'out/cover_prof_{ang}.npy', np.unique(np.round(p,2), axis=0))
    p = prof(shell, ang).reshape(-1,2); p = p[p[:,0]>0]; np.save(f'out/shell_prof_{ang}.npy', np.unique(np.round(p,2), axis=0))
np.savez('out/ringframe.npz', n=n, c=c, u=u, w=w)
oc.export('out/cover_assembled.stl'); ol.export('out/light_assembled.stl')
