import glob,os,subprocess,json,trimesh
P='src/Vi_Gauntlet_V5_Print_Pack'
files={}
for f in glob.glob(P+'/**/*.*',recursive=True):
    if f.endswith('.3mf'): files[os.path.basename(f)]=f
for b in ['L_Crystal_translucent.3mf','L_Hand_Lens_A_translucent_81mm.3mf','L_Hand_Lens_B_translucent_46mm.3mf','L_Pressure_Gauge_Insert.3mf','L_Ring_Light_Cover_translucent.3mf']:
    files[b]='/home/claude/out/L_inserts_fix/'+b
meta={}
for b,f in sorted(files.items()):
    if 'T2_' in b or 'Dowel' in b: continue
    c='#8a8f99'
    if 'translucent' in b: c='#7fc4e8'
    elif 'Gauge' in b: c='#b08a4a'
    elif 'Handle_One' in b: c='#c9a26b'
    elif 'CONCEPT' in b: c='#6b8f6b'
    out='Inventory/images/'+b.replace('.3mf','.png')
    subprocess.run(['python3','scripts/render.py',f,out,c],check=True)
    m=trimesh.load(f,force='mesh',process=False)
    meta[b]=[round(x) for x in sorted(m.extents,reverse=True)]
    print(b,meta[b],flush=True)
json.dump(meta,open('meta.json','w'),indent=1)
