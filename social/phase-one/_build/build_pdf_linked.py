#!/usr/bin/env python3
# Build the presentation PDF from slide screenshots + add clickable hyperlink
# annotations over every asset thumbnail (-> its GitHub Pages download URL).
import os, json, img2pdf
from PIL import Image
from pypdf import PdfReader, PdfWriter
try:
    from pypdf.annotations import Link
except Exception:
    Link=None

PNGDIR="slidepng8"
SLIDES=json.load(open("/sessions/quirky-bold-heisenberg/mnt/outputs/_social/pptx/slides.json"))
OUT="/sessions/quirky-bold-heisenberg/mnt/Ki Brand/06_World-of-Ki/social/phase-one/Ki_Social_Phase-One.pdf"
BASE="https://jalulia.github.io/ki-brand-world/social/phase-one"
W,H=SLIDES["W"],SLIDES["H"]            # 1280 x 720
PW,PH=img2pdf.in_to_pt(13.333), img2pdf.in_to_pt(7.5)   # 960 x 540 pt
SX,SY=PW/W, PH/H

def to_url(src):
    return BASE+"/"+src.split("/phase-one/",1)[1] if "/phase-one/" in src else None

# 1) assemble image-only PDF
os.makedirs("pdfjpgL",exist_ok=True); jpgs=[]
for i in range(1,len(SLIDES["slides"])+1):
    p=f"{PNGDIR}/s{i:02d}.png"
    if not os.path.exists(p): continue
    im=Image.open(p).convert("RGB"); im.info.pop("icc_profile",None)
    o=f"pdfjpgL/s{i:02d}.jpg"; im.save(o,"JPEG",quality=92,subsampling=0,optimize=True); jpgs.append(o)
tmp="/sessions/quirky-bold-heisenberg/mnt/outputs/_render/_tmp_linked.pdf"
with open(tmp,"wb") as f:
    f.write(img2pdf.convert(jpgs, layout_fun=img2pdf.get_layout_fun((PW,PH))))

# 2) add link annotations
reader=PdfReader(tmp); writer=PdfWriter(); writer.append(reader)
n=0
for i,s in enumerate(SLIDES["slides"]):
    for e in s["els"]:
        if e.get("type")!="image": continue
        url=to_url(e["src"])
        if not url: continue
        x0=e["x"]*SX; x1=(e["x"]+e["w"])*SX
        y_top=PH-e["y"]*SY; y_bot=PH-(e["y"]+e["h"])*SY
        rect=(x0,y_bot,x1,y_top)
        writer.add_annotation(page_number=i, annotation=Link(rect=rect, url=url))
        n+=1
with open(OUT,"wb") as f: writer.write(f)
print("linked PDF written:",n,"links ->",round(os.path.getsize(OUT)/1024/1024,2),"MB")
