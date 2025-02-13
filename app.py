import streamlit as st

# Set page configuration
st.set_page_config(page_title="AlzAI", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Center-align text */
        .center-text {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Button styling */
        .stButton>button {
            width: 150px;
            height: 40px;
            font-size: 16px;
            border-radius: 8px;
            background-color: #3674B5;
            color: white;
            border: none;
            display: block;
            margin: 10px auto;  /* Center align buttons */
        }

        .stButton>button:hover {
            background-color: white;
            color: #3674B5;
            border: 2px solid #3674B5;
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Sidebar styling */
        .sidebar .sidebar-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        /* Header styling */
        h1 {
            color: #3674B5;
            text-align: center;
            margin-bottom: 1rem;
        }

        h3 {
            color: #3674B5;
            text-align: center;
            margin: 1.5rem 0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation - Centered Buttons
with st.sidebar:
    # Profile Icon and Name
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="100" style="border-radius: 50%;">
            <h3 style="color: #3674B5;">User Profile </h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Navigation Buttons
    if st.button("Home"):
        st.session_state["page"] = "home"
        st.rerun()
    if st.button("About"):
        st.session_state["page"] = "about"
        st.rerun()
    if st.button("Contact"):
        st.session_state["page"] = "contact"
        st.rerun()
 

# Page Routing Logic
if "page" not in st.session_state:
    st.session_state["page"] = "home"

if st.session_state["page"] == "home":
    # Home Page Content
    st.markdown("<h1>Alzheimer's Detection from MRI Scans</h1>", unsafe_allow_html=True)
    st.markdown("<p class='center-text'>Upload MRI images and get AI-driven predictions for early Alzheimer's detection.</p>", unsafe_allow_html=True)

    # File Upload Section
    st.markdown("<h3>Upload MRI Scan</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    # Image Preview
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded MRI Scan", use_column_width=True)

    # Analysis Section
    st.markdown("<h3>Analysis Result</h3>", unsafe_allow_html=True)

    # Analyze Button
    if st.button("Analyze MRI Scan"):
        st.info("Model integration pending. Results will be displayed here.")

elif st.session_state["page"] == "about":
    # About Page Content
    st.markdown("<h1>About Us</h1>", unsafe_allow_html=True)
    st.write("""
    At AlzAI, we are dedicated to revolutionizing Alzheimer’s detection through cutting-edge deep learning technology. Our project focuses on leveraging Convolutional Neural Networks (CNNs) to analyze MRI scans, enabling early and accurate diagnosis of Alzheimer’s disease.
Why It Matters?

Alzheimer’s is a progressive neurodegenerative disorder where early detection plays a vital role in slowing disease progression and improving patient care. Traditional diagnostic methods are often time-consuming and subjective, leading to delays in intervention. Our AI-powered system aims to assist medical professionals by providing a faster, more reliable, and objective way to classify brain conditions into different stages of Alzheimer’s.
Our Vision

We strive to bridge the gap between technology and healthcare by making advanced Alzheimer’s detection accessible, efficient, and accurate. Through this project, we aim to support early intervention strategies, helping patients receive the right care at the right time.
How It Works?

Our model processes MRI scan data, extracting patterns that indicate the presence and progression of Alzheimer’s. With the power of deep learning, we aim to enhance medical diagnostics and contribute to the fight against this challenging disease.

Join us on our mission to make a difference in neurological healthcare with AI-driven innovation.
    """)

elif st.session_state["page"] == "contact":
    st.markdown("<h1>Contact Us</h1>", unsafe_allow_html=True)

    st.write("For any queries, suggestions, or collaborations, feel free to reach out to us!")

    st.markdown("""
**Email:** alzai@gmail.com  
                
**Phone:** +91 1234567890
                
**Address:** Department of Artificial Intelligence and Data Science, VIIT, Pune, India  
                
**GitHub:** https://github.com/ManasBhise/BugSmashers 
""", unsafe_allow_html=True)


    # Contact Form
    st.markdown("### Send us a Message")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Submit"):
        if name and email and message:
            st.success("Thank you for reaching out! We will get back to you soon.")
        else:
            st.warning("Please fill all fields before submitting.")

# Footer
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            right: 0;
            width: calc(100% - 250px); /* Adjust width to exclude sidebar */
            background-color: #3674B5;
            color: white;
            text-align: center;
            padding: 12px 0;
            font-size: 14px;
            font-weight: bold;
            box-shadow: 0px -2px 5px rgba(0, 0, 0, 0.2);
        }

        /* Ensure footer does not overlap content */
        .main-content {
            padding-bottom: 60px;
            margin-left: 250px; /* Align main content */
        }
    </style>
    <div class="footer">
        © 2024 AlzAI | Developed by Team Bug Smashers
    </div>
    """,
    unsafe_allow_html=True
)

