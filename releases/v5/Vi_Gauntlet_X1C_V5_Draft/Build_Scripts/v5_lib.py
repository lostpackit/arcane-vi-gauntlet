import numpy as np, trimesh, manifold3d as m3, json
def to_m(v, f):
    return m3.Manifold(m3.Mesh(vert_properties=np.asarray(v, np.float32), tri_verts=np.asarray(f, np.uint32)))
def from_tm(tm):
    tm = tm.copy(); tm.merge_vertices(); return to_m(tm.vertices, tm.faces)
def to_tm(M):
    me = M.to_mesh(); return trimesh.Trimesh(np.asarray(me.vert_properties)[:, :3], np.asarray(me.tri_verts), process=False)
def arm():
    d = np.load('/home/claude/out/fullR.npz'); return to_m(d['v'], d['f'])
_t = None
def tog():
    global _t
    if _t is None: _t = np.load('/home/claude/out/together.npz')
    return _t
def comp_tm(c):
    t = tog(); f = t['f'][t['lab'] == c]; u, inv = np.unique(f, return_inverse=True)
    return trimesh.Trimesh(t['v'][u], inv.reshape(-1, 3), process=False)
def part3mf(name, c):
    objs = {o['name']: o for o in json.load(open('/home/claude/out/3mf_objects.json'))}
    d = np.load('/home/claude/out/cache3mf/' + objs[name]['files'][0].split('/')[-1] + '.npz')
    m = trimesh.Trimesh(d['v'], d['f'], process=False); t = tog()
    m.apply_translation((t['lo'][c] + t['hi'][c]) / 2 - (m.bounds[0] + m.bounds[1]) / 2); return m
def scaled(M, s):
    b = M.bounding_box(); c = (np.array(b[:3]) + np.array(b[3:])) / 2
    return M.translate(tuple(-c)).scale((s, s, s) if np.isscalar(s) else tuple(s)).translate(tuple(c))
