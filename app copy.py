import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

# --- Page config ---
st.set_page_config(
    page_title="Md. Injamul Haque | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for black body background & white text ---
st.markdown(
    """
    <style>
    /* Main content background */
    [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }
    /* Ensure block containers inherit white text */
    .block-container, .main {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }
    /* Sidebar styling unchanged */
    [data-testid="stSidebar"] {
        background: #2c3e50;
        color: white;
    }
    /* Header fonts */
    h1, h2, h3 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Button hover */
    button:hover {
        background-color: #2980b9 !important;
        color: white !important;
    }
    /* Force all Markdown and header text white */
    h1, h2, h3, h4, h5, h6,
    .stMarkdown p, .stMarkdown li,
    .streamlit-expanderHeader,
    .streamlit-expanderContent p,
    .streamlit-expanderContent li {
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Helper to load Lottie animations ---
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return {}

lottie_wave = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_jtbfg2nb.json")
lottie_gear = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_q5pk6p1k.json")

# --- Sidebar navigation (icon menu) ---
with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=[
            "About", "Skills", "Experience", "Education", 
            "Projects", "Pubs", "Tools", "Awards", "Contact"
        ],
        icons=[
            "person", "tools", "briefcase", "book", 
            "project-diagram", "file-alt", "wrench", "award", "envelope"
        ],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#2c3e50"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"4px 0"},
            "nav-link-selected": {"background-color": "#1abc9c"},
        }
    )

# --- Header with animation ---
st.title("Md. Injamul Haque 🇧🇩")
st_lottie(lottie_wave, height=150, key="wave")
st.markdown(
    """
**Machine Learning Engineer & Python Expert**  
> Building AI‑driven web apps & solving real‑world problems with cutting‑edge tech.
"""
)

# --- Section renderers ---
def about():
    st.header("About Me")
    st_lottie(lottie_gear, height=200, key="gear")
    st.markdown(
        """
- 🔹 **Email:** injamulhaque9117@gmail.com  
- 🔹 **Phone:** +8801745-449117  
- 🔹 **GitHub:** [injamul3798](https://github.com/injamul3798)  
- 🔹 **LinkedIn:** [injamul-haque21](https://linkedin.com/in/injamul-haque21/)  

Experienced ML Engineer skilled in AI, computer vision, NLP, backend APIs, and scalable cloud deployments.
"""
    )

def skills():
    st.header("Skills")
    cols = st.columns(2)
    with cols[0]:
        st.subheader("Languages")
        st.write("C/C++ • Java • Python • JavaScript • SQL")
    with cols[1]:
        st.subheader("Tools & Frameworks")
        st.write("EC2 • Django • Flask • FastAPI • Streamlit • TensorFlow • PyTorch • LangChain • YOLOv8")

def experience():
    st.header("Experience")
    st.markdown(
        """
**Machine Learning Engineer @ DevTechGuru Ltd** *(Feb 2024 – Present)*  
- YOLOv8 plate detection (93% acc) + secure JWT APIs + React/Redux integration.  
- Avail Ortho: HDMI‑driven hip anatomy overlay for surgical assistance.

**ML Researcher @ Health Informatics Lab** *(Dec 2022 – Dec 2023)*  
- Q1 papers on medical imaging & AI diagnostics.  
- Models: YOLOv7/v8, LightGBM for vision & NLP.
"""
    )

def education():
    st.header("Education")
    st.markdown(
        """
**BSc in CSE**  
Daffodil International University (Mar 2020 – Jun 2024)  
**CGPA:** 3.74/4.00  
_Courses_: DS, Algo, DB, ML, Networks, OS, Image Processing
"""
    )

def projects():
    st.header("Projects")
    st.markdown(
        """
- **ThinkWithInjamul**: AI chatbot w/ LangChain & PDF loader (Streamlit, FAISS, HuggingFace).  
- **Parking Management**: YOLOv8 plate detection + POS reporting (Django, MySQL).  
- **Avail Ortho**: Real‑time hip anatomy tool w/ OpenCV HDMI feed.
"""
    )

def publications():
    st.header("Publications")
    st.markdown(
        """
- *Gallbladder Cancer Detection with GNNs* (Q1 Journal, Mar 2025)  
- *Hybrid BERT‑BiGRU for Transliteration* (ICCCNT 2024, Jun 2024)  
- *NewsNet: Bangla News Categorization* (ICCCNT 2024, Jun 2024)  
- *Impact of Lifestyle on Career* (LNNS, Dec 2023)
"""
    )

def tools_section():
    st.header("Tools & Repos")
    st.markdown(
        """
- **Tool Fusion**: AI/data pipeline. [GitHub]  
- **DSA Resource**: DS & Algo tutorials. [GitHub]  
- **ML Resource**: ML projects & notebooks. [GitHub]
"""
    )

def awards():
    st.header("Awards & Certificates")
    st.markdown(
        """
- ML Specialization (Coursera)  
- Software Eng. Cert (HackerRank)  
- Problem Solving Basic (HackerRank)  
- Intermediate ML & CV (Kaggle)  
- SQL for Data Science (Coursera)
"""
    )

def contact_form():
    st.header("Contact Me")
    with st.form("contact"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thanks for reaching out! I'll get back to you soon.")

# --- Page routing ---
if selected == "About":
    about()
elif selected == "Skills":
    skills()
elif selected == "Experience":
    experience()
elif selected == "Education":
    education()
elif selected == "Projects":
    projects()
elif selected == "Pubs":
    publications()
elif selected == "Tools":
    tools_section()
elif selected == "Awards":
    awards()
elif selected == "Contact":
    contact_form()
