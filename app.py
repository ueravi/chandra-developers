import streamlit as st
from utils.css_loader import load_css
from components.navbar import render_navbar

# Pages
from pages import (
    home,
    about,
    joint_development,
    projects,
    project_detail,
    buy_site,
    why_choose_us,
    contact,
    testimonials,
    faq
)

# ---------------------------------
# SESSION STATE INITIALIZATION
# ---------------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

if "selected_project" not in st.session_state:
    st.session_state.selected_project = None


# ---------------------------------
# NAVBAR (USER INTENT FIRST)
# ---------------------------------
nav_page = render_navbar()

if nav_page != st.session_state.current_page:
    st.session_state.current_page = nav_page
    st.session_state.selected_project = None


# ---------------------------------
# PAGE TITLES (SEO)
# ---------------------------------
PAGE_TITLES = {
    "Home": "Chandra Developers | Joint Development & Residential Plots",
    "About Us": "About Chandra Developers | Trusted Joint Development Partner",
    "Joint Development": "Joint Development for Landowners | Chandra Developers",
    "Projects": "Residential Plot Projects | Chandra Developers",
    "Buy a Site": "Buy Residential Plots | Chandra Developers",
    "Why Choose Us": "Why Choose Chandra Developers",
    "Testimonials": "Client Testimonials | Chandra Developers",
    "FAQ": "FAQs | Chandra Developers",
    "Contact": "Contact Chandra Developers"
}


# ---------------------------------
# PAGE CONFIG (NOW CORRECT)
# ---------------------------------
st.set_page_config(
    page_title=PAGE_TITLES.get(
        st.session_state.current_page,
        "Chandra Developers"
    ),
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------------------------
# LOAD CSS
# ---------------------------------
load_css()


# ---------------------------------
# ROUTING
# ---------------------------------
page = st.session_state.current_page

if page == "Home":
    home.render()

elif page == "About Us":
    about.render()

elif page == "Joint Development":
    joint_development.render()

elif page == "Projects":
    if st.session_state.selected_project:
        project_detail.render()
    else:
        projects.render()

elif page == "Buy a Site":
    buy_site.render()

elif page == "Why Choose Us":
    why_choose_us.render()

elif page == "Testimonials":
    testimonials.render()

elif page == "FAQ":
    faq.render()

elif page == "Contact":
    contact.render()
