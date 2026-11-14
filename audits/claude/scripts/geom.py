import sys, os, json, csv, hashlib, glob
import numpy as np, trimesh
root = sys.argv[1]; out = sys.argv[2]
rows = []
files = sorted(glob.glob(os.path.join(root, '**', '*.stl'), recursive=True))
for f in files:
    sz = os.path.getsize(f)
    if sz > 60e6:   # big sources handled separately
        continue
    h = hashlib.sha256(open(f,'rb').read()).hexdigest()
    m = trimesh.load(f, force='mesh', process=False)
    raw_faces = len(m.faces)
    m.merge_vertices()
    area = m.area_faces
    degen = int((area < 1e-10).sum())
    comps = m.split(only_watertight=False)
    e = m.edges_sorted
    uniq, cnt = np.unique(e, axis=0, return_counts=True)
    boundary = int((cnt == 1).sum()); nonman = int((cnt > 2).sum())
    b = m.bounds; ext = m.extents
    rows.append(dict(file=os.path.relpath(f, root), bytes=sz, sha256=h, triangles=raw_faces,
        vertices=len(m.vertices), min_x=round(b[0,0],3), min_y=round(b[0,1],3), min_z=round(b[0,2],3),
        size_x=round(ext[0],3), size_y=round(ext[1],3), size_z=round(ext[2],3),
        volume_cm3=round(m.volume/1000,3), area_cm2=round(m.area/100,2),
        watertight=m.is_watertight, winding_consistent=m.is_winding_consistent,
        components=len(comps), comp_volumes_cm3=';'.join(str(round(c.volume/1000,3)) for c in sorted(comps, key=lambda c:-abs(c.volume))[:6]),
        boundary_edges=boundary, nonmanifold_edges=nonman, degenerate_faces=degen,
        euler=m.euler_number))
    print(rows[-1]['file'], ext.round(2), rows[-1]['volume_cm3'], m.is_watertight, len(comps), boundary, nonman, degen, flush=True)
with open(out,'w',newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
