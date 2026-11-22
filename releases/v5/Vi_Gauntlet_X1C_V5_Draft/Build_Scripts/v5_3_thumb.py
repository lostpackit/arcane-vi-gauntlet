"""V5.3 thumb joint (owner-approved 2026-11-22): socket for Thumb_Base in shell 13 + one 6 mm dowel.
Inputs (Claude workspace): V5.1 R_13 print file, out/placed_Thumb_Base.stl (printable Thumb_Base in assembled coords),
out/cache3mf/object_86.model.npz (+3mf_objects.json) for the base's original print pose."""
import sys, json, zipfile, re, os, hashlib
sys.path.insert(0, '/home/claude/thumbstudy')
from lib import *
OUT = '/home/claude/v53/out'
R13 = '/home/claude/pack_named/Vi_Gauntlet_V5_Print_Pack/6_Right_Arm_Knuckles_AFTER_FINGER_TEST/R_13_Knuckles_Right_V5_1.3mf'
P = trimesh.load(R13, force='mesh', process=False)
Tp = np.load('/home/claude/out/r13_asm_to_print_mat.npy')           # assembled -> print pose (exact axis map)
tb = trimesh.load('/home/claude/out/placed_Thumb_Base.stl')
S = P.copy(); S.apply_transform(np.linalg.inv(Tp))
Ms, Mb = M(S), M(tb)
d = np.array([0.94, 0, -0.342]); d /= np.linalg.norm(d)              # insertion direction (base slides in along -d)
C = cutter(Mb, d, 0.25, 40)                                          # 0.25 mm clearance, swept 40 mm outward
# dowel axis through the best-supported spot (≈50 mm solid in base, ≈57 mm in shell)
c = np.array([337., 144., 485.]); u = np.cross(d, [0, 1, 0]); u /= np.linalg.norm(u); v = np.cross(d, u)
p0 = c + u*8.0 + v*(-19.5)
o = p0 - d*80; hb = tb.ray.intersects_location([o], [d])[0]; t_in = np.sort((hb-o)@d)[0]; q = o + d*t_in   # interface point
def rod(a, b, r=3.2):
    L = np.linalg.norm(b-a); z = (b-a)/L
    cyl = trimesh.creation.cylinder(radius=r, height=L, sections=48)
    Rm = trimesh.geometry.align_vectors([0, 0, 1], z); cyl.apply_transform(Rm); cyl.apply_translation((a+b)/2)
    return M(cyl)
hole_shell = rod(q - d*16.0, q + d*1.0)
hole_base = rod(q - d*1.0, q + d*16.0)
S3 = Ms - C - hole_shell
B3 = Mb - hole_base
log = dict(insertion_dir=d.round(4).tolist(), dowel_interface_point=q.round(2).tolist(),
           shell_removed_cm3=round((Ms.volume()-S3.volume())/1000, 2), base_removed_cm3=round((Mb.volume()-B3.volume())/1000, 2),
           shell_status=str(S3.status()), base_status=str(B3.status()), shell_genus=[Ms.genus(), S3.genus()])
def bed(m):
    b = m.bounds; m.apply_translation([128-(b[0][0]+b[1][0])/2, 128-(b[0][1]+b[1][1])/2, -b[0][2]]); return m
def export(m, path, name):
    m.export(path)
    zin = zipfile.ZipFile(path); items = [(i, zin.read(i.filename)) for i in zin.infolist()]; zin.close()
    with zipfile.ZipFile(path+'.t', 'w', zipfile.ZIP_DEFLATED) as z:
        for i, dat in items:
            if i.filename == '3D/3dmodel.model': dat = re.sub(rb'(<object\b[^>]*\bname=")[^"]*(")', rb'\g<1>'+name.encode()+rb'\g<2>', dat)
            z.writestr(i.filename, dat)
    os.replace(path+'.t', path)
# shell 13 back to print pose
Sr = T(S3); Sr.apply_transform(Tp); Sr = bed(Sr)
export(Sr, f'{OUT}/R_13_Knuckles_Right_V5_3.3mf', 'R_13_Knuckles_Right_V5_3')
Sl = Sr.copy(); Sl.apply_transform(np.diag([-1, 1, 1, 1])); Sl = bed(Sl)
export(Sl, f'{OUT}/L_13_Knuckles_Right_V5_3.3mf', 'L_13_Knuckles_Right_V5_3')
# thumb base back to its original print pose
K = np.load('/home/claude/out/thumb_asm_to_print.npz'); Rk, ca, cb = K['R'], K['ca'], K['cb']
Br = T(B3); Br.vertices = (Br.vertices-ca)@Rk.T + cb; Br = bed(Br)
export(Br, f'{OUT}/R_Thumb_Base_V5_3_dowel.3mf', 'R_Thumb_Base_V5_3_dowel')
Bl = Br.copy(); Bl.apply_transform(np.diag([-1, 1, 1, 1])); Bl = bed(Bl)
export(Bl, f'{OUT}/L_Thumb_Base_V5_3_dowel.3mf', 'L_Thumb_Base_V5_3_dowel')
for f in sorted(os.listdir(OUT)):
    if f.endswith('.3mf'):
        m = trimesh.load(f'{OUT}/{f}', force='mesh', process=False)
        log[f] = dict(volume_cm3=round(m.volume/1000, 2), extents=m.extents.round(1).tolist(), watertight=bool(m.is_watertight),
                      sha256=hashlib.sha256(open(f'{OUT}/{f}', 'rb').read()).hexdigest())
json.dump(log, open(f'{OUT}/V5_3_thumb_build_log.json', 'w'), indent=1); print(json.dumps(log, indent=1))
