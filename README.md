# AI Resume Builder and ATS Optimization Agent

This project is a full-stack application that allows users to upload a resume, extract key information, calculate an ATS score, enhance skills and experience using Gemini AI, and generate a clean DOCX resume. It demonstrates backend development, frontend development, NLP, AI integration, and full-stack deployment.

---

Working Link:
https://resume-frontend-qhf5.onrender.com/

## Features

### 1. Resume Upload
Supports:
- PDF
- DOCX
- TXT

### 2. Resume Parsing
Extracts essential fields using a custom lightweight spaCy parser:
- Name  
- Email  
- Phone  
- Skills  
- Experience lines  

The parser is optimized for speed and reliability.

### 3. ATS Score Calculation
Scores resumes based on:
- Keyword relevance  
- Skills presence  
- Experience depth  
- Contact information  
- Education signals  

### 4. AI-Based Enhancement (Gemini 2.5 Flash)
Uses the Gemini API to:
- Rewrite experience points
- Improve clarity and structure
- Enhance skills list
- Align content with job-specific keywords

### 5. DOCX Resume Generator
Generates a clean, ATS-friendly resume using:
- A DOCX template
- The DocxTemplate library

---

## Tech Stack

### Backend (FastAPI)
- FastAPI  
- Uvicorn  
- spaCy  
- Gemini API  
- DocxTemplate  
- Python 3.11  
- Docker  

### Frontend (React + Vite)
- React  
- Axios  
- Vite  

---

## Project Structure

ai-resume-agent/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── parse_resume.py
│ │ ├── gemini_client.py
│ │ ├── ats.py
│ │ ├── generate_docx.py
│ │ └── templates/
│ │ └── resume_template.docx
│ ├── Dockerfile
│ └── requirements.txt
│
└── frontend/
├── src/
│ ├── App.jsx
│ ├── api.js
│ └── main.jsx
├── package.json
└── vite.config.js



### Frontend Setup

cd frontend
npm install
npm run dev


---

## Deployment (Render)

Both backend and frontend can be deployed on Render.

- Backend uses Docker  
- Frontend uses Vite build + static file hosting  
- A `render.yaml` file can automate deployment and service creation  

---

## Environment Variables

### Backend
GEMINI_API_KEY=your_key


### Frontend
https://resume-backend-z71j.onrender.com

---

## Notes

- Heavy libraries like `pyresparser` are intentionally excluded to avoid deployment issues.  
- The resume parser is lightweight for fast execution on Render.  
- The DOCX generator uses a simple customizable template located in `backend/app/templates/`.  

---

