import streamlit as st
from services.project_service import load_projects
from components.project_card import project_card

def render():
    st.markdown("<h1>Buy a Site</h1>", unsafe_allow_html=True)

    st.write(
        "Secure your future with legally approved, well-planned residential plots "
        "in prime locations."
    )

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.subheader("Why Buy From Us")
    st.write("""
    - Clear titles & statutory approvals  
    - Transparent pricing  
    - Prime locations with growth potential  
    - End-to-end support from booking to registration  
    """)

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.subheader("Available Projects")

    projects = load_projects()

    if not projects:
        st.info("Projects will be announced soon.")
        return

    cols = st.columns(3)
    for i, project in enumerate(projects):
        with cols[i % 3]:
            project_card(project)
