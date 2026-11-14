import numpy as np, trimesh
rf = np.load('out/ringframe.npz'); n, c, u, w = rf['n'], rf['c'], rf['u'], rf['w']
oc = trimesh.load('out/cover_assembled.stl', force='mesh')
s8 = np.load('out/asm_R_08.npz'); shell = trimesh.Trimesh(s8['v'], s8['f'], process=False)
t = np.load('out/together.npz'); TV, TF, lab = t['v'], t['f'], t['lab']
pts = trimesh.sample.volume_mesh(oc, 6000)
ins = shell.contains(pts)
print('cover volume sample pts', len(pts), 'fraction inside V4 shell 08 solid: %.3f' % ins.mean())
r = np.linalg.norm((pts-c) - ((pts-c)@n)[:,None]*n, axis=1); h = (pts-c)@n
for a,b in ((0,13),(13,29),(29,56),(56,60)):
    s = (r>=a)&(r<b); print(f'  r {a}-{b}: n={s.sum()} inside {ins[s].mean():.3f}  h range {h[s].min():.2f}..{h[s].max():.2f}')
# what is directly above the chamber? axial column at r=42: list all surface crossings
def P(r, ang, hh): a = np.radians(ang); return c + r*(np.cos(a)*u + np.sin(a)*w) + hh*n
for ang in (0, 45, 90, 135, 180, 225, 315):
    for rr in (42, 20, 5):
        o = P(rr, ang, 60)[None]; loc, ir, _ = shell.ray.intersects_location(o, -n[None], multiple_hits=True)
        hs = np.sort(60 - ((loc-o)*(-n)).sum(1))[::-1]
        print(f'  shell column r={rr} ang={ang}: surface crossings h =', np.round(hs[hs>-12],2).tolist())
# Pressure component (46) and top plates: do they have openings above trough?
pr = trimesh.Trimesh(TV, TF[lab==46], process=False)
for ang in (0, 90, 180):
    o = P(42, ang, 60)[None]; loc, ir, _ = pr.ray.intersects_location(o, -n[None], multiple_hits=True)
    print('  Pressure part column r=42 ang', ang, np.round(np.sort(60 - ((loc-o)*(-n)).sum(1))[::-1],2).tolist())
# cover dims
rc = np.linalg.norm((oc.vertices-c) - ((oc.vertices-c)@n)[:,None]*n, axis=1); hc = (oc.vertices-c)@n
cc = oc.center_mass; rc2 = np.linalg.norm((oc.vertices-cc) - ((oc.vertices-cc)@n)[:,None]*n, axis=1)
print('cover: h range', hc.min().round(2), hc.max().round(2), 'max radius about own axis', rc2.max().round(3), 'radius p99', np.percentile(rc2,99).round(3))
