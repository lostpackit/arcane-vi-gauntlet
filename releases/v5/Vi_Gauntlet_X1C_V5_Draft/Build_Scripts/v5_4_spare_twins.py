"""V5.4 spare-twin left arm (2026-11-22): owner has spare printed R_05 and R_01. Mirror twins: R_05 ~ L_06, R_01 ~ L_03.
Their dowel holes differ from L_06/L_03, so the new LEFT neighbours that meet them (L_08, L_09, L_11) get their seam
dowel holes moved to match the spares. Work in the right-arm assembled frame, then mirror to left like the V5 pipeline."""
import sys, json, glob, os, re, zipfile, hashlib
sys.path.insert(0, '/home/claude/thumbstudy')
from lib import *
REPO = '/home/claude/arcane-vi-gauntlet/releases/v5/Vi_Gauntlet_X1C_V5_Draft'
PACK = '/home/claude/pack_named/Vi_Gauntlet_V5_Print_Pack'
OUT = '/home/claude/v54/out'
D = json.load(open(f'{REPO}/V5_build_log.json'))['dowels']
AX = {'X': 0, 'Y': 1, 'Z': 2}
def refl(p): q = np.array(p, float); q[0] = 422.0 - q[0]; return q          # mirror about the X = 211 centre seam
def seam(a, b): return [x for x in D if sorted(x['shells']) == sorted([a, b])]
# changes in the right-arm frame: (shell to modify, [(old seam partner), spare shell, spare seam partner])
# spares (owner, 2026-11-22): R_01 -> L_03, R_02 -> L_04, R_05 -> L_06
plan = {9:  [(6, 5, 7), (4, 2, 7)],     # L_09 meets spare R_05 (as L_06) and spare R_02 (as L_04)
        11: [(6, 5, 10)],
        8:  [(4, 2, 8)]}
def asm_bounds(n): d = np.load(f'/home/claude/out/asm_R_{n:02d}.npz'); return d['v'].min(0), d['v'].max(0)
import itertools
Tm_fit = [None]
def reg(n, P):
    if n == 8:   # V5.2 shell 08 is thinner than the V5 reference, so bbox-centre matching fails; use the seam planes:
        # Y=180 face on the bed (z = Y-180), X 100..300 -> x, Z 145..310 -> -y, bed-centred (exact, median 0.0 mm)
        T8 = np.eye(4); T8[:3, :3] = 0; T8[0, 0] = 1; T8[1, 2] = -1; T8[2, 1] = 1
        c = P.bounds.mean(0); T8[0, 3] = c[0]-200; T8[1, 3] = c[1]+227.5; T8[2, 3] = -180
        Tm_fit[0] = 0.0; return T8
    d = np.load(f'/home/claude/out/asm_R_{n:02d}.npz'); A = trimesh.Trimesh(d['v'], d['f'], process=False)
    pts = trimesh.sample.sample_surface(A, 1500, seed=1)[0]; best = None
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for i, (pp, s_) in enumerate(zip(perm, sg)): R[i, pp] = s_
            if np.linalg.det(R) < 0: continue
            Tq = np.eye(4); Tq[:3, :3] = R; Tq[:3, 3] = P.bounds.mean(0) - A.bounds.mean(0) @ R.T
            _, dd, _ = trimesh.proximity.closest_point(P, trimesh.transform_points(pts[:500], Tq))
            if best is None or np.median(dd) < best[0]: best = (np.median(dd), Tq)
    Tm_fit[0] = round(float(best[0]), 4); return best[1]
def cyl(p, ax, sign, r, depth):
    c = trimesh.creation.cylinder(radius=r, height=depth, sections=48)
    z = np.zeros(3); z[ax] = sign
    c.apply_transform(trimesh.geometry.align_vectors([0, 0, 1], z)); c.apply_translation(np.array(p) + z*depth/2)
    return M(c)
