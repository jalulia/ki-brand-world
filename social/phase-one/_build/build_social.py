#!/usr/bin/env python3
# KI SOCIAL — rebuilt: crisp pucks (KI_NEW_UK_*_01, 1920px) on flavour landscapes,
# no invented eyebrows, optional subtle flavour-name-in-kanji tag only.
import os, json, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
MNT  = "/sessions/quirky-bold-heisenberg/mnt/Ki Brand"
ASSET = MNT + "/Digital-Banners/assets"
SRC   = MNT + "/04_Source-Assets"
LIB   = MNT + "/06_World-of-Ki/social/assets/library"
FONTS = MNT + "/06_World-of-Ki/social/phase-one/_assets/fonts"   # self-contained
BACKS = MNT + "/06_World-of-Ki/social/phase-one/_assets/bg"   # sRGB-clean landscapes (bad Linear ICC stripped)

def url(p): return "file://" + urllib.parse.quote(p)
css = open(f"{HERE}/social.css").read().replace("FONTS/", url(FONTS)+"/")
open(f"{HERE}/social.resolved.css","w").write(css)

LOGO_W = url(f"{ASSET}/ki-logo-white.svg")
LOGO_B = url(f"{ASSET}/ki-logo-black.svg")
# flavour → KI_BACK landscape (flav_*.jpg crops were removed in the folder reshuffle)
BG_MAP={"yuzu":"KI_BACK_05.png","satsuma":"KI_BACK_04.png","maple":"KI_BACK_03.png",
        "cola":"KI_BACK_01.png","hokkaido":"KI_BACK_02.png"}
def bg_flav(name): return url(f"{BACKS}/{BG_MAP[name]}")
def puck(fl): return url(f"{SRC}/Pucks/KI_NEW_UK_{fl}_01.png")
def plate(name, ratio): return url(f"{LIB}/{name}-{'1x1' if ratio=='sq' else '9x16'}.png")

# flavour data: key -> (name, kanji, landscape, PUCKID)
FLAV = {
 "yuzu":    ("Yuzu Mint","柚子ミント","yuzu","YUZU"),
 "satsuma": ("Satsuma Citrus","薩摩シトラス","satsuma","SATSUMA"),
 "maple":   ("Maple Coffee","メープルコーヒー","maple","MAPLE"),
 "cola":    ("Tokyo Cola","東京コーラ","cola","COLA"),
 "hokkaido":("Hokkaido Mint","北海道ミント","hokkaido","HOKKAIDO"),
}

POSTS=[
 # SKU — clean crisp product on its landscape, subtle kanji tag only
 dict(id="sku-yuzu", section="Single-flavour (SKU)", kind="product", flav="yuzu",
      caption="Hit refresh 🔄🌿🍋"),
 dict(id="sku-satsuma", section="Single-flavour (SKU)", kind="product", flav="satsuma",
      caption="We’ve got a juicy secret (it’s satsuma) 🍊"),
 dict(id="sku-maple", section="Single-flavour (SKU)", kind="product", flav="maple",
      caption="Rich coffee. Sweet maple. A match made in heaven. Or just in your mouth."),
 dict(id="sku-cola", section="Single-flavour (SKU)", kind="product", flav="cola",
      caption="Enjoy the refined flavour of Tokyo craft cola. For the full experience try it at 1am under a neon sign just as it stops raining."),
 dict(id="sku-hokkaido", section="Single-flavour (SKU)", kind="product", flav="hokkaido",
      caption="Chill. Literally ❄️"),
 # RTB
 # pre-composited: yuzu ingredient cutout on a tighter-cropped misty-sage landscape (KI_BACK_02), no copy
 dict(id="rtb-ingredients", section="Reason to believe (RTB)", kind="plate", plate="rtb-ingredients",
      caption="Obsessed with ingredients? Us? Absolutely 🤓"),
 dict(id="rtb-chef", section="Reason to believe (RTB)", kind="headline", bg="yuzu", logo="white",
      lines=["It goes in your","mouth. So we","hired a chef."], fs_sq=94, fs_st=120,
      caption="Yes, a chef, for a pouch. 👨‍🍳"),
 dict(id="rtb-nature", section="Reason to believe (RTB)", kind="headline", bg="cola", logo="white",
      lines=["Sweetened by","nature.","Not by a lab."], fs_sq=98, fs_st=124,
      caption="Natural sweeteners are better than artificial ones. We checked."),
 dict(id="rtb-carbon", section="Reason to believe (RTB)", kind="headline", bg="hokkaido", logo="white",
      lines=["Smaller carbon","footprint.","Regular","sized can."], fs_sq=80, fs_st=104,
      caption="Our cans are environmentally certified, lower carbon, and made with pine oil. They also do a good job holding your pouches."),
 # Brand lines
 dict(id="brand-clarity", section="Brand lines", kind="headline", bg="cola", logo="white",
      lines=["A moment","of clarity.","You need it."], fs_sq=98, fs_st=124,
      caption="Clarity, made with intention. 気"),
 dict(id="brand-bamboo", section="Brand lines", kind="headline", bg="hokkaido", logo="white",
      lines=["Turns out","bamboo isn’t","just for","pandas."], fs_sq=80, fs_st=102,
      caption="Our packaging has a green streak. 🎋"),
]

