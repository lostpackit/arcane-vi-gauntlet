import sys, os, json, numpy as np, trimesh
from scipy.spatial import cKDTree
V4 = 'cad/releases/v4/Vi_Gauntlet_X1C_V4_Print_Release'
d = np.load('out/fullR.npz'); SV = d['v']; SF = d['f']
src = trimesh.Trimesh(SV, SF, process=False)
tree = cKDTree(SV)
regions = [('Cuff_Left_Front',(-1,211,-1,147,-1,145)),('Cuff_Left_Rear',(-1,211,147,300,-1,145)),('Cuff_Right_Front',(211,425,-1,147,-1,145)),('Cuff_Right_Rear',(211,425,147,300,-1,145)),
 ('LightBand_Front_Left',(-1,211,-1,180,145,310)),('LightBand_Front_Right',(211,425,-1,180,145,310)),('LightBand_Rear_Left',(-1,100,180,300,145,310)),('LightBand_REAR_RING_CARRIER',(100,300,180,300,145,310)),('LightBand_Rear_Right',(300,425,180,300,145,310)),
 ('Wrist_Upper_Left',(-1,211,-1,300,310,400)),('Wrist_Upper_Right',(211,425,-1,300,310,400)),('Knuckles_Left',(-1,211,-1,300,400,601)),('Knuckles_Right',(211,425,-1,300,400,601))]
def R(ax, deg):
    return trimesh.transformations.rotation_matrix(np.radians(deg), {'X':[1,0,0],'Y':[0,1,0],'Z':[0,0,1]}[ax])[:3,:3]
def rot_for(i, name):
    if i<=4: return R('X',180)
    if i<=6: return R('X',-90)
    if i<=9: return R('X',90)
    if i<=11: return np.eye(3)
    return R('Y', 90 if 'Left' in name else -90)
def clip_bounds(bb):
    x0,x1,y0,y1,z0,z1 = bb
    v = SV; f = SF
    for o,n in [((x0,0,0),(1,0,0)),((x1,0,0),(-1,0,0)),((0,y0,0),(0,1,0)),((0,y1,0),(0,-1,0)),((0,0,z0),(0,0,1)),((0,0,z1),(0,0,-1))]:
        r_ = trimesh.intersections.slice_faces_plane(v, f, np.array(n,float), np.array(o,float)); v, f = r_[0], r_[1]
    used = np.unique(f); return v[used].min(0), v[used].max(0)
covered = np.zeros(len(SV), bool); rep = []; asm = {}
planes = {'X':[100,211,300], 'Y':[147,180], 'Z':[145,310,400]}
for i,(name,bb) in enumerate(regions,1):
    f = [p for p in os.listdir(V4+'/Right_Shells') if p.startswith(f'R_{i:02d}_')][0]
    m = trimesh.load(os.path.join(V4,'Right_Shells',f), force='mesh', process=False); m.merge_vertices()
    Rm = rot_for(i,name)
    w = m.vertices @ Rm   # inverse rotation (R^T applied: v @ R == R^T v)
    lo, hi = clip_bounds(bb)
    t = lo - w.min(0); w = w + t
    size_err = np.abs((w.max(0)-w.min(0)) - (hi-lo)).max()
    dist, idx = tree.query(w, distance_upper_bound=0.02)
    matched = np.isfinite(dist)
    covered[idx[matched]] = True
    un = w[~matched]
    onplane = np.zeros(len(un), bool)
    for k,a in enumerate('XYZ'):
        for p in planes[a]: onplane |= np.abs(un[:,k]-p) < 0.02
    off = un[~onplane]
    # distance of leftover verts to source surface
    far = 0; maxd = 0
    if len(off):
        cp, dd, _ = trimesh.proximity.closest_point(src, off[:3000]) if len(off) else (None,[0],None)
        maxd = float(np.max(dd)); far = int((dd>0.05).sum())
    asm[i] = (w, m.faces)
    rep.append(dict(shell=i, name=name, verts=len(w), matched_source=int(matched.sum()), on_cut_plane=int(onplane.sum()), other=int(len(off)), other_far_gt_0p05=far, other_max_dev_mm=round(maxd,3), size_err_mm=round(float(size_err),4), translation=[round(float(x),3) for x in t], assembled_lo=[round(float(x),2) for x in w.min(0)], assembled_hi=[round(float(x),2) for x in w.max(0)]))
    print(rep[-1], flush=True)
    np.savez(f'out/asm_R_{i:02d}.npz', v=w, f=m.faces)
unc = ~covered
print('source verts', len(SV), 'not present in any shell', int(unc.sum()))
if unc.sum():
    pts = SV[unc]
    # cluster uncovered by connectivity over source faces
    fm = unc[SF].all(1)
    sub = trimesh.Trimesh(SV, SF[fm], process=False)
    comps = trimesh.graph.connected_components(sub.face_adjacency, nodes=np.arange(len(sub.faces)), min_len=1)
    out = []
    for c in comps:
        tri = sub.triangles[c]; lo = tri.reshape(-1,3).min(0); hi = tri.reshape(-1,3).max(0)
        vol = float(np.einsum('ij,ij->i', tri[:,0], np.cross(tri[:,1], tri[:,2])).sum()/6)
        out.append((len(c), np.round(lo,1).tolist(), np.round(hi,1).tolist(), round(float(sub.area_faces[c].sum()),2)))
    out.sort(key=lambda x:-x[3])
    print('uncovered clusters (ntri, lo, hi, area mm2):')
    for o in out[:40]: print(o)
    print('n clusters', len(out), 'total area', round(sum(o[3] for o in out),1))
    lone = pts
    print('uncovered vert bounds', lone.min(0).round(1), lone.max(0).round(1))
json.dump(rep, open('out/reassembly_report.json','w'), indent=1)
