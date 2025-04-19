import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests
from streamlit_extras.switch_page_button import switch_page

# Page configuration
st.set_page_config(
    page_title="Md. Injamul Haque | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚀"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

:root {
    --primary: #6C63FF;
    --secondary: #4D44DB;
    --dark: #2F2E41;
    --light: #F8F9FA;
    --accent: #FF6584;
}

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background-color: var(--light);
    color: var(--dark);
}

[data-testid="stSidebar"] {
    background-color: var(--light) !important;
}

h1, h2, h3, h4, h5, h6 {
    color: var(--dark) !important;
}

p, li, span, div {
    color: var(--dark) !important;
}

.st-emotion-cache-1kyxreq {
    display: flex;
    justify-content: center;
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
    :root {
        --light: #0E1117;
        --dark: #F8F9FA;
    }
    
    .card {
        background-color: #1E1E1E !important;
    }
}

/* Navigation buttons */
.nav-btn {
    border: none;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white !important;
    padding: 12px 24px;
    border-radius: 30px;
    font-weight: 600;
    margin: 5px;
    width: 100%;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.nav-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    background: linear-gradient(135deg, var(--secondary), var(--primary));
}

/* Card styling */
.card {
    background: white;
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
    border: none;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 20px rgba(0,0,0,0.1);
}

/* Progress bars */
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--primary), var(--accent));
}

/* Contact form */
.contact-form {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.05);
}

/* Animation classes */
.fade-in {
    animation: fadeIn 1s ease-in;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.slide-in-left {
    animation: slideInLeft 1s ease-out;
}

@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-50px); }
    to { opacity: 1; transform: translateX(0); }
}

/* Social icons */
.social-icon {
    font-size: 24px;
    margin: 0 10px;
    color: var(--primary);
    transition: all 0.3s ease;
}

.social-icon:hover {
    color: var(--accent);
    transform: scale(1.2);
}

/* Sidebar styling */
[data-testid="stSidebar"] .nav-btn {
    margin-bottom: 10px;
}

