#!/usr/bin/env python3
import os, io, base64, html, json
from PIL import Image

MNT="/sessions/quirky-bold-heisenberg/mnt/Ki Brand"
IMG=MNT+"/06_World-of-Ki/social/phase-one/1080"
FONTS=MNT+"/06_World-of-Ki/social/assets/fonts"
HERITAGE=MNT+"/06_World-of-Ki/social/assets/img-ki-heritage.png"
OUT=MNT+"/06_World-of-Ki/social/phase-one/Ki_Social_Phase-One.html"

def fb64(name):
    return base64.b64encode(open(f"{FONTS}/{name}","rb").read()).decode()
FONT_SEMI=fb64("Obviously-Semibold.woff2")
FONT_MED=fb64("Obviously-Medium.woff2")
FONT_REG=fb64("Obviously-Regular.woff2")
LOGO_HERITAGE="data:image/png;base64,"+base64.b64encode(open(HERITAGE,"rb").read()).decode()

def img_b64(path, w):
    im=Image.open(path).convert("RGB")
    if im.width>w:
        im=im.resize((w, round(im.height*w/im.width)), Image.LANCZOS)
    b=io.BytesIO(); im.save(b,"JPEG",quality=82,optimize=True)
    return "data:image/jpeg;base64,"+base64.b64encode(b.getvalue()).decode()

def sq(id): return img_b64(f"{IMG}/{id}_1x1.png", 720)
def st(id): return img_b64(f"{IMG}/{id}_9x16.png", 600)

def esc(s): return html.escape(s).replace("\n","<br>")

POSTS=[
 ("Single-flavour · SKU","The five faces of the range. Product-forward, flavour-led, caption does the talking.",[
   ("sku-yuzu","Yuzu Mint","Hit refresh 🔄🌿🍋"),
   ("sku-satsuma","Satsuma Citrus","We’ve got a juicy secret (it’s satsuma) 🍊"),
   ("sku-maple","Maple Coffee","Rich coffee. Sweet maple. A match made in heaven. Or just in your mouth."),
   ("sku-cola","Tokyo Cola","Enjoy the refined flavour of Tokyo craft cola. For the full experience try it at 1am under a neon sign just as it stops raining."),
   ("sku-hokkaido","Hokkaido Mint","Chill. Literally ❄️"),
 ]),
 ("Reason to believe · RTB","The proof points — craft, ingredients, sweetening, sustainability — as bold type on the landscape.",[
   ("rtb-ingredients","Real Ingredients","Obsessed with ingredients? Us? Absolutely 🤓"),
   ("rtb-chef","Chef-Crafted","Yes, a chef, for a pouch. 👨‍🍳"),
   ("rtb-nature","Naturally Sweetened","Natural sweeteners are better than artificial ones. We checked."),
   ("rtb-carbon","Lower Carbon","Our cans are environmentally certified, lower carbon, and made with pine oil. They also do a good job holding your pouches."),
 ]),
 ("Range triptych","Three posts, one horizon. Posted in sequence they lock together across the feed grid into a single panorama.",[
   ("tri-1","Range · I","Some waits are worth their weight. Which in this case, if you’re curious, is .5278 grams."),
   ("tri-2","Range · II","Like the sunrise, we didn’t wait all night for it, dawn would be pretty meh."),
   ("tri-3","Range · III","If you think nicotine pouches should have taste and that taste should taste like what it is supposed to taste like — without the lab-made ‘alternatives’ when nature already does it pretty well — we were thinking the same thing.\n\nHi. Nice to meet you. We’re Ki."),
 ]),
 ("Brand lines","One-line brand voice moments — dry, confident, unmistakably Ki.",[
   ("brand-clarity","A Moment of Clarity","Clarity, made with intention. 気"),
   ("brand-bamboo","Sustainable by Design","Our packaging has a green streak. 🎋"),
 ]),
]

# icons
HEART='<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#262626" stroke-width="1.8"><path d="M12 21s-7.5-4.6-10-9.3C.4 8.3 2 4.8 5.3 4.8 7.3 4.8 8.7 6 12 9.2 15.3 6 16.7 4.8 18.7 4.8 22 4.8 23.6 8.3 22 11.7 19.5 16.4 12 21 12 21z"/></svg>'
COMMENT='<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#262626" stroke-width="1.8"><path d="M21 11.5A8.5 8.5 0 0 1 4.8 17L3 21l4-1.2A8.5 8.5 0 1 0 21 11.5z"/></svg>'
SHARE='<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#262626" stroke-width="1.8"><path d="M22 3 11 14M22 3l-7 19-4-8-8-4 19-7z"/></svg>'
SAVE='<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#262626" stroke-width="1.8"><path d="M19 21l-7-5-7 5V4a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1z"/></svg>'
KIAVA=f'<div class="ava"><img src="{LOGO_HERITAGE}" alt="KI"></div>'

