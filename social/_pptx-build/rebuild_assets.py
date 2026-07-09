#!/usr/bin/env python3
"""Ki Social v2 — recomposed to the web type system + deck layouts.
   Obviously Semibold/Regular only. No crests. No dark scrims. Extended landscapes for stories."""
import os, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

B="/sessions/modest-sharp-gauss/mnt/outputs/_social_build"; SRC=f"{B}/src"
OUTL=f"{B}/out2/library"; OUTP=f"{B}/out2/prev"
os.makedirs(OUTL,exist_ok=True); os.makedirs(OUTP,exist_ok=True)
SEMI=f"{SRC}/fonts/Obviously-Semibold.otf"; REG=f"{SRC}/fonts/Obviously-Regular.otf"
BOLD=f"{SRC}/fonts/Obviously-Bold.otf"
MED=f"{SRC}/fonts/Obviously-Medium.otf"
DISP=MED   # per the production banner Illustrator file: Obviously Medium

def enhance_tin(tin):
    """richer, studio-lit punch to match the hero renders (the flat web product PNGs read too light)."""
    r,g,b,a=tin.split(); rgb=Image.merge("RGB",(r,g,b))
    rgb=ImageEnhance.Color(rgb).enhance(1.26)
    rgb=ImageEnhance.Contrast(rgb).enhance(1.12)
    rgb=ImageEnhance.Brightness(rgb).enhance(0.96)
    r2,g2,b2=rgb.split(); return Image.merge("RGBA",(r2,g2,b2,a))
def font(p,s): return ImageFont.truetype(p,s)

# ---------- landscape helpers ----------
def cover(im,w,h,fy=0.5):
    im=im.convert("RGB"); s=max(w/im.width,h/im.height)
    im=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    x=(im.width-w)//2; y=int((im.height-h)*fy)
    return im.crop((x,y,x+w,y+h))

def land(im,w,h,zoom=1.0,fx=0.5,fy=0.5):
    """crop a WINDOW of the painting — zoom>1 excludes the darkest edges and lets us frame
       the brighter upper-mid dunes (fy<0.5 keeps sky + light dunes, drops the deep bottom band)."""
    im=im.convert("RGB"); s=max(w/im.width,h/im.height)*zoom
    nw,nh=round(im.width*s),round(im.height*s)
    im=im.resize((nw,nh),Image.LANCZOS)
    x=int((nw-w)*fx); y=int((nh-h)*fy)
    return im.crop((x,y,x+w,y+h))

def edge_colour(im,top=True):
    a=np.asarray(im.convert("RGB")); band=a[:24] if top else a[-24:]
    return tuple(int(v) for v in band.reshape(-1,3).mean(0))

def vgrad(w,h,c0,c1):
    arr=np.zeros((h,1,3),np.float32)
    for y in range(h):
        t=y/max(1,h-1); arr[y,0]=[c0[i]*(1-t)+c1[i]*t for i in range(3)]
    return Image.fromarray(np.repeat(arr.astype(np.uint8),w,axis=1))

def story_extend(painting, W=1080, H=1920, bandh=1360, fy=0.5):
    """Tall painting crop across the top (real sky + dunes), with a gentle gradient ground
       extension beneath so the tin has somewhere to rest. No dead flat zones."""
    band=cover(painting,W,bandh,fy)
    grnd=edge_colour(band,False); g2=tuple(int(v*0.80) for v in grnd)
    canvas=Image.new("RGB",(W,H),grnd)
    canvas.paste(band,(0,0))
    canvas.paste(vgrad(W,H-bandh,grnd,g2),(0,bandh))
    # feather the seam
    seam=Image.new("L",(W,240),0); sd=ImageDraw.Draw(seam)
    for i in range(240): sd.line([(0,i),(W,i)],fill=int(255*(1-i/240)))
    strip=cover(painting,W,bandh,fy).crop((0,bandh-240,W,bandh))
    canvas.paste(strip,(0,bandh-240),seam)
    return canvas

