"""V5 draft builder. Reads originals only; writes derived meshes to a new folder. Originals are never modified."""
import sys; sys.path.insert(0, '/home/claude/scripts')
import numpy as np, trimesh, manifold3d as m3, json, os, time
from shapely.geometry import Polygon, Point, box as sbox
from shapely.ops import unary_union
from v5_lib import *
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
log = {}
A0 = arm(); log['source_volume_cm3'] = A0.volume()/1000
rf = np.load('/home/claude/out/ringframe.npz'); n = rf['n']
# ---------- 1. ring light: cover and gauge become removable ----------
cover = from_tm(trimesh.load('/home/claude/out/cover_assembled.stl', force='mesh'))
gauge = from_tm(part3mf('Pressure.stl', 46)) + from_tm(comp_tm(45))          # Pressure + needle = one insert
u_, w_ = rf['u'], rf['w']; cc = rf['c']
CL = 0.35                                                        # clearance per side, mm
def sweep(M, down=0.25, dist=40.0, step=1.0):
    ring8 = [M] + [M.translate(tuple(CL*(np.cos(a)*u_ + np.sin(a)*w_))) for a in np.linspace(0, 2*np.pi, 8, endpoint=False)]
    off = m3.Manifold.batch_boolean(ring8, m3.OpType.Add)        # in-plane clearance offset
    return m3.Manifold.batch_boolean([off.translate(tuple(n*d)) for d in np.arange(-down, dist+1e-6, step)], m3.OpType.Add)
cut_cover = sweep(cover); cut_gauge = sweep(gauge)
# guaranteed-open LED trough: annular air column (measured walls r 28.8 / 55.9, floor h -3.46)
ann = trimesh.creation.annulus(r_min=29.3, r_max=55.4, height=15.3, sections=180); ann.apply_translation([0, 0, -3.3 + 15.3/2])
Mr = np.eye(4); Mr[:3, 0] = u_; Mr[:3, 1] = w_; Mr[:3, 2] = n; Mr[:3, 3] = cc; ann.apply_transform(Mr)
A1 = A0 - cut_cover - cut_gauge - from_tm(ann)
# ---------- 1b. hand light strip and crystal (V5.1, owner-approved 2026-11-15) ----------
lens_tm = comp_tm(10); crystal_tm = comp_tm(50)
lens = from_tm(lens_tm); crystal = from_tm(crystal_tm)
lv = lens_tm.vertices; lc = (lv.min(0) + lv.max(0)) / 2
_, _, Vt = np.linalg.svd(lv - lv.mean(0), full_matrices=False)
eL = Vt[0] * np.sign(Vt[0][2]); eN = Vt[2] * np.sign(Vt[2][1]); eW = np.cross(eN, eL)      # along hand (+Z), outward (+Y), across
pl = (lv - lc) @ np.array([eL, eW, eN]).T; lmin, lmax = pl[:, 0].min(), pl[:, 0].max(); nmin = pl[:, 2].min()
def shifts(M, c, dirs): return m3.Manifold.batch_boolean([M] + [M.translate(tuple(c * d)) for d in dirs], m3.OpType.Add)
def frame_box(l0, l1, w0, w1, n0, n1):       # box given in lens frame (mm), returned in assembled coordinates
    bx = trimesh.creation.box(extents=[l1 - l0, w1 - w0, n1 - n0]); bx.apply_translation([(l0 + l1) / 2, (w0 + w1) / 2, (n0 + n1) / 2])
    T = np.eye(4); T[:3, 0] = eL; T[:3, 1] = eW; T[:3, 2] = eN; T[:3, 3] = lc; bx.apply_transform(T); return from_tm(bx)
