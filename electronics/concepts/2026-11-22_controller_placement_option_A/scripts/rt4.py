import trimesh, numpy as np, json
exec(open('rt2.py').read().split('# ---------- in-gauntlet views ----------')[0])
p=json.load(open('place3.json')); S=trimesh.load('sled3_placed.ply'); Cv=trimesh.load('cover3_placed.ply'); Bd=trimesh.load('board3_placed.ply')
col.update({'cover':(240,170,90)})
def screw(x,z,yhead,L=8.0,up=True):   # head at yhead, shank pointing +Y (up into the post)
    sgn=1 if up else -1
    sh=trimesh.creation.cylinder(radius=1.0,segment=[[x,yhead,z],[x,yhead+sgn*L,z]],sections=16)
    hd=trimesh.creation.cylinder(radius=1.9,segment=[[x,yhead,z],[x,yhead-sgn*2.0,z]],sections=24); return trimesh.util.concatenate([sh,hd])
PT=p['PCB_top']; FO=p['cover_bottom']
sb=[screw(h[0],h[2],PT) for h in p['holes']]; sc_=[screw(p['X0']+s*p['SPX'],p['CZ'],FO) for s in (-1,1)]
def sh(m,dy): m=m.copy(); m.apply_translation([0,dy,0]); return m
E=[('sled',S),('board',sh(Bd,-14)),('screw',trimesh.util.concatenate([sh(s,-26) for s in sb])),('cover',sh(Cv,-40)),('screw',trimesh.util.concatenate([sh(s,-52) for s in sc_]))]
sc=Scene(E); c=S.centroid+np.array([0,-16,0]); sc.cam(c+np.array([120,-60,-95]),c,48,1200,1150); im=sc.render(); d=ImageDraw.Draw(im)
label(d,sc,S.centroid+np.array([0,6,0]),'sled: glue face on top,\nshaped to the ceiling',(-200,-120),(166,80,0),24)
label(d,sc,np.array([p['X0'],p['PCB_bottom']-14-1.0,p['Zb']+12]),'board',(-260,40),(30,30,30),24)
label(d,sc,np.array(p['holes'][1])+np.array([0,-26+(PT-p['holes'][1][1])-1.0,0]),'4 × M2 × 8 screws go up through the\nboard holes and thread into the posts',(140,10),(80,80,80),24)
label(d,sc,np.array([p['X0'],FO-40,p['CZ']]),'vented cover, ends open for\nUSB-C and the wires',(80,60),(170,100,30),24)
label(d,sc,np.array([p['X0']+p['SPX'],FO-52-1.5,p['CZ']]),'2 more M2 × 8 hold the cover',(120,40),(80,80,80),24)
d.text((15,15),'Sled with cover, using your M2 × 8 screws (exploded)',font=FB(28),fill=(20,20,20)); im.save('sled_v3_exploded.png')
A=trimesh.load('armR.ply'); Hm=A.slice_plane([211.0,0,0],[-1,0,0])
import fast_simplification as fs
v,f=fs.simplify(Hm.vertices.astype(np.float32),Hm.faces.astype(np.int64),target_reduction=1-400000/len(Hm.faces)); Hm=trimesh.Trimesh(v,f,process=False)
R=json.load(open('routes.json'))
sc2=Scene([('shell',Hm),('sled',S),('board',Bd),('cover',Cv),('screw',trimesh.util.concatenate(sc_))]+[(k,tubes(R[k])) for k in ('led','usb','buttons')])
sc2.cam((330,120,205),(222,205,262),55,1400,950); im=sc2.render(); d=ImageDraw.Draw(im)
label(d,sc2,np.array([p['X0']+8,FO,p['CZ']]),'vented cover: board protected,\nair can still get to it',(-60,200),(170,100,30))
d.text((20,20),'Installed, seen from below: sled, board and cover under the LED ring',font=FB(30),fill=(20,20,20)); im.save('sled_v3_inside.png')
