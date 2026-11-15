import sys; sys.path.insert(0, '/home/claude/scripts')
import numpy as np, trimesh, glob, os, json, csv, subprocess, re, manifold3d as m3
from v5_lib import *
OUT = sys.argv[1]; V5 = '/home/claude/arcane-vi-gauntlet/releases/v5/Vi_Gauntlet_X1C_V5_Draft'; res = {}
def info(f):
    o = subprocess.run(['prusa-slicer', '--info', f], capture_output=True, text=True).stdout
    g = lambda k: (re.search(k + r' = +(\S+)', o) or [None, ''])[1]; return g('manifold'), g('number_of_parts')
old = {r['file']: r for r in csv.DictReader(open(V5 + '/V5_Geometry_Check.csv'))}
rows = []; changed = []
for f in sorted(glob.glob(OUT + '/*/*.3mf')):
    m = trimesh.load(f, force='mesh', process=False); e = m.edges_sorted; _, cnt = np.unique(e, axis=0, return_counts=True); man, parts = info(f)
    rel = os.path.relpath(f, OUT); prev = old.get(rel.replace('_V5_1', '_V5'))
    dv = round(float(m.volume)/1000 - float(prev['volume_cm3']), 2) if prev else None
    rows.append(dict(file=rel, triangles=len(m.faces), size_x=round(float(m.extents[0]), 2), size_y=round(float(m.extents[1]), 2), size_z=round(float(m.extents[2]), 2), volume_cm3=round(float(m.volume)/1000, 2),
        watertight=bool(m.is_watertight), winding_ok=bool(m.is_winding_consistent), boundary_edges=int((cnt == 1).sum()), nonmanifold_edges=int((cnt > 2).sum()), slicer_manifold=man, slicer_parts=parts,
        fits_X1C=bool(m.extents[0] <= 252 and m.extents[1] <= 240 and m.extents[2] <= 250), volume_change_vs_V5_cm3=dv))
    if dv is None or abs(dv) > 0.005: changed.append((rel, dv))
