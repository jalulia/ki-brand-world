import PptxGenJS from "pptxgenjs";
const LIB="/sessions/modest-sharp-gauss/mnt/Ki Brand/06_World-of-Ki/social/assets/library";
const HERITAGE="/sessions/modest-sharp-gauss/mnt/Ki Brand/06_World-of-Ki/social/assets/img-ki-heritage.png";
const OUT="/sessions/modest-sharp-gauss/mnt/Ki Brand/06_World-of-Ki/social/Ki_Social_Showcase.pptx";

const INK="111111", PAPER="F4F2ED", MUTED="555555", META="6B7280", GOLD="B88448", LINE="E7E3DA", WHITE="FFFFFF";
const HEAD="Obviously";           // resolves to installed Obviously (Semibold via bold flag)
const BODY="Obviously";

const pptx=new PptxGenJS();
pptx.defineLayout({name:"W",width:13.333,height:7.5});
pptx.layout="W";

const posts={
 "sku-yuzu":     {t:"Yuzu Mint",     cap:"Hit refresh 🔄 🌱 🍋"},
 "sku-satsuma":  {t:"Satsuma Citrus",cap:"We’ve got a juicy secret (it’s satsuma) 🍊"},
 "sku-maple":    {t:"Maple Coffee",  cap:"Rich coffee. Sweet maple. A match made in heaven."},
 "sku-cola":     {t:"Tokyo Cola",    cap:"Enjoy the refined flavour of Tokyo craft cola."},
 "sku-hokkaido": {t:"Hokkaido Mint", cap:"Chill. Literally ❄️"},
 "rtb-ingredients":{t:"Ingredients", cap:"Obsessed with ingredients? Us? Absolutely 🤓"},
 "rtb-chef":     {t:"Hired a Chef",  cap:"Yes, a chef, for a pouch 👨‍🍳"},
 "rtb-sweetened":{t:"Sweetened by Nature",cap:"Natural sweeteners are better than artificial ones."},
 "rtb-can":      {t:"Regular Sized Can",cap:"Environmentally certified, lower carbon, pine-oil cans."},
 "range-1":      {t:"The Range · 1",  cap:"A better nicotine experience has landed 👀"},
 "range-2":      {t:"The Range · 2",  cap:"A new dawn is here 🌅"},
 "range-3":      {t:"The Range · 3",  cap:"The smoke has cleared."},
};

// ---- native post card ----
function card(slide, key, x, y, w){
  const p=posts[key];
  const img=w-0.16, headH=0.56, capH=0.82;
  const cardH=headH+img+capH+0.12;
  slide.addShape("roundRect",{x,y,w,h:cardH,rectRadius:0.08,fill:{color:WHITE},line:{color:LINE,width:0.75},shadow:{type:"outer",blur:11,offset:4,angle:90,color:"6A5A40",opacity:0.20}});
  // header — heritage logo avatar
  const av=0.36;
  slide.addImage({path:HERITAGE,x:x+0.12,y:y+0.11,w:av,h:av});
  slide.addText("ki.bio",{x:x+0.54,y:y+0.10,w:w-0.62,h:0.24,fontFace:HEAD,bold:true,color:INK,fontSize:10,valign:"middle",margin:0});
  slide.addText("",{x:x+0.54,y:y+0.30,w:w-0.62,h:0.20,fontFace:BODY,color:META,fontSize:8,valign:"middle",margin:0});
  // media (placed image, live)
  slide.addImage({path:`${LIB}/${key}-1x1.png`,x:x+0.08,y:y+headH,w:img,h:img});
  // caption
  slide.addText([
    {text:"ki.bio ",options:{fontFace:HEAD,bold:true,color:INK}},
    {text:p.cap,options:{fontFace:BODY,color:INK}},
  ],{x:x+0.1,y:y+headH+img+0.06,w:w-0.2,h:capH,fontSize:9,align:"left",valign:"top",lineSpacingMultiple:1.05,margin:0});
  return cardH;
}

function sectionSlide(title, eyebrow, keys){
  const s=pptx.addSlide(); s.background={color:PAPER};
  s.addText(eyebrow,{x:0.55,y:0.45,w:12,h:0.3,fontFace:HEAD,bold:true,color:GOLD,fontSize:12,charSpacing:2,margin:0});
  s.addText(title.toUpperCase(),{x:0.52,y:0.72,w:12,h:0.7,fontFace:HEAD,bold:true,color:INK,fontSize:30,charSpacing:-0.5,margin:0});
  const n=keys.length, marg=0.55, gap=0.16;
  const w=(13.333-2*marg-(n-1)*gap)/n;
  const cardH=0.56+(w-0.16)+0.82+0.12;
  const y=(7.5+1.5-cardH)/2;   // centre below header band
  keys.forEach((k,i)=>card(s,k,marg+i*(w+gap),y,w));
  s.addText("Feed · 1080 × 1080 px",{x:0.55,y:7.0,w:6,h:0.3,fontFace:BODY,color:META,fontSize:9,charSpacing:1,margin:0});
}

// ---- cover ----
const c=pptx.addSlide(); c.background={color:INK};
c.addImage({path:HERITAGE,x:(13.333-1.7)/2,y:1.25,w:1.7,h:1.7});
c.addText("KI SOCIAL",{x:0,y:3.15,w:13.333,h:1.0,align:"center",fontFace:HEAD,bold:true,color:PAPER,fontSize:52,charSpacing:-1,margin:0});
c.addText("PHASE ONE · SOCIAL ASSET SHOWCASE",{x:0,y:4.15,w:13.333,h:0.4,align:"center",fontFace:HEAD,bold:true,color:GOLD,fontSize:14,charSpacing:4,margin:0});
c.addText("Ten posts · composed to the brand system",{x:0,y:4.65,w:13.333,h:0.4,align:"center",fontFace:BODY,color:"9A958C",fontSize:12,margin:0});
const cols=["7FA33C","E08A2E","8A5A3B","B23A48","3E8E7E"];
cols.forEach((col,i)=>c.addShape("rect",{x:i*(13.333/5),y:7.32,w:13.333/5,h:0.18,fill:{color:col}}));

sectionSlide("SKU Posts","01 — Flavour heroes",["sku-yuzu","sku-satsuma","sku-maple","sku-cola","sku-hokkaido"]);
sectionSlide("Reasons to Believe","02 — Proof points",["rtb-ingredients","rtb-chef","rtb-sweetened","rtb-can"]);
sectionSlide("The Range · Carousel","03 — The line render, three crops",["range-1","range-2","range-3"]);

await pptx.writeFile({fileName:OUT});
console.log("wrote",OUT);
