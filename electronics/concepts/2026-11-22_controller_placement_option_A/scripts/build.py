import trimesh, numpy as np, manifold3d as m3, json
def to_m(t): return m3.Manifold(m3.Mesh(vert_properties=np.asarray(t.vertices,np.float32), tri_verts=np.asarray(t.faces,np.uint32)))
def to_t(M): k=M.to_mesh(); return trimesh.Trimesh(np.asarray(k.vert_properties)[:,:3], np.asarray(k.tri_verts), process=False)
B=lambda s: m3.Manifold.cube(s)
A=trimesh.load('armR.ply'); AM=to_m(A); print('arm manifold ok', AM.status())
X0=211.0
# ceiling heightmap over footprint
xs=np.arange(X0-14,X0+14.01,1.0); zs=np.arange(212,252.01,1.0)
O=np.array([[x,160,z] for z in zs for x in xs]); D=np.tile([0,1,0],(len(O),1))
loc,ri,_=A.ray.intersects_location(O,D,multiple_hits=False)
H=np.full(len(O),np.nan); H[ri]=loc[:,1]; H=H.reshape(len(zs),len(xs))
print('ceiling over footprint: min %.1f max %.1f'%(np.nanmin(H),np.nanmax(H)))
print('ceiling along Z at X211 near hole:',[(z,round(float(H[i,len(xs)//2]),1)) for i,z in enumerate(zs) if z>=244])
# --- board placement (Adafruit 6160 STL, local: x along board, USB at x<0, module side -z)
Zb=216.0; Yb_flat=None
EDGE=13.0; ZS0, ZS1 = Zb-3.0, Zb+33.0                         # sled footprint
sub=H[(zs>=ZS0)&(zs<=ZS1)][:, (xs>=X0-EDGE)&(xs<=X0+EDGE)]
Yb=float(np.nanmin(sub))-2.0                                  # flat underside, >=2 mm under lowest ceiling point
STAND=4.5; ytop_pcb_bottom=Yb-STAND
R=np.array([[0,-1,0],[0,0,-1],[1,0,0]],float)                 # columns: local x->+Z, local y->-X, local z->-Y
# rows are world X,Y,Z : X = -y, Y = -z, Z = x
def placeL(p): p=np.asarray(p,float); return np.c_[X0-(p[:,1]-9.875), ytop_pcb_bottom-(p[:,2]-0.15), Zb+p[:,0]]
brd=trimesh.load('/home/claude/ext/cad/6160 Sparkle Motion Mini/6160 Sparkle Motion Mini.stl',force='mesh')
brd=trimesh.Trimesh(placeL(brd.vertices), brd.faces, process=False)   # proper rotation (det +1)
holes_local=[(2.54,2.54),(27.94,2.667),(2.54,17.145),(27.94,17.0815)]
hw=placeL([[x,y,0.15] for x,y in holes_local])
# --- sled
base=B((2*EDGE, 237.0-Yb, ZS1-ZS0)).translate((X0-EDGE, Yb, ZS0)) - AM
parts=[base]
for h in hw:
    post=m3.Manifold.cylinder(STAND,2.9,2.9,40).rotate((-90,0,0)).translate((h[0],Yb-STAND,h[2]))
    parts.append(post)
sled=m3.Manifold.batch_boolean(parts, m3.OpType.Add)
for h in hw:
    sled=sled-m3.Manifold.cylinder(STAND+6,1.1,1.1,24).rotate((-90,0,0)).translate((h[0],Yb-STAND-0.5,h[2]))   # 2.2 mm pilot for M2.5 self-tapping
# strain-relief bridge for the wires at the pad end (zip tie passes over)
bridge=B((2*EDGE,2.0,4.0)).translate((X0-EDGE,Yb-2.0,ZS1-4.0)) - B((2*EDGE-8,2.0+0.2,4.2)).translate((X0-EDGE+4,Yb-2.1,ZS1-4.1))
sled=sled+bridge
sled=sled.decompose(); sled.sort(key=lambda q:-q.volume()); sledM=sled[0]
S=to_t(sledM)
print('sled vol cm3 %.2f, extents'%(sledM.volume()/1000), S.extents.round(1), 'overlap with arm mm3 %.3f'%((sledM^AM).volume()))
print('Yb (flat underside) %.1f, PCB bottom Y %.1f, board lowest Y %.1f'%(Yb, ytop_pcb_bottom, brd.bounds[0][1]))
# --- button pod (rebuild of Mounts_CONCEPT/mounts.py parameters) along +X axis, centred on handle axis
HY,HZ,HR=156.0,375.95,9.4; GAP,WALL,LEN=0.25,2.8,26.0; SW,SWD,PADT,PADW=12.5,4.2,6.0,30.0
C=lambda h,r: m3.Manifold.cylinder(h,r,r,96)
clip=C(LEN,HR+GAP+WALL)-C(LEN+2,HR+GAP).translate((0,0,-1))
mouth=B((40,15.0,LEN+2)).translate((-40,-7.5,-1))
x0=HR+GAP+WALL-1.0
pad=B((PADT+1.2,PADW,LEN)).translate((x0,-PADW/2,0))
pk=[]
for yc in (-7.45,7.45):
    pk.append(B((SWD+0.1,SW,SW)).translate((x0+PADT+1.2-SWD,yc-SW/2,(LEN-SW)/2)))
    pk.append(B((PADT,9.0,3.0)).translate((x0+1.6,yc-4.5,-1)))
    pk.append(B((PADT-SWD-1.4,9.0,(LEN-SW)/2+3.5)).translate((x0+1.6,yc-4.5,-0.5)))
pod=(clip-mouth+pad)-m3.Manifold.batch_boolean(pk,m3.OpType.Add)-C(LEN+2,HR+GAP).translate((0,0,-1))
pod=pod.decompose(); pod.sort(key=lambda q:-q.volume()); pod=pod[0]
# local: cylinder axis = local z, pad faces local +x.  World: axis along +X (handle), pad faces direction d in YZ plane
ang=np.deg2rad(225)                       # pad facing -Y/-Z (down and back toward the wrist): adjustable by rotating the clip
d=np.array([0,np.sin(ang),np.cos(ang)])   # (0,-0.707,-0.707)
ez=np.array([-1.0,0,0]); ex=d; ey=np.cross(ez,ex)
M=np.eye(4); M[:3,0]=ex; M[:3,1]=ey; M[:3,2]=ez; M[:3,3]=[288.0,HY,HZ]   # wire slots exit the +X end face
P=to_t(pod); P.apply_transform(M)
podM=to_m(P)
print('pod vs arm overlap mm3 %.3f'%((podM^AM).volume()), 'pod bounds', P.bounds.round(1).tolist())
handle=trimesh.creation.cylinder(radius=HR,segment=[[86.0,HY,HZ],[336.0,HY,HZ]])
sw=[]
for yc in (-7.45,7.45):
    s=trimesh.creation.box(extents=[3.6,12,12]); s.apply_translation([x0+PADT+1.2-SWD+1.8,yc,LEN/2]); s.apply_transform(M); sw.append(s)
    cap=trimesh.creation.cylinder(radius=3.0,height=4.0); cap.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[0,1,0])); cap.apply_translation([x0+PADT+1.2+2.0,yc,LEN/2]); cap.apply_transform(M); sw.append(cap)
for n,m in [('sled',S),('board',brd),('pod',P),('handle',handle)]: m.export(f'{n}_placed.ply')
trimesh.util.concatenate(sw).export('switches_placed.ply')
json.dump(dict(X0=X0,Zb=Zb,Yb=Yb,pcb_bottom=ytop_pcb_bottom,board_low=float(brd.bounds[0][1]),holes=hw.tolist()),open('place.json','w'),indent=1)
