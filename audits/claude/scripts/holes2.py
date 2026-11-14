import numpy as np, trimesh, warnings; warnings.filterwarnings('ignore')
d = np.load('out/fullR.npz'); full = trimesh.Trimesh(d['v'], d['f'], process=False)
fb = trimesh.load('out/placed_Fingers_Base.stl', force='mesh')
def loops(m, n, o, amax=60, amin=2):
    sec = m.section(plane_origin=o, plane_normal=n)
    if sec is None: return []
    p2, T = sec.to_2D(); out = []
    for poly in p2.polygons_closed:
        if poly is not None and amin < poly.area < amax:
            c = poly.centroid.coords[0]; c3 = (T @ np.array([c[0], c[1], 0, 1]))[:3]; b = poly.bounds
            out.append((round(poly.area,1), c3.round(1).tolist(), round(b[2]-b[0],2), round(b[3]-b[1],2)))
    return out
print('Full arm: finger string holes by Z (holes near X=114,179,245,308)')
for z in range(494, 541, 2):
    L = [l for l in loops(full, [0,0,1], [0,0,z], amax=14) if 130 < l[1][1] < 150]
    print(' Z', z, [(l[1][0], l[1][1], l[2], l[3]) for l in sorted(L, key=lambda x: x[1][0])])
print('3MF Fingers_Base (placed): small loops by Z')
for z in range(521, 541, 3):
    L = loops(fb, [0,0,1], [0,0,z], amax=14); print(' Z', z, [(l[1][0], l[1][1], l[2], l[3]) for l in sorted(L, key=lambda x: x[1][0])])
print('Thumb-side hole trace (Y planes), X>320')
for y in range(125, 186, 6):
    L = [l for l in loops(full, [0,1,0], [0,y,0], amax=80) if l[1][0] > 320 and l[1][2] > 420]
    print(' Y', y, [(l[1][0], l[1][2], l[2], l[3], l[0]) for l in L])
print('little-finger-side slot (X 50-72) trace by Z')
for z in (410, 425, 440, 500, 530, 545, 555):
    L = [l for l in loops(full, [0,0,1], [0,0,z], amax=80) if l[1][0] < 80]; print(' Z', z, [(l[1][0], l[1][1], l[2], l[3]) for l in L])
# hand cavity ceiling height above handle along finger lines
for x in (114.1, 179.4, 244.6, 308.2, 211):
    o = np.array([[x, 143.0, 420.0]]); loc, ir, _ = full.ray.intersects_location(o, [[0,0,1.0]], multiple_hits=True)
    print(' cavity ceiling above (x=%.1f,y=143): Z hits' % x, np.sort(loc[:,2]).round(1).tolist()[:4])
