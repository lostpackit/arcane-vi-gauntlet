"""Digital assembly simulation from the files in the repo (not from builder variables)."""
import sys; sys.path.insert(0, '/home/claude/scripts')
import numpy as np, trimesh, glob, json, os, manifold3d as m3, itertools
from scipy.spatial import cKDTree
from v5_lib import *
REL = '/home/claude/arcane-vi-gauntlet/releases/v5/Vi_Gauntlet_X1C_V5_Draft'; res = {}
def Rm(ax, deg): return trimesh.transformations.rotation_matrix(np.radians(deg), {'X': [1,0,0], 'Y': [0,1,0], 'Z': [0,0,1]}[ax])[:3, :3]
def rot_for(i, name):
    if i <= 4: return Rm('X', 180)
    if i <= 6: return Rm('X', -90)
    if i <= 9: return Rm('X', 90)
    if i <= 11: return np.eye(3)
    return Rm('Y', 90 if 'Left' in name else -90)
shells = {}; dev = {}
files = [f for f in sorted(glob.glob(REL + '/Right_Shells/*.3mf')) if '/R_08_' not in f] + glob.glob('/home/claude/v52/build/Right_Shells/R_08_*.3mf')
for f in sorted(files, key=os.path.basename):
    b = os.path.basename(f); i = int(b[2:4]); m = trimesh.load(f, force='mesh', process=False)
    ref = np.load(f"/home/claude/out/{'v52' if '_V5_2' in b else 'v51' if '_V5_1' in b else 'v5'}_asm_{i:02d}.npz")
    w = m.vertices @ rot_for(i, b); w = w + (ref['v'].min(0) - w.min(0))
    d = cKDTree(ref['v']).query(w)[0].max(); dev[i] = round(float(d), 4)
    shells[i] = to_m(w, m.faces); assert shells[i].status() == m3.Error.NoError, b
print('repo shells loaded:', len(shells), '| max deviation of repo file from verified build (mm):', max(dev.values())); res['repo_vs_build_max_dev_mm'] = max(dev.values())
vol = {i: s.volume() for i, s in shells.items()}
inter = {}
for a, b in itertools.combinations(sorted(shells), 2):
    v = (shells[a] ^ shells[b]).volume()
    if v > 0.01: inter[f'{a}-{b}'] = round(v, 2)
U = m3.Manifold.batch_boolean(list(shells.values()), m3.OpType.Add)
print('shell-shell interference pairs (mm3):', inter or 'none'); print('sum of shell volumes cm3 %.2f | union volume cm3 %.2f | bodies in union %d' % (sum(vol.values())/1000, U.volume()/1000, len([p for p in U.decompose() if p.volume() > 1])))
res['shell_interference'] = inter; res['union_bodies'] = len([p for p in U.decompose() if p.volume() > 1])
tU = to_tm(U)
# ---- inserts as designed positions
rf = np.load('/home/claude/out/ringframe.npz'); n, c, u, w = rf['n'], rf['c'], rf['u'], rf['w']
log = json.load(open(REL + '/V5_1_build_log.json')); F = log['lens_frame']; lc = np.array(F['centre']); eL = np.array(F['along']); eW = np.array(F['across']); eN = np.array(F['outward']); lmin, lmax = F['lmin'], F['lmax']
cover = from_tm(trimesh.load('/home/claude/out/cover_assembled.stl', force='mesh')).translate(tuple(-n * 0.25))   # measured seat: 0.25 mm below modelled height
gauge = (from_tm(part3mf('Pressure.stl', 46)) + from_tm(comp_tm(45))).translate(tuple(-n * 0.25)); crystal = from_tm(comp_tm(50)); lens = from_tm(comp_tm(10))
def box_l(l0, l1):
    bx = trimesh.creation.box(extents=[l1 - l0, 40, 40]); bx.apply_translation([(l0 + l1) / 2, 0, 0]); T = np.eye(4); T[:3, 0] = eL; T[:3, 1] = eW; T[:3, 2] = eN; T[:3, 3] = lc; bx.apply_transform(T); return from_tm(bx)
segs = log['lens_exposed_segments_mm_from_ring_end'][:2]
lensA = lens ^ box_l(lmin + segs[0][0] + 0.3, lmin + segs[0][1] - 0.3); lensB = lens ^ box_l(lmin + segs[1][0] + 0.3, lmin + segs[1][1] - 0.3)
handle = m3.Manifold.cylinder(250.0, 9.4, 9.4, 96).rotate((0, 90, 0)).translate((86.0, 156.0, 375.95))
parts = {'cover': cover, 'gauge': gauge, 'crystal': crystal, 'lens A': lensA, 'lens B': lensB, 'handle': handle}
# LED strip solids
angs = np.radians(np.arange(0, 360, 3)); dirs = np.array([np.cos(a_) * u + np.sin(a_) * w for a_ in angs]); o0 = np.tile(c + n * 2.0, (len(angs), 1))
loc, ir, _ = tU.ray.intersects_location(o0, dirs, multiple_hits=True); tt = ((loc - o0[ir]) * dirs[ir]).sum(1); rad = np.full(len(angs), np.nan)
for k in range(len(angs)):
    s_ = np.sort(tt[ir == k]); s_ = s_[s_ > 40]
    if len(s_) and s_[0] < 60: rad[k] = s_[0]
