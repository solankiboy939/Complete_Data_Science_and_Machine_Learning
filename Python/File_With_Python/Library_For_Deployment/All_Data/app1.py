import streamlit as st

# Define the CSS styles for the background image and navigation bar
st.markdown("""
    <style>
    .main {
        background-image: url("./gfg_internship/images/banner.png");
        background-size: cover;
        background-position: center;
        color: #fff;
    }
    .nav-bar {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .nav-bar a {
        color: #fff;
        font-size: 18px;
        margin: 0 15px;
        text-decoration: none;
        padding: 10px;
    }
    .nav-bar a:hover {
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 5px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }
    .button-container button {
        font-size: 20px;
        padding: 15px 30px;
        margin: 0 10px;
        border-radius: 5px;
        border: none;
        color: #fff;
        cursor: pointer;
    }
    .button-container button.school {
        background-color: #007bff;
    }
    .button-container button.college {
        background-color: #28a745;
    }
    .search-bar {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    .search-bar input {
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    .search-bar button {
        font-size: 18px;
        padding: 10px 15px;
        margin-left: 10px;
        border-radius: 5px;
        border: none;
        background-color: #007bff;
        color: #fff;
        cursor: pointer;
    }
    .search-bar button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="main">', unsafe_allow_html=True)

# Navigation Bar
st.markdown("""
    <div class="nav-bar">
        <a href="#home">Home</a>
        <a href="#about">About Us</a>
        <a href="#contact">Contact Us</a>
    </div>
""", unsafe_allow_html=True)

# Page Title
st.title("📚 Welcome to Edudrag")

# Brief Introduction
st.write("""
    Welcome to the Interactive Library! We offer a range of educational resources for both school and college students. 
    Explore our content and find the resources you need for your studies.
""")

# Search Bar
st.markdown("""
    <div class="search-bar">
        <input type="text" placeholder="Search for subjects..."/>
        <button>Search</button>
    </div>
""", unsafe_allow_html=True)

# Button Container
import streamlit as st

import streamlit as st

import streamlit as st

def authenticate():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if not st.session_state.authenticated:
        if st.button("Authenticate"):
            st.session_state.authenticated = True

# Display authentication button if not authenticated
authenticate()

# Only show the navigation buttons if authenticated
if st.session_state.authenticated:
    if st.button("School"):
        st.experimental_rerun('/school')
    if st.button("College"):
        st.experimental_rerun('/college')
    if st.button("GeeksforGeeks"):
        st.write("Redirecting to GeeksforGeeks...")
        js_code = """
        <script>
        window.open('https://www.geeksforgeeks.org', '_blank');
        </script>
        """
        st.markdown(js_code, unsafe_allow_html=True)




# About Us Section
st.markdown('<div id="about">', unsafe_allow_html=True)
st.subheader("About Us")
st.write("""
    Our library provides educational resources across various subjects for school and college students. 
    We aim to support your learning journey with high-quality materials and resources.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Contact Us Section
st.markdown('<div id="contact">', unsafe_allow_html=True)
st.subheader("Contact Us")
st.write("""
    Feel free to reach out to us for any queries or feedback. We are here to help you!
    - **Email:** support@example.com
    - **Phone:** +1-234-567-890
""")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
