"""Button pod v2 (2026-11-22, Claude print/vault session): pockets sized for the owner's HUAZIZ LED push buttons
(12 x 12 x 7 mm illuminated tact switch, through-hole legs). Owner caliper: 13.4 mm across the legs, 14.64 mm across the
white side tabs. Clip unchanged from pod_export.py (v1)."""
import numpy as np, manifold3d as m3, trimesh, zipfile, re, os
B=lambda s: m3.Manifold.cube(s); C=lambda h,r: m3.Manifold.cylinder(h,r,r,128)
PX, PY = 15.2, 13.8          # pocket: across the white tabs (14.64 + 0.56) x across the legs (13.4 + 0.4)
PD     = 4.5                 # pocket depth for the black body; white top + cap stand proud for the thumb
CAV_W, CAV_D = 2.6, 5.0      # perimeter channel under the pocket edge for legs + solder joints
ISL    = 7.6                 # central island the button body rests on (glue here)
def pod(HR, GAP=0.25, WALL=2.8, LEN=26.0, MOUTH=None):
    MOUTH = MOUTH or round(2*HR*0.8,1)
    PADT = PD + CAV_D + 1.2                       # pad thickness from the clip wall outwards
    PADW = 2*PY + 2.0 + 2*1.6                     # two pockets side by side (legs axis across the pad)
    clip=C(LEN,HR+GAP+WALL)-C(LEN+2,HR+GAP).translate((0,0,-1))
    mouth=B((40,MOUTH,LEN+2)).translate((-40,-MOUTH/2,-1))
    x0=HR+GAP+WALL-1.0; xf=x0+PADT                # pad from x0 to xf (button face at xf)
    pad=B((PADT,PADW,LEN)).translate((x0,-PADW/2,0)); cut=[]
    for yc in (-(PY/2+1.0), PY/2+1.0):
        zc=LEN/2
        cut.append(B((PD+0.1,PY,PX)).translate((xf-PD,yc-PY/2,zc-PX/2)))                       # body pocket
        ring=B((CAV_D,PY,PX)).translate((xf-PD-CAV_D,yc-PY/2,zc-PX/2)) - B((CAV_D+2,ISL,ISL)).translate((xf-PD-CAV_D-1,yc-ISL/2,zc-ISL/2))
        cut.append(ring)                                                                          # leg/solder channel round the island
        cut.append(B((CAV_D,6.0,zc-ISL/2+1.0)).translate((xf-PD-CAV_D,yc-3.0,-1.0)))             # wire exit down to the pod's bottom end
    p=(clip-mouth+pad)-m3.Manifold.batch_boolean(cut,m3.OpType.Add)-C(LEN+2,HR+GAP).translate((0,0,-1))
    p=p.decompose(); p.sort(key=lambda q:-q.volume()); p=p[0]; k=p.to_mesh()
    t=trimesh.Trimesh(np.asarray(k.vert_properties)[:,:3],np.asarray(k.tri_verts))
    t.apply_translation([128-t.bounds[:,0].mean(),128-t.bounds[:,1].mean(),-t.bounds[0][2]])
    return t, MOUTH, PADT, PADW
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','print')
for name,HR in [('Button_Pod_v2_HUAZIZ_for_18p8_printed_handle',9.4),('Button_Pod_v2_HUAZIZ_for_18p0_beech_rod',9.0)]:
    t,mouth,padt,padw=pod(HR); sc=trimesh.Scene(); sc.add_geometry(t,node_name=name,geom_name=name)
    fn=os.path.join(OUT,name+'.3mf'); sc.export(fn)
    print(name,'wt',t.is_watertight,'vol cm3 %.2f'%(t.volume/1000),'size',t.extents.round(1),'pad %.1f x %.1f'%(padt,padw),'clip ID %.1f mouth %.1f'%(2*(HR+0.25),mouth))