# ---------- product ----------
def crop_alpha(im):
    im=im.convert("RGBA"); bb=im.split()[3].getbbox(); return im.crop(bb) if bb else im

def place_tin(c, path, target_w, cx, cy, ground=True):
    tin=enhance_tin(crop_alpha(Image.open(path))); s=target_w/tin.width
    tin=tin.resize((round(tin.width*s),round(tin.height*s)),Image.LANCZOS)
    x=round(cx-tin.width/2); y=round(cy-tin.height/2)
    a=tin.split()[3]
    if ground:
        # subtle contact ellipse under the base (soft, not a dark halo)
        cs=Image.new("RGBA",c.size,(0,0,0,0)); cd=ImageDraw.Draw(cs)
        ew=int(tin.width*0.60); eh=int(tin.height*0.085)
        ex=round(cx-ew/2); ey=round(y+tin.height*0.82)
        cd.ellipse([ex,ey,ex+ew,ey+eh],fill=(12,14,9,70))
        c.alpha_composite(cs.filter(ImageFilter.GaussianBlur(int(tin.width*0.05))))
    # light directional drop shadow — grounds the tin without darkening the scene
    sh=Image.new("RGBA",tin.size,(0,0,0,0)); sh.paste((14,16,10,58),(0,0),a)
    blur=max(9,int(target_w*0.035)); pad=blur*3
    big=Image.new("RGBA",(tin.width+pad*2,tin.height+pad*2),(0,0,0,0)); big.paste(sh,(pad,pad),sh)
    big=big.filter(ImageFilter.GaussianBlur(blur))
    c.alpha_composite(big,(x-pad+int(target_w*0.015),y-pad+int(target_w*0.03)))
    c.alpha_composite(tin,(x,y)); return c

# ---------- type (Obviously Semibold, tracked) ----------
def line_w(f,s,track):
    w=0
    for ch in s: w+=f.getbbox(ch)[2]-f.getbbox(ch)[0]+f.getlength(ch)-(f.getbbox(ch)[2]-f.getbbox(ch)[0]) # use advance
    # simpler: sum advances + track
    adv=sum(f.getlength(ch) for ch in s)
    return adv+track*(len(s)-1)

def draw_tracked(draw,xy,s,f,fill,track):
    x,y=xy
    for ch in s:
        draw.text((x,y),ch,font=f,fill=fill); x+=f.getlength(ch)+track

def headline(c, lines, x, y, maxw, target_h, em=-0.02, fill=(255,255,255)):
    lo,hi,best=44,150,44
    for _ in range(22):
        mid=(lo+hi)//2; f=font(DISP,mid); tr=em*mid
        widest=max(line_w(f,ln,tr) for ln in lines); lh=mid*1.0
        total=lh*(len(lines)-1)+mid
        if widest<=maxw and total<=target_h: best=mid; lo=mid+1
        else: hi=mid-1
    f=font(DISP,best); tr=em*best; lh=best*1.0
    # soft drop shadow for legibility only (kept light — no heavy scrim per the web voice)
    sh=Image.new("RGBA",c.size,(0,0,0,0)); sd=ImageDraw.Draw(sh); cy=y
    for ln in lines: draw_tracked(sd,(x,cy),ln,f,(0,0,0,95),tr); cy+=lh
    c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)),(3,7))
    d=ImageDraw.Draw(c); cy=y
    for ln in lines: draw_tracked(d,(x,cy),ln,f,fill+(255,),tr); cy+=lh
    return best,cy

def save(c,name,pw):
    c=c.convert("RGB"); c.save(f"{OUTL}/{name}.png","PNG")
    p=c.copy(); p.thumbnail((pw,pw*2),Image.LANCZOS); p.save(f"{OUTP}/{name}.webp","WEBP",quality=90,method=6)
    print("  ",name,c.size)

def canvasRGBA(w,h): return Image.new("RGBA",(w,h),(0,0,0,255))

FLAV=["yuzu","satsuma","maple","cola","hokkaido"]

