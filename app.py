import streamlit as st

# Set page configuration
st.set_page_config(page_title="AlzAI", layout="wide")

# Inject Custom CSS and JavaScript for Smooth Scrolling
st.markdown(
    """
    <style>
        /* Remove the top space */
        .block-container {
            padding-top: 0px !important;
            margin-top: -50px !important;
        }
        
        /* Navbar Styling */
        .nav-container {
            display: flex;
            justify-content: center;
            background-color: #ffffff;
            padding: 10px;
            border-bottom: 2px solid #ddd;
            margin-bottom: 10px;
        }
        .nav-item {
            color: black;
            text-decoration: none;
            font-size: 18px;
            font-weight: bold;
            margin: 0 15px;
            padding: 8px 12px;
            border-radius: 5px;
            cursor: pointer;
        }
        .nav-item:hover {
            background-color: #f0f0f0;
        }

        /* Smooth Scrolling Effect */
        html {
            scroll-behavior: smooth;
        }
    </style>

    <script>
        function smoothScroll(targetId) {
            document.getElementById(targetId).scrollIntoView({ behavior: 'smooth' });
        }
    </script>
    """,
    unsafe_allow_html=True
)

# Title and Subtitle
st.markdown(
    """
    <h1 style='text-align: center; margin-bottom: 5px;'>Alzheimer's Detection from MRI Scans</h1>
    <h3 style='text-align: center; margin-bottom: 5px;'>Upload MRI images and get predictions.</h3>
    """,
    unsafe_allow_html=True
)

# Navigation Bar with Smooth Scrolling
st.markdown(
    """
    <div class="nav-container">
        <a class="nav-item" onclick="smoothScroll('home')">Home</a>
        <a class="nav-item" onclick="smoothScroll('about')">About</a>
        <a class="nav-item" onclick="smoothScroll('contact')">Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# MRI Upload Section
st.markdown('<div id="home" class="card">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Upload MRI Scan</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])  # No label (removes space)
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded MRI Scan", use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Analysis Results Section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Analysis Results</h2>", unsafe_allow_html=True)
st.warning("Model is not yet integrated. Prediction results will appear here.")
st.markdown('</div>', unsafe_allow_html=True)

# Analyze Button
if st.button("Analyze MRI Scan"):
    st.info("Model integration pending. Results will be displayed here.")

# About Section with Smooth Scrolling
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.subheader("About Us")

st.markdown(
    """
    **At AlzAI,** we are dedicated to revolutionizing **Alzheimer’s detection** through cutting-edge **deep learning technology**.  
    Our project focuses on leveraging **Convolutional Neural Networks (CNNs)** to analyze **MRI scans**, enabling early and accurate diagnosis of Alzheimer’s disease.  

    ### Why It Matters?
    Alzheimer’s is a **progressive neurodegenerative disorder**, where **early detection** plays a vital role in slowing disease progression and improving patient care.  
    Traditional diagnostic methods are often **time-consuming and subjective**, leading to delays in intervention.  
    Our **AI-powered system** aims to assist medical professionals by providing a **faster, more reliable, and objective** way to classify brain conditions into different stages of Alzheimer’s.  

    ### Our Vision  
    We strive to bridge the gap between **technology and healthcare** by making **advanced Alzheimer’s detection** accessible, efficient, and accurate.  
    Through this project, we aim to support **early intervention strategies**, helping patients receive the right care at the right time.  

    ### How It Works?  
    Our model processes **MRI scan data**, extracting **patterns** that indicate the **presence and progression** of Alzheimer’s.  
    With the power of **deep learning**, we aim to enhance **medical diagnostics** and contribute to the fight against this challenging disease.  

    **Join us on our mission to make a difference in neurological healthcare with AI-driven innovation.**  
    """,
    unsafe_allow_html=True
)

# Contact Section with Smooth Scrolling
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.subheader("Contact Us")
st.write("For queries, email us at: example@email.com")
