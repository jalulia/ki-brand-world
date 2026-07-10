#!/usr/bin/env python3
# Shared slide spec -> slides.json (for native PPTX) + slides.html (for crisp PDF).
import os, json, urllib.parse

MNT="/sessions/quirky-bold-heisenberg/mnt/Ki Brand"
IMG=MNT+"/06_World-of-Ki/social/phase-one/1080"
FONTS=MNT+"/06_World-of-Ki/social/phase-one/_assets/fonts"
HERE=os.path.dirname(os.path.abspath(__file__))

W,H=1280,720
PAPER="#EFEDE6"; INK="#111111"; GOLD="#B88448"; MUTED="#555555"; META="#6B7280"; LINE="#D9D4C8"

def u(p): return "file://"+urllib.parse.quote(p)

CONCEPTS=[
 ("Single-flavour · SKU","SKU","Yuzu Mint","sku-yuzu","Hit refresh 🔄🌿🍋"),
 ("Single-flavour · SKU","SKU","Satsuma Citrus","sku-satsuma","We’ve got a juicy secret (it’s satsuma) 🍊"),
 ("Single-flavour · SKU","SKU","Maple Coffee","sku-maple","Rich coffee. Sweet maple. A match made in heaven. Or just in your mouth."),
 ("Single-flavour · SKU","SKU","Tokyo Cola","sku-cola","Enjoy the refined flavour of Tokyo craft cola. For the full experience try it at 1am under a neon sign just as it stops raining."),
 ("Single-flavour · SKU","SKU","Hokkaido Mint","sku-hokkaido","Chill. Literally ❄️"),
 ("Reason to believe · RTB","RTB","Real Ingredients","rtb-ingredients","Obsessed with ingredients? Us? Absolutely 🤓"),
 ("Reason to believe · RTB","RTB","Chef-Crafted","rtb-chef","Yes, a chef, for a pouch. 👨‍🍳"),
 ("Reason to believe · RTB","RTB","Naturally Sweetened","rtb-nature","Natural sweeteners are better than artificial ones. We checked."),
 ("Reason to believe · RTB","RTB","Lower Carbon","rtb-carbon","Our cans are environmentally certified, lower carbon, and made with pine oil. They also do a good job holding your pouches."),
]
STORYBGS=[("bg-yuzu","Yuzu"),("bg-satsuma","Satsuma"),("bg-maple","Maple"),
          ("bg-cola","Cola"),("bg-hokkaido","Hokkaido"),("bg-horizon","Full horizon")]

slides=[]
def T(x,y,w,h,text,size,color=INK,weight=400,align="left",spacing=0,lh=1.15,upper=False,jp=False):
    return dict(type="text",x=x,y=y,w=w,h=h,text=text,size=size,color=color,weight=weight,
                align=align,spacing=spacing,lh=lh,upper=upper,jp=jp)
def IMGEL(x,y,w,h,path,r=0):
    return dict(type="image",x=x,y=y,w=w,h=h,src=path,round=r)
def R(x,y,w,h,fill):
    return dict(type="rect",x=x,y=y,w=w,h=h,fill=fill)

# ---- Cover ----
cov=[R(0,0,W,H,PAPER),
 T(80,60,200,40,"気",30,GOLD,600),
 T(80,116,700,24,"KI · INSTAGRAM · PHASE ONE",13,GOLD,600,spacing=2.4,upper=True),
 T(76,150,780,230,"SOCIAL\nCONTENT",92,INK,500,spacing=-1.8,lh=0.98,upper=True),
 T(80,410,600,120,"A first flight of Instagram creative for Ki — single-flavour features and reasons to believe, plus a set of blank landscape story backgrounds. Every post designed on the Ki landscape system.",16,MUTED,400,lh=1.55),
 T(80,556,900,24,"9 CONCEPTS   ·   18 POSTS + 6 STORY BGS   ·   FEED 1:1 + STORY 9:16   ·   @KI.BIO",12.5,META,600,spacing=1.2,upper=True),
 IMGEL(742,300,168,168,f"{IMG}/sku-yuzu_1x1.png",14),
 IMGEL(918,300,168,168,f"{IMG}/rtb-chef_1x1.png",14),
 IMGEL(1094,300,168,168,f"{IMG}/sku-cola_1x1.png",14),
 IMGEL(742,478,168,168,f"{IMG}/sku-maple_1x1.png",14),
 IMGEL(918,478,168,168,f"{IMG}/sku-satsuma_1x1.png",14),
 IMGEL(1094,478,168,168,f"{IMG}/rtb-ingredients_1x1.png",14),
 T(80,676,400,20,"Ki · Social · Phase One",11,META,400),
 T(1150,676,60,20,"01",11,META,600,align="right"),
]
slides.append(dict(bg=PAPER,els=cov))

def header(section, page, total):
    return [R(0,0,W,H,PAPER),
      T(80,48,500,20,"KI · SOCIAL — PHASE ONE",11,META,600,spacing=1.4,upper=True),
      T(700,48,500,20,section.upper(),11,META,600,spacing=1.4,align="right",upper=True),
      R(80,78,1120,1.4,LINE),
      T(1150,676,60,20,f"{page:02d}",11,META,600,align="right"),
      T(80,676,300,20,f"{total} / {total}" if False else "Ki · Social",11,META,400)]

