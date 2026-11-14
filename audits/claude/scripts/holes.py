import json, numpy as np, trimesh
d = np.load('out/fullR.npz'); full = trimesh.Trimesh(d['v'], d['f'], process=False)
def loops(m, n, o, amax=80, amin=1.5):
    try:
        sec = m.section(plane_origin=o, plane_normal=n)
        if sec is None: return []
        p2, T = sec.to_planar()
    except Exception as e: return []
    out = []
    for poly in p2.polygons_closed:
        if poly is None: continue
        a = poly.area
        if amin < a < amax:
            c = np.array(poly.centroid.coords[0]); c3 = (T @ np.array([c[0], c[1], 0, 1]))[:3]
            b = poly.bounds; out.append((round(a,1), c3.round(1).tolist(), round(b[2]-b[0],1), round(b[3]-b[1],1)))
    return out
print('--- Full_Arm_Right small closed loops (candidate string/pin holes) ---')
for z in (440, 470, 495, 505, 512, 518, 524, 530, 540, 560, 580, 595):
    L = loops(full, [0,0,1], [0,0,z]); print(' Z', z, len(L), sorted(L, key=lambda x:x[1][0])[:14])
for y in (120, 135, 143, 150, 165, 180, 195):
    L = [l for l in loops(full, [0,1,0], [0,y,0]) if l[1][2] > 420]; print(' Y', y, len(L), sorted(L, key=lambda x:x[1][0])[:14])
objs = json.load(open('out/3mf_objects.json'))
print('--- 3MF finger-related parts: small loops in 5 slices along each axis ---')
for o in objs:
    nm = o['name']
    if not any(k in nm for k in ('inger','Thumb','Ring_5X','Knot')): continue
    dd = np.load('out/cache3mf/'+o['files'][0].split('/')[-1]+'.npz'); m = trimesh.Trimesh(dd['v'], dd['f'], process=False)
    res = {}
    for ax in range(3):
        n = np.eye(3)[ax]; lo, hi = m.bounds[0][ax], m.bounds[1][ax]; cnt = []
        for f in (0.2, 0.35, 0.5, 0.65, 0.8):
            L = loops(m, n, n*(lo + f*(hi-lo)), amax=40)
            cnt.append(sorted({(l[2], l[3]) for l in L}))
        res['XYZ'[ax]] = cnt
    print(nm, 'size', (m.bounds[1]-m.bounds[0]).round(1).tolist(), {k: [c[:4] for c in v] for k, v in res.items() if any(v)})