def export(m, path, name):
    m.export(path)
    zin = zipfile.ZipFile(path); items = [(i, zin.read(i.filename)) for i in zin.infolist()]; zin.close()
    with zipfile.ZipFile(path+'.t', 'w', zipfile.ZIP_DEFLATED) as z:
        for i, dat in items:
            if i.filename == '3D/3dmodel.model': dat = re.sub(rb'(<object\b[^>]*\bname=")[^"]*(")', rb'\g<1>'+name.encode()+rb'\g<2>', dat)
            z.writestr(i.filename, dat)
    os.replace(path+'.t', path)
log = {}
for k, changes in plan.items():
    f = glob.glob(f'{PACK}/*/R_{k:02d}_*.3mf')[0]; stem = os.path.basename(f)[:-4]
    P = trimesh.load(f, force='mesh', process=False)
    Tm = reg(k, P)                                   # assembled -> print pose (axis map + translation, exact)
    S = P.copy(); S.apply_transform(np.linalg.inv(Tm)); Ms = M(S); entry = dict(source=os.path.basename(f), seams=[], fit_median_mm=Tm_fit[0])
    for old_partner, spare, spare_partner in changes:
        old = seam(k, old_partner); new = seam(spare, spare_partner)
        for x in old:                                   # plug the old holes on this seam
            ax = AX[x['axis']]; sign = 1 if S.bounds.mean(0)[ax] > x['plane'] else -1
            Ms = Ms + (cyl(x['point'], ax, sign, 3.45, 16.6) ^ M(S.convex_hull))
        checks = []
        for x in new:                                   # drill holes where the spare's holes land after mirroring
            ax = AX[x['axis']]; p = refl(x['point']); sign = 1 if S.bounds.mean(0)[ax] > x['plane'] else -1
            So = M(S)
            for x0 in old: So = So + (cyl(x0['point'], AX[x0['axis']], 1 if S.bounds.mean(0)[AX[x0['axis']]] > x0['plane'] else -1, 3.45, 16.6) ^ M(S.convex_hull))
            ring = cyl(p, ax, sign, 3.2+1.2, 16.0); hole = cyl(p, ax, sign, 3.2, 16.0)
            miss_ring = (ring - So).volume(); miss_hole = (hole - So).volume()
            keep = miss_hole < 1.0 and miss_ring < 0.25*ring.volume()       # hole fully in material, walls mostly >= 1.2 mm
            if keep: Ms = Ms - cyl(p - (np.eye(3)[ax]*sign*0.5), ax, sign, 3.2, 16.5)
            checks.append(dict(point=p.round(2).tolist(), axis=x['axis'], hole_outside_mm3=round(miss_hole, 1),
                               wall_ring_outside_pct=round(100*miss_ring/ring.volume(), 1), drilled=bool(keep)))
        entry['seams'].append(dict(meets=f'spare R_{spare:02d} (as L_{old_partner:02d})', old_holes=len(old), new_holes=checks))
    R2 = T(Ms); R2.apply_transform(Tm)
    Lm = R2.copy(); Lm.apply_transform(np.diag([-1, 1, 1, 1]))
    b = Lm.bounds; Lm.apply_translation([128-(b[0][0]+b[1][0])/2, 128-(b[0][1]+b[1][1])/2, -b[0][2]])
    name = 'L' + stem[1:] + '_SPAREMATCH'
    export(Lm, f'{OUT}/{name}.3mf', name)
    chk = trimesh.load(f'{OUT}/{name}.3mf', force='mesh', process=False)
    entry.update(output=name+'.3mf', volume_cm3=round(chk.volume/1000, 2), source_volume_cm3=round(P.volume/1000, 2),
                 watertight=bool(chk.is_watertight), extents=chk.extents.round(2).tolist(), source_extents=P.extents.round(2).tolist(),
                 status=str(Ms.status()), sha256=hashlib.sha256(open(f'{OUT}/{name}.3mf', 'rb').read()).hexdigest())
    log[name] = entry; print(json.dumps(entry, indent=1), flush=True)
json.dump(log, open(f'{OUT}/V5_4_spare_twins_log.json', 'w'), indent=1)