lens_off = shifts(lens, 0.25, [eW, -eW, eL, -eL])
lens_skin = m3.Manifold.batch_boolean([lens_off.translate(tuple(eN * d)) for d in np.arange(0, 1.21, 0.2)], m3.OpType.Add)
protect = from_tm(part3mf('Crystal_Base.stl', 51)) if False else None
plate = comp_tm(7); base = comp_tm(51)
keep = m3.Manifold.batch_boolean([from_tm(plate), from_tm(part3mf('Crystal_Base.stl', 51))], m3.OpType.Add)
assert keep.status() == m3.Error.NoError and lens.status() == m3.Error.NoError and crystal.status() == m3.Error.NoError
cut_lens = lens_off + (lens_skin - keep)                                   # lens body everywhere; skin only where nothing sits on it
CH_W, CH_EXTRA = 10.5, 2.0                                                 # channel width; extra depth below the original 2.2 mm
wc = ((np.array([210.75, 0, 0]) - lc) @ eW)
cut_chan = frame_box(lmin + 3.0, lmax - 3.0, wc - CH_W / 2, wc + CH_W / 2, nmin - 2.2 - CH_EXTRA, nmin + 0.2)
cr_off = shifts(crystal, 0.3, [eW, -eW, eL, -eL])
cut_crystal = m3.Manifold.batch_boolean([cr_off.translate(tuple(eN * d)) for d in np.arange(-0.2, 25.01, 1.0)], m3.OpType.Add)
A1b = A1 - cut_lens - cut_chan - cut_crystal
log['hand_crystal_removed_cm3'] = (A1.volume() - A1b.volume()) / 1000; log['lens_frame'] = dict(centre=lc.tolist(), along=eL.tolist(), across=eW.tolist(), outward=eN.tolist(), lmin=float(lmin), lmax=float(lmax))
assert A1b.status() == m3.Error.NoError and A1b.volume() > 1e7
A1 = A1b
# ---------- 1c. V5.2: wire link trough -> hand channel ----------
def ring_box(u0, u1, w0, w1, h0, h1):
    bx = trimesh.creation.box(extents=[u1 - u0, w1 - w0, h1 - h0]); bx.apply_translation([(u0 + u1) / 2, (w0 + w1) / 2, (h0 + h1) / 2])
    T = np.eye(4); T[:3, 0] = u_; T[:3, 1] = w_; T[:3, 2] = n; T[:3, 3] = cc; bx.apply_transform(T); return from_tm(bx)
wire_slot = ring_box(-4.9, 4.1, -70.0, -50.0, -3.45, 0.2)
A1 = A1 - wire_slot
log['v5_2_removed_cm3'] = (A1b.volume() - A1.volume()) / 1000
assert A1.status() == m3.Error.NoError
log['ring_removed_cm3'] = (A0.volume()-A1.volume())/1000; log['cover_cm3'] = cover.volume()/1000; log['gauge_cm3'] = gauge.volume()/1000
# ---------- 2. handle: one-piece bar in deepened sockets ----------
HY, HZ, HR = 156.0, 375.95, 9.4
XL, XR = 85.5, 336.5                                             # socket floors; >= 7 mm wall left behind each
def cylx(x0, x1, r): return m3.Manifold.cylinder(x1-x0, r, r, 96).rotate((0, 90, 0)).translate((x0, HY, HZ))
collar = cylx(89.0, 97.8, 15.5) + cylx(324.6, 333.0, 15.5)       # reinforcing collars around both sockets (added material)
sock = cylx(XL, XR, HR+0.25)
A2 = (A1 + collar) - sock - from_tm(comp_tm(80))
log['handle_removed_cm3'] = (A1.volume()-A2.volume())/1000
handle = m3.Manifold.cylinder(XR-XL-1.0, HR, HR, 96).rotate((0, 90, 0)).translate((XL+0.5, HY, HZ))
# ---------- 3. seam dowel sockets (6 mm x 30 mm dowels) ----------
regions = [('Cuff_Left_Front',(-1,211,-1,147,-1,145)),('Cuff_Left_Rear',(-1,211,147,300,-1,145)),('Cuff_Right_Front',(211,425,-1,147,-1,145)),('Cuff_Right_Rear',(211,425,147,300,-1,145)),
 ('LightBand_Front_Left',(-1,211,-1,180,145,310)),('LightBand_Front_Right',(211,425,-1,180,145,310)),('LightBand_Rear_Left',(-1,100,180,300,145,310)),('LightBand_Rear_RingCarrier',(100,300,180,300,145,310)),('LightBand_Rear_Right',(300,425,180,300,145,310)),
 ('Wrist_Left',(-1,211,-1,300,310,400)),('Wrist_Right',(211,425,-1,300,310,400)),('Knuckles_Left',(-1,211,-1,300,400,601)),('Knuckles_Right',(211,425,-1,300,400,601))]
