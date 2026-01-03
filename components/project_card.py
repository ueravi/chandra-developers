import streamlit as st
import os

def project_card(project):
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)

    # PROJECT IMAGE (CARD LEVEL)
    images = project.get("images", [])
    if images and os.path.exists(images[0]):
        st.image(images[0], use_container_width=True)
    else:
        st.markdown(
            "<div style='height:160px; background:#F4F4F4; "
            "border-radius:10px; margin-bottom:10px'></div>",
            unsafe_allow_html=True
        )

    st.markdown(
        f"<div class='project-title'>{project['name']}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='project-location'>📍 {project['location']}</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='project-status'>Status: {project['status']}</div>",
        unsafe_allow_html=True
    )

    st.write(project["overview"])

    if st.button("View Details", key=f"view_{project['id']}"):
        st.session_state.selected_project = project["id"]
        st.session_state.current_page = "Projects"
        st.rerun()   # 🔴 IMPORTANT (explained below)

    st.markdown("</div>", unsafe_allow_html=True)
