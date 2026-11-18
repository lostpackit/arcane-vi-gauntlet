#!/usr/bin/env python3
"""Ring-safe partition: every plane stays >=10 mm away from the ring base."""
import vtk,numpy as np, json, os, time, collections
from vtk.util.numpy_support import vtk_to_numpy
OUT='/mnt/data/vi_redesign/V4_Work';os.makedirs(OUT,exist_ok=True)
src='/mnt/data/Full_Arm_Right (No Fingers).stl'
r=vtk.vtkSTLReader();r.SetFileName(src);r.Update();input_mesh=r.GetOutput()
# Use roomy cutting boxes, respecting right gauntlet xyz 422,294,600
regions=[]
for name,(x0,x1,y0,y1) in {
 'Cuff_Left_Front':(-1,211,-1,147), 'Cuff_Left_Rear':(-1,211,147,300),
 'Cuff_Right_Front':(211,425,-1,147),'Cuff_Right_Rear':(211,425,147,300),
}.items():regions.append((name,(x0,x1,y0,y1,-1,145)))
for name,bb in {
 'LightBand_Front_Left':(-1,211,-1,180,145,310),
 'LightBand_Front_Right':(211,425,-1,180,145,310),
 'LightBand_Rear_Left':(-1,100,180,300,145,310),
 'LightBand_REAR_RING_CARRIER':(100,300,180,300,145,310),
 'LightBand_Rear_Right':(300,425,180,300,145,310),
 'Wrist_Upper_Left':(-1,211,-1,300,310,400),
 'Wrist_Upper_Right':(211,425,-1,300,310,400),
 'Knuckles_Left':(-1,211,-1,300,400,601),
 'Knuckles_Right':(211,425,-1,300,400,601),
}.items():regions.append((name,bb))

def clip_box(mesh, bb):
 x0,x1,y0,y1,z0,z1=bb
 pc=vtk.vtkPlaneCollection()
 for o,n in [((x0,0,0),(1,0,0)),((x1,0,0),(-1,0,0)),((0,y0,0),(0,1,0)),((0,y1,0),(0,-1,0)),((0,0,z0),(0,0,1)),((0,0,z1),(0,0,-1))]:
  p=vtk.vtkPlane();p.SetOrigin(*o);p.SetNormal(*n);pc.AddItem(p)
 c=vtk.vtkClipClosedSurface();c.SetInputData(mesh);c.SetClippingPlanes(pc);c.SetGenerateFaces(True);c.Update();return c.GetOutput()

def transform(poly,rots):
 t=vtk.vtkTransform();t.PostMultiply()
 for ax,ang in rots:getattr(t,'Rotate'+ax)(ang)
 f=vtk.vtkTransformPolyDataFilter();f.SetInputData(poly);f.SetTransform(t);f.Update();out=f.GetOutput();b=out.GetBounds()
 tt=vtk.vtkTransform();tt.Translate(-b[0]+3,-b[2]+3,-b[4]);ff=vtk.vtkTransformPolyDataFilter();ff.SetInputData(out);ff.SetTransform(tt);ff.Update()
 return ff.GetOutput(), np.round([b[1]-b[0],b[3]-b[2],b[5]-b[4]],3).tolist(), rots

def edges(poly):
 f=vtk.vtkFeatureEdges();f.SetInputData(poly);f.BoundaryEdgesOn();f.NonManifoldEdgesOff();f.FeatureEdgesOff();f.ManifoldEdgesOff();f.Update(); nbd=f.GetOutput().GetNumberOfCells()
 f=vtk.vtkFeatureEdges();f.SetInputData(poly);f.BoundaryEdgesOff();f.NonManifoldEdgesOn();f.FeatureEdgesOff();f.ManifoldEdgesOff();f.Update();return nbd,f.GetOutput().GetNumberOfCells()

rows=[]
for i,(name,box) in enumerate(regions,1):
 tm=time.time();print('clip',i,name,flush=True)
 cut=clip_box(input_mesh,box)
 if i<=4:rot=[('X',180)] # cap z=145 down
 elif i<=6:rot=[('X',-90)] # y=180 face down
 elif i<=9:rot=[('X',90)]  # y=180 face down and optics uppermost
 elif i<=11:rot=[('Z',45)] if False else []
 else:rot=[('Y',90 if 'Left' in name else -90)]
 tilted,sz,rots=transform(cut,rot)
 # if upper pieces y width exceeds 256, use rotation Z -45
 if max(sz[:2])>256 and i in [10,11]:
  for angle in [15,-15,30,-30,45,-45]:
   q,dim,rr=transform(cut,[('Z',angle)])
   if max(dim[:2])<256:
    tilted,sz,rots=q,dim,rr;break
 origdim=np.array(cut.GetBounds()).reshape(3,2).ptp(axis=1) if False else list(np.round(np.array(cut.GetBounds()).reshape(3,2)[:,1]-np.array(cut.GetBounds()).reshape(3,2)[:,0],2))
 bd,nm=edges(tilted)
 path=f'{i:02d}_{name}_V4_RAW.stl'
 wr=vtk.vtkSTLWriter();wr.SetFileName(os.path.join(OUT,path));wr.SetFileTypeToBinary();wr.SetInputData(tilted);wr.Write()
 # connected components
 conn=vtk.vtkPolyDataConnectivityFilter();conn.SetInputData(tilted);conn.SetExtractionModeToAllRegions();conn.Update();regions_count=conn.GetNumberOfExtractedRegions()
 row={'id':i,'part':name,'source_limits_mm':box,'original_dimensions_mm':origdim,'print_dimensions_mm':sz,'rotations':rots,'boundary_edges':bd,'nonmanifold_edges':nm,'mesh_components':regions_count,'triangles':cut.GetNumberOfPolys(),'fits_nominal_X1C':max(sz)<=256,'file':path,'seconds':round(time.time()-tm,1)}
 rows.append(row)
 print(' RESULT',row['print_dimensions_mm'],'manifold',bd,nm,'conn',regions_count,'faces',row['triangles'],'fits',row['fits_nominal_X1C'],'s',row['seconds'],flush=True)
 json.dump(rows,open(OUT+'/manifest_partial.json','w'),indent=2)
json.dump(rows,open(OUT+'/ring_safe_partitions.json','w'),indent=2)
print('ALL COMPLETE',flush=True)