for i,(section,kick,name,pid,cap) in enumerate(CONCEPTS):
    page=i+2
    els=header(section,page,14)
    # feed 1:1
    els+=[IMGEL(80,150,430,430,f"{IMG}/{pid}_1x1.png",16),
          T(80,590,300,18,"FEED · 1:1",11,META,600,spacing=1.2,upper=True),
          # story 9:16
          IMGEL(560,120,300,533,f"{IMG}/{pid}_9x16.png",20),
          T(560,662,300,18,"STORY · 9:16",11,META,600,spacing=1.2,upper=True),
          # right column
          T(930,152,290,20,section.split("·")[0].strip().upper(),12,GOLD,600,spacing=1.4,upper=True),
          T(930,178,300,130,name,31,INK,500,spacing=-1.0,lh=1.0,upper=True),
          T(930,330,260,18,"CAPTION",11,GOLD,600,spacing=1.6,upper=True),
          T(930,356,285,190,cap,15.5,INK,400,lh=1.5),
          T(930,606,290,40,"1080×1080 feed\n1080×1920 story",12,META,400,lh=1.5)]
    slides.append(dict(bg=PAPER,els=els))

# ---- Story backgrounds (two slides: the landscape + colour wash) ----
def storybg_slide(page, subtitle, suffix):
    els=header("Story backgrounds",page,14)
    els+=[T(80,150,900,20,f"BLANK LANDSCAPES · {subtitle}",12,GOLD,600,spacing=1.4,upper=True),
          T(80,176,1120,40,"Clean 1080×1920 story backgrounds — no product, no type. Drop your own copy, stickers or polls on top for quick organic stories.",14,MUTED,400,lh=1.4)]
    bw=165; gap=26; by=256; bh=293
    for j,(bid,nm) in enumerate(STORYBGS):
        x=80+j*(bw+gap)
        els+=[IMGEL(x,by,bw,bh,f"{IMG}/{bid}{suffix}_9x16.png",14),
              T(x,by+bh+14,bw,18,nm,10.5,META,600,spacing=1.0,upper=True)]
    slides.append(dict(bg=PAPER,els=els))
SHOW_STORYBG=False   # Sam pulled the blank story backgrounds 2026-07-10; flip to True to bring them back
if SHOW_STORYBG:
    storybg_slide(len(CONCEPTS)+2, "THE LANDSCAPE", "")
    storybg_slide(len(CONCEPTS)+3, "COLOUR WASH · CLOSER CROP", "-wash")

# ---- Closing ----
els=[R(0,0,W,H,PAPER),
     T(0,250,W,40,"気",34,GOLD,600,align="center"),
     T(0,300,W,60,"THAT’S THE FLIGHT.",44,INK,500,spacing=-1.0,align="center",upper=True),
     T(0,378,W,40,"9 concepts · 18 posts + 6 story backgrounds · built on the Ki landscape system",15,MUTED,400,align="center"),
     T(0,414,W,40,"Product from KI_NEW_UK pucks · Obviously Regular + Semibold · Site Gold #B88448",12.5,META,400,align="center"),
     T(1150,676,60,20,f"{len(slides)+1:02d}",11,META,600,align="right")]
slides.append(dict(bg=PAPER,els=els))

json.dump(dict(W=W,H=H,slides=slides), open(f"{HERE}/slides.json","w"), ensure_ascii=False)
print("slides:",len(slides))

# ---------- emit slides.html for crisp PDF ----------
def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace("\n","<br>")
fam="'Obviously'"
face=""
for wt,fn in [(400,"Obviously-Regular.woff2"),(500,"Obviously-Medium.woff2"),(600,"Obviously-Semibold.woff2")]:
    face+=f"@font-face{{font-family:'Obviously';src:url({u(FONTS+'/'+fn)}) format('woff2');font-weight:{wt}}}\n"
html=[f'<!doctype html><html><head><meta charset="utf-8">',
 '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;600&display=swap" rel="stylesheet">',
 f'<style>{face}*{{margin:0;box-sizing:border-box}}body{{background:#222}}',
 f'.slide{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:{fam},sans-serif}}',
 '.el{position:absolute}.tx{white-space:pre-wrap}',
 '</style></head><body>']
for s in slides:
    html.append(f'<div class="slide" data-shot style="background:{s["bg"]}">')
    for e in s["els"]:
        if e["type"]=="rect":
            html.append(f'<div class="el" style="left:{e["x"]}px;top:{e["y"]}px;width:{e["w"]}px;height:{e["h"]}px;background:{e["fill"]}"></div>')
        elif e["type"]=="image":
            r=e.get("round",0)
            html.append(f'<img class="el" src="{u(e["src"])}" style="left:{e["x"]}px;top:{e["y"]}px;width:{e["w"]}px;height:{e["h"]}px;object-fit:cover;border-radius:{r}px">')
        else:
            fw=e.get("weight",400); ls=e.get("spacing",0); lh=e.get("lh",1.15)
            tt="text-transform:uppercase;" if e.get("upper") else ""
            al=e.get("align","left")
            html.append(f'<div class="el tx" style="left:{e["x"]}px;top:{e["y"]}px;width:{e["w"]}px;height:{e["h"]}px;'
                        f'font-size:{e["size"]}px;font-weight:{fw};color:{e["color"]};letter-spacing:{ls}px;line-height:{lh};'
                        f'text-align:{al};{tt}">{esc(str(e["text"]))}</div>')
    html.append('</div>')
html.append('</body></html>')
open(f"{HERE}/slides.html","w").write("\n".join(html))
print("wrote slides.html + slides.json")
