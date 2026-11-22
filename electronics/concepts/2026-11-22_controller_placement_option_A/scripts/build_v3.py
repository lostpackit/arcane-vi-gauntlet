import trimesh, numpy as np, manifold3d as m3, json
def to_m(t): return m3.Manifold(m3.Mesh(vert_properties=np.asarray(t.vertices,np.float32), tri_verts=np.asarray(t.faces,np.uint32)))
def to_t(M): k=M.to_mesh(); return trimesh.Trimesh(np.asarray(k.vert_properties)[:,:3], np.asarray(k.tri_verts), process=False)
B=lambda s: m3.Manifold.cube(s)
def cylY(y0,y1,x,z,r,n=48): return m3.Manifold.cylinder(y1-y0,r,r,n).rotate((-90,0,0)).translate((x,y0,z))   # axis along +Y from y0 to y1
A=trimesh.load('armR.ply'); AM=to_m(A)
X0,Zb=211.0,216.0; STAND=4.2; EDGE=17.0; ZS0,ZS1=Zb-3.0,Zb+33.0
xs=np.arange(X0-EDGE,X0+EDGE+0.01,1.0); zs=np.arange(ZS0,ZS1+0.01,1.0)
O=np.array([[x,160,z] for z in zs for x in xs]); loc,ri,_=A.ray.intersects_location(O,np.tile([0,1,0],(len(O),1)),multiple_hits=False)
Hc=np.full(len(O),np.nan); Hc[ri]=loc[:,1]; Yb=float(np.nanmin(Hc))-2.0
PB=Yb-STAND                                   # PCB bottom (module side faces up)
def placeL(p): p=np.asarray(p,float); return np.c_[X0-(p[:,1]-9.875), PB-(p[:,2]-0.0)-0.05, Zb+p[:,0]]
brd0=trimesh.load('/home/claude/ext/cad/6160 Sparkle Motion Mini/6160 Sparkle Motion Mini.stl',force='mesh')
brd=trimesh.Trimesh(placeL(brd0.vertices),brd0.faces,process=False)
PT=PB-0.05-1.99; BL=float(brd.bounds[0][1])      # PCB top (visible side) Y, board lowest Y
holes=placeL([[x,y,0.0] for x,y in [(2.54,2.54),(27.94,2.667),(2.54,17.145),(27.94,17.0815)]])
# ---- cover geometry numbers
FLOOR_IN=min(BL,PT-2.0)-1.2   # 1.2 mm under the lowest component / screw head                     # 1.2 mm under the lowest component / nut+thread
FL=1.6; FLOOR_OUT=FLOOR_IN-FL; FLANGE_TOP=FLOOR_IN
W_IN=10.9; WALL=1.4; SPX=14.2; SPR=2.6; CZ=Zb+15.24; CL0,CL1=Zb+0.2,Zb+30.3
# ---- sled
base=B((2*EDGE,240.0-Yb,ZS1-ZS0)).translate((X0-EDGE,Yb,ZS0)) - AM
parts=[base]+[cylY(PB,Yb+0.5,h[0],h[2],2.5) for h in holes]+[cylY(FLANGE_TOP+0.15,Yb+0.5,X0+s*SPX,CZ,2.8) for s in (-1,1)]
sled=m3.Manifold.batch_boolean(parts,m3.OpType.Add)
cut=[cylY(PB-1,PB+7.0,h[0],h[2],0.85,24) for h in holes]            # 1.7 mm pilot: M2 x 8 threads straight into the post (head on the board side)
cut+=[cylY(FLANGE_TOP-1,FLANGE_TOP+8.5,X0+s*SPX,CZ,0.85,24) for s in (-1,1)]   # cover screws from below
cut.append(B((4.6,2.0,2.7)).translate((X0-(4.8+0.3-9.875),PB-0.1,Zb+4.0)))   # clear the small underside part by the USB-end hole
sled=sled-m3.Manifold.batch_boolean(cut,m3.OpType.Add)
tie=B((2*EDGE-14,2.0,4.0)).translate((X0-EDGE+7,Yb-2.0,ZS1-4.0))-B((2*EDGE-22,2.2,4.4)).translate((X0-EDGE+11,Yb-2.1,ZS1-4.2))
sled=(sled+tie).decompose(); sled.sort(key=lambda q:-q.volume()); sledM=sled[0]
# ---- perforated cover (open ends for USB-C and the wires)
tray=B((2*(W_IN+WALL),Yb-1.0-FLOOR_OUT,CL1-CL0)).translate((X0-W_IN-WALL,FLOOR_OUT,CL0)) - B((2*W_IN,40,CL1-CL0+2)).translate((X0-W_IN,FLOOR_IN,CL0-1))
tabs=B((2*(SPX+3.2),FL,8.0)).translate((X0-SPX-3.2,FLOOR_OUT,CZ-4.0))
cov=tray+tabs
cc=[cylY(FLOOR_OUT-1,FLOOR_IN+1,X0+s*SPX,CZ,1.25,24) for s in (-1,1)]+[cylY(FLOOR_IN,260,X0+s*SPX,CZ,2.8+0.4) for s in (-1,1)]
for k in range(6):                                       # ventilation slots in the floor
    z=CL0+3.0+k*4.6; cc.append(B((2*W_IN-6,FL+2,2.0)).translate((X0-W_IN+3,FLOOR_OUT-1,z)))
for s in (-1,1):                                         # and in each side wall
    for k in range(3): cc.append(B((WALL+2,4.0,2.0)).translate((X0+s*(W_IN+WALL/2)-(WALL+2)/2,FLOOR_IN+1.2,CL0+3+k*4.6 if k<2 else CL1-5)))
cov=cov-m3.Manifold.batch_boolean(cc,m3.OpType.Add)
cov=cov.decompose(); cov.sort(key=lambda q:-q.volume()); covM=cov[0]
BM=to_m(brd) if brd.is_volume else None
S,Cv=to_t(sledM),to_t(covM)
def gap(a,b,n=6000):
    p,_=trimesh.sample.sample_surface(a,n,seed=1); return float(np.abs(trimesh.proximity.signed_distance(b,p[:2000])).min())
rep=dict(Yb=Yb,PCB_bottom=PB,PCB_top=PT,board_low=BL,cover_floor_in=FLOOR_IN,cover_bottom=FLOOR_OUT,
 sled_vol=sledM.volume()/1000,cover_vol=covM.volume()/1000,sled_ext=S.extents.round(1).tolist(),cover_ext=Cv.extents.round(1).tolist(),
 sled_x_arm=(sledM^AM).volume(),cover_x_arm=(covM^AM).volume(),cover_x_sled=(covM^sledM).volume())
brd_pts=brd.vertices
inside_cover=Cv.contains(brd_pts[::7]).sum(); inside_sled=S.contains(brd_pts[::7]).sum()
rep.update(board_pts_in_cover=int(inside_cover),board_pts_in_sled=int(inside_sled))
print(json.dumps(rep,indent=1))
S.export('sled3_placed.ply'); Cv.export('cover3_placed.ply'); brd.export('board3_placed.ply')
json.dump(dict(rep,holes=holes.tolist(),SPX=SPX,CZ=CZ,X0=X0,Zb=Zb),open('place3.json','w'),indent=1)
