import os,json,subprocess,re,sys
ROOT="/Users/juliacompton/Library/CloudStorage/GoogleDrive-comptonjulia@gmail.com/My Drive/Ki Render Sheet"
OUT="/Users/juliacompton/Documents/Claude/Projects/Ki Brand/06_World-of-Ki/renders/manifest.json"
FL={"Tokyo Cola":"cola","Hokkaido Mint":"hokkaido","Maple Coffee":"maple","Satsuma Citrus":"satsuma","Yuzu Mint":"yuzu"}
SLOT={"01 Front ortho":"front-ortho","02 Side ortho":"side-ortho","03 Top view":"top","04 Bottom view":"bottom",
"05 Cross-section":"cross-section","06 Exploded view":"exploded","07 Three-quarter beauty":"beauty","08 Open puck":"open",
"09 Stacked pair":"stacked","10 Label flat unwrapped":"label-flat","11 Detail insets":"detail","12 Material callouts":"callouts","13 Color palette":"palette"}
def gid(p):
    try: return subprocess.run(["xattr","-p","com.google.drivefs.item-id#S",p],capture_output=True,text=True).stdout.strip() or None
    except: return None
def hsize(n): return f"{n/1048576:.1f} MB" if n>=1048576 else f"{n/1024:.0f} KB"
def strength(name,slot):
    if "KI_ANGLES" in name: return None
    m=re.search(r'(3|9)\s?MG',name,re.I)
    if m: return m.group(1)+"MG"
    m=re.search(r'_(\d\d)\.png$',name)
    if m: return {"01":"3MG","02":"9MG","03":"3MG","04":"9MG","07":"3MG","08":"9MG"}.get(m.group(1))
    if name.endswith("_00.pdf"): return "3MG"
    return None
def preview(name,fk):
    m=re.search(r'_(\d\d)\.png$',name)
    if fk!="line" and m: return f"previews/{fk}/{m.group(1)}.webp"
    if fk=="line":
        m=re.search(r'KI_ANGLES_(\d\d)',name)
        if m: return f"previews/line/{m.group(1)}.webp"
    if "sleeve" in name.lower() and "3MG" in name.upper(): return f"previews/labels/{fk}_sleeve_wide.webp"
    if name.upper().startswith("UK_LABEL") and (("3MG" in name.upper()) or name.endswith("_00.pdf")): return f"previews/labels/{fk}_label.webp"
    return None
man={"generated":"2026-07-02","rootFolderId":gid(ROOT),"flavors":{}}
missing=0
for fname,fk in list(FL.items())+[("Full Line","line")]:
    fdir=os.path.join(ROOT,"UK",fname)
    fobj={"folderId":gid(fdir),"slots":{}}
    for sf in sorted(os.listdir(fdir)):
        sp=os.path.join(fdir,sf)
        if not os.path.isdir(sp): continue
        files=[]
        for f in sorted(os.listdir(sp)):
            p=os.path.join(sp,f)
            if f.startswith(".") or not os.path.isfile(p): continue
            i=gid(p)
            if not i: missing+=1
            part="Sleeve" if "sleeve" in f.lower() else ("Label" if f.upper().startswith("UK_LABEL") else None)
            files.append({"name":f,"fmt":f.rsplit(".",1)[-1].upper(),"size":hsize(os.path.getsize(p)),"part":part,
                          "strength":strength(f,SLOT.get(sf)),"id":i,"preview":preview(f,fk)})
        files.sort(key=lambda x:("sleeve" not in x["name"].lower(), x["name"].lower()))
        sid=SLOT.get(sf)
        if fk=="line":
            for fl_ in files:
                m=re.search(r'KI_ANGLES_(\d\d)',fl_["name"])
                if m: fobj["slots"]["angle-"+m.group(1)]={"folderId":gid(sp),"files":[fl_]}
        elif sid:
            fobj["slots"][sid]={"folderId":gid(sp),"files":files}
    fobj["slots"]["inbox"]={"folderId":fobj["folderId"],"files":[]}
    man["flavors"][fk]=fobj
json.dump(man,open(OUT,"w"),indent=1,ensure_ascii=False)
ids=sum(1 for fv in man["flavors"].values() for s in fv["slots"].values() for f in s["files"] if f["id"])
tot=sum(len(s["files"]) for fv in man["flavors"].values() for s in fv["slots"].values())
print(f"root={man['rootFolderId']} files={tot} with_id={ids} missing_id={missing}")
