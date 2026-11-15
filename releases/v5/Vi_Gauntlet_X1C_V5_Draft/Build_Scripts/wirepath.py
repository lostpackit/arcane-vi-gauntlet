import sys; sys.path.insert(0, '/home/claude/scripts')
import numpy as np, trimesh, json, manifold3d as m3
from scipy import ndimage as ndi
from v5_lib import *
arm = sys.argv[1]
d = np.load(arm); A = to_m(d['v'], d['f'])
rf = np.load('/home/claude/out/ringframe.npz'); n, c, u, w = rf['n'], rf['c'], rf['u'], rf['w']
cover = from_tm(trimesh.load('/home/claude/out/cover_assembled.stl', force='mesh'))
seat = 0.0
for dz in np.arange(0, 0.61, 0.05):
    if (A ^ cover.translate(tuple(-n * dz))).volume() > 0.5: break
    seat = dz
print('cover seats %.2f mm below its modelled height' % seat)
gauge = from_tm(part3mf('Pressure.stl', 46)) + from_tm(comp_tm(45))
full = m3.Manifold.batch_boolean([A, cover.translate(tuple(-n * seat)), gauge.translate(tuple(-n * seat))], m3.OpType.Add); tF = to_tm(full)
p = 0.5; gu = np.arange(-66, 66.01, p); gw = np.arange(-112, 66.01, p); gh = np.arange(-60, 11.01, p)
U_, W_, H_ = np.meshgrid(gu, gw, gh, indexing='ij'); pts = (c + U_[..., None]*u + W_[..., None]*w + H_[..., None]*n).reshape(-1, 3)
sol = np.zeros(len(pts), bool)
for i in range(0, len(pts), 200000): sol[i:i+200000] = tF.contains(pts[i:i+200000])
air = ~sol.reshape(U_.shape); del pts
edt = ndi.distance_transform_edt(air) * p            # clearance radius at each air voxel
def ix(uu, ww, hh): return (np.argmin(abs(gu-uu)), np.argmin(abs(gw-ww)), np.argmin(abs(gh-hh)))
seed = ix(42, 0, 2)
# hand channel point in ring frame
F = json.load(open('/home/claude/arcane-vi-gauntlet/releases/v5/Vi_Gauntlet_X1C_V5_Draft/V5_1_build_log.json'))['lens_frame']; lc = np.array(F['centre']); eL = np.array(F['along']); eW = np.array(F['across']); eN = np.array(F['outward'])
lv = comp_tm(10).vertices; n_in = ((lv - lc) @ eN).min(); wc = (np.array([210.75, 0, 0]) - lc) @ eW
chp = lc + eL * (F['lmin'] + 12) + eW * wc + eN * (n_in - 2.0); q = chp - c; chan = ix(q @ u, q @ w, q @ n)
print('channel target in ring frame (u,w,h):', (q@u).round(1), (q@w).round(1), (q@n).round(1), 'air there:', bool(air[chan]), 'clearance', edt[chan].round(2))
targets = {'hand LED channel': chan}
cav = np.argwhere(air[:, :, 0])   # any air on the h=-60 face = hand cavity
def bottleneck(mask_fn):
    lo, hi = 0.0, 8.0; best = 0.0
    for r in np.arange(0.5, 8.01, 0.25):
        lab, _ = ndi.label(edt >= r); L = lab[seed]
        if L and mask_fn(lab, L): best = r
        else: break
    return best
r1 = bottleneck(lambda lab, L: lab[chan] == L); r2 = bottleneck(lambda lab, L: (lab[:, :, 0] == L).any())
print('largest sphere that passes trough -> hand LED channel: diameter %.1f mm' % (2*r1)); print('largest sphere that passes trough -> hand cavity: diameter %.1f mm' % (2*r2))
json.dump(dict(cover_seat_drop_mm=float(seat), trough_to_channel_diameter_mm=2*r1, trough_to_cavity_diameter_mm=2*r2), open(sys.argv[2], 'w'))
