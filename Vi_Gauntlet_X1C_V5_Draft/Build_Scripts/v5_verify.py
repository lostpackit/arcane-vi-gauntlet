"""Independent re-check of exported V5 files (reads the STL files, not the builder's variables)."""
import sys; sys.path.insert(0, '/home/claude/scripts')
import numpy as np, trimesh, glob, os, json, csv, manifold3d as m3
from v5_lib import *
OUT = sys.argv[1]; res = {}
rows = []
import subprocess, re
def info(f):
    o = subprocess.run(['prusa-slicer', '--info', f], capture_output=True, text=True).stdout
    g = lambda k: (re.search(k + r' = +(\S+)', o) or [None, ''])[1]
    return g('manifold'), g('number_of_parts'), g('open_edges') or '0'
for f in sorted(glob.glob(OUT + '/*/*.3mf')):
    m = trimesh.load(f, force='mesh', process=False)
    e = m.edges_sorted; _, cnt = np.unique(e, axis=0, return_counts=True); man, parts, oe = info(f)
    rows.append(dict(file=os.path.relpath(f, OUT), triangles=len(m.faces), size_x=round(float(m.extents[0]), 2), size_y=round(float(m.extents[1]), 2), size_z=round(float(m.extents[2]), 2), min_z=round(float(m.bounds[0][2]), 3),
        volume_cm3=round(float(m.volume)/1000, 2), watertight=bool(m.is_watertight), winding_ok=bool(m.is_winding_consistent), bodies=len(m.split(only_watertight=False)),
        boundary_edges=int((cnt == 1).sum()), nonmanifold_edges=int((cnt > 2).sum()), slicer_manifold=man, slicer_parts=parts, slicer_open_edges=oe,
        fits_X1C=bool(m.extents[0] <= 252 and m.extents[1] <= 240 and m.extents[2] <= 250), fits_A1mini=bool(m.extents[0] <= 180 and m.extents[1] <= 180 and m.extents[2] <= 180)))
