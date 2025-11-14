import uuid,shutil,json
from fastapi import FastAPI,File,UploadFile,Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse,FileResponse
from pathlib import Path
from .parse_resume import parse_resume
from .ats import score
from .gemini_client import gen_text
from .generate_docx import render

app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

u=Path("uploads");u.mkdir(exist_ok=True)

@app.post("/upload")
async def up(f:UploadFile=File(...)):
    p=u/f"{uuid.uuid4().hex}_{f.filename}"
    with open(p,"wb") as w: shutil.copyfileobj(f.file,w)
    return {"parsed":parse_resume(str(p))}

@app.post("/score")
async def sc(p:str=Form(...),kw:str=Form("")):
    return {"score":score(json.loads(p),[i.strip() for i in kw.split(",")])}

@app.post("/enhance")
async def en(p:str=Form(...),title:str=Form(""),kw:str=Form("")):
    d=json.loads(p)
    exp=d.get("experience") or []
    if isinstance(exp,str): exp=[i for i in exp.splitlines() if i]
    k=[i for i in kw.split(",") if i]
    out=[]
    for b in exp:
        pr=f"Rewrite for resume. Job:{title}. Keywords:{', '.join(k)}. Text:{b}"
        out.append({"o":b,"e":gen_text(pr)})
    sk=", ".join(d.get("skills",[]) if isinstance(d.get("skills"),list) else [str(d.get("skills",""))])
    sk2=gen_text(f"Clean top skills for {title}: {sk}")
    return {"exp":out,"skills":sk2}

@app.post("/generate_docx")
async def g(e:str=Form(...),name:str=Form(""),email:str=Form(""),phone:str=Form(""),hl:str=Form("")):
    d=json.loads(e)
    exp="
".join([i.get("e") for i in d.get("exp",[])])
    ctx={"name":name,"email":email,"phone":phone,"headline":hl,"skills":d.get("skills",""),"experience":exp}
    p=render(ctx)
    return FileResponse(p,filename=Path(p).name)
