// Native editable PPTX from slides.json (shared spec). Real text boxes + placed images + shapes.
import fs from 'fs';
import PptxGenJS from 'pptxgenjs';

const spec = JSON.parse(fs.readFileSync(new URL('./slides.json', import.meta.url)));
const {W,H,slides} = spec;
const IN = px => px/96;                 // px -> inches (96dpi)
const PT = px => px*0.75;               // px -> points
const hex = c => (c||'#000000').replace('#','').toUpperCase();
const FONT = w => w>=600 ? 'Obviously SemiBold' : (w>=500 ? 'Obviously Medium' : 'Obviously');

const p = new PptxGenJS();
p.defineLayout({name:'KI', width:IN(W), height:IN(H)});
p.layout='KI';

for(const s of slides){
  const sl = p.addSlide();
  sl.background = { color: hex(s.bg||'#EFEDE6') };
  for(const e of s.els){
    if(e.type==='rect'){
      sl.addShape('rect',{x:IN(e.x),y:IN(e.y),w:IN(e.w),h:IN(e.h),fill:{color:hex(e.fill)},line:{type:'none'}});
    } else if(e.type==='image'){
      const opt={path:e.src,x:IN(e.x),y:IN(e.y),w:IN(e.w),h:IN(e.h)};
      if(e.round){ opt.rounding=false; } // square placed image (fully editable); corners via FX optional
      sl.addImage(opt);
    } else { // text
      const opt={
        x:IN(e.x), y:IN(e.y), w:IN(e.w), h:IN(e.h),
        fontFace:FONT(e.weight||400), fontSize:PT(e.size), color:hex(e.color),
        align:e.align||'left', valign:'top', margin:0,
        bold:false, charSpacing: e.spacing? PT(e.spacing):0,
        lineSpacingMultiple: e.lh||1.15,
      };
      let txt = String(e.text);
      // manual line breaks
      const runs = txt.split('\n').map((line,i)=>({text:line, options:{breakLine:true}}));
      sl.addText(runs, opt);
    }
  }
}
const out = process.argv[2] || 'Ki_Social_Phase-One.pptx';
await p.writeFile({fileName: out});
console.log('wrote', out);
