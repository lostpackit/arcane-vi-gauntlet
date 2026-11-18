from pathlib import Path
import cadquery as cq
import trimesh
import numpy as np
out=Path('/mnt/data/vi_redesign/V4_Work/Hardware');out.mkdir(exist_ok=True)

def strap(label,L,W,T,nplate,col,gap):
 s=cq.Workplane('XY').rect(L,W).extrude(T).edges('|Z').fillet(2 if W>=14 else 1.5)
 # three key holes on both sides of the seam provide epoxy keying + surface area
 pts=[(xx,yy) for xx in (-L*.3,0,L*.3) for yy in (-W*.23,W*.23)]
 s=s.faces('>Z').workplane().pushPoints(pts).hole(3.2 if W<14 else 4.2)
 fn=out/(label+'.stl');cq.exporters.export(s,str(fn),tolerance=.06,angularTolerance=.15)
 m=trimesh.load(fn,force='mesh');assert m.is_volume
 rows=int(np.ceil(nplate/col));items=[]
 for i in range(nplate):
  mm=m.copy();mm.apply_translation([i%col*(L+gap),i//col*(W+gap),0]);items.append(mm)
 combined=trimesh.util.concatenate(items);combined.export(out/(f'{label}_BATCH_{nplate}x.stl'))
 print(label,'single dims',np.round(m.extents,2),'batch',np.round(combined.extents,2),'mass',round(m.volume/1000,1),'cm3',flush=True)
strap('Bonded_Spline_Long_65x14x2p4',65,14,2.4,18,3,6)
strap('Bonded_Spline_Short_38x12x2p2',38,12,2.2,18,4,7)
# Native optical parts; ring base is deliberately NOT separately printed (already integrated in shell #8).
for f,name,reflect in [('/mnt/data/Circle_Light_Cover.stl','R_Circle_Light_Cover_Original',False),('/mnt/data/Circle_Light_Cover.stl','L_Circle_Light_Cover_Mirrored',True)]:
 m=trimesh.load(f,force='mesh',process=True)
 if reflect:
  center=float((m.bounds[0,0]+m.bounds[1,0])/2)
  mat=np.eye(4);mat[0,0]=-1;mat[0,3]=2*center;m.apply_transform(mat)
 m.export(out/(name+'.stl'));print(name,np.round(m.extents,2),m.is_volume,flush=True)
