import vtk,numpy as np, json, os, math
from PIL import Image,ImageDraw,ImageFont
ROOT='/mnt/data/vi_redesign/V4_Work';MAN=json.load(open(ROOT+'/ring_safe_partitions.json'));OUT=ROOT+'/Final_Views';os.makedirs(OUT,exist_ok=True)
r=vtk.vtkSTLReader();r.SetFileName('/mnt/data/Full_Arm_Right (No Fingers).stl');r.Update();full=r.GetOutput()

def cut(b):
 x0,x1,y0,y1,z0,z1=b;planes=vtk.vtkPlaneCollection()
 for pt,n in [((x0,0,0),(1,0,0)),((x1,0,0),(-1,0,0)),((0,y0,0),(0,1,0)),((0,y1,0),(0,-1,0)),((0,0,z0),(0,0,1)),((0,0,z1),(0,0,-1))]:
  p=vtk.vtkPlane();p.SetOrigin(*pt);p.SetNormal(*n);planes.AddItem(p)
 c=vtk.vtkClipClosedSurface();c.SetInputData(full);c.SetClippingPlanes(planes);c.SetGenerateFaces(True);c.Update()
 poly=c.GetOutput()
 if poly.GetNumberOfPolys()>100000:
  d=vtk.vtkQuadricDecimation();d.SetInputData(poly);d.SetTargetReduction(.80);d.VolumePreservationOn();d.Update();return d.GetOutput()
 return poly
parts=[cut(m['source_limits_mm']) for m in MAN]
colors=[(0.22,.43,.62),(.27,.60,.75),(.29,.53,.76),(.37,.69,.79),(.67,.64,.49),(.73,.72,.56),(.50,.64,.53),(.91,.63,.25),(.59,.72,.63),(.32,.64,.72),(.30,.54,.66),(.45,.56,.77),(.36,.43,.65)]

def render(f,vec,exploded=False):
 ren=vtk.vtkRenderer();ren.SetBackground(.976,.980,.989);ren.SetBackground2(.94,.955,.972);ren.GradientBackgroundOn()
 for i,(m,p) in enumerate(zip(MAN,parts)):
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputData(p);mapper.ScalarVisibilityOff()
  a=vtk.vtkActor();a.SetMapper(mapper);a.GetProperty().SetColor(*colors[i]);a.GetProperty().SetSpecular(.13);a.GetProperty().SetSpecularPower(22)
  if exploded:
   x0,x1,y0,y1,z0,z1=m['source_limits_mm'];dx=(-1 if x1<=211 else (1 if x0>=211 else 0))*23
   dy=(-1 if y1<=180 else (1 if y0>=180 else 0))*26
   dz= -40 if i<4 else 0 if i<9 else 40 if i<11 else 76
   a.SetPosition(dx,dy,dz)
  ren.AddActor(a)
 rw=vtk.vtkRenderWindow();rw.SetOffScreenRendering(1);rw.SetSize(900,1100);rw.AddRenderer(ren)
 cam=ren.GetActiveCamera();cen=(211,147,300)
 cam.SetFocalPoint(*cen);cam.SetPosition(*[cen[i]+vec[i]*1500 for i in range(3)]);cam.SetViewUp(0,0,1);cam.ParallelProjectionOn();cam.SetParallelScale(410 if exploded else 360);ren.ResetCameraClippingRange();rw.Render()
 w=vtk.vtkWindowToImageFilter();w.SetInput(rw);w.SetInputBufferTypeToRGB();w.ReadFrontBufferOff();w.Update();save=vtk.vtkPNGWriter();save.SetFileName(OUT+'/'+f);save.SetInputConnection(w.GetOutputPort());save.Write()
 print('rendered',f,flush=True)
for fname,c,e in [('Palm_Side.png',(0,-1,0),False),('Lighting_Side.png',(0,1,0),False),('Exploded.png',(1,-1,.7),True),('Ring_Carrier.png',(1,1,.6),False)]:render(fname,c,e)
W,H=2100,1400;im=Image.new('RGB',(W,H),'#f4f7fb');d=ImageDraw.Draw(im)
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';h1=ImageFont.truetype(font,48);h2=ImageFont.truetype(font,27);body=ImageFont.truetype(font,21)
d.text((65,25),'VI GAUNTLET  |  X1C 13-SECTION ARMOR',font=h1,fill='#18344c')
d.text((68,95),'V4 ring-safe cut layout  •  full size  •  13 watertight mesh pieces per gauntlet',font=body,fill='#52758b')
for x,f,t in [(45,'Palm_Side.png','PALM / HAND'),(730,'Lighting_Side.png','BACK / CIRCLE LIGHT'),(1415,'Exploded.png','EXPLODED SECTIONS')]:
 pic=Image.open(OUT+'/'+f).convert('RGB');pic.thumbnail((635,1120));im.paste(pic,(x,160));d.text((x+100,1290),t,font=h2,fill='#1a405d')
im.save(OUT+'/V4_Shell_Layout.png',optimize=True)
print('DONE')