# =========== SKU posts ===========
print("SKU")
# per-flavour crop focus (keep sky + a dune the tin can rest on)
FY={"yuzu":0.5,"satsuma":0.5,"maple":0.5,"cola":0.46,"hokkaido":0.5}
for f in FLAV:
    bg=f"{SRC}/bg/{f}.png"; tin=f"{SRC}/tins/{f}.png"
    # frame the brighter upper-mid of the painting (sky + light dunes), drop the dark bottom band
    c=land(Image.open(bg),1080,1080,zoom=1.16,fy=0.28).convert("RGBA")
    place_tin(c,tin,640,540,600)
    save(c,f"sku-{f}-1x1",900)
    c=story_extend(Image.open(bg),bandh=1360,fy=0.34).convert("RGBA")
    place_tin(c,tin,600,540,1180)
    save(c,f"sku-{f}-9x16",560)

# =========== RTB ===========
print("RTB")
# ingredients — real yuzu still on yuzu landscape (no crest)
ING="10sl2Ctb7yrqarwhH48GK6BcPoC84-GWq"  # handled by browser comp separately; here fallback uses open puck? no -> skip, done in browser
# typographic
RTB={
 "chef":     dict(bg="yuzu",  fy=0.30, sfy=0.62, lines=["IT GOES","IN YOUR","MOUTH.","SO WE","HIRED","A CHEF."]),
 "sweetened":dict(bg="cola",  fy=0.24, sfy=0.5,  lines=["SWEETENED","BY NATURE.","NOT BY","A LAB."]),
 "can":      dict(bg="hokkaido",fy=0.24, sfy=0.5, lines=["SMALLER","CARBON","FOOTPRINT.","REGULAR","SIZED CAN."], tin="hokkaido"),
}
for k,m in RTB.items():
    bg=f"{SRC}/bg/{m['bg']}.png"
    c=cover(Image.open(bg),1080,1080,m["fy"]).convert("RGBA")
    if m.get("tin"): place_tin(c,f"{SRC}/tins/{m['tin']}.png",384,812,946)
    headline(c,m["lines"],76,84,928,target_h=858)
    save(c,f"rtb-{k}-1x1",900)
    # RTB story: cover-fill (text wants a filled darker field), not the sky-extend
    c=cover(Image.open(bg),1080,1920,m["sfy"]).convert("RGBA")
    if m.get("tin"): place_tin(c,f"{SRC}/tins/{m['tin']}.png",600,540,1520)
    headline(c,m["lines"],84,232,912,target_h=980)
    save(c,f"rtb-{k}-9x16",560)

# =========== Range ===========
# symmetric pyramid resting in the panorama — Yuzu largest, front & centre by the sun,
# flanked by Satsuma/Hokkaido, then Maple/Cola outermost. Grounded, drawn back-to-front.
print("Range")
c=cover(Image.open(f"{SRC}/bg/pano.png"),1080,1080,0.30).convert("RGBA")
base=600
for f,wf,cxf,cyf in [("maple",0.58,0.165,0.700),("cola",0.58,0.835,0.700),
                     ("satsuma",0.74,0.335,0.685),("hokkaido",0.74,0.665,0.685),
                     ("yuzu",1.00,0.500,0.665)]:
    place_tin(c,f"{SRC}/tins/{f}.png",round(base*wf),round(1080*cxf),round(1080*cyf),ground=True)
save(c,"range-1x1",900)
c=story_extend(Image.open(f"{SRC}/bg/pano.png"),bandh=1360,fy=0.34).convert("RGBA"); base=520
for f,wf,cxf,cyf in [("maple",0.58,0.170,0.615),("cola",0.58,0.830,0.615),
                     ("satsuma",0.74,0.340,0.600),("hokkaido",0.74,0.660,0.600),
                     ("yuzu",1.00,0.500,0.580)]:
    place_tin(c,f"{SRC}/tins/{f}.png",round(base*wf),round(1080*cxf),round(1920*cyf),ground=True)
save(c,"range-9x16",560)
print("DONE")
