import numpy as np, os, glob
def stl_verts(p):
    with open(p,'rb') as f:
        f.seek(80); n = np.frombuffer(f.read(4), '<u4')[0]
        d = np.frombuffer(f.read(), dtype=np.dtype([('n','<f4',3),('v','<f4',(3,3)),('a','<u2')]), count=n)
    return d['v'], d['n']
def canon(v):  # per-triangle centroid set, sorted
    c = v.mean(1).astype(np.float64); c -= v.reshape(-1,3).min(0)
    return c[np.lexsort(c.T[::-1])]
V4='cad/releases/v4/Vi_Gauntlet_X1C_V4_Print_Release'
for i in range(1,14):
    r = glob.glob(f'{V4}/Right_Shells/R_{i:02d}_*.stl')[0]; l = glob.glob(f'{V4}/Left_Shells/L_{i:02d}_*.stl')[0]
    rv,_ = stl_verts(r); lv, ln = stl_verts(l)
    same = rv.shape==lv.shape and np.abs(canon(rv)-canon(lv)).max()
    m = lv.copy(); m[...,0] = -m[...,0]
    mir = np.abs(canon(rv)-canon(m)).max() if rv.shape==lv.shape else None
    # winding sanity on left: signed volume
    vol = np.einsum('ij,ij->i', lv[:,0].astype(float), np.cross(lv[:,1].astype(float), lv[:,2].astype(float))).sum()/6
    print(i, 'tris', len(rv), len(lv), 'identical-dev', None if same is False else round(float(same),4), 'mirror-dev', None if mir is None else round(float(mir),5), 'L signed vol cm3', round(vol/1000,2), 'L minXYZ', lv.reshape(-1,3).min(0).round(2))
a,_ = stl_verts('cad/originals/Full_Arm_Right (No Fingers).stl'); b,_ = stl_verts('cad/originals/Full_Arm_Left (No Fingers).stl')
print('full arm tris', len(a), len(b), 'L bounds', b.reshape(-1,3).min(0), b.reshape(-1,3).max(0))
m = b.copy(); m[...,0] = -m[...,0]
print('FullLeft identical to FullRight dev', np.abs(canon(a)-canon(b)).max(), ' mirror dev', np.abs(canon(a)-canon(m)).max())
