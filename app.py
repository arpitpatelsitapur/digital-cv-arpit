from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ----
currrent_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file=currrent_dir/"styles"/"main.css"
resume_file=currrent_dir/"assets"/"Resume Arpit Patel.pdf"
profile_pic=currrent_dir/"assets"/"profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Arpit Patel"
PAGE_ICON = ":wave:"
NAME = "Arpit Patel"
DESCRIPTION = """
Information Technology Student at SoS in E&T, Guru Ghasidas University, Bilaspur.
"""
EMAIL = "arpitaa9918@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/arpit-patel-b17416229/",
    "GitHub": "https://github.com/arpitpatelsitapur",
    "Leetcode": "https://leetcode.com/parpit/",
    "Twitter": "https://twitter.com/ArpitPa46091094",
}
PROJECTS = {
    "🏆 Laptop Price predictor ML app": "https://laptop-price-predictor-using-ml.streamlit.app/",
    "🏆 Multiple Disease Prediction ML App": "https://app-multiple-disease-prediction-ml-appcheck.streamlit.app/",
    "🏆 25+ Top ML projects": "https://github.com/arpitpatelsitapur/ML-projects",
    "🏆 Django CRUD project with Registration System": "https://github.com/arpitpatelsitapur/Django-CRUD-Project",
}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

st.title("Hello there!")



# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Created Dashboard and Report for University
- ✔️ Strong hands on experience and knowledge in Python and Machine Learning
- ✔️ Enrolled in the Salesforce `SFVIP-23` Program for a virtual internship, acquiring valuable insights into industry operations and augmenting my comprehension of professional workflows.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- 👩‍💻 Languages : `Python` , `C++`, `C`
- 📊 Data Visulization: `PowerBi`
- 🤖 Technologies : `Machine Learning` , `GitHub`
- 💻 Frameworks : `Django`
- 💾 Databases: `MySQL`
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Backend Devloper Intern | Presear Software Pvt Limited**")
st.write("06/2023 - Present")
st.write(
    """
- ► Interned as a proficient backend developer, specializing in Django.
- ► Acquired in-depth knowledge of databases and successfully applied them to project development
- ► Demonstrated expertise in utilizing Django and database skills for effective project execution
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