def feed_card(id, name, cap):
    return f'''<div class="ig">
      <div class=" igh">{KIAVA}<div class="hmeta hmeta-solo"><b>ki.bio</b></div><div class="dots">•••</div></div>
      <img class="igimg" src="{sq(id)}" alt="{esc(name)}">
      <div class="igact"><div class="l">{HEART}{COMMENT}{SHARE}</div>{SAVE}</div>
      <div class="iglikes">2,480 likes</div>
      <div class="igcap"><b>ki.bio</b> {esc(cap)}</div>
      <div class="igtime">2 hours ago</div>
    </div>'''

def story_card(id, name):
    return f'''<div class="story">
      <img src="{st(id)}" alt="{esc(name)} story">
      <div class="sbars"><i></i><i></i><i></i></div>
      <div class="shead">{KIAVA}<b>ki.bio</b><span>2h</span></div>
      <div class="sfoot"><div class="smsg">Send message</div>{HEART}{SHARE}</div>
    </div>'''

concepts_html=[]
for section, blurb, items in POSTS:
    rows=[]
    for id,name,cap in items:
        rows.append(f'''<div class="concept">
          <div class="mocks">{feed_card(id,name,cap)}{story_card(id,name)}</div>
          <div class="copy">
            <div class="cname">{esc(name)}</div>
            <div class="clabel">Caption</div>
            <div class="cbox">{esc(cap)}</div>
            <div class="cmeta">1080×1080 feed &nbsp;·&nbsp; 1080×1920 story</div>
            <div class="cdl"><a href="1080/{id}_1x1.png" download>↓ Feed 1:1</a><a href="1080/{id}_9x16.png" download>↓ Story 9:16</a></div>
          </div>
        </div>''')
    extra=""
    if section.startswith("Range"):
        extra=f'<div class="pano"><div class="panolabel">Feed grid — the three posts join into one horizon</div><img src="{img_b64(IMG+"/tri-panorama_3x1.png",1400)}"></div>'
    concepts_html.append(f'''<section class="sec">
        <div class="sechead"><span class="kick">{esc(section.split("·")[0].strip())}</span>
        <h2>{esc(section)}</h2><p>{esc(blurb)}</p></div>
        {extra}
        {''.join(rows)}
      </section>''')

# profile grid (9 tiles)
# triptych occupies the top row so it reads as one seamless panorama across the grid
grid_ids=["tri-1","tri-2","tri-3","sku-yuzu","sku-satsuma","sku-cola","rtb-chef","rtb-ingredients","sku-hokkaido"]
grid=''.join(f'<img src="{sq(i)}">' for i in grid_ids)
all_ids=[it[0] for _sec,_blurb,items in POSTS for it in items]

HTML=f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ki — Social · Phase One</title>
<style>
/* Website type system (uk.ki.bio sheet): Obviously Regular + Semibold ONLY, never Black.
   Display = refined uppercase Semibold, lh~1.0, negative tracking. Body = Regular 1.6. */
