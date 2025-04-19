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

# --- Custom CSS ---
st.markdown("""
<style>
/* Background & Text Styling */
[data-testid="stAppViewContainer"], .block-container, .main {
    background-color: #0d1117 !important;  /* Dark gray */
    color: #e6edf3 !important;
}
[data-testid="stSidebar"] {
    background-color: #161b22;
    color: white;
}
h1, h2, h3, h4, h5, h6, .stMarkdown p, .stMarkdown li {
    color: #f0f6fc !important;
}

/* Header Fonts and General Styles */
h1, h2, h3 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
a {
    color: #58a6ff;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

/* Animations */
@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(10px); }
    100% { opacity: 1; transform: translateY(0); }
}
.fade-in {
    animation: fadeIn 1s ease-in;
}
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.03); }
}
.pulse {
    animation: pulse 2s infinite;
}

/* Button hover */
button:hover {
    background-color: #238636 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# --- Lottie Loader ---
def load_lottie_url(url: str):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else {}

# Load Animations
lottie_wave = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_jtbfg2nb.json")
lottie_gear = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_q5pk6p1k.json")

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=["About", "Skills", "Experience", "Education", "Projects", "Pubs", "Tools", "Awards", "Contact"],
        icons=["person", "tools", "briefcase", "book", "project-diagram", "file-alt", "wrench", "award", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#161b22"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"4px 0"},
            "nav-link-selected": {"background-color": "#1f6feb"},
        }
    )

# --- Header ---
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.title("Md. Injamul Haque 🇧🇩")
st_lottie(lottie_wave, height=150, key="wave")
st.markdown("""
**🚀 Machine Learning Engineer & Python Expert**  
> Passionate about **AI‑driven systems**, building **real-time solutions**, and automating workflows that **save time** and **improve accuracy**.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- Sections ---
def about():
    st.header("🔍 About Me")
    st_lottie(lottie_gear, height=200, key="gear")
    st.markdown("""
**Hi, I’m Injamul!** A tech enthusiast specializing in **Computer Vision**, **ML system design**, and **AI automation**.

- 📧 **Email:** injamulhaque9117@gmail.com  
- 📱 **Phone:** +8801745-449117  
- 🧑‍💻 **GitHub:** [injamul3798](https://github.com/injamul3798)  
- 💼 **LinkedIn:** [injamul-haque21](https://linkedin.com/in/injamul-haque21/)  

> 🧠 I focus on **practical ML applications**, especially in **healthcare**, **parking systems**, and **automated workflows**.
""")

def skills():
    st.header("🛠️ Skills")
    st.subheader("💡 Languages")
    st.write("Python • JavaScript • SQL • Java • C/C++")

    st.subheader("🧰 Frameworks & Tools")
    st.write("Streamlit • Django • Flask • FastAPI • TensorFlow • PyTorch • LangChain • YOLOv8")

    st.subheader("☁️ Cloud & DevOps")
    st.write("EC2 • Docker • Git • GitHub Actions")

def experience():
    st.header("💼 Experience")
    st.markdown("""
### 🔧 **Machine Learning Engineer @ DevTechGuru Ltd** *(Feb 2024 – Present)*  
**Key Contributions:**
- ✅ Designed and deployed **YOLOv8-based license plate recognition system** achieving **93% accuracy**.
- ✅ Developed **secure backend APIs** using FastAPI & JWT auth.
- ✅ Built real-time **React/Redux dashboards** integrated with Python microservices.
- ✅ Built **HIP surgery assistance tool** using **HDMI input** + **OpenCV overlays**.

---

### 🧪 **ML Researcher @ Health Informatics Lab** *(Dec 2022 – Dec 2023)*  
**Highlights:**
- 📈 Published multiple **Q1-ranked papers** on medical AI.
- 💡 Developed hybrid **YOLO + BiGRU + Attention models** for diagnostics.
- 🧬 Used **LightGBM, YOLOv7/v8** for structured + imaging data fusion.
""")

def education():
    st.header("🎓 Education")
    st.markdown("""
**BSc in Computer Science & Engineering**  
**Daffodil International University** *(Mar 2020 – Jun 2024)*  
📘 **CGPA:** 3.74 / 4.00  
**Key Courses:** DS, Algo, ML, CV, Networks, OS, DBMS  
""")

def projects():
    st.header("🚧 Projects")
    st.markdown("""
- **🧠 ThinkWithInjamul:** AI chatbot using **LangChain + FAISS**, supports **multi-PDF queries** via HuggingFace embeddings.
- **🚗 Parking Management System:** Built end-to-end solution with **YOLOv8 plate detection**, **barrier control logic**, **MySQL + Django backend**, and **PDF reports**.
- **🏥 Avail Ortho (Live Surgery Assist):** Developed **OpenCV HDMI pipeline** to project hip implant overlays on real-time surgical footage.
""")

def publications():
    st.header("📚 Publications")
    st.markdown("""
- 🧬 *Precision in Gallbladder Cancer Detection Using GNNs* — Q1 Journal (Mar 2025)  
- 🔡 *Hybrid BERT-BiGRU for Bangla Transliteration* — ICCCNT 2024  
- 📰 *NewsNet: Bangla News Categorization with Deep NLP* — ICCCNT 2024  
- 🧠 *Impact of Lifestyle on Career* — LNNS, Springer (Dec 2023)
""")

def tools_section():
    st.header("🧰 Tools & Resources")
    st.markdown("""
- **Tool Fusion:** Modular data & model pipelines. [GitHub]  
- **DSA Resource:** Coding + Algorithm tutorials. [GitHub]  
- **ML Resource:** Research notebooks, pretrained models. [GitHub]
""")

def awards():
    st.header("🏅 Awards & Certifications")
    st.markdown("""
- ✅ Machine Learning Specialization – *Coursera*  
- ✅ Software Engineering Certificate – *HackerRank*  
- ✅ Intermediate ML & CV – *Kaggle*  
- ✅ SQL for Data Science – *Coursera*  
- ✅ Problem Solving (Basic) – *HackerRank*
""")

def contact_form():
    st.header("📬 Contact Me")
    with st.form("contact"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("✅ Thanks for reaching out! I’ll get back to you soon.")

# --- Routing ---
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