[data-testid="stSidebar"] .social-icon {
    color: var(--primary) !important;
}
</style>
""", unsafe_allow_html=True)

# Load Lottie animations
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_contact = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_u25cckyh.json")

# Sidebar navigation with icons
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h2 style="color: #6C63FF;">Md. Injamul Haque</h2>
        <p style="color: #4D44DB;">Machine Learning Engineer</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🏠 About Me", key="about", type="primary", use_container_width=True):
        switch_page("About_Me")
    if st.button("💻 Skills", key="skills", type="primary", use_container_width=True):
        switch_page("Skills")
    if st.button("💼 Experience", key="experience", type="primary", use_container_width=True):
        switch_page("Experience")
    if st.button("🎓 Education", key="education", type="primary", use_container_width=True):
        switch_page("Education")
    if st.button("🚀 Projects", key="projects", type="primary", use_container_width=True):
        switch_page("Projects")
    if st.button("📚 Publications", key="publications", type="primary", use_container_width=True):
        switch_page("Publications")
    if st.button("🛠️ Tools", key="tools", type="primary", use_container_width=True):
        switch_page("Tools")
    if st.button("🏆 Awards", key="awards", type="primary", use_container_width=True):
        switch_page("Awards")
    if st.button("📩 Contact", key="contact", type="primary", use_container_width=True):
        switch_page("Contact")
    
    st.markdown("""
    <div style="margin-top: 50px; text-align: center;">
        <a href="https://github.com/injamul3798" target="_blank" class="social-icon">🔗</a>
        <a href="https://linkedin.com/in/injamul-haque21/" target="_blank" class="social-icon">💼</a>
        <a href="mailto:injamulhaque9117@gmail.com" class="social-icon">✉️</a>
    </div>
    """, unsafe_allow_html=True)

# Header section with animation
def header():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="fade-in">
            <h1 style="color: #6C63FF;">Md. Injamul Haque</h1>
            <h3 style="color: #4D44DB;">🇧🇩 Machine Learning Engineer & Python Expert</h3>
            <p style="font-size: 18px; color: var(--dark);">
                Passionate about building AI-driven web applications and solving real-world problems with cutting-edge technology.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if lottie_coding:
            st_lottie(lottie_coding, height=200, key="coding")

# Content sections with animations
def about_me():
    header()
    st.markdown("""
    <div class="fade-in">
        <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">About Me</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="card slide-in-left">
            <h4>👨‍💻 Professional Summary</h4>
            <p>Experienced ML Engineer with a strong background in AI, computer vision, NLP, and backend development. 
            Skilled in designing robust APIs, managing cloud infrastructure, and deploying scalable solutions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h4>📬 Contact Information</h4>
            <p>✉️ <strong>Email:</strong> injamulhaque9117@gmail.com</p>
            <p>📱 <strong>Phone:</strong> +8801745-449117</p>
            <p>🔗 <strong>GitHub:</strong> <a href="https://github.com/injamul3798" target="_blank">injamul3798</a></p>
            <p>💼 <strong>LinkedIn:</strong> <a href="https://linkedin.com/in/injamul-haque21/" target="_blank">injamul-haque21</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card slide-in-left">
            <h4>🌟 Core Competencies</h4>
            <ul>
                <li>Machine Learning & Deep Learning</li>
                <li>Computer Vision & NLP</li>
                <li>Backend Development</li>
                <li>Cloud Infrastructure</li>
                <li>API Design & Development</li>
                <li>Data Analysis & Visualization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h4>🌐 Languages</h4>
            <p>🇧🇩 Bengali (Native)</p>
            <p>🇬🇧 English (Fluent)</p>
        </div>
        """, unsafe_allow_html=True)

def skills():
    header()
    st.markdown("""
    <div class="fade-in">
        <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Skills</h2>
    </div>
    """, unsafe_allow_html=True)
    
    cols = st.columns(2)
    with cols[0]:
        st.markdown("""
        <div class="card slide-in-left">
            <h3>💻 Programming Languages</h3>
            <p>Python <span style="float: right;">90%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 90%;"></div>
                </div>
            </div>
            
            <p>JavaScript <span style="float: right;">75%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 75%;"></div>
                </div>
            </div>
            
            <p>Java <span style="float: right;">80%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 80%;"></div>
                </div>
            </div>
            
            <p>C/C++ <span style="float: right;">85%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 85%;"></div>
                </div>
            </div>
            
            <p>SQL <span style="float: right;">85%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 85%;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h3>🧠 Machine Learning</h3>
            <p>TensorFlow/PyTorch <span style="float: right;">90%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 90%;"></div>
                </div>
            </div>
            
            <p>Computer Vision <span style="float: right;">85%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 85%;"></div>
                </div>
            </div>
            
            <p>Natural Language Processing <span style="float: right;">80%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 80%;"></div>
                </div>
            </div>
            
            <p>Data Analysis <span style="float: right;">85%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 85%;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="card slide-in-left">
            <h3>🛠️ Tools & Frameworks</h3>
            <p>Django/Flask/FastAPI <span style="float: right;">90%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 90%;"></div>
                </div>
            </div>
            
            <p>AWS/GCP <span style="float: right;">75%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 75%;"></div>
                </div>
            </div>
            
            <p>Docker/Kubernetes <span style="float: right;">80%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 80%;"></div>
                </div>
            </div>
            
            <p>Git/CI-CD <span style="float: right;">85%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 85%;"></div>
                </div>
            </div>
            
            <p>MySQL/PostgreSQL <span style="float: right;">85%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 85%;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h3>🌐 Web Development</h3>
            <p>HTML/CSS <span style="float: right;">80%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 80%;"></div>
                </div>
            </div>
            
            <p>React/Redux <span style="float: right;">75%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 75%;"></div>
                </div>
            </div>
            
            <p>RESTful APIs <span style="float: right;">90%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 90%;"></div>
                </div>
            </div>
            
            <p>Streamlit/Dash <span style="float: right;">85%</span></p>
            <div class="stProgress">
                <div data-testid="stProgress" style="width: 100%;">
                    <div role="progressbar" style="width: 85%;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def experience():
    header()
    st.markdown("""
    <div class="fade-in">
        <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Work Experience</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card slide-in-left">
        <div style="display: flex; justify-content: space-between;">
            <h3>Machine Learning Engineer</h3>
            <span style="color: #6C63FF; font-weight: bold;">DevTechGuru Limited | Feb 2024 - Present</span>
        </div>
        <ul>
            <li>Developed backend & AI features for parking management: vehicle entry tracking, revenue & traffic reports.</li>
            <li>Implemented YOLOv8-based number plate detection (93% accuracy) for automated entry.</li>
            <li>Built secure JWT-auth APIs for user/session management & dynamic role control integrated with React & Redux.</li>
            <li>Created Avail Ortho: real-time hip anatomy evaluation tool with HDMI integration for surgical assistance.</li>
        </ul>
        <div style="margin-top: 10px;">
            <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Python</span>
            <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Django</span>
            <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">YOLOv8</span>
            <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">React</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card slide-in-left">
        <div style="display: flex; justify-content: space-between;">
            <h3>Machine Learning Researcher</h3>
            <span style="color: #6C63FF; font-weight: bold;">Health Informatics Research Lab | Dec 2022 - Dec 2023</span>
        </div>
        <ul>
            <li>Published Q1 journal papers on medical imaging & AI diagnostics.</li>
            <li>Applied YOLOv7/YOLOv8 and LightGBM for advanced research.</li>
            <li>Developed deep learning models for NLP & computer vision applications.</li>
        </ul>
        <div style="margin-top: 10px;">
            <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">PyTorch</span>
            <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">YOLOv7</span>
            <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">LightGBM</span>
            <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">NLP</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def education():
    header()
    st.markdown("""
    <div class="fade-in">
        <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Education</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card slide-in-left">
        <div style="display: flex; justify-content: space-between;">
            <h3>BSc in Computer Science & Engineering</h3>
            <span style="color: #6C63FF; font-weight: bold;">Mar 2020 - Jun 2024</span>
        </div>
        <p style="font-weight: bold; color: #4D44DB;">Daffodil International University</p>
        <p>CGPA: 3.74 / 4.00</p>
        <div style="margin-top: 15px;">
            <h4>Relevant Coursework:</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Data Structures</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Algorithms</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Databases</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Machine Learning</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Computer Networks</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Operating Systems</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Image Processing</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def projects():
    header()
    st.markdown("""
    <div class="fade-in">
        <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Highlighted Projects</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card slide-in-left">
            <h3>Real-Time AI Web App: ThinkWithInjamul</h3>
            <p>AI-powered chatbot using LangChain & HuggingFace embeddings for context-aware responses from PDF sources.</p>
            <h4>Key Features:</h4>
            <ul>
                <li>Real-time conversation</li>
                <li>Dynamic model switching via Groq API</li>
                <li>Prompt templating</li>
                <li>PDF document loader</li>
            </ul>
            <div style="margin-top: 10px;">
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Python</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Streamlit</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">LangChain</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">HuggingFace</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h3>Semi-Automated Parking Management System</h3>
            <p>AI-based vehicle number plate detection & POS integration for entry/exit reporting.</p>
            <h4>Key Features:</h4>
            <ul>
                <li>Number plate recognition</li>
                <li>Automated billing</li>
                <li>Real-time reporting</li>
                <li>User management</li>
            </ul>
            <div style="margin-top: 10px;">
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Python</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Django</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">YOLOv8</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">MySQL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card slide-in-left">
            <h3>Avail Ortho - Hip Overlay Project</h3>
            <p>Real-time hip anatomy evaluation tool for surgeons with HDMI & C-ARM integration.</p>
            <h4>Key Features:</h4>
            <ul>
                <li>Real-time anatomy evaluation</li>
                <li>HDMI integration</li>
                <li>Surgical assistance</li>
                <li>3D visualization</li>
            </ul>
            <div style="margin-top: 10px;">
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Python</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Django</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">OpenCV</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">MySQL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h3>Tool Fusion</h3>
            <p>Modular pipeline for integrating multiple AI and data-processing tools.</p>
            <h4>Key Features:</h4>
            <ul>
                <li>Modular design</li>
                <li>Multiple tool integration</li>
                <li>Data processing pipeline</li>
                <li>Customizable workflow</li>
            </ul>
            <div style="margin-top: 10px;">
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Python</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">FastAPI</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">Docker</span>
                <span class="chip" style="background: #E0E0FF; color: #4D44DB; padding: 5px 10px; border-radius: 20px; margin-right: 5px; display: inline-block;">CI/CD</span>
            </div>
            <div style="margin-top: 15px; text-align: center;">
                <a href="https://github.com/injamul3798/tool-fusion" target="_blank" style="background: #6C63FF; color: white; padding: 8px 15px; border-radius: 5px; text-decoration: none;">View on GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def publications():
    header()
    st.markdown("""
    <div class="fade-in">
        <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Research & Publications</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card slide-in-left">
        <h3>A Region-of-Interest Embedded Graph Neural Architecture for Gallbladder Cancer Detection</h3>
        <p><strong>Journal Article, Q1, Mar 2025</strong></p>
        <p>Full‑text: <a href="https://www.researchgate.net/publication/389864226_A_region-of-interest_embedded_graph_neural_architecture_for_gallbladder_cancer_detection" target="_blank">ResearchGate</a></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card slide-in-left">
        <h3>An Efficient Framework for Transliteration Sentence Identification of Low Resource Languages Using Hybrid BERT-BiGRU</h3>
        <p><strong>Conference Paper, ICCCNT 2024, Jun 2024</strong></p>
        <p>DOI: <a href="https://doi.org/10.1109/ICCCNT61001.2024.10725039" target="_blank">10.1109/ICCCNT61001.2024.10725039</a></p>
        <p><strong>Authors:</strong> Saiful Islam, Md Jabed Hosen, Fowzia Rahman Taznin, Shakil Rana, et al.</p>
        <p><strong>Lab:</strong> Md. Injamul Haque's Lab</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card slide-in-left">
        <h3>NewsNet: A Comprehensive Neural Network Hybrid Model for Efficient Bangla News Categorization</h3>
        <p><strong>Conference Paper, ICCCNT 2024, Jun 2024</strong></p>
        <p>DOI: <a href="https://doi.org/10.1109/ICCCNT61001.2024.10725173" target="_blank">10.1109/ICCCNT61001.2024.10725173</a></p>
        <p><strong>Authors:</strong> Shakil Rana, Md. Injamul Haque, Naznin Sultana, Saiful Islam, et al.</p>
        <p><strong>Lab:</strong> Md. Injamul Haque's Lab</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card slide-in-left">
        <h3>Impact of Lifestyle on Career: A Review</h3>
        <p><strong>Chapter in Lecture Notes in Networks and Systems (LNNS), Dec 2023</strong></p>
        <p>DOI: <a href="https://doi.org/10.1007/978-3-031-50158-6_38" target="_blank">10.1007/978-3-031-50158-6_38</a></p>
        <p><strong>Authors:</strong> Ahmed Wasif Reza, Md. Jabed Hosen, Md. Injamul Haque, Saiful Islam, et al.</p>
        <p><strong>Publisher:</strong> Springer Nature</p>
    </div>
    """, unsafe_allow_html=True)


def tools():
    header()
    st.markdown("""
    <div class="fade-in">
        <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Tools & Repositories</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card slide-in-left">
            <h3>Tool Fusion</h3>
            <p>Modular pipeline for integrating multiple AI and data-processing tools.</p>
            <div style="margin-top: 15px; text-align: center;">
                <a href="https://github.com/injamul3798/tool-fusion" target="_blank" style="background: #6C63FF; color: white; padding: 8px 15px; border-radius: 5px; text-decoration: none;">View on GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h3>DSA Resource</h3>
            <p>Curated collection of Data Structures & Algorithms tutorials and references.</p>
            <div style="margin-top: 15px; text-align: center;">
                <a href="https://github.com/injamul3798/dsa-resource" target="_blank" style="background: #6C63FF; color: white; padding: 8px 15px; border-radius: 5px; text-decoration: none;">View on GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card slide-in-left">
            <h3>ML Resource</h3>
            <p>Repository of machine learning projects, notebooks, and best practices.</p>
            <div style="margin-top: 15px; text-align: center;">
                <a href="https://github.com/injamul3798/ml-resource" target="_blank" style="background: #6C63FF; color: white; padding: 8px 15px; border-radius: 5px; text-decoration: none;">View on GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h3>AI Chatbot Template</h3>
            <p>Template for building AI-powered chatbots with Streamlit and LangChain.</p>
            <div style="margin-top: 15px; text-align: center;">
                <a href="https://github.com/injamul3798/ai-chatbot-template" target="_blank" style="background: #6C63FF; color: white; padding: 8px 15px; border-radius: 5px; text-decoration: none;">View on GitHub</a>
            </div>
        </div>
        """, unsafe_allow_html=True)

def awards():
    header()
    st.markdown("""
    <div class="fade-in">
        <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Awards & Certificates</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card slide-in-left">
            <h3>🎓 Certifications</h3>
            <ul>
                <li>Machine Learning Specialization (Coursera)</li>
                <li>Software Engineer Certificate (HackerRank)</li>
                <li>Problem Solving Basic (HackerRank)</li>
                <li>Intermediate ML & Computer Vision (Kaggle)</li>
                <li>SQL for Data Science (Coursera)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card slide-in-left">
            <h3>🏆 Awards</h3>
            <ul>
                <li>Dean's List Award for Academic Excellence (2022, 2023)</li>
                <li>Best Project Award - University Tech Fest 2023</li>
                <li>Hackathon Winner - DIU Code Warriors 2022</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def contact():
    header()
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="fade-in">
            <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Get In Touch</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card slide-in-left">
            <h3>📬 Contact Information</h3>
            <p>✉️ <strong>Email:</strong> injamulhaque9117@gmail.com</p>
            <p>📱 <strong>Phone:</strong> +8801745-449117</p>
            <p>📍 <strong>Location:</strong> Dhaka, Bangladesh</p>
            
            <div style="margin-top: 20px;">
                <h4>Connect with me:</h4>
                <a href="https://github.com/injamul3798" target="_blank" style="margin-right: 15px; font-size: 24px;">🔗 GitHub</a>
                <a href="https://linkedin.com/in/injamul-haque21/" target="_blank" style="margin-right: 15px; font-size: 24px;">💼 LinkedIn</a>
                <a href="mailto:injamulhaque9117@gmail.com" style="font-size: 24px;">✉️ Email</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if lottie_contact:
            st_lottie(lottie_contact, height=300, key="contact")
    
    with col2:
        st.markdown("""
        <div class="fade-in">
            <h2 style="border-bottom: 2px solid #6C63FF; padding-bottom: 10px;">Send Me a Message</h2>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your Name", placeholder="Enter your name")
            email = st.text_input("Your Email", placeholder="Enter your email")
            subject = st.text_input("Subject", placeholder="What's this about?")
            message = st.text_area("Message", placeholder="Your message here...", height=150)
            
            submitted = st.form_submit_button("Send Message", type="primary")
            if submitted:
                if name and email and message:
                    # In a real app, you would send this data to your email or database
                    st.success("Thank you for your message! I'll get back to you soon.")
                else:
                    st.warning("Please fill in all required fields.")

# Main app logic
query_params = st.query_params
page = query_params.get("page", ["about"])[0].lower()

if page == "about":
    about_me()
elif page == "skills":
    skills()
elif page == "experience":
    experience()
elif page == "education":
    education()
elif page == "projects":
    projects()
elif page == "publications":
    publications()
elif page == "tools":
    tools()
elif page == "awards":
    awards()
elif page == "contact":
    contact()
else:
    about_me()