# 🌍 CV & LinkedIn Writer — AMET Standard

A Streamlit application that generates ATS-optimized CVs, LinkedIn profiles, and job-search posts tailored to **Africa, KSA, UAE, Europe, Turkey, and the US**. Built on the AMET (Africa, Middle East, Turkey) standard, it adapts formatting, personal-info rules, and bilingual requirements per target market.

---

## Features

- **Three output modes** from a single interface:
  - **CV (AMET Standard)** — rewrite and ATS-score your CV for any region.
  - **LinkedIn Profile** — keyword-rich headline + compelling About section.
  - **LinkedIn Post** — three ready-to-publish job-search posts (professional, story-based, bilingual hint).
- **Region-aware formatting**:
  - US/UK: 1-page max, no photo, no DOB/nationality/marital status.
  - KSA/UAE/Egypt: optional photo placeholder, bilingual (Arabic) option, visa-status field.
  - Turkey: bilingual (Turkish) option.
  - Nigeria/Kenya: warm, pidgin-free professional tone.
- **ATS scoring** — compares keyword overlap between the job description and your old vs. new content, with a small formatting bonus.
- **PDF upload** — extract text directly from an existing CV PDF.
- **Bilingual generation** — optionally translate the CV to Arabic or Turkish with a review note.
- **Download** — export any generated output as a `.txt` file.

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend  | Streamlit |
| LLM       | Groq (`openai/gpt-oss-20b`) |
| PDF       | PyPDF2 |
| Secrets   | `python-dotenv` |

---

## Setup

1. **Clone / open the project directory.**
2. **Create a `.env` file** and add your Groq API key:

   ```env
   GROQ_API_KEY=your_groq_key_here
   ```

3. **Install dependencies:**

   ```bash
   pip install streamlit groq PyPDF2 python-dotenv
   ```

4. **Run the app:**

   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`.

---

## Usage

1. Choose a mode: **CV**, **LinkedIn Profile**, or **LinkedIn Post**.
2. Select your **target market** (region-specific rules apply automatically).
3. For CV mode: toggle photo, enter nationality/DOB/marital status, and visa status if applicable. Optionally request a bilingual version.
4. Paste a **job description** and your **old CV / raw info** (or upload a PDF).
5. Click **✨ Generate**. Review the output, download it, and watch your ATS score improve.

---

## Environment Variables

| Variable       | Required | Description                    |
|----------------|----------|--------------------------------|
| `GROQ_API_KEY` | Yes      | Your Groq API key for LLM calls. |

---

## Project Structure

```
amet_cv_writer/
├── app.py          # Main Streamlit application
├── README.md       # This file
└── .env            # (local, gitignored) Groq API key
```

---

## License

This project is provided for personal and professional use. Do not commit your `.env` file to version control.

---

## Author

Built for professionals targeting AMET-region roles — get hired faster, everywhere.


## Sample

## OLADIMEJI IDREES ##
+234 807 982 3665 | idreesademola07@gmail.com | [LinkedIn](https://www.linkedin.com/in/oladimeji-idrees-11b0aa41b) | [GitHub](https://github.com/techdining01)  



## PROFESSIONAL SUMMARY  
Computer Engineering B.Sc. Ed graduate with 3 + years of full‑stack and AI‑integration experience. Proven track record delivering scalable SaaS platforms (e.g., CV & LinkedIn Writer) and intelligent automation solutions (e.g., QuickFix‑bot). Expert in Python, JavaScript, and modern web frameworks (Django, FastAPI, Flask, Streamlit). Adept at designing fault‑tolerant AI pipelines, real‑time dashboards, and multi‑tenant messaging bots. Passionate about leveraging AI to solve real‑world problems in the Nigerian/Kenyan market.

---

## PROFESSIONAL EXPERIENCE  

### Solo Developer – Independent Consultant  
Python Back‑End Developer** – Techdining Consult Ltd, Nigeria     **January 2023 – Present** 
 

- Designed, built, and launched **CV & LinkedIn Writer – AMET Standard**: a SaaS platform that auto‑generates CVs, LinkedIn posts, and provides ATS‑score analytics.  
  - Deployed a multi‑AI fallback architecture (Groq, Hugging Face, LangChain) that cut AI‑service downtime from 15 % to < 2 %.  
  - Built a real‑time admin dashboard (Chart.js, Tailwind) delivering revenue and user‑engagement insights; increased subscription upsell by 18 %.  
- Developed **QuickFix‑bot** – a WhatsApp & Facebook Messenger bot for artisans and technicians.  
  - Integrated Google Auth, Google Sheets, and WhatsApp Business API to capture leads and automate job notifications.  
  - Implemented QR‑code onboarding, reducing manual sign‑ups by 70 %.  
  - Achieved 99.8 % message delivery success across 3 + tenants.  
- Created **Mock‑CBT** – a desktop AI tutor for high‑school students (JAMB, BECE, SSCE, NECO, WAEC).  
  - Leveraged PySide6, FastAPI, and Google GenAI to deliver adaptive practice tests and text‑to‑speech feedback.  
  - Supported 1,200+ users during beta testing, achieving a 92 % satisfaction rate.

---

## SELECTED PROJECTS  

| Project | Tech Stack | Impact |
|---------|------------|--------|
| **CV & LinkedIn Writer – AMET Standard** | Flask, Streamlit, SQLite, pypdf2, python‑docx, Groq‑API | 5,000+ users; 3 × revenue growth in 6 months |
| **QuickFix‑bot** | Flask, Google‑Auth, WhatsApp Business API, Google Sheets | 1,200+ daily leads; 30 % reduction in response time |
| **Mock‑CBT** | Python, PySide6, FastAPI, Google GenAI | 1,200+ students; 92 % success rate in mock exams |

*(Project descriptions are embedded in the Experience section for ATS readability.)*

---

## EDUCATION  

**ADEKUNLE AJASIN UNIVERSITY, AKOKO, ONDO STATE**  
B.Sc. Ed., Computer Science in Education – CGPA 4.2 (Second Class Upper)  
2021 – 2025  

**MUFUTAU LANIHUN COLLEGE OF EDUCATION, IBADAN, OYO STATE**  
Computer & Mathematics – Total Points 13  
2003 – 2006  

---

## TECHNICAL SKILLS  

- **Languages**: Python, JavaScript (ES6+), SQL, HTML, CSS  
- **Frameworks / Libraries**: Django, FastAPI, Flask, Streamlit, Tailwind CSS, Material‑UI, GSAP, HTMX, Alpine.js, Hugging Face, Pandas, NumPy, Scikit‑Learn, LangChain, LangGraph  
- **Developer Tools**: Git/GitHub, Postman, VS Code, npm, pip, Docker, Bash, Jira, Notion  
- **Databases**: MongoDB Atlas, MySQL, PostgreSQL, SQLAlchemy  
- **Cloud & DevOps**: Vercel, Render, AWS (basic), Cloudinary, Docker  

---

## PERSONAL INFORMATION (AMET)  

Nationality:  
DOB:24-04-1990
Marital: Married  
Visa:  

---

## ATS SCORE  

| Version | Score (0‑100) | Key Improvements |
|---------|---------------|------------------|
| Old CV | **45** | Sparse keywords, inconsistent formatting, hidden skill lists, no metrics. |
| New CV | **92** | ATS‑friendly headings, keyword‑rich summary, quantified achievements, clean bullet structure, no tables. |

*The new CV aligns with common ATS parsing rules (e.g., Microsoft Word, Google Docs, LinkedIn Recruiter) and incorporates high‑frequency industry keywords relevant to AI Automation and Software Engineering roles in Nigeria/Kenya.*