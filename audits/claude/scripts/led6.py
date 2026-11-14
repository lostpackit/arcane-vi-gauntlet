import numpy as np, trimesh
from scipy import ndimage as ndi
rf = np.load('out/ringframe.npz'); n, c, u, w = rf['n'], rf['c'], rf['u'], rf['w']
ol = trimesh.load('out/light_assembled.stl', force='mesh')
s8 = np.load('out/asm_R_08.npz'); shell = trimesh.Trimesh(s8['v'], s8['f'], process=False)
d = np.load('out/fullR.npz'); full = trimesh.Trimesh(d['v'], d['f'], process=False)
def P(r, ang, h): a = np.radians(ang); return c + r*(np.cos(a)*u + np.sin(a)*w) + h*n
# notch width on inner & outer wall (original light)
angs = np.arange(240, 300, 0.25)
for h0 in (-3, -2, -1, 0, 1, 2):
    o = np.array([P(42, a, h0) for a in angs]); do = np.array([np.cos(np.radians(a))*u + np.sin(np.radians(a))*w for a in angs])
    def fh(m, o, dd):
        loc, ir, _ = m.ray.intersects_location(o, dd, multiple_hits=True); t = ((loc-o[ir])*dd[ir]).sum(1); out = np.full(len(o), np.inf)
        np.minimum.at(out, ir, np.where(t>1e-6, t, np.inf)); return out
    ri = 42 - fh(ol, o, -do); ro = 42 + fh(ol, o, do)
    ai = angs[ri < 27.5]; ao = angs[ro > 57.5]
    wi = (np.radians(ai.max()-ai.min())*28.8) if len(ai) else 0; wo = (np.radians(ao.max()-ao.min())*55.9) if len(ao) else 0
    print(f'h={h0}: inner-wall opening {ai.min() if len(ai) else None}-{ai.max() if len(ai) else None} deg => {wi:.1f} mm wide; outer-wall opening {ao.min() if len(ao) else None}-{ao.max() if len(ao) else None} deg => {wo:.1f} mm wide')
# voxel flood from chamber in the fused arm
pitch = 1.0
gu = np.arange(-75, 75.01, pitch); gw = np.arange(-110, 75.01, pitch); gh = np.arange(-70, 12.01, pitch)
U, W, H = np.meshgrid(gu, gw, gh, indexing='ij')
pts = c + U[...,None]*u + W[...,None]*w + H[...,None]*n
solid = np.zeros(U.size, bool); flat = pts.reshape(-1,3)
for i in range(0, len(flat), 200000): solid[i:i+200000] = full.contains(flat[i:i+200000])
solid = solid.reshape(U.shape); air = ~solid
lab, nl = ndi.label(air)
seed = (np.argmin(abs(gu-42)), np.argmin(abs(gw-0)), np.argmin(abs(gh-3)))
L = lab[seed]; reg = lab == L
print('chamber air region voxels (cm3 at 1mm):', reg.sum()/1000)
idx = np.argwhere(reg); 
print(' region extent u', gu[idx[:,0].min()], gu[idx[:,0].max()], 'w', gw[idx[:,1].min()], gw[idx[:,1].max()], 'h', gh[idx[:,2].min()], gh[idx[:,2].max()])
touch = reg[0].any() or reg[-1].any() or reg[:,0].any() or reg[:,-1].any() or reg[:,:,0].any() or reg[:,:,-1].any()
print(' reaches probe-box boundary:', bool(touch))
for er in (1, 2, 3):
    e = ndi.binary_erosion(air, structure=ndi.generate_binary_structure(3,1), iterations=er)
    l2, _ = ndi.label(e); Ls = l2[seed]
    r2 = l2 == Ls if Ls else np.zeros_like(e)
    i2 = np.argwhere(r2)
    print(f' passable by a {2*er+1} mm probe: region h-min {gh[i2[:,2].min()] if len(i2) else None}, w-min {gw[i2[:,1].min()] if len(i2) else None}, reaches boundary {bool(len(i2) and (r2[:,:,0].any() or r2[:,0].any() or r2[0].any() or r2[-1].any()))}')
# where does the region go below the ring floor?
below = idx[gh[idx[:,2]] < -8]
if len(below): print(' air connected to chamber below ring base: u', gu[below[:,0].min()], gu[below[:,0].max()], 'w', gw[below[:,1].min()], gw[below[:,1].max()], 'h', gh[below[:,2].min()], gh[below[:,2].max()], 'vox', len(below))
print(' w axis in assembled coords', w.round(3), ' u', u.round(3))
