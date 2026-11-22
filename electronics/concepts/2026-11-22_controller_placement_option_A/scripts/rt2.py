import trimesh, numpy as np, json
from PIL import Image, ImageDraw, ImageFont
import fast_simplification as fs
from trimesh.ray.ray_pyembree import RayMeshIntersector
F=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',s); FB=lambda s: ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',s)
col={'shell':(205,205,205),'sled':(232,135,30),'board':(35,70,50),'pod':(47,111,208),'bank':(138,92,194),'handle':(176,138,90),'switches':(25,25,25),'led':(24,165,88),'usb':(221,51,51),'buttons':(47,111,208),'screw':(150,150,155)}
def tubes(pts,r=1.3):
    pts=np.array(pts)[::3]; return trimesh.util.concatenate([trimesh.creation.cylinder(radius=r,segment=[a,b],sections=8) for a,b in zip(pts[:-1],pts[1:]) if np.linalg.norm(b-a)>0.5])
class Scene:
    def __init__(s,meshes):
        s.m=trimesh.util.concatenate([m for _,m in meshes]); s.fc=np.vstack([np.tile(col[k],(len(m.faces),1)) for k,m in meshes]); s.r=RayMeshIntersector(s.m)
    def cam(s,eye,target,fov,W,H,up=(0,1,0)):
        s.eye=np.array(eye,float); t=np.array(target,float); f=t-s.eye; f/=np.linalg.norm(f); r=np.cross(f,up); r/=np.linalg.norm(r); u=np.cross(r,f)
        s.f,s.rr,s.u,s.a,s.W,s.H=f,r,u,np.tan(np.deg2rad(fov)/2),W,H
    def render(s):
        xs=np.linspace(-s.a,s.a,s.W); ys=np.linspace(s.a*s.H/s.W,-s.a*s.H/s.W,s.H); X,Y=np.meshgrid(xs,ys)
        D=s.f[None]+X.reshape(-1,1)*s.rr[None]+Y.reshape(-1,1)*s.u[None]; D/=np.linalg.norm(D,axis=1)[:,None]
        tri=s.r.intersects_first(np.tile(s.eye,(len(D),1)),D); img=np.full((len(D),3),255.0); h=tri>=0
        n=s.m.face_normals[tri[h]]; n=np.where(((n*D[h]).sum(1)>0)[:,None],-n,n); L=-s.f+0.6*s.u+0.3*s.rr; L/=np.linalg.norm(L)
        img[h]=s.fc[tri[h]]*(0.35+0.65*np.clip(n@L,0,1))[:,None]
        return Image.fromarray(img.reshape(s.H,s.W,3).clip(0,255).astype(np.uint8))
    def px(s,p):
        d=np.array(p,float)-s.eye; z=d@s.f; x=(d@s.rr)/z; y=(d@s.u)/z
        return (int((x/s.a+1)/2*s.W), int((1-(y/(s.a*s.H/s.W)))/2*s.H))
def label(dr,sc,p,text,off,color=(20,20,20),size=26):
    a=sc.px(p); b=(a[0]+off[0],a[1]+off[1]); f=F(size)
    bb=dr.multiline_textbbox((0,0),text,font=f); w,h=bb[2]-bb[0],bb[3]-bb[1]
    x=b[0]+6 if off[0]>=0 else b[0]-6-w; y=b[1]-h-4 if off[1]<0 else b[1]+4
    x=max(8,min(sc.W-w-8,x)); y=max(60,min(sc.H-h-8,y))
    dr.rectangle([x-4,y-3,x+w+4,y+h+6],fill=(255,255,255))
    dr.line([a,b],fill=color,width=3); dr.ellipse([a[0]-5,a[1]-5,a[0]+5,a[1]+5],fill=color)
    dr.multiline_text((x,y),text,font=f,fill=color)
