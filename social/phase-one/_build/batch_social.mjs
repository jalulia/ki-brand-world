// Render all social HTMLs in ONE browser session. node batch_social.mjs
import { chromium } from 'playwright-core';
import fs from 'fs'; import path from 'path';
const DIR=path.resolve('.'); const CACHE=DIR+'/home/.cache/ms-playwright';
function findShell(){let d=fs.readdirSync(CACHE).filter(x=>x.startsWith('chromium_headless_shell'));
  if(d.length)return path.join(CACHE,d.sort().pop(),'chrome-linux','headless_shell');
  d=fs.readdirSync(CACHE).filter(x=>x.startsWith('chromium-'));return path.join(CACHE,d.sort().pop(),'chrome-linux','chrome');}
const B='/sessions/quirky-bold-heisenberg/mnt/outputs/_social/build';
const O='/sessions/quirky-bold-heisenberg/mnt/Ki Brand/06_World-of-Ki/social/phase-one/1080';
// only the real post HTMLs — tri-* are photo crops (sliced from the hero), never re-rendered here
const files=fs.readdirSync(B).filter(f=>/_(sq|st)\.html$/.test(f) && !f.startsWith('tri'));
const b=await chromium.launch({executablePath:findShell(),args:['--no-sandbox','--disable-gpu','--force-color-profile=srgb']});
for(const f of files){
  const sq=f.endsWith('_sq.html'); const id=f.replace(/_(sq|st)\.html$/,'');
  const w=1080, h=sq?1080:1920; const out=`${O}/${id}_${sq?'1x1':'9x16'}.png`;
  const pg=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
  await pg.goto('file://'+path.join(B,f),{waitUntil:'networkidle',timeout:30000}).catch(()=>{});
  try{await pg.evaluate(()=>document.fonts.ready);}catch(e){}
  await pg.waitForTimeout(250);
  const el=await pg.$('[data-shot]');
  await (el||pg).screenshot({path:out});
  await pg.close(); console.log('OK',path.basename(out));
}
await b.close(); console.log('ALL DONE');
