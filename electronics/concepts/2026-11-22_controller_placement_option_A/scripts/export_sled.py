import trimesh, numpy as np
D='/home/claude/arcane-vi-gauntlet/electronics/concepts/2026-11-22_controller_placement_option_A/print/'
S=trimesh.load('sled3_placed.ply'); C=trimesh.load('cover3_placed.ply')
def bed(m, flip):
    m=m.copy()            # stand the sled on its USB-end face (world -Z): world Z becomes print Z
    m.apply_translation([128-m.bounds[:,0].mean(),128-m.bounds[:,1].mean(),-m.bounds[0][2]]); return m
def out(m,name):
    sc=trimesh.Scene(); sc.add_geometry(m,node_name=name,geom_name=name); sc.export(D+name+'.3mf'); print(name,m.is_watertight,m.extents.round(1),'vol %.2f cm3'%(m.volume/1000))
s=bed(S,True)   # sled: glue face down
print('sled lowest region is glue face? top-of-part z max at posts:', s.bounds[1][2].round(1))
out(s,'Sled_Right_Arm_M2_CONCEPT')
L=S.copy(); L.apply_transform(np.diag([-1,1,1,1])); out(bed(L,True),'Sled_Left_Arm_M2_CONCEPT')
c=C.copy(); c.apply_transform(trimesh.transformations.rotation_matrix(np.pi/2,[1,0,0]))   # floor (-Y) down
c.apply_translation([128-c.bounds[:,0].mean(),128-c.bounds[:,1].mean(),-c.bounds[0][2]]); out(c,'Board_Cover_vented_both_arms_CONCEPT')