w = csv.DictWriter(open(OUT + '/V5_1_Geometry_Check.csv', 'w', newline=''), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
bad = [r['file'] for r in rows if not (r['watertight'] and r['winding_ok'] and r['boundary_edges'] == 0 and r['nonmanifold_edges'] == 0 and r['slicer_manifold'] == 'yes' and r['fits_X1C'])]
print('files', len(rows), 'failing closed-solid/envelope:', bad); print('changed vs V5 (or new):'); [print('   ', c) for c in changed if '/L_' not in c[0] and 'Left' not in c[0]]
res['failing'] = bad; res['changed_vs_V5'] = changed
from scipy.spatial import cKDTree
md = 0
for r in sorted(glob.glob(OUT + '/Right_Shells/*.3mf')):
    a = trimesh.load(r, force='mesh', process=False).triangles.copy(); b = trimesh.load(r.replace('Right_Shells/R_', 'Left_Shells/L_'), force='mesh', process=False).triangles.copy(); b[..., 0] *= -1
    ca = a.mean(1) - a.reshape(-1, 3).min(0); cb = b.mean(1) - b.reshape(-1, 3).min(0); md = max(md, cKDTree(cb).query(ca)[0].max(), cKDTree(ca).query(cb)[0].max())
print('left = mirror(right) max dev mm', round(md, 4)); res['mirror_max_dev_mm'] = round(float(md), 4)
d = np.load('/home/claude/out/v51_arm.npz'); A = to_m(d['v'], d['f']); tA = to_tm(A)
log = json.load(open(OUT + '/V5_build_log.json')); F = log['lens_frame']; lc = np.array(F['centre']); eL = np.array(F['along']); eW = np.array(F['across']); eN = np.array(F['outward']); lmin, lmax = F['lmin'], F['lmax']
lens = from_tm(comp_tm(10)); crystal = from_tm(comp_tm(50)); lv = comp_tm(10).vertices; pn = (lv - lc) @ eN; n_in, n_out = pn.min(), pn.max()
wc = (np.array([210.75, 0, 0]) - lc) @ eW
for nm, T in (('lens', lens), ('crystal', crystal)):
    v = [round((A ^ T.translate(tuple(eN * dd))).volume(), 2) for dd in (0, 1, 3, 6, 12, 25)]; print(f'  {nm}: overlap with V5.1 arm (mm3) seated and lifted 1/3/6/12/25 mm outward: {v}'); res[nm + '_lift_overlap_mm3'] = v
print('  (lens lift overlap is expected to be non-zero where the top plate and crystal base bridge over it; segments A and B are checked separately below)')
def box(l0, l1):
    bx = trimesh.creation.box(extents=[l1 - l0, 40, 40]); bx.apply_translation([(l0 + l1) / 2, 0, 0]); T = np.eye(4); T[:3, 0] = eL; T[:3, 1] = eW; T[:3, 2] = eN; T[:3, 3] = lc; bx.apply_transform(T); return from_tm(bx)
for k, (a_, b_) in enumerate(log['lens_exposed_segments_mm_from_ring_end'][:2]):
    seg = lens ^ box(lmin + a_ + 0.3, lmin + b_ - 0.3); v = [round((A ^ seg.translate(tuple(eN * dd))).volume(), 2) for dd in (0, 1, 3, 6, 12)]
    print(f'  lens segment {chr(65+k)} ({a_}-{b_} mm from ring end, Z {286+a_*eL[2]:.0f}-{286+b_*eL[2]:.0f}): overlap seated/lifted {v}'); res[f'lens_{chr(65+k)}_lift_overlap_mm3'] = v
def ray(o, dd):
    loc, _, _ = tA.ray.intersects_location(np.array([o]), np.array([dd]), multiple_hits=True)
    t = np.sort(((loc - o) * dd).sum(1)); t = t[t > 1e-6]; return t
print('  channel profile (in lens frame; depth measured from lens underside):'); prof = []
for l in np.linspace(lmin + 8, lmax - 8, 12):
    o = lc + eL * l + eW * wc + eN * (n_in - 1.0)
    tw1 = ray(o, eW); tw2 = ray(o, -eW); td = ray(o, -eN)
    width = (tw1[0] + tw2[0]) if len(tw1) and len(tw2) else float('nan'); depth = 1.0 + td[0] if len(td) else float('nan'); wall = (td[1] - td[0]) if len(td) > 1 else float('nan')
    z = (o)[2]; prof.append((round(float(z), 0), round(float(width), 2), round(float(depth), 2), round(float(wall), 2))); print(f'    Z~{z:5.0f}: width {width:5.2f}  depth {depth:4.2f}  wall left to hand cavity {wall:4.2f}')
res['channel_profile_Z_width_depth_wall'] = prof
o = lc + eL * (lmin + 6) + eW * wc + eN * (n_in - 2.0); t = ray(o, eL); print('  straight clear run along channel from ring end (mm):', round(float(t[0]), 1) if len(t) else 'unobstructed', 'of', round(lmax - lmin - 12, 1)); res['channel_clear_run_mm'] = float(t[0]) if len(t) else None
t = ray(lc + eL * (lmin + 6) + eW * wc + eN * (n_in - 2.0), -eL); print('  from channel start toward the ring: clear distance before first wall (mm):', round(float(t[0]), 1) if len(t) else 'none')
# ledges for lens: ray down from lens underside near each edge
for side in (-1, 1):
    hits = []
    for l in np.linspace(lmin + 10, lmin + 75, 8):
        o = lc + eL * l + eW * (side * 6.0) + eN * (n_in + 0.5); td = ray(o, -eN); hits.append(td[0] - 0.5 if len(td) else np.nan)
    print(f'  lens ledge at {side*6.0:+.1f} mm from centre: gap under lens edge min {np.nanmin(hits):.2f} max {np.nanmax(hits):.2f} mm')
# crystal well: from channel under crystal, outward ray should exit freely through the crystal pocket
for z in (465, 480, 500):
    l = (z - lc[2]) / eL[2]; o = lc + eL * l + eW * wc + eN * (n_in - 2.0); t = ray(o, eN); print(f'  channel -> crystal pocket at Z~{z}: first obstruction outward at {t[0]:.1f} mm' if len(t) else f'  channel -> crystal pocket at Z~{z}: open to outside')
tc = to_tm(crystal); pts, fi = trimesh.sample.sample_surface(tc, 20000, seed=1); dn = tc.face_normals[fi] @ eN; under = pts[dn < -0.8]
loc, ir, _ = tA.ray.intersects_location(under + eN * 0.05, np.tile(-eN, (len(under), 1)), multiple_hits=False); gap = np.full(len(under), np.inf); gap[ir] = ((under[ir] - loc) * eN).sum(1)
print('  crystal underside resting on arm within 0.6 mm: fraction %.2f' % (gap < 0.6).mean()); res['crystal_seat_fraction'] = round(float((gap < 0.6).mean()), 3)
D = log['dowels']; rot = {0: (0, 90, 0), 1: (-90, 0, 0), 2: (0, 0, 0)}
cy = [m3.Manifold.cylinder(32.0, 3.2, 3.2, 48).translate((0, 0, -16)).rotate(rot['XYZ'.index(q['axis'])]).translate(tuple(q['point'])) for q in D]; thin = []
for q, c in zip(D, cy):
    fat = m3.Manifold.cylinder(34.0, 4.7, 4.7, 48).translate((0, 0, -17)).rotate(rot['XYZ'.index(q['axis'])]).translate(tuple(q['point'])); miss = (fat - c - A).volume() - sum((fat ^ o2).volume() for o2 in cy if o2 is not c)
    if miss > 1.0: thin.append((q['shells'], q['point'], round(miss, 1)))
old_d = json.load(open(V5 + '/V5_build_log.json'))['dowels']; print('  dowels', len(D), 'identical to V5:', D == old_d, '| thin-wall dowels:', thin); res['dowels_identical_to_V5'] = D == old_d; res['dowel_thin_wall'] = thin
json.dump(res, open(OUT + '/V5_1_Verification.json', 'w'), indent=1, default=str)
