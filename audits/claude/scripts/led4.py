import numpy as np, trimesh
rf = np.load('out/ringframe.npz'); n, c, u, w = rf['n'], rf['c'], rf['u'], rf['w']
ol = trimesh.load('out/light_assembled.stl', force='mesh'); oc = trimesh.load('out/cover_assembled.stl', force='mesh')
s8 = np.load('out/asm_R_08.npz'); shell = trimesh.Trimesh(s8['v'], s8['f'], process=False)
def P(r, ang, h): a = np.radians(ang); return c + r*(np.cos(a)*u + np.sin(a)*w) + h*n
def first_hit(m, o, d):
    loc, ir, _ = m.ray.intersects_location(o, d, multiple_hits=True)
    out = np.full(len(o), np.nan)
    t = ((loc - o[ir]) * d[ir]).sum(1)
    for i in range(len(o)):
        s = t[ir == i]; s = s[s > 1e-6]
        if len(s): out[i] = s.min()
    return out
angs = np.arange(0, 360, 5)
for name, m in (('original Circle_Light', ol), ('V4 shell 08', shell)):
    print('=====', name)
    # axial probe from above (h=+11.5 just under cover plane? use +40 for light, for shell also +40)
    for r in (20, 30, 35, 42, 50, 55, 58):
        o = np.array([P(r, a, 40) for a in angs]); d = np.tile(-n, (len(o),1))
        t = first_hit(m, o, d); h = 40 - t
        print(f' top-down first hit r={r}: h min {np.nanmin(h):.2f} med {np.nanmedian(h):.2f} max {np.nanmax(h):.2f}')
    # inside the chamber: from (r=42,h) cast outward / inward / up / down
    for h0 in (-2, 0, 3, 6, 9):
        o = np.array([P(42, a, h0) for a in angs])
        do = np.array([np.cos(np.radians(a))*u + np.sin(np.radians(a))*w for a in angs])
        ro = 42 + first_hit(m, o, do); ri = 42 - first_hit(m, o, -do)
        print(f' chamber h={h0}: outer wall r min {np.nanmin(ro):.2f} med {np.nanmedian(ro):.2f} max {np.nanmax(ro):.2f} | inner wall r min {np.nanmin(ri):.2f} med {np.nanmedian(ri):.2f} max {np.nanmax(ri):.2f}  inner-wall anomalies at deg {[int(a) for a,x in zip(angs,ri) if not abs(x-np.nanmedian(ri))<0.5]}  outer anomalies {[int(a) for a,x in zip(angs,ro) if not abs(x-np.nanmedian(ro))<0.5]}')
    for r in (31, 36, 42, 48, 54):
        o = np.array([P(r, a, 3) for a in angs])
        up = 3 + first_hit(m, o, np.tile(n,(len(o),1))); dn = 3 - first_hit(m, o, np.tile(-n,(len(o),1)))
        print(f' chamber r={r}: ceiling h min {np.nanmin(up):.2f} med {np.nanmedian(up):.2f} max {np.nanmax(up):.2f} nan {int(np.isnan(up).sum())} | floor h min {np.nanmin(dn):.2f} med {np.nanmedian(dn):.2f} max {np.nanmax(dn):.2f} floor anomalies deg {[int(a) for a,x in zip(angs,dn) if not abs(x-np.nanmedian(dn))<0.5]}')
