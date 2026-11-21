import sys,os,numpy as np,trimesh,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
def cluster(m,n=200):
    cell=max(m.extents)/n
    q=np.round((m.vertices-m.bounds[0])/cell).astype(np.int64)
    key=q[:,0]*10**12+q[:,1]*10**6+q[:,2]
    u,inv=np.unique(key,return_inverse=True)
    v=np.zeros((len(u),3));c=np.bincount(inv)
    for i in range(3): v[:,i]=np.bincount(inv,m.vertices[:,i])/c
    f=inv[m.faces]; ok=(f[:,0]!=f[:,1])&(f[:,1]!=f[:,2])&(f[:,0]!=f[:,2])
    return v,f[ok]
def render(path,out,color):
    m=trimesh.load(path,force='mesh',process=False)
    m.apply_translation(-m.bounds.mean(0))
    v,f=cluster(m)
    tri=v[f]
    n=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]); n/=np.linalg.norm(n,axis=1,keepdims=True)+1e-12
    if m.volume<0: n=-n
    light=np.array([-0.4,-0.6,0.7]);light/=np.linalg.norm(light)
    shade=0.35+0.65*np.clip(np.abs(n@light),0,1)
    base=np.array(matplotlib.colors.to_rgb(color))
    fc=np.clip(base[None,:]*shade[:,None],0,1)
    fig=plt.figure(figsize=(4,4),dpi=100);ax=fig.add_subplot(111,projection='3d')
    pc=Poly3DCollection(tri,facecolors=fc,edgecolors='none',linewidths=0);ax.add_collection3d(pc)
    r=max(m.extents)/2*float(os.environ.get("ZOOM","0.82"))
    ax.set_xlim(-r,r);ax.set_ylim(-r,r);ax.set_zlim(-r,r);ax.set_box_aspect((1,1,1))
    ax.view_init(elev=28,azim=-55);ax.set_axis_off()
    plt.subplots_adjust(0,0,1,1);fig.savefig(out,transparent=False,facecolor='white');plt.close(fig)
if __name__=='__main__':
    render(sys.argv[1],sys.argv[2],sys.argv[3])
