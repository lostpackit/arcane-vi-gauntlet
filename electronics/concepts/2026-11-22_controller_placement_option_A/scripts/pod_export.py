import numpy as np, manifold3d as m3, trimesh, zipfile, re
B=lambda s: m3.Manifold.cube(s); C=lambda h,r: m3.Manifold.cylinder(h,r,r,128)
def pod(HR, GAP=0.25, WALL=2.8, LEN=26.0, MOUTH=None):
    SW,SWD,PADT,PADW=12.5,4.2,6.0,30.0
    MOUTH = MOUTH or round(2*HR*0.8,1)                      # snap opening ~80 % of rod diameter
    clip=C(LEN,HR+GAP+WALL)-C(LEN+2,HR+GAP).translate((0,0,-1))
    mouth=B((40,MOUTH,LEN+2)).translate((-40,-MOUTH/2,-1))
    x0=HR+GAP+WALL-1.0; pad=B((PADT+1.2,PADW,LEN)).translate((x0,-PADW/2,0)); pk=[]
    for yc in (-7.45,7.45):
        pk.append(B((SWD+0.1,SW,SW)).translate((x0+PADT+1.2-SWD,yc-SW/2,(LEN-SW)/2)))
        pk.append(B((PADT,9.0,3.0)).translate((x0+1.6,yc-4.5,-1)))
        pk.append(B((PADT-SWD-1.4,9.0,(LEN-SW)/2+3.5)).translate((x0+1.6,yc-4.5,-0.5)))
    p=(clip-mouth+pad)-m3.Manifold.batch_boolean(pk,m3.OpType.Add)-C(LEN+2,HR+GAP).translate((0,0,-1))
    p=p.decompose(); p.sort(key=lambda q:-q.volume()); p=p[0]; k=p.to_mesh()
    t=trimesh.Trimesh(np.asarray(k.vert_properties)[:,:3],np.asarray(k.tri_verts))
    t.apply_translation([128-t.bounds[:,0].mean(),128-t.bounds[:,1].mean(),-t.bounds[0][2]])   # clip axis vertical, on the bed
    return t, MOUTH
for name,HR in [('Button_Pod_for_18p8_printed_handle',9.4),('Button_Pod_for_18p0_beech_rod',9.0)]:
    t,mouth=pod(HR); sc=trimesh.Scene(); sc.add_geometry(t,node_name=name,geom_name=name)
    fn=f'/home/claude/arcane-vi-gauntlet/electronics/concepts/2026-11-22_controller_placement_option_A/print/{name}.3mf'
    import os; os.makedirs(os.path.dirname(fn),exist_ok=True); sc.export(fn)
    z=zipfile.ZipFile(fn); x=[n for n in z.namelist() if n.endswith('.model')][0]; names=re.findall(r'name="([^"]+)"',z.read(x).decode())
    print(name,'wt',t.is_watertight,'vol cm3 %.2f'%(t.volume/1000),'size',t.extents.round(1),'clip ID %.1f mouth %.1f'%(2*(HR+0.25),mouth),'3mf names',names[:3])
