import os
import streamlit as st
from groq import Groq
import PyPDF2
from dotenv import load_dotenv


load_dotenv()

st.set_page_config(page_title="CV & LinkedIn Writer - AMET", page_icon="🌍")
st.title("🌍 CV & LinkedIn Writer - AMET Standard with ATS Score")
st.caption("One tool for CV + LinkedIn Bio + Post - Adapts to Africa, KSA, UAE, Europe & US, Turkey")

# --- KEY ---
groq_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_key)

# --- MODE - THIS FIXES INTEGRITY ---
mode = st.radio("What do you want to create?", ["CV (AMET Standard)", "LinkedIn Profile (Headline + About)", "LinkedIn Post (Job Search)"], horizontal=True)

# --- ATS SCORER ---
def ats_score(job, cv):
    job_words = set(job.lower().split())
    cv_words = set(cv.lower().split())
    # Remove small words
    stop = {"and","the","for","with","a","an","in","to"}
    job_words = job_words - stop
    match = len(job_words & cv_words) / max(len(job_words),1) * 100
    # Format penalty if has photo words, tables etc
    return min(95, int(match * 0.8 + 20))  # +20 for clean format


# --- AMET SETTINGS (Only for CV mode) ---
if mode == "CV (AMET Standard)":
    st.divider()
    col_a, col_b = st.columns(2)
    with col_a:
        target = st.selectbox("Target Market", ["Nigeria / Kenya", "KSA / UAE / Egypt", "Turkey", "US / UK / Remote"])
    with col_b:
        include_photo = st.checkbox("Include Photo?", value=False, help="Common in KSA/UAE/TR. Optional in Nigeria. No for US/UK")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        nationality = st.text_input("Nationality", placeholder="Nigerian")
    with col2:
        dob = st.text_input("DOB", placeholder="Optional")
    with col3:
        marital = st.selectbox("Marital", ["", "Single", "Married"])
    
    visa = ""
    if "KSA" in target or "UAE" in target:
        visa = st.text_input("Visa Status", placeholder="Iqama transferable, etc")
    
    bilingual = st.checkbox("Generate Bilingual Version?")
    cv_length = st.selectbox("Length", ["Auto (Recommended)", "1 Page (US)", "2 Pages (AMET)"])
else:
    # LinkedIn defaults
    target = st.selectbox("Target Market for LinkedIn", ["Nigeria / Kenya", "KSA / UAE / Egypt", "Turkey", "US / UK / Remote"])
    include_photo = False
    nationality = dob = marital = visa = bilingual = ""
    cv_length = ""

# --- INPUTS ---
st.divider()
job_desc = st.text_area("Paste Job Description / Role you want", height=150, placeholder="e.g. Social Media Manager in Dubai...")
old_cv = st.text_area("Paste Old CV / Old LinkedIn About / Raw Info", height=150, placeholder="Paste everything you have...")

uploaded = st.file_uploader("Or upload PDF", type=["pdf"])
if uploaded:
    reader = PyPDF2.PdfReader(uploaded)
    old_cv = "".join([p.extract_text() for p in reader.pages])

# --- PROMPT BUILDER BASED ON MODE ---
if mode == "CV (AMET Standard)":
    if "US" in target:
        photo_rule = "NO PHOTO. No DOB, nationality, marital."
        length_rule = "1 page max."
        personal_rule = "Remove personal info."
    else:
        photo_rule = "Add [Professional Headshot 2x2 top right, not selfie]" if include_photo else "No photo placeholder"
        length_rule = "2 pages acceptable per AMET" if "2" in cv_length or "Auto" in cv_length else "1 page"
        personal_rule = f"Include only provided: Nationality:{nationality}, DOB:{dob}, Marital:{marital}, Visa:{visa}"

    system_prompt = f"""
    You are AMET CV expert. Target: {target}
    {photo_rule}. {length_rule}. {personal_rule}
    Rewrite CV for ATS for {target}. Format: Header, Summary, Experience with numbers, Education, Skills, Personal Info (if AMET). No tables. Then ATS Score Old vs New.
    """

elif mode == "LinkedIn Profile (Headline + About)":
    system_prompt = f"""
    You are LinkedIn expert for AMET markets.
    Target: {target}
    Rules for LinkedIn:
    - Headline: 220 chars max, keyword rich for {target} recruiters. Include | separator. Example: Social Media Manager | Content Strategy | UAE Market | Arabic & English
    - About: 1200-2000 chars, first person, story, not CV copy. No DOB, marital, photo mention. Photo is handled by LinkedIn profile itself.
    - For KSA/UAE: Mention Arabic/English bilingual, visa status if provided, open to relocation.
    - For Nigeria: Keep pidgin-free professional but warm.
    - For US/UK: No personal info.
    - Include: Call to action, 5 skills for LinkedIn Skills section.
    Old info: Use provided text.
    Job: {job_desc}
    """

else:  # LinkedIn Post
    system_prompt = f"""
    You are viral LinkedIn writer for {target}.
    Write 3 different posts for job search:
    1. Professional (for US/UK/UAE)
    2. Story-based (for Nigeria/Kenya - relatable)
    3. Bilingual hint (for KSA/Turkey if needed)
    Each post: Hook first line, 3-5 lines value, what you offer, CTA, 3-5 hashtags for {target}.
    No DOB/marital. Keep under 150 words each.
    """

# --- GENERATE ---
if st.button(f"✨ Generate {mode}", type="primary"):
    if not old_cv or not job_desc:
        st.error("Need Job Description + Your Info")
    else:
        with st.spinner(f"Generating {mode} for {target}..."):
            res = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"JOB: {job_desc}\nOLD: {old_cv}"}
                ],
                temperature=0.4
            )
            out = res.choices[0].message.content
            st.success("Done!")
            st.markdown(out)
            st.download_button("Download", out, file_name=f"{mode}_{target}.txt")

            old_score = ats_score(job_desc, old_cv)
            new_score = ats_score(job_desc, out)

            st.metric(
                label="ATS Score",
                value=f"{new_score}%",
                delta=f"{new_score - old_score}%"
            )
            st.metric(label="ATS Score", value=f"{old_score}% → {new_score}%")

            if mode == "CV (AMET Standard)" and bilingual:
                with st.spinner("Bilingual..."):
                    tr = client.chat.completions.create(
                        model="openai/gpt-oss-20b",
                        messages=[
                            {"role": "system", "content": "Translate CV to Arabic for KSA/UAE/Egypt, Turkish for Turkey. Keep format. Add note: Have native speaker review."},
                            {"role": "user", "content": out}
                        ]
                    )
                    st.markdown("---")
                    st.subheader("Bilingual Version")
                    st.markdown(tr.choices[0].message.content)

