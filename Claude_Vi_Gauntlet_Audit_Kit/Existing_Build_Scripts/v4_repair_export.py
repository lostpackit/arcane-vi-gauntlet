import os,json,glob,time,sys
import vtk,numpy as np,trimesh
from vtk.util.numpy_support import vtk_to_numpy
# Import only functions (avoid running patch on V2)
namespace={}
s=open('/mnt/data/vi_redesign/repair_v2.py').read().split('\nrows=[]')[0]
exec(s,namespace)
patch=namespace['patch'];boxinfo=namespace['info']
ROOT='/mnt/data/vi_redesign/V4_Work';OUT=ROOT+'/Print_Shells';os.makedirs(OUT,exist_ok=True)
manifest=json.load(open(ROOT+'/ring_safe_partitions.json'))
report=[]
for row in manifest:
 ts=time.time();idx=row['id'];name=row['part'];print('PROCESS',idx,name,flush=True)
 r=vtk.vtkSTLReader();r.SetFileName(os.path.join(ROOT,row['file']));r.Update();poly=r.GetOutput()
 if row['mesh_components']>1:
  conn=vtk.vtkPolyDataConnectivityFilter();conn.SetInputData(poly);conn.SetExtractionModeToLargestRegion();conn.Update()
  geo=vtk.vtkGeometryFilter();geo.SetInputConnection(conn.GetOutputPort());geo.Update();poly=geo.GetOutput();
  print('  DROPPED',row['mesh_components']-1,'floating disconnected minor components',flush=True)
 points=vtk_to_numpy(poly.GetPoints().GetData()).copy().astype('float32')
 faces=vtk_to_numpy(poly.GetPolys().GetConnectivityArray()).reshape(-1,3).copy().astype('int64')
 original_faces=len(faces)
 mesh=trimesh.Trimesh(vertices=points,faces=faces,process=False)
 modified,stats=patch(mesh)
 result=OUT+f'/R_{idx:02d}_{name}_X1C.stl'
 modified.export(result)
 rr=vtk.vtkSTLReader();rr.SetFileName(result);rr.Update();p2=rr.GetOutput();vv=vtk_to_numpy(p2.GetPoints().GetData());ff=vtk_to_numpy(p2.GetPolys().GetConnectivityArray()).reshape(-1,3)
 boundary,un,inv,cnt,ee=boxinfo(ff)
 dims=np.round(vv.max(axis=0)-vv.min(axis=0),2).tolist()
 # Extra connected component check
 cx=vtk.vtkPolyDataConnectivityFilter();cx.SetInputData(p2);cx.SetExtractionModeToAllRegions();cx.Update();comps=cx.GetNumberOfExtractedRegions()
 is_ok= len(boundary)==0 and np.sum(cnt>2)==0 and comps==1 and max(dims)<250
 print('  REPAIRED',stats['initial_boundary_edges'],'=>',len(boundary),'nm',sum(cnt>2),'cmp',comps,'size',dims,'PASS',is_ok,'time',int(time.time()-ts),flush=True)
 if not is_ok:print('  WARNING failed',flush=True)
 from trimesh import transformations
 left=modified.copy()
 mat=np.eye(4);mat[0,0]=-1;mat[0,3]=256
 left.apply_transform(mat);left.invert()
 lpath=OUT+f'/L_{idx:02d}_{name}_X1C.stl';left.export(lpath)
 report.append({'id':idx,'name':name,'right':os.path.basename(result),'left':os.path.basename(lpath),'dims_mm':dims,'face_count':len(ff),'components':comps,'boundary_edges':len(boundary),'nonmanifold_edges':int(sum(cnt>2)),'pass':bool(is_ok),'repair':stats,'seconds':int(time.time()-ts)})
 json.dump(report,open(OUT+'/validation_progress.json','w'),indent=2)
json.dump(report,open(OUT+'/Shell_Validation_Report.json','w'),indent=2)
print('DONE',len(report),sum(x['pass'] for x in report),'passed',flush=True)
