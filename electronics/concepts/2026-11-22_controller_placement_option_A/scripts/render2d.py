import trimesh, numpy as np, json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as Pg, Ellipse, Rectangle
from shapely.geometry import MultiPoint, Polygon as SP
from shapely.geometry import GeometryCollection
def xorfill(ax, loops, **kw):
    g=None
    for L in loops:
        p=SP(L).buffer(0)
        g=p if g is None else g.symmetric_difference(p)
    geoms=getattr(g,'geoms',[g])
    for q in geoms:
        if q.is_empty or q.geom_type!='Polygon': continue
        from matplotlib.path import Path
        from matplotlib.patches import PathPatch
        verts=[np.array(q.exterior.coords)]+[np.array(i.coords) for i in q.interiors]
        codes=[]
        for v in verts: codes+= [Path.MOVETO]+[Path.LINETO]*(len(v)-2)+[Path.CLOSEPOLY]
        ax.add_patch(PathPatch(Path(np.vstack(verts),codes),**kw))
A=trimesh.load('armR.ply'); P=json.load(open('place.json')); R=json.load(open('routes.json'))
parts={k:trimesh.load(f'{k}_placed.ply') for k in ['sled','board','pod','bank','handle','switches']}
col={'sled':'#e8871e','board':'#1d3b2a','pod':'#2f6fd0','bank':'#8a5cc2','handle':'#b08a5a','switches':'#222'}
rc={'led':'#18a558','usb':'#d33','buttons':'#2f6fd0'}
def fore(z): z=np.clip(z,0,330); return 140+10*z/330, 50-17*z/330, 42-18*z/330   # ASSUMED forearm: centre Y, half-width X, half-height Y
def fill_section(ax, mesh, o, n, ax0, ax1, **kw):
    s=mesh.section(plane_origin=o, plane_normal=n)
    if s is None: return False
    for e in s.discrete: ax.fill(e[:,ax0], e[:,ax1], **kw)
    return True
def proj(ax, mesh, ax0, ax1, **kw):
    h=MultiPoint(mesh.vertices[:,[ax0,ax1]]).convex_hull; ax.add_patch(Pg(np.array(h.exterior.coords), closed=True, **kw))
# ---------- side view: section at X = 211 ----------
fig,ax=plt.subplots(figsize=(17,9))
XS=212.5
s=A.section(plane_origin=[XS,0,0],plane_normal=[1,0,0])
xorfill(ax,[e[:,[2,1]] for e in s.discrete],fc='#cfcfcf',ec='#777',lw=.6,zorder=1)
z=np.linspace(0,330,100); cy,a,b=fore(z)
ax.fill_between(z,cy-b,cy+b,color='#f3c9a8',alpha=.45,zorder=0); ax.plot(z,cy+b,'--',color='#b5651d',lw=1); ax.plot(z,cy-b,'--',color='#b5651d',lw=1)
ax.add_patch(Rectangle((330,112),95,88,fc='#f3c9a8',alpha=.45,ec='#b5651d',ls='--',zorder=0))
ax.text(150,150,'your forearm\n(assumed size)',ha='center',color='#8a4a10',fontsize=11)
ax.text(378,186,'fist on handle\n(assumed)',ha='center',color='#8a4a10',fontsize=10)
proj(ax,parts['bank'],2,1,fc=col['bank'],alpha=.35,ec=col['bank'],ls='--',zorder=2); ax.text(95,150,'power bank\n(cuff side wall,\nX≈93–108)',ha='center',fontsize=9,color='#5b3a8a')
proj(ax,parts['pod'],2,1,fc=col['pod'],alpha=.35,ec=col['pod'],ls='--',zorder=2); ax.text(378,106,'button pod clipped on the handle\nbeside the fist (X≈262–288)',ha='center',fontsize=9,color=col['pod'],va='top')
ax.add_patch(plt.Circle((375.95,156),9.4,fc=col['handle'],ec='k',lw=.6,zorder=3)); ax.text(392,160,'handle',fontsize=9)
for k in ['sled','board']: fill_section(ax,parts[k],[XS,0,0],[1,0,0],2,1,color=col[k],zorder=4)
for k,c in rc.items():
    r=np.array(R[k]); ax.plot(r[:,2],r[:,1],'-',color=c,lw=2.2,zorder=5)
ax.annotate('exit hole to the LED ring\n(16 × 12 mm)',xy=(263,240),xytext=(285,275),arrowprops=dict(arrowstyle='->'),fontsize=10)
ax.annotate('sled + board\n(glued under the ring)',xy=(225,214),xytext=(150,262),arrowprops=dict(arrowstyle='->'),fontsize=10,color='#a65a00')
cy,a,b=fore(231); ax.annotate('',xy=(231,cy+b),xytext=(231,P['board_low']),arrowprops=dict(arrowstyle='<->',color='#8a4a10'))
ax.text(236,(cy+b+P['board_low'])/2,'≈%d mm\nclear'%round(P['board_low']-(cy+b)),fontsize=10,color='#8a4a10',va='center')
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([],[],color=rc['led'],lw=2.5,label='LED lead (pigtail → strip JST, ~5 cm)'),Line2D([],[],color=rc['usb'],lw=2.5,label='USB-C power (bank → board, ~18 cm)'),Line2D([],[],color=rc['buttons'],lw=2.5,label='button wires 14 / 27 / G (~20 cm)')],loc='lower right',fontsize=10)
ax.set_xlim(-5,610); ax.set_ylim(0,300); ax.set_aspect('equal'); ax.set_xlabel('along the arm, mm  (cuff opening → knuckles)'); ax.set_ylabel('mm (up = back of the arm)')
ax.set_title('Right gauntlet, cut lengthwise through the middle: where the electronics sit. Parts off the cut plane shown dashed.',fontsize=12)
fig.tight_layout(); fig.savefig('placement_side.png',dpi=110)
# ---------- cross-section at the sled ----------
Zc=231.0
fig,ax=plt.subplots(figsize=(10,8.5))
s=A.section(plane_origin=[0,0,Zc],plane_normal=[0,0,1])
xorfill(ax,[e[:,[0,1]] for e in s.discrete],fc='#cfcfcf',ec='#777',lw=.6,zorder=1)
cy,a,b=fore(Zc); ax.add_patch(Ellipse((211,cy),2*a,2*b,fc='#f3c9a8',alpha=.5,ec='#b5651d',ls='--',zorder=0)); ax.text(211,cy,'forearm\n(assumed size)',ha='center',va='center',color='#8a4a10',zorder=6)
for k in ['sled','board']: fill_section(ax,parts[k],[0,0,Zc],[0,0,1],0,1,color=col[k],zorder=4)
ax.annotate('',xy=(190,cy+b),xytext=(190,P['board_low']),arrowprops=dict(arrowstyle='<->',color='#8a4a10')); ax.text(170,(cy+b+P['board_low'])/2,'≈%d mm'%round(P['board_low']-(cy+b)),color='#8a4a10',ha='right',va='center')
ax.annotate('sled follows the\nridged ceiling',xy=(222,222),xytext=(255,250),arrowprops=dict(arrowstyle='->'),fontsize=10,color='#a65a00')
ax.annotate('board (USB-C side down)',xy=(214,210),xytext=(240,190),arrowprops=dict(arrowstyle='->'),fontsize=10)
ax.set_xlim(60,360); ax.set_ylim(30,290); ax.set_aspect('equal'); ax.set_title('Cross-section across the arm at the sled (Z = %d)'%Zc); ax.set_xlabel('mm'); ax.set_ylabel('mm')
fig.tight_layout(); fig.savefig('placement_cross.png',dpi=110)