okm = np.isfinite(rad); Amat = np.c_[np.cos(angs[okm]), np.sin(angs[okm]), np.ones(okm.sum())]; sol_, *_ = np.linalg.lstsq(Amat, rad[okm], rcond=None); du, dw_, R0 = sol_
print('trough outer wall fit: radius %.2f mm, true axis offset from COM (u,w) = (%.2f, %.2f) mm, residual max %.2f mm' % (R0, du, dw_, np.abs(Amat @ sol_ - rad[okm]).max())); res['trough_outer_radius_fit_mm'] = round(float(R0), 2)
ring_strip = trimesh.creation.annulus(r_min=R0 - 0.2 - 2.2, r_max=R0 - 0.2, height=7.2, sections=180); ring_strip.apply_translation([du, dw_, -3.5 + 0.3 + 3.6])
wedge = trimesh.creation.box(extents=[16, 30, 20]); wedge.apply_translation([du, dw_ - R0, 0])     # joint gap at the notch (270 deg)
ring_strip = to_tm(from_tm(ring_strip) - from_tm(wedge))
Mr = np.eye(4); Mr[:3, 0] = u; Mr[:3, 1] = w; Mr[:3, 2] = n; Mr[:3, 3] = c; ring_strip.apply_transform(Mr); parts['LED strip, ring (7.2 x 2.2 mm band on outer wall)'] = from_tm(ring_strip)
lv = comp_tm(10).vertices; n_in = ((lv - lc) @ eN).min(); wc = (np.array([210.75, 0, 0]) - lc) @ eW
hs = trimesh.creation.box(extents=[229.2, 7.2, 2.2]); hs.apply_translation([(lmin + lmax) / 2, wc, n_in - 4.2 + 1.1 + 0.05]); T = np.eye(4); T[:3, 0] = eL; T[:3, 1] = eW; T[:3, 2] = eN; T[:3, 3] = lc; hs.apply_transform(T); parts['LED strip, hand (33 LEDs, 229 x 7.2 x 2.2 mm in channel)'] = from_tm(hs)
dw = []
rot = {0: (0, 90, 0), 1: (-90, 0, 0), 2: (0, 0, 0)}
for q in log['dowels']: dw.append(m3.Manifold.cylinder(30.0, 3.0, 3.0, 48).translate((0, 0, -15)).rotate(rot['XYZ'.index(q['axis'])]).translate(tuple(q['point'])))
parts['57 dowels 6 x 30 mm'] = m3.Manifold.batch_boolean(dw, m3.OpType.Add)
print('insert / hardware interference with the assembled shells:'); res['parts'] = {}
for nm, P in parts.items():
    v = (U ^ P).volume(); g = U.min_gap(P, 3.0)
    res['parts'][nm] = dict(interference_mm3=round(v, 2), volume_cm3=round(P.volume()/1000, 2), min_gap_to_shells_mm=round(float(g), 2))
    print(f'  {nm}: interference {v:.2f} mm3; minimum gap to shells {g:.2f} mm (search limit 3 mm)')
names = list(parts); pp = {}
for a, b in itertools.combinations(names, 2):
    v = (parts[a] ^ parts[b]).volume()
    if v > 0.01: pp[f'{a} | {b}'] = round(v, 2)
print('part-part interference:', pp or 'none'); res['part_part_interference'] = pp
# dowel engagement per side
short = []
for q in log['dowels']:
    ax = 'XYZ'.index(q['axis']); p = np.array(q['point']); e = np.eye(3)[ax]
    for sgn in (-1, 1):
        t = tU.ray.intersects_location(np.array([p + e * sgn * 0.5]), np.array([e * sgn]), multiple_hits=False)[0]
        depth = abs((t[0] - p) @ e) if len(t) else np.inf
        if depth < 15.0: short.append((q['shells'], round(float(depth), 1)))
print('dowel sockets shallower than 15 mm on a side:', short or 'none'); res['short_dowel_sockets'] = short
# clearances LED to cover / lens
g = cover.min_gap(parts['LED strip, ring (7.2 x 2.2 mm band on outer wall)'], 10.0); print('ring strip to cover: min gap %.2f mm' % g); res['ring_strip_to_cover_min_gap_mm'] = round(float(g), 2)
g = lensA.min_gap(parts['LED strip, hand (33 LEDs, 229 x 7.2 x 2.2 mm in channel)'], 10.0); print('hand strip to lens A: min gap %.2f mm' % g); res['hand_strip_to_lens_min_gap_mm'] = round(float(g), 2)
json.dump(res, open('/home/claude/out/assembly_sim.json', 'w'), indent=1, default=str)