def esc(s): return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def flav_tag(name, kanji, x, by, story):
    fs = 25 if not story else 28
    return (f'<div class="flavtag" style="left:{x}px;bottom:{by}px;font-size:{fs}px">'
            f'<span class="bar" style="width:30px;height:2px;margin-right:14px"></span>'
            f'{esc(name).upper()}<span class="jp">{esc(kanji)}</span></div>')

def age_mark(story, W):
    s = 60 if not story else 68
    return (f'<div class="age" style="right:72px;bottom:{64 if not story else 90}px;'
            f'width:{s}px;height:{s}px;font-size:{s*0.34:.0f}px">18+</div>')

def render_html(post, ratio):
    W=1080; H=1080 if ratio=="sq" else 1920
    story = ratio=="st"
    E=[f'<!doctype html><html><head><meta charset="utf-8">'
       f'<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@500;600&display=swap" rel="stylesheet">'
       f'<link rel="stylesheet" href="social.resolved.css"><style>.post{{width:{W}px;height:{H}px}}</style></head><body>'
       f'<div class="post" data-shot>']

    if post["kind"]=="product":
        name,kanji,land,pk = FLAV[post["flav"]]
        E.append(f'<img class="bg" src="{bg_flav(land)}" style="object-position:{"50% 38%" if not story else "50% 30%"}">')
        # crisp puck, centred, grounded with soft shadow
        if not story:
            Wt=940; left=(W-Wt)//2; top=118
        else:
            Wt=900; left=(W-Wt)//2; top=560
        E.append(f'<div style="position:absolute;z-index:3;left:{left}px;top:{top}px;width:{Wt}px;height:{Wt}px;'
                 f'background:url({puck(pk)}) center/contain no-repeat;'
                 f'filter:drop-shadow(0 38px 42px rgba(8,14,6,.48))"></div>')
        E.append(flav_tag(name, kanji, 72, (64 if not story else 96), story))

    elif post["kind"]=="plate":
        E.append(f'<img class="bg" src="{plate(post["plate"],ratio)}">')
        # no on-art KI logo — the tin carries the brand; chrome carries it in social
        if post.get("tag"):
            E.append(flav_tag(post["tag"][0], post["tag"][1], 72, (64 if not story else 96), story))

    else:  # headline
        E.append(f'<img class="bg" src="{bg_flav(post["bg"])}" style="object-position:50% 42%">')
        E.append('<div class="scrim top"></div>')
        # no on-art KI logo (redundant in social)
        # story: slightly smaller so intended line breaks hold, and lifted for a bottom safe zone
        hf = round(post["fs_st"]*0.86) if story else post["fs_sq"]
        lh = hf*1.0
        n=len(post["lines"]); block=(n-1)*lh+hf
        bottom = 150 if not story else 430   # 9:16 bottom safe-zone clearance
        top = H-bottom-block
        lines_html="<br>".join(esc(l).upper() for l in post["lines"])
        E.append(f'<div class="headline" style="left:72px;width:936px;top:{top:.0f}px;font-size:{hf}px">{lines_html}</div>')

    # 18+ badge removed across the board per brand direction
    E.append('</div></body></html>')
    return "".join(E)

manifest=[]
for p in POSTS:
    entry=dict(id=p["id"], section=p["section"], caption=p["caption"], files={})
    for ratio in ("sq","st"):
        open(f'{HERE}/{p["id"]}_{ratio}.html',"w").write(render_html(p,ratio))
        entry["files"][ratio]=f'{p["id"]}_{ratio}.html'
    manifest.append(entry)
json.dump(manifest, open(f"{HERE}/manifest.json","w"), ensure_ascii=False, indent=1)
print("generated", len(POSTS)*2, "html")
