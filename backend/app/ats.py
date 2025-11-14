def score(d,kw):
    s=0
    t=" ".join([str(v) for v in d.values() if v]).lower()
    if d.get("email") or d.get("phone"): s+=20
    if d.get("education"): s+=15
    if d.get("experience") or d.get("company_names"): s+=25
    kw=[i.lower() for i in kw if i]
    if kw:
        f=sum(1 for i in kw if i in t)
        s+=int(40*(f/max(1,len(kw))))
    return min(100,s)