w = csv.DictWriter(open(OUT + '/V5_Geometry_Check.csv', 'w', newline=''), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
bad = [(r['file'], r['bodies'], r['slicer_manifold'], r['slicer_parts']) for r in rows if not (r['watertight'] and r['winding_ok'] and r['boundary_edges'] == 0 and r['nonmanifold_edges'] == 0 and r['slicer_manifold'] == 'yes')]
print('files', len(rows), 'failing closed-solid checks:', bad); print('multi-body files:', [(r['file'], r['bodies'], r['slicer_parts']) for r in rows if r['bodies'] != 1 or r['slicer_parts'] != '1'])
print('not within X1C envelope:', [(r['file'], r['size_x'], r['size_y'], r['size_z']) for r in rows if not r['fits_X1C']]); print('fits A1 Mini:', [r['file'] for r in rows if r['fits_A1mini'] and 'Left' not in r['file'] and '/L_' not in r['file']])
res['files'] = len(rows); res['failing_closed_solid'] = bad
from scipy.spatial import cKDTree
md = 0
for r in sorted(glob.glob(OUT + '/Right_Shells/*.3mf')):
    a = trimesh.load(r, force='mesh', process=False).triangles.copy(); b = trimesh.load(r.replace('Right_Shells/R_', 'Left_Shells/L_'), force='mesh', process=False).triangles.copy(); b[..., 0] *= -1
    ca = a.mean(1) - a.reshape(-1, 3).min(0); cb = b.mean(1) - b.reshape(-1, 3).min(0); md = max(md, cKDTree(cb).query(ca)[0].max(), cKDTree(ca).query(cb)[0].max())
print('left = mirror(right): max centroid deviation mm', round(md, 4)); res['mirror_max_dev_mm'] = round(float(md), 4)
# ---- functional re-checks in assembled frame on the saved pre-rotation shells
rf = np.load('/home/claude/out/ringframe.npz'); n, c, u, wv = rf['n'], rf['c'], rf['u'], rf['w']
def P(r, ang, h): a = np.radians(ang); return c + r*(np.cos(a)*u + np.sin(a)*wv) + h*n
sh = {i: trimesh.Trimesh(**{k: np.load(f'/home/claude/out/v5_asm_{i:02d}.npz')[k2] for k, k2 in (('vertices', 'v'), ('faces', 'f'))}, process=False) for i in range(1, 14)}
s8 = sh[8]; angs = np.arange(0, 360, 5)
print('R_08 saved-vs-exported volume', round(s8.volume/1000, 2), [r['volume_cm3'] for r in rows if 'R_08' in r['file']])
out = {}
for r in (31, 36, 42, 48, 54):
    o = np.array([P(r, a, 60) for a in angs]); loc, ir, _ = s8.ray.intersects_location(o, np.tile(-n, (len(o), 1)), multiple_hits=True)
    t = ((loc - o[ir]) * (-n)).sum(1); first = np.full(len(o), np.inf); np.minimum.at(first, ir, t); h = 60 - first
    out[r] = (round(float(np.nanmin(h)), 2), round(float(np.median(h)), 2), round(float(np.max(h)), 2), int((h > -2.5).sum()))
    print(f'  V5 shell 08 top-down probe r={r}: first surface h min/med/max = {out[r][:3]}; angles (of {len(angs)}) where something sits above the trough floor: {out[r][3]}')
res['trough_topdown'] = out
A = to_m(np.load('/home/claude/out/v5_arm.npz')['v'], np.load('/home/claude/out/v5_arm.npz')['f'])
cover = from_tm(trimesh.load('/home/claude/out/cover_assembled.stl', force='mesh')); gauge = from_tm(part3mf('Pressure.stl', 46)) + from_tm(comp_tm(45)); handle_orig = from_tm(comp_tm(80))
for nm, T in (('cover', cover), ('gauge', gauge)):
    v = [round((A ^ T.translate(tuple(n*d))).volume(), 2) for d in (0, 1, 3, 6, 10, 20, 40)]
    print(f'  {nm}: overlap with V5 arm (mm3) when lifted 0/1/3/6/10/20/40 mm along ring axis: {v}'); res[nm + '_lift_overlap_mm3'] = v
# seat: how much of the cover's underside is supported (arm material within 0.6 mm below the cover)
tc = to_tm(cover); pts, fi = trimesh.sample.sample_surface(tc, 20000, seed=1); dn = tc.face_normals[fi] @ n
under = pts[dn < -0.9]; tA = to_tm(A)
loc, ir, _ = tA.ray.intersects_location(under + n*0.05, np.tile(-n, (len(under), 1)), multiple_hits=False)
gap = np.full(len(under), np.inf); gap[ir] = ((under[ir] - loc) * n).sum(1)
rr = np.linalg.norm((under - c) - ((under - c) @ n)[:, None]*n, axis=1)
print('  cover underside: fraction resting on arm within 0.6 mm: %.2f ; supported radii range %.1f-%.1f mm' % ((gap < 0.6).mean(), rr[gap < 0.6].min() if (gap < 0.6).any() else -1, rr[gap < 0.6].max() if (gap < 0.6).any() else -1))
res['cover_seat_fraction'] = round(float((gap < 0.6).mean()), 3)
# handle
hn = trimesh.load(OUT + '/Inserts/Handle_OnePiece_18p8x250.3mf', force='mesh'); print('  handle insert size', hn.extents.round(2), 'vol', round(hn.volume/1000, 2))
H = m3.Manifold.cylinder(250.0, 9.4, 9.4, 96).rotate((0, 90, 0)).translate((86.0, 156.0, 375.95))
print('  handle (as placed) overlap with V5 arm mm3:', round((A ^ H).volume(), 2), '| original handle volume left in arm mm3:', round((A ^ handle_orig).volume(), 2))
for d, x0 in (([-1.0, 0, 0], 100.0), ([1.0, 0, 0], 322.0)):
    for dy, dz in ((0, 0), (8, 0), (-8, 0), (0, 8), (0, -8)):
        loc, _, _ = tA.ray.intersects_location(np.array([[x0, 156.0 + dy, 375.95 + dz]]), [d], multiple_hits=True); xs = np.sort(loc[:, 0])[::int(d[0])]
        print(f'    socket dir {d[0]:+.0f} offset ({dy},{dz}): socket floor X={xs[0]:.1f}, wall behind it {abs(xs[1]-xs[0]):.1f} mm' if len(xs) > 1 else f'    socket dir {d[0]:+.0f} offset ({dy},{dz}): hits {xs.round(1).tolist()}')
# socket engagement: wall face positions along handle axis just outside the bar radius
for d, x0 in (([-1.0, 0, 0], 211.0), ([1.0, 0, 0], 211.0)):
    loc, _, _ = tA.ray.intersects_location(np.array([[x0, 156.0, 375.95 + 12.5]]), [d], multiple_hits=True); xs = np.sort(loc[:, 0])[::int(d[0])]
    print(f'    cavity wall face next to socket, dir {d[0]:+.0f}: X={xs[0]:.1f}')
# dowels
log = json.load(open(OUT + '/V5_build_log.json')); D = log['dowels']; rot = {0: (0, 90, 0), 1: (-90, 0, 0), 2: (0, 0, 0)}
cy = [m3.Manifold.cylinder(32.0, 3.2, 3.2, 48).translate((0, 0, -16)).rotate(rot['XYZ'.index(d['axis'])]).translate(tuple(d['point'])) for d in D]
clash = [(i, j) for i in range(len(cy)) for j in range(i+1, len(cy)) if np.linalg.norm(np.array(D[i]['point']) - np.array(D[j]['point'])) < 40 and (cy[i] ^ cy[j]).volume() > 0.01]
left = [round((A ^ q).volume(), 2) for q in cy]; print('  dowel holes:', len(D), 'pairs intersecting each other:', clash, '| max material left inside a hole mm3:', max(left))
# breakthrough: a slightly fatter, longer cylinder must still be fully solid around the hole -> (fat - arm - hole) == 0
thin = []
for d, q in zip(D, cy):
    fat = m3.Manifold.cylinder(34.0, 4.7, 4.7, 48).translate((0, 0, -17)).rotate(rot['XYZ'.index(d['axis'])]).translate(tuple(d['point']))
    miss = (fat - q - A).volume()
    others = sum((fat ^ o).volume() for o in cy if o is not q)
    if miss - others > 1.0: thin.append((d['shells'], d['point'], round(miss - others, 1)))
print('  dowel holes with less than 1.5 mm surrounding wall somewhere:', thin); res['dowels'] = len(D); res['dowel_thin_wall'] = thin; res['dowel_clashes'] = clash
json.dump(res, open(OUT + '/V5_Verification.json', 'w'), indent=1, default=str)
