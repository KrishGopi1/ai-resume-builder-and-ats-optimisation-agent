import spacy

nlp = spacy.load("en_core_web_sm")

def parse_resume(path):
    text = open(path, "r", errors="ignore").read()
    doc = nlp(text)

    # Extract candidate info (simple but works for ATS)
    data = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
        "experience": [],
    }

    # Email
    for token in doc:
        if token.like_email:
            data["email"] = token.text
            break

    # Phone
    for token in doc:
        if token.like_num and len(token.text) >= 10:
            data["phone"] = token.text
            break

    # Name (first line of resume)
    first_line = text.strip().split("\n")[0]
    data["name"] = first_line.strip()

    # Skills (naive extraction)
    skills_list = ["python", "java", "javascript", "react", "c++", "c", "aws", "node", "sql", "mongodb", "django", "fastapi", "ml", "ai"]
    low_text = text.lower()
    data["skills"] = [s for s in skills_list if s in low_text]

    # Experience (detect bullets)
    lines = text.split("\n")
    data["experience"] = [l.strip() for l in lines if l.strip().startswith("-") or l.strip().startswith("*")]

    return data
