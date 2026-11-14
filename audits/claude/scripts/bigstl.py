import sys, numpy as np, trimesh, os, pickle
f = sys.argv[1]; out = sys.argv[2]
m = trimesh.load(f, force='mesh', process=False); m.merge_vertices()
print(os.path.basename(f), 'tris', len(m.faces), 'bounds', m.bounds.round(2).tolist(), 'vol cm3', round(m.volume/1000,2), 'watertight', m.is_watertight, flush=True)
import scipy.sparse.csgraph as cg, scipy.sparse as sp
adj = m.face_adjacency
n = len(m.faces)
g = sp.coo_matrix((np.ones(len(adj)), (adj[:,0], adj[:,1])), shape=(n,n))
nc, lab = cg.connected_components(g, directed=False)
print('components', nc)
tri = m.triangles
sv = np.einsum('ij,ij->i', tri[:,0], np.cross(tri[:,1], tri[:,2]))/6
vols = np.bincount(lab, weights=sv, minlength=nc)
cnt = np.bincount(lab, minlength=nc)
lo = np.full((nc,3), np.inf); hi = np.full((nc,3), -np.inf)
for k in range(3):
    np.minimum.at(lo, lab, tri[:,k]); np.maximum.at(hi, lab, tri[:,k])
order = np.argsort(-np.abs(vols))
for i in order[:120]:
    print(f'{i:4d} tris {cnt[i]:8d} vol {vols[i]/1000:9.2f} size {np.round(hi[i]-lo[i],1).tolist()} lo {np.round(lo[i],1).tolist()}')
np.savez(out, v=m.vertices, f=m.faces, lab=lab, vols=vols, lo=lo, hi=hi)