@font-face{{font-family:'Obviously';src:url(data:font/woff2;base64,{FONT_SEMI}) format('woff2');font-weight:600}}
@font-face{{font-family:'Obviously';src:url(data:font/woff2;base64,{FONT_MED}) format('woff2');font-weight:500}}
@font-face{{font-family:'Obviously';src:url(data:font/woff2;base64,{FONT_REG}) format('woff2');font-weight:400}}
:root{{--paper:#EFEDE6;--ink:#111111;--muted:#555555;--meta:#6B7280;--gold:#B88448;--sage:#619C8A;--line:#ddd8cc}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--paper);color:var(--ink);font-family:'Obviously',-apple-system,sans-serif;font-weight:400;-webkit-font-smoothing:antialiased;letter-spacing:-.005em}}
.wrap{{max-width:1200px;margin:0 auto;padding:0 40px}}
/* cover */
.cover{{padding:96px 0 40px;border-bottom:1px solid var(--line)}}
.cover .kanji{{font-family:'Obviously';font-weight:600;color:var(--gold);font-size:26px}}
.cover h1{{font-family:'Obviously';font-weight:500;text-transform:uppercase;font-size:78px;line-height:1.0;letter-spacing:-.02em;margin:14px 0 10px}}
.cover .sub{{font-family:'Obviously';font-weight:600;text-transform:uppercase;letter-spacing:.16em;color:var(--gold);font-size:14px}}
.cover p{{max-width:640px;margin-top:22px;font-size:17px;line-height:1.6;color:var(--muted)}}
.legend{{display:flex;gap:26px;margin-top:30px;flex-wrap:wrap;font-size:13px;color:var(--meta)}}
.legend b{{color:var(--ink)}}
/* profile grid */
.profile{{margin:54px 0 20px;background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;max-width:430px;box-shadow:0 20px 50px rgba(40,34,20,.10)}}
.phead{{display:flex;align-items:center;gap:20px;padding:22px 22px 14px}}
.pava{{width:76px;height:76px;border-radius:50%;overflow:hidden;background:#000;flex:0 0 auto}}
.pava img{{width:100%;height:100%;object-fit:cover;display:block}}
.pstats{{display:flex;gap:22px;font-size:14px}}.pstats b{{display:block;font-size:18px}}
.pbio{{padding:0 22px 16px;font-size:14px;line-height:1.5}}
.pbio .h{{font-weight:700}}
.pgrid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;background:#fff}}
.pgrid img{{width:100%;aspect-ratio:1;object-fit:cover;display:block}}
/* sections */
.sec{{padding:64px 0;border-bottom:1px solid var(--line)}}
.sechead{{margin-bottom:34px}}
.kick{{font-family:'Obviously';font-weight:600;text-transform:uppercase;letter-spacing:.16em;color:var(--gold);font-size:13px}}
.sechead h2{{font-family:'Obviously';font-weight:500;text-transform:uppercase;font-size:38px;letter-spacing:-.02em;line-height:1.0;margin:10px 0 12px}}
.sechead p{{max-width:680px;color:var(--muted);font-size:16px;line-height:1.6}}
.pano{{margin-bottom:36px}}
.panolabel{{font-size:12px;text-transform:uppercase;letter-spacing:.14em;color:#6b665a;margin-bottom:10px}}
.pano img{{width:100%;border-radius:10px;display:block;box-shadow:0 14px 34px rgba(40,34,20,.14)}}
/* concept card */
.concept{{display:grid;grid-template-columns:auto 300px;gap:44px;align-items:center;
  background:#fff;border:1px solid var(--line);border-radius:18px;padding:34px 38px;margin-bottom:22px;
  box-shadow:0 14px 36px rgba(40,34,20,.06)}}
.mocks{{display:flex;gap:26px;align-items:center}}
/* IG feed card */
.ig,.story{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}}
.ig{{width:326px;background:#fff;border:1px solid #efefef;border-radius:8px;overflow:hidden;box-shadow:0 16px 40px rgba(40,34,20,.12);flex:0 0 auto}}
.igh{{display:flex;align-items:center;gap:10px;padding:11px 12px}}
.ava{{width:34px;height:34px;border-radius:50%;overflow:hidden;background:#000;flex:0 0 auto}}
.ava img{{width:100%;height:100%;object-fit:cover;display:block}}
.hmeta{{display:flex;flex-direction:column;line-height:1.2;flex:1}}
.hmeta b{{font-size:13px}}.hmeta span{{font-size:11px;color:#8a8a8a}}
.hmeta-solo{{justify-content:center}}
.dots{{color:#262626;letter-spacing:1px}}
.igimg{{width:100%;aspect-ratio:1;object-fit:cover;display:block}}
.igact{{display:flex;justify-content:space-between;align-items:center;padding:10px 12px 6px}}
.igact .l{{display:flex;gap:14px}}
.iglikes{{padding:0 12px;font-size:13px;font-weight:700}}
.igcap{{padding:4px 12px 2px;font-size:13px;line-height:1.45}}
.igcap b{{font-weight:700}}
.igtime{{padding:6px 12px 12px;font-size:10px;color:#9a9a9a;text-transform:uppercase;letter-spacing:.05em}}
/* Story card */
.story{{width:210px;aspect-ratio:9/16;border-radius:22px;overflow:hidden;position:relative;background:#000;box-shadow:0 16px 40px rgba(40,34,20,.18);flex:0 0 auto}}
.story>img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.sbars{{position:absolute;top:10px;left:10px;right:10px;display:flex;gap:4px;z-index:2}}
.sbars i{{flex:1;height:2.5px;border-radius:2px;background:rgba(255,255,255,.45)}}
.sbars i:first-child{{background:#fff}}
.shead{{position:absolute;top:22px;left:12px;right:12px;display:flex;align-items:center;gap:8px;z-index:2;color:#fff}}
.shead .ava{{width:26px;height:26px}}.shead .ava span{{font-size:9px}}
.shead b{{font-size:12px}}.shead span{{font-size:11px;opacity:.8}}
.sfoot{{position:absolute;bottom:12px;left:12px;right:12px;display:flex;align-items:center;gap:10px;z-index:2}}
.smsg{{flex:1;border:1.5px solid rgba(255,255,255,.7);border-radius:999px;padding:9px 14px;color:#fff;font-size:11px}}
.sfoot svg{{width:20px;height:20px;stroke:#fff}}
/* copy col */
.copy{{padding-top:6px;min-width:200px}}
.cname{{font-family:'Obviously';font-weight:500;text-transform:uppercase;font-size:22px;letter-spacing:-.02em;line-height:1.0}}
.clabel{{margin-top:18px;font-size:11px;text-transform:uppercase;letter-spacing:.14em;color:var(--gold);font-weight:600}}
.cbox{{margin-top:8px;background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-size:15px;line-height:1.55;color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}}
.cmeta{{margin-top:14px;font-size:12px;color:var(--meta);letter-spacing:.02em}}
.cdl{{margin-top:16px;display:flex;gap:9px;flex-wrap:wrap}}
.cdl a{{font-family:'Obviously';font-weight:500;font-size:11.5px;text-transform:uppercase;letter-spacing:.04em;
  color:var(--ink);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:8px 14px;transition:.15s}}
.cdl a:hover{{background:var(--ink);color:#fff;border-color:var(--ink)}}
.dlall{{margin-top:26px;font-family:'Obviously';font-weight:500;font-size:13px;text-transform:uppercase;letter-spacing:.05em;
  color:#fff;background:var(--ink);border:none;border-radius:999px;padding:13px 24px;cursor:pointer;transition:.15s}}
.dlall:hover{{background:#000;transform:translateY(-1px)}}
.foot{{padding:50px 0 80px;color:var(--meta);font-size:13px;line-height:1.6}}
@media(max-width:1080px){{.concept{{grid-template-columns:1fr}}.mocks{{flex-wrap:wrap}}}}
@media(max-width:560px){{.wrap{{padding:0 20px}}.cover h1{{font-size:52px}}.ig{{width:300px}}}}
</style></head>
<body>
<div class="wrap">
  <header class="cover">
    <div class="kanji">気</div>
    <div class="sub">Ki · Instagram · Phase One</div>
    <h1>Social<br>Content</h1>
    <p>A first flight of Instagram creative for Ki — single-flavour features, reason-to-believe statements, a grid-spanning range triptych and brand-voice one-liners. Every post is designed on the Ki landscape system and delivered crisp at <b>1080×1080</b> (feed) and <b>1080×1920</b> (story).</p>
    <div class="legend"><span><b>14</b> concepts</span><span><b>28</b> assets</span><span>Feed <b>1:1</b> + Story <b>9:16</b></span><span>Handle <b>@ki.bio</b></span></div>
    <button class="dlall" id="dlall">↓ Download all 28 image assets</button>
    <div class="profile">
      <div class="phead"><div class="pava"><img src="{LOGO_HERITAGE}" alt="KI"></div>
        <div class="pstats"><div><b>112</b>posts</div><div><b>2,480</b>followers</div><div><b>5</b>following</div></div>
      </div>
      <div class="pbio"><div class="h">Ki · Nicotine Pouches</div>気 A moment of clarity, made with intention. All in a little pouch.</div>
      <div class="pgrid">{grid}</div>
    </div>
  </header>
  {''.join(concepts_html)}
  <footer class="foot">Ki · Social Phase One · designed on the Ki landscape system · Obviously + Noto Sans JP · gold #B88448.<br>Full-resolution PNGs (1080) live alongside this deck in <b>/phase-one/1080/</b> — use the download links on each concept, or “Download all”.</footer>
</div>
<script>
(function(){{
  var ids={json.dumps(all_ids)};
  var btn=document.getElementById('dlall'); if(!btn) return;
  btn.addEventListener('click',function(){{
    var files=[]; ids.forEach(function(id){{ files.push('1080/'+id+'_1x1.png'); files.push('1080/'+id+'_9x16.png'); }});
    var i=0;(function next(){{ if(i>=files.length) return;
      var a=document.createElement('a'); a.href=files[i]; a.download=files[i].split('/').pop();
      document.body.appendChild(a); a.click(); document.body.removeChild(a); i++; setTimeout(next,350); }})();
  }});
}})();
</script>
</body></html>'''

open(OUT,"w").write(HTML)
print("wrote deck:", round(os.path.getsize(OUT)/1024/1024,2),"MB ->", OUT)
