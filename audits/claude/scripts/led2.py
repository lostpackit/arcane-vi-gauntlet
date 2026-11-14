import numpy as np, trimesh, matplotlib, json
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
def loc(name):
    d = np.load(f'out/cache3mf/{name}.npz'); return d['v'], d['f']
lv, lf = loc('object_1.model'); cv, cf = loc('object_2.model')
print('local light bounds', lv.min(0).round(3), lv.max(0).round(3), 'size', (lv.max(0)-lv.min(0)).round(3))
print('local cover bounds', cv.min(0).round(3), cv.max(0).round(3), 'size', (cv.max(0)-cv.min(0)).round(3))
def kabsch(A, B):
    ca, cb = A.mean(0), B.mean(0); H = (A-ca).T @ (B-cb); U, S, Vt = np.linalg.svd(H); d = np.sign(np.linalg.det(Vt.T @ U.T))
    R = Vt.T @ np.diag([1,1,d]) @ U.T; return R, cb - R @ ca
t = np.load('out/together.npz'); TV, TF, lab = t['v'], t['f'], t['lab']
def to_assembled(lv, stlpath, comp):
    o = trimesh.load(stlpath, force='mesh', process=False)
    # STL triangle soup -> first occurrence order equals 3MF vertex order? use ICP-free: match via triangle corners
    ov = o.vertices
    # robust: PCA-free approach - sort-free: use trimesh registration on vertex sets
    M, _, cost = trimesh.registration.icp(lv[::7], ov, initial=trimesh.registration.procrustes(lv[::50], ov[np.random.default_rng(0).choice(len(ov), len(lv[::50]))], reflection=False, scale=False)[0], max_iterations=1) if False else (None, None, None)
    return o
ol = trimesh.load('cad/originals/Circle_Light.stl', force='mesh', process=False); ol.merge_vertices()
print('3MF verts', len(lv), 'STL merged verts', len(ol.vertices))
# plane fit: the ring's flat base. Find axis via inertia of orig STL
I = ol.principal_inertia_vectors; print('principal inertia comps', ol.principal_inertia_components.round(0)); print(I.round(4))
