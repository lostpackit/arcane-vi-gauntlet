import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
P=6.25; L=232.5
zones=[('Lens A window',0,81,'#ffd59a'),('under top plate\n(tunnel, hidden)',81,103,'#bdbdbd'),('Lens B window',103,149,'#ffd59a'),('under crystal base\n(tunnel, hidden)',149,167,'#bdbdbd'),('crystal well',167,232.5,'#a8d8ff')]
fig,(a1,a2)=plt.subplots(2,1,figsize=(17,9.5),gridspec_kw={'height_ratios':[1.25,1]})
# ---------- side view ----------
a1.add_patch(Rectangle((-25,-6),L+40,4.0,fc='#cfcfcf',ec='#777'))                    # channel floor
a1.text(-24,-5,'shell (channel floor)',fontsize=9,va='center')
a1.add_patch(Rectangle((0,-2),L,0.6,fc='#f2f2f2',ec='#555'))                        # strip PCB
n=36
for i in range(n):
    x=P/2+i*P; c='#2b6cb0' if x>167 else ('#555' if (81<x<103 or 149<x<167) else '#e8871e')
    a1.add_patch(Rectangle((x-1,-1.4),2.0,1.0,fc=c,ec='k',lw=.3))
a1.add_patch(Rectangle((0,3.0),81,1.6,fc='#ffd59a',ec='#b07a20',alpha=.9)); a1.text(40,5.6,'Lens A (81 mm, translucent)',ha='center',fontsize=10)
a1.add_patch(Rectangle((81,2.2),22,9,fc='#9e9e9e',ec='#555')); a1.text(92,12.2,'top plate',ha='center',fontsize=10)
a1.add_patch(Rectangle((103,3.0),46,1.6,fc='#ffd59a',ec='#b07a20',alpha=.9)); a1.text(126,5.6,'Lens B (46 mm)',ha='center',fontsize=10)
a1.add_patch(Rectangle((149,2.2),18,18,fc='#9e9e9e',ec='#555')); a1.text(158,21.2,'crystal\nbase front',ha='center',fontsize=9)
a1.add_patch(Polygon([[165,24],[230,20],[232,22],[166,27]],closed=True,fc='#a8d8ff',ec='#2b6cb0',alpha=.9))
a1.add_patch(Rectangle((166,2.2),2.5,22,fc='#9e9e9e',ec='#555')); a1.add_patch(Rectangle((229,2.2),3.5,18,fc='#9e9e9e',ec='#555'))
a1.text(198,29,'CRYSTAL (65 mm, lifts out; sits on a narrow rim)',ha='center',fontsize=11,color='#1a4f8a',weight='bold')
a1.add_patch(FancyArrowPatch((198,1),(198,18),arrowstyle='->',mutation_scale=14,color='#2b6cb0')); a1.text(201,9,'light goes straight up\nthrough the open well',fontsize=9,color='#1a4f8a')
a1.annotate('strip arrives from the ring\n(through the 9 mm slot at the ring notch;\ntwist it 90° there so LEDs face UP here)',xy=(0,-1.7),xytext=(-24,14),arrowprops=dict(arrowstyle='->'),fontsize=9)
a1.text(L+2,-1.7,'channel end\n(cut the strip here,\ninsulate the cut)',fontsize=9,va='center')
a1.set_xlim(-26,272); a1.set_ylim(-8,33); a1.set_yticks([]); a1.set_xlabel('mm along the hand channel from where it leaves the ring  (the channel really slopes down ~4° toward the knuckles)')
a1.set_title('Side view along the back of the hand: LEDs lie flat on the channel floor, facing up into the lenses and the crystal',fontsize=12)
for s in ['top','right','left']: a1.spines[s].set_visible(False)
# ---------- top view ----------
for name,z0,z1,c in zones:
    a2.add_patch(Rectangle((z0,-6),z1-z0,12,fc=c,ec='#666',alpha=.8)); a2.text((z0+z1)/2,8.5,name,ha='center',va='bottom',fontsize=9.5)
a2.add_patch(Rectangle((0,-2.5),L-7.5,5,fc='#f7f7f7',ec='#555'))
for i in range(n):
    x=P/2+i*P; c='#2b6cb0' if x>167 else ('#555' if (81<x<103 or 149<x<167) else '#e8871e')
    a2.add_patch(Rectangle((x-1,-1),2,2,fc=c,ec='k',lw=.3)); 
    if i in (0,12,13,15,16,23,24,26,27,35): a2.text(x,-4.6,str(i+1),ha='center',fontsize=8)
a2.text(-2,-4.6,'LED #',ha='right',fontsize=8)
a2.text(40,-10,'LEDs 1–13 glow through Lens A',ha='center',fontsize=10,color='#a65a00')
a2.text(126,-10,'LEDs 17–24 through Lens B',ha='center',fontsize=10,color='#a65a00')
a2.text(198,-10,'LEDs 28–36 (about 9–10) light the crystal',ha='center',fontsize=10,color='#1a4f8a',weight='bold')
a2.text(92,-13.5,'14–16 and 25–27 are hidden under bridges: set them dark in WLED',ha='center',fontsize=9,color='#555')
a2.set_xlim(-26,272); a2.set_ylim(-16,16); a2.set_yticks([]); a2.set_xlabel('mm  (6.25 mm per LED on your 160/m strip; channel 232.5 mm holds 36 LEDs with ~7 mm spare)')
a2.set_title('Top view of the same channel (lenses and crystal removed). Numbers count LEDs from where the strip leaves the ring',fontsize=12)
for s in ['top','right','left']: a2.spines[s].set_visible(False)
fig.text(0.01,0.005,'Schematic from the V5.1/V5.2 CAD (channel 232.5 mm, Lens A 81 mm, top-plate tunnel 22 mm, Lens B 46 mm, crystal-base tunnel ~18 mm, crystal 65 mm). Zone edges ±1 LED: confirm in the dry-fit.',fontsize=9,color='#555')
fig.tight_layout(); fig.savefig('hand_crystal_layout.png',dpi=110)