# ---------- in-gauntlet views ----------
A=trimesh.load('armR.ply'); Hm=A.slice_plane([211.0,0,0],[-1,0,0])
v,f=fs.simplify(Hm.vertices.astype(np.float32),Hm.faces.astype(np.int64),target_reduction=1-400000/len(Hm.faces)); Hm=trimesh.Trimesh(v,f,process=False)
P={k:trimesh.load(f'{k}_placed.ply') for k in ['sled','board','pod','bank','handle','switches']}; R=json.load(open('routes.json'))
sc=Scene([('shell',Hm)]+list(P.items())+[(k,tubes(R[k])) for k in R])
sc.cam((780,40,300),(205,170,290),48,1600,900); im=sc.render(); dr=ImageDraw.Draw(im)
label(dr,sc,(214,213,236),'controller board on its sled,\nglued under the LED ring',(120,-230),(166,80,0))
label(dr,sc,(211,236,263),'LED lead up into the ring',(-330,-160),(24,140,70))
label(dr,sc,(275,140,370),'button pod clipped\non the handle',(-40,170),(30,80,170))
label(dr,sc,(100,150,95),'power bank on the cuff wall\n(example size, not chosen yet)',(-60,200),(100,60,150))
label(dr,sc,(170,216,160),'USB-C power cable',(90,130),(190,40,40))
dr.text((20,20),'Right gauntlet: near half cut away, looking in from the thumb side',font=FB(30),fill=(20,20,20))
dr.text((20,860),'← knuckles / fingers',font=F(24),fill=(90,90,90)); dr.text((1360,860),'cuff opening →',font=F(24),fill=(90,90,90))
im.save('view_inside.png')
sc.cam((330,120,205),(225,205,265),55,1400,950); im=sc.render(); dr=ImageDraw.Draw(im)
label(dr,sc,(218,217,230),'sled, glued to the\nceiling under the ring',(60,-230),(166,80,0))
label(dr,sc,(205,209,228),'board: USB-C end toward\nthe cuff, labels facing down',(-120,220),(30,30,30))
label(dr,sc,(211,236,263),'LED lead into the ring',(-200,-150),(24,140,70))
bw=np.array(R['buttons']); label(dr,sc,bw[int(len(bw)*0.62)],'button wires from the handle',(-60,170),(30,80,170))
dr.text((20,20),'Close-up from below: board and sled under the LED ring',font=FB(30),fill=(20,20,20))
im.save('view_close.png')
# ---------- parts on their own ----------
pl=json.load(open('place.json')); S=P['sled']; Bd=P['board']
c=S.centroid
screws=trimesh.util.concatenate([trimesh.creation.cylinder(radius=1.25,segment=[[h[0],h[1]-12,h[2]],[h[0],h[1]-1,h[2]]]) for h in pl['holes']]+[trimesh.creation.cylinder(radius=2.2,height=1.6,transform=trimesh.transformations.translation_matrix([h[0],h[1]-12.8,h[2]])@trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0])) for h in pl['holes']])
Bx=Bd.copy(); Bx.apply_translation([0,-14,0]); sx=screws.copy(); sx.apply_translation([0,-14,0])
sc2=Scene([('sled',S),('board',Bx),('screw',sx)]); sc2.cam(c+np.array([95,-85,-55]),c+np.array([0,-12,0]),40,1100,900); im1=sc2.render(); d1=ImageDraw.Draw(im1)
label(d1,sc2,c+np.array([0,8,-8]),'top follows the ridged\nceiling: glue face',(-40,-150),(166,80,0),24)
label(d1,sc2,np.array([pl['holes'][0][0],pl['Yb']-4.4,pl['holes'][0][2]]),'4 posts: M2.5 screws\nthrough the board holes',(-200,-60),(80,80,80),24)
label(d1,sc2,np.array([200.0,pl['Yb']-1.0,247.0]),'cable-tie bar for strain\nrelief at the wire end',(180,-80),(166,80,0),24)
label(d1,sc2,np.array([211,pl['board_low']-14,232]),'Sparkle Motion Mini\n(Adafruit 3D model)',(40,150),(30,30,30),24)
d1.text((15,15),'Sled 36 × 26 mm (exploded)',font=FB(28),fill=(20,20,20)); im1.save('part_sled.png')
Pp=P['pod']; Sw=P['switches']; hs=trimesh.creation.cylinder(radius=9.4,segment=[[240,156,375.95],[310,156,375.95]])
sc3=Scene([('pod',Pp),('switches',Sw),('handle',hs)]); cp=Pp.centroid; sc3.cam(cp+np.array([70,-80,-95]),cp,38,1100,900); im2=sc3.render(); d2=ImageDraw.Draw(im2)
swc=[m.centroid for m in Sw.split(only_watertight=False)]; swc=sorted(swc,key=lambda q:q[0]); label(d2,sc3,swc[0],'two 12 × 12 mm push buttons',(-260,160),(20,20,20),24)
bk=np.array([287.5,156.0,375.95-12.3]); label(d2,sc3,bk,'C-clip snaps onto the 18.8 mm handle;\nslide and turn it to suit your thumb',(-120,-230),(30,80,170),24)
label(d2,sc3,np.array([305,156-9.4,375.95]),'handle',(60,120),(120,90,50),24)
d2.text((15,15),'Button pod 26 × 31 × 30 mm',font=FB(28),fill=(20,20,20)); im2.save('part_pod.png')
w=Image.new('RGB',(2200,900),'white'); w.paste(im1,(0,0)); w.paste(im2,(1100,0)); w.save('parts.png')