def region_of(p, margin=0.0, free=-1):
    mg = [0.0 if k == free else margin for k in range(3)]
    for i, (_, b) in enumerate(regions):
        if b[0]+mg[0] <= p[0] <= b[1]-mg[0] and b[2]+mg[1] <= p[1] <= b[3]-mg[1] and b[4]+mg[2] <= p[2] <= b[5]-mg[2]: return i
    return -1
planes = [(0,100),(0,211),(0,300),(1,147),(1,180),(2,145),(2,310),(2,400)]
DR, DD = 3.2, 16.0          # hole radius, depth each side
tmA = to_tm(A2)
ring = np.linspace(0, 2*np.pi, 12, endpoint=False)
def cyl_pts(p, ax, r):
    e = np.eye(3); a = e[ax]; b1 = e[(ax+1)%3]; b2 = e[(ax+2)%3]; pts = []
    for d in (-DD-2.0, -DD*0.5, -1.0, 1.0, DD*0.5, DD+2.0):
        for th in ring: pts.append(p + a*d + r*(np.cos(th)*b1 + np.sin(th)*b2))
        pts.append(p + a*d)
    return np.array(pts)
dowels = json.load(open('/home/claude/arcane-vi-gauntlet/releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_build_log.json'))['dowels']   # identical to V5 so printed V5 shells stay compatible
rot = {0: (0, 90, 0), 1: (-90, 0, 0), 2: (0, 0, 0)}
holes = []
for d in dowels:
    ax = 'XYZ'.index(d['axis']); p = np.array(d['point']); c = m3.Manifold.cylinder(2*DD, DR, DR, 48).translate((0, 0, -DD)).rotate(rot[ax]).translate(tuple(p)); holes.append(c)
A3 = A2 - m3.Manifold.batch_boolean(holes, m3.OpType.Add) if holes else A2
log['dowel_count'] = len(dowels); log['dowels'] = dowels; log['dowel_removed_cm3'] = (A2.volume()-A3.volume())/1000
log['edited_volume_cm3'] = A3.volume()/1000; log['edited_status'] = str(A3.status())
# ---------- 4. cut into 13 shells, same planes and print orientations as V4 ----------
def R(i, name):
    if i <= 4: return (180, 0, 0)
    if i <= 6: return (-90, 0, 0)
    if i <= 9: return (90, 0, 0)
    if i <= 11: return (0, 0, 0)
    return (0, 90, 0) if 'Left' in name else (0, -90, 0)
def bed(M):
    b = M.bounding_box(); return M.translate((128-(b[0]+b[3])/2, 128-(b[1]+b[4])/2, -b[2]))
def export(M, path):
    t = to_tm(M); t.export(path); return t
shells = []
for i, (name, b) in enumerate(regions, 1):
    bx = m3.Manifold.cube((b[1]-b[0], b[3]-b[2], b[5]-b[4])).translate((b[0], b[2], b[4]))
    S = A3 ^ bx
    parts = S.decompose(); parts.sort(key=lambda q: -q.volume())
    main = parts[0]; frag = [round(q.volume(), 2) for q in parts[1:]]
    big = [q for q in parts[1:] if q.volume() > 500.0]     # > 0.5 cm3 would be a real loose piece
    Pm = bed(main.rotate(R(i, name)))
    fn = f'R_{i:02d}_{name}_V5_2'
    os.makedirs(f'{OUT}/Right_Shells', exist_ok=True); os.makedirs(f'{OUT}/Left_Shells', exist_ok=True)
    export(Pm, f'{OUT}/Right_Shells/{fn}.3mf')
    export(bed(Pm.mirror((1, 0, 0))), f'{OUT}/Left_Shells/L{fn[1:]}.3mf')
    np.savez(f'/home/claude/out/v52_asm_{i:02d}.npz', v=to_tm(main).vertices, f=to_tm(main).faces)
    shells.append(dict(shell=i, name=name, volume_cm3=round(main.volume()/1000, 2), dropped_fragments_mm3=frag, loose_pieces_over_0p5cm3=len(big)))
    print(shells[-1], flush=True)
