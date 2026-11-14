import sys, os, re, json, numpy as np
from lxml import etree
root = sys.argv[1]; cache = sys.argv[2]; os.makedirs(cache, exist_ok=True)
NS = '{http://schemas.microsoft.com/3dmanufacturing/core/2015/02}'
PNS = '{http://schemas.microsoft.com/3dmanufacturing/production/2015/06}'
def load_obj(path):
    key = os.path.basename(path)
    cp = os.path.join(cache, key + '.npz')
    if os.path.exists(cp):
        d = np.load(cp); return d['v'], d['f']
    V = []; F = []
    for ev, el in etree.iterparse(path, events=('end',), tag=(NS+'vertex', NS+'triangle')):
        if el.tag == NS+'vertex': V.append((float(el.get('x')), float(el.get('y')), float(el.get('z'))))
        else: F.append((int(el.get('v1')), int(el.get('v2')), int(el.get('v3'))))
        el.clear()
    v = np.array(V, dtype=np.float64); f = np.array(F, dtype=np.int64)
    np.savez(cp, v=v, f=f); return v, f
def mat(s):
    a = [float(x) for x in s.split()] if s else [1,0,0,0,1,0,0,0,1,0,0,0]
    M = np.eye(4); M[:3,:3] = np.array(a[:9]).reshape(3,3).T; M[:3,3] = a[9:]; return M
tree = etree.parse(os.path.join(root, '3D/3dmodel.model'))
objs = {}
for o in tree.getroot().iter(NS+'object'):
    comps = [(c.get(PNS+'path'), c.get('objectid'), mat(c.get('transform'))) for c in o.iter(NS+'component')]
    objs[o.get('id')] = comps
items = [(it.get('objectid'), mat(it.get('transform')), it.get('printable')) for it in tree.getroot().iter(NS+'item')]
# names / plates
cfg = etree.parse(os.path.join(root, 'Metadata/model_settings.config')).getroot()
names = {}; ext = {}
for o in cfg.iter('object'):
    md = {m.get('key'): m.get('value') for m in o.findall('metadata')}
    names[o.get('id')] = md.get('name'); ext[o.get('id')] = md.get('extruder')
plates = {}
for p in cfg.iter('plate'):
    md = {m.get('key'): m.get('value') for m in p.findall('metadata')}
    for mi in p.iter('model_instance'):
        mm = {m.get('key'): m.get('value') for m in mi.findall('metadata')}
        plates[mm.get('object_id')] = (md.get('plater_id'), md.get('plater_name'))
res = []
def tri_vol(v, f):
    a = v[f[:,0]]; b = v[f[:,1]]; c = v[f[:,2]]
    return float(np.einsum('ij,ij->i', a, np.cross(b, c)).sum() / 6)
for oid, M, pr in items:
    allv = []; ntri = 0; vol = 0
    for path, cid, CM in objs[oid]:
        v, f = load_obj(os.path.join(root, path.lstrip('/')))
        T = M @ CM
        w = v @ T[:3,:3].T + T[:3,3]
        allv.append(w); ntri += len(f); vol += tri_vol(w, f)
    w = np.vstack(allv); lo = w.min(0); hi = w.max(0)
    res.append(dict(id=oid, name=names.get(oid), plate=plates.get(oid, (None,None))[0], plate_name=plates.get(oid,(None,None))[1],
        printable=pr, parts=len(objs[oid]), triangles=ntri, volume_cm3=round(vol/1000,2),
        size=[round(x,2) for x in (hi-lo)], lo=[round(x,2) for x in lo], hi=[round(x,2) for x in hi],
        rot=[[round(x,4) for x in r] for r in M[:3,:3].tolist()], trans=[round(x,2) for x in M[:3,3]], files=[p for p,_,_ in objs[oid]]))
    r = res[-1]; print(r['id'], '|', r['name'], '| plate', r['plate'], '|', r['size'], '| vol', r['volume_cm3'], '| tris', ntri, flush=True)
json.dump(res, open(sys.argv[3], 'w'), indent=1)
