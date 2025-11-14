from docxtpl import DocxTemplate
from pathlib import Path
import time

def render(ctx):
    t=Path(__file__).parent/"templates"/"resume_template.docx"
    o=Path("outputs");o.mkdir(exist_ok=True)
    out=o/f"res_{int(time.time())}.docx"
    d=DocxTemplate(str(t))
    d.render(ctx)
    d.save(str(out))
    return str(out)
