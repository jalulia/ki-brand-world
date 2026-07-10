#!/usr/bin/env python3
# High-quality PIL compositor: clean SKU (no names), custom range triptych, blank story backgrounds.
from PIL import Image, ImageFilter, ImageEnhance
MNT="/sessions/quirky-bold-heisenberg/mnt/Ki Brand"
BACKS=MNT+"/06_World-of-Ki/social/phase-one/_assets/bg"   # sRGB-clean landscapes (bad Linear ICC stripped)
EXT=BACKS+"/KI_BACK_17_Ext.png"
PUCKS=MNT+"/04_Source-Assets/Pucks"
OUT=MNT+"/06_World-of-Ki/social/phase-one/1080"

LMAP={"yuzu":"KI_BACK_05.png","satsuma":"KI_BACK_04.png","maple":"KI_BACK_03.png",
      "cola":"KI_BACK_01.png","hokkaido":"KI_BACK_02.png"}
PMAP={"yuzu":"YUZU","satsuma":"SATSUMA","maple":"MAPLE","cola":"COLA","hokkaido":"HOKKAIDO"}

def load(p):
    im=Image.open(p).convert("RGBA"); im.info.pop("icc_profile",None); return im  # no colour-profile leak
def cover(im,tw,th,fx=0.5,fy=0.5):
    w,h=im.size; s=max(tw/w,th/h); nw,nh=round(w*s),round(h*s)
    im=im.resize((nw,nh),Image.LANCZOS)
    x=int((nw-tw)*fx); y=int((nh-th)*fy)
    return im.crop((x,y,x+tw,y+th))
def puck(fl):
    p=load(f"{PUCKS}/KI_NEW_UK_{PMAP[fl]}_01.png"); return p.crop(p.getbbox())
def shadow(s,blur=46,dy=34,alpha=120,tint=(10,14,10)):
    # pad on ALL sides so the gaussian falloff never clips (no hard edge/line)
    a=s.split()[3]; base=Image.new("RGBA",s.size,(0,0,0,0))
    solid=Image.new("RGBA",s.size,tint+(alpha,)); sc=Image.composite(solid,base,a)
    pad=blur*3
    c=Image.new("RGBA",(s.size[0]+pad*2, s.size[1]+pad*2),(0,0,0,0)); c.paste(sc,(pad,pad),sc)
    return c.filter(ImageFilter.GaussianBlur(blur)), pad, dy
def place(bg,p,width,cx,cy):
    k=width/p.size[0]; s=p.resize((width,round(p.size[1]*k)),Image.LANCZOS)
    shd,pad,dy=shadow(s)
    x=cx-s.size[0]//2; y=cy-s.size[1]//2
    bg.alpha_composite(shd,(x-pad, y-pad+dy)); bg.alpha_composite(s,(x,y)); return bg

# ---------- SKU (clean, no names) ----------
for fl in LMAP:
    land=load(f"{BACKS}/{LMAP[fl]}")
    # feed 1:1
    bg=cover(land,1080,1080,0.5,0.30)
    bg=place(bg,puck(fl),790,540,520)
    bg.convert("RGB").save(f"{OUT}/sku-{fl}_1x1.png","PNG")
    # story 9:16
    bg=cover(land,1080,1920,0.5,0.28)
    bg=place(bg,puck(fl),760,540,1040)
    bg.convert("RGB").save(f"{OUT}/sku-{fl}_9x16.png","PNG")
    print("sku",fl)

# ---------- Custom range triptych ----------
ext=load(EXT)
# panorama 3240x1080, 5 pucks along the horizon
pano=cover(ext,3240,1080,0.5,0.52)
GROUND=712
specs=[("maple",520,470),("satsuma",580,1010),("yuzu",660,1620),("hokkaido",580,2235),("cola",520,2805)]
for fl,w,cx in specs:
    pano=place(pano,puck(fl),w,cx,GROUND)
pano.convert("RGB").save(f"{OUT}/tri-panorama_3x1.png","PNG")
# feed tiles = clean thirds of the panorama
for i in range(3):
    pano.crop((i*1080,0,(i+1)*1080,1080)).convert("RGB").save(f"{OUT}/tri-{i+1}_1x1.png","PNG")
# story tiles: tall 9:16 crops of EXT with the matching puck group
story_groups=[[("maple",560,300),("satsuma",610,760)],
              [("yuzu",720,540)],
              [("hokkaido",610,320),("cola",560,780)]]
fxs=[0.16,0.5,0.84]
for i,grp in enumerate(story_groups):
    bg=cover(ext,1080,1920,fxs[i],0.42)
    for fl,w,cx in grp:
        bg=place(bg,puck(fl),w,cx,1120)
    bg.convert("RGB").save(f"{OUT}/tri-{i+1}_9x16.png","PNG")
print("triptych done")

# ---------- Blank story backgrounds (landscape only) ----------
STORYBG={"yuzu":"KI_BACK_05.png","satsuma":"KI_BACK_04.png","maple":"KI_BACK_03.png",
         "cola":"KI_BACK_01.png","hokkaido":"KI_BACK_02.png","horizon":None}
for name,fn in STORYBG.items():
    src=ext if fn is None else load(f"{BACKS}/{fn}")
    bg=cover(src,1080,1920,0.5,0.34)
    bg.convert("RGB").save(f"{OUT}/bg-{name}_9x16.png","PNG")
    print("storybg",name)

# ---------- Ingredient RTB (recomposite clean, no colour-profile leak) ----------
subj=Image.open("/sessions/quirky-bold-heisenberg/mnt/outputs/_ingredient/subject.png").convert("RGBA")
subj.info.pop("icc_profile",None); subj=subj.crop(subj.getbbox()); sw2,sh2=subj.size
def compose_ing(box,out,w,cyf,f):
    bg=load(f"{BACKS}/KI_BACK_07.png").crop(box).resize(out,Image.LANCZOS).convert("RGB")
    bg=ImageEnhance.Brightness(bg).enhance(0.80).convert("RGBA")   # slightly darker — sets the "ingredients" story apart
    k=w/sw2; s=subj.resize((w,round(sh2*k)),Image.LANCZOS)
    shd,pad,dy=shadow(s)
    W,H=out; cx=W//2; cy=int(H*cyf); x=cx-s.size[0]//2; y=cy-s.size[1]//2
    bg.alpha_composite(shd,(x-pad, y-pad+dy)); bg.alpha_composite(s,(x,y))
    bg.convert("RGB").save(f,"PNG"); print("ingredient",f.split("/")[-1])
compose_ing((1300,720,1300+1520,720+1520),(1080,1080),800,0.50,f"{OUT}/rtb-ingredients_1x1.png")   # centred
compose_ing((1050,560,1050+981,560+1744),(1080,1920),780,0.50,f"{OUT}/rtb-ingredients_9x16.png")   # centred
print("ALL DONE")
