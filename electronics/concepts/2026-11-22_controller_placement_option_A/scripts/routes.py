import trimesh, numpy as np, json
A=trimesh.load('armR.ply')
bank=trimesh.creation.box(extents=[15,65,100]); bank.apply_translation([100.0,150.0,95.0])
print('bank inside-shell fraction', A.contains(bank.sample(4000)).mean().round(3)); bank.export('bank_placed.ply')
W={'usb':[[211,209,216],[211,222,195],[205,226,170],[160,214,152],[115,190,148],[100,172,146]],
'buttons':[[290,148,366],[300,180,350],[285,212,330],[250,222,305],[222,224,280],[218,220,262],[214,212,247]],
'led':[[211,210,246.5],[211,214,256],[211,218,262],[211,236,263],[211,249,263]]}
offs=np.array([[3,0,0],[-3,0,0],[0,3,0],[0,-3,0],[0,0,3],[0,0,-3]])
def clear(p): return not A.contains(np.vstack([p,p+offs])).any()
out={}
for k,w in W.items():
    w=np.array(w,float); pts=np.vstack([w[i]+(w[i+1]-w[i])*t for i in range(len(w)-1) for t in np.linspace(0,1,30,endpoint=False)]+[w[-1:]])
    res=[]
    for p in pts:
        q=p.copy(); c=np.array([211,145,p[2]]); v=(c-q); v/=np.linalg.norm(v)
        n=0
        while k!='led' and not clear(q) and n<80: q+=0.5*v; n+=1
        res.append(q)
    res=np.array(res); L=np.linalg.norm(np.diff(res,axis=0),axis=1).sum()
    print(k,'length %.0f mm'%L, 'still inside:', int(A.contains(res).sum()))
    out[k]=res.tolist()
json.dump(out,open('routes.json','w'))
