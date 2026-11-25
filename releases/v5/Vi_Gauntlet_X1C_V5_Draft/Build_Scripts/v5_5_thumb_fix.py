"""V5.5 thumb finding (Claude, 2026-11-25). Reproduces the analysis in V5_5_Thumb_Fix/README_V5_5_THUMB_FIX.md.
Inputs (LFS): originals/Together For Sizing.stl, originals/Full_Arm_Right (No Fingers).stl,
originals/Vi Gauntlet 3mf Project File.3mf (object 112 -> object_86.model id 111 = Thumb_Base),
Right_Shells/R_13_Knuckles_Right_V5_1.3mf, V5_3_Thumb_Joint/R_13_Knuckles_Right_V5_3.3mf.
Steps:
 1. Split Together For Sizing into bodies; right-arm thumb base = body with volume 115.22 cm3 (bounds x 328-401, y 101-183, z 437-518).
 2. Load stock Thumb_Base (113.66 cm3). Rigid ICP vs that body: no fit (<1 % of surface within 0.1 mm from 1500 starts).
    Mirror X first, then ICP: median deviation 0.013 mm, p90 0.042 mm  => stock base is the LEFT-hand part.
 3. Shell 13 print -> assembly: x = z', y = y' + 26.079, z = -x' + 628.059 (inverse of rotate(0,-90,0) + bed);
    89 % of shell surface within 0.02 mm of Full_Arm_Right.
 4. Correct right base (mirrored stock, step 2 pose) vs shell 13: V5_1 overlap 0.35 cm3, 28 cm2 within 0.5 mm;
    printed V5_3 overlap 0.30 cm3, 19 cm2 within 0.5 mm; sections x = 338/335/332/329: key inside the tapered pocket.
 5. V5.3 bases fitted back to the correct poses: the L_ file is right-handed, the R_ file left-handed; stray 6.4 x 16 mm hole
    mouth at about (390, 165, 491) on the outer face (axis direction (-0.94, 0, -0.34)).
 6. Export: L_Thumb_Base_V5_5_stock = stock base in its 3MF print pose; R_Thumb_Base_V5_5_mirrored = X-mirror of it; both bed-centred.
"""
import numpy as np, trimesh, zipfile, re, os
from lxml import etree
SRC = '/home/claude/arcane-vi-gauntlet/originals/Vi Gauntlet 3mf Project File.3mf'
def stock_thumb_base_print_pose():
    z = zipfile.ZipFile(SRC); root = etree.fromstring(z.read('3D/Objects/object_86.model')); ns = {'m': root.nsmap[None]}
    o = root.find(".//m:object[@id='111']", ns)
    V = np.array([[float(x.get(k)) for k in 'xyz'] for x in o.iterfind('.//m:vertex', ns)])
    F = np.array([[int(x.get(k)) for k in ('v1', 'v2', 'v3')] for x in o.iterfind('.//m:triangle', ns)])
    tr = [float(x) for x in re.search(r'<item objectid="112"[^>]*transform="([^"]*)"', z.read('3D/3dmodel.model').decode()).group(1).split()]
    M = np.eye(4); M[:3, :3] = np.array(tr[:9]).reshape(3, 3).T; M[:3, 3] = tr[9:]
    m = trimesh.Trimesh(V, F, process=True); m.apply_transform(M); return m
def bed(m):
    b = m.bounds; m.apply_translation([90-(b[0][0]+b[1][0])/2, 90-(b[0][1]+b[1][1])/2, -b[0][2]]); return m
if __name__ == '__main__':
    out = os.sys.argv[1] if len(os.sys.argv) > 1 else 'out'; os.makedirs(out, exist_ok=True)
    L = bed(stock_thumb_base_print_pose()); R = L.copy(); R.apply_transform(np.diag([-1, 1, 1, 1])); R = bed(R)
    L.export(f'{out}/L_Thumb_Base_V5_5_stock.3mf'); R.export(f'{out}/R_Thumb_Base_V5_5_mirrored.3mf')
    print('volumes cm3', L.volume/1000, R.volume/1000)
