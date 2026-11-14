import pymeshlab, glob, os, json, sys
V4='cad/releases/v4/Vi_Gauntlet_X1C_V4_Print_Release'; out={}
for f in sorted(glob.glob(V4+'/Right_Shells/*.stl')+glob.glob(V4+'/Lighting_Covers/*.stl')+glob.glob(V4+'/Print_Hardware/*[!x].stl')):
    ms = pymeshlab.MeshSet(); ms.load_new_mesh(f); ms.meshing_merge_close_vertices()
    ms.compute_selection_by_self_intersections_per_face(); n = ms.current_mesh().selected_face_number()
    ms.set_selection_none(); ms.compute_selection_by_small_disconnected_components_per_face(nbfaceratio=0.01); small = ms.current_mesh().selected_face_number()
    out[os.path.basename(f)] = dict(self_intersecting_faces=n, faces=ms.current_mesh().face_number(), faces_in_small_components=small)
    print(os.path.basename(f), out[os.path.basename(f)], flush=True)
json.dump(out, open('out/selfint.json','w'), indent=1)