log['shells'] = shells
# ---------- 5. inserts ----------
os.makedirs(f'{OUT}/Inserts', exist_ok=True)
u = rf['u']; w = rf['w']
Rm = np.eye(4); Rm[:3, :3] = np.array([u, w, n])          # ring frame -> flat on bed, axis up
def flat(M, flip=False):
    t = to_tm(M); t.apply_transform(Rm)
    if flip: t.apply_transform(trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0]))
    t.apply_translation([128-(t.bounds[0][0]+t.bounds[1][0])/2, 128-(t.bounds[0][1]+t.bounds[1][1])/2, -t.bounds[0][2]]); return t
def save_pair(t, name):
    t.export(f'{OUT}/Inserts/R_{name}.3mf'); l = t.copy(); l.apply_transform(np.diag([-1, 1, 1, 1])); l.invert()
    l.apply_translation([128-(l.bounds[0][0]+l.bounds[1][0])/2, 0, 0]); l.export(f'{OUT}/Inserts/L_{name}.3mf')
save_pair(flat(cover), 'Ring_Light_Cover_translucent'); save_pair(flat(gauge), 'Pressure_Gauge_Insert')
h = to_tm(handle); h.apply_translation([128-(h.bounds[0][0]+h.bounds[1][0])/2, 128-HY, -h.bounds[0][2]]); h.export(f'{OUT}/Inserts/Handle_OnePiece_18p8x250.3mf')
peg = to_tm(m3.Manifold.cylinder(30.0, 2.95, 2.95, 48)); peg.export(f'{OUT}/Inserts/Dowel_Peg_5p9x30_optional.3mf')
np.savez('/home/claude/out/v52_arm.npz', v=to_tm(A3).vertices, f=to_tm(A3).faces)
json.dump(log, open(f'{OUT}/V5_build_log.json', 'w'), indent=1)
print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in log.items() if k not in ('dowels', 'shells')})
from collections import Counter; print(Counter((d['axis'], d['plane']) for d in dowels))

# ---------- 6. T-2 finger-slot coupon (forefinger slot of shell 13, printed in shell-13 orientation) ----------
os.makedirs(f'{OUT}/Test_Coupons', exist_ok=True)
C = (A3 ^ m3.Manifold.cube((75, 115, 105)).translate((270, 95, 495))).decompose(); C.sort(key=lambda q: -q.volume())
export(bed(C[0].rotate((0, -90, 0))), f'{OUT}/Test_Coupons/T2_Knuckle_Slot_Forefinger_Coupon.3mf')

# ---------- 7. V5.1 inserts: crystal and hand lens segments ----------
tA3 = to_tm(A3)
ls = np.arange(lmin + 0.5, lmax - 0.49, 1.0); o = lc + np.outer(ls, eL) + np.outer(np.full(len(ls), wc), eW) + eN * (pl[:, 2].max() + 0.05)
hit = tA3.ray.intersects_any(o, np.tile(eN, (len(o), 1)))
segs = []; start = None
for l, h in zip(ls, hit):
    if not h and start is None: start = l
    if h and start is not None: segs.append((start - 0.5, l - 0.5)); start = None
if start is not None: segs.append((start - 0.5, ls[-1] + 0.5))
segs = [sg for sg in segs if sg[1] - sg[0] >= 8]
log['lens_exposed_segments_mm_from_ring_end'] = [[round(float(a_ - lmin), 1), round(float(b_ - lmin), 1)] for a_, b_ in segs]
Tl = np.eye(4); Tl[:3, :3] = np.array([eL, eW, eN]); Tl[:3, 3] = -np.array([eL, eW, eN]) @ lc
def flat_local(M):
    t = to_tm(M); t.apply_transform(Tl); t.apply_translation([128 - (t.bounds[0][0] + t.bounds[1][0]) / 2, 128 - (t.bounds[0][1] + t.bounds[1][1]) / 2, -t.bounds[0][2]]); return t
for k, (a_, b_) in enumerate(segs):
    seg = lens ^ frame_box(a_ + 0.3, b_ - 0.3, -20, 20, -20, 20)
    save_pair(flat_local(seg), f'Hand_Lens_{chr(65 + k)}_translucent_{b_ - a_ - 0.6:.0f}mm')
save_pair(flat_local(crystal), 'Crystal_translucent')
json.dump(log, open(f'{OUT}/V5_build_log.json', 'w'), indent=1)
print('lens segments', log['lens_exposed_segments_mm_from_ring_end'], 'hand/crystal removed cm3', round(log['hand_crystal_removed_cm3'], 2))
