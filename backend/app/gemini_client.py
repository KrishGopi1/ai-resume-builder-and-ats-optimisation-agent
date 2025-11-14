import os
from google import genai
from google.genai import types

k=os.getenv("GEMINI_API_KEY")
def client():
    return genai.Client(api_key=k) if k else genai.Client()

def gen_text(p):
    r=client().models.generate_content(model="gemini-2.5-flash",contents=p,config=types.GenerateContentConfig())
    try:return r.text
    except:return str(r)
