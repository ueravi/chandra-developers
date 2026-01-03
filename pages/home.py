import streamlit as st
import os
from services.project_service import load_projects
from components.project_card import project_card

def render():
    # ===============================
    # HERO SECTION
    # ===============================
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            "<div class='hero-text'>"
            "<h1>Transforming Land into Valuable Communities</h1>"
            "<p>We specialize in joint development with landowners and deliver legally clear, "
            "well-planned residential sites for buyers.</p>"
            "</div>",
            unsafe_allow_html=True
        )


    with col2:
        image_path = "assets/images/hero/hero.jpg"
        if os.path.exists(image_path):
            st.image(image_path, use_container_width=True)
        else:
            st.info("Hero image coming soon")

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    # ===============================
    # FEATURED PROJECTS
    # ===============================
    st.markdown("<h2>Featured Developments</h2>", unsafe_allow_html=True)

    projects = [p for p in load_projects() if p.get("featured")]

    if not projects:
        st.info("Projects will be announced soon.")
        return

    cols = st.columns(3)
    for i, project in enumerate(projects):
        with cols[i % 3]:
            project_card(project)
