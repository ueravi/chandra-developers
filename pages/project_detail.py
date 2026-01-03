import streamlit as st
from services.project_service import get_project_by_id
from components.forms import buyer_form
import os

def render():

    if st.button("⬅ Back to Projects"):
        st.session_state.selected_project = None
        st.rerun()   # 🔴 THIS IS THE KEY FIX

    project_id = st.session_state.get("selected_project")

    if not project_id:
        st.warning("Please select a project to view details.")
        return

    project = get_project_by_id(project_id)

    st.markdown(f"<h1>{project['name']}</h1>", unsafe_allow_html=True)
    st.caption(project["location"])
    st.write(project["overview"])

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.subheader("Amenities")
    for a in project["amenities"]:
        st.write(f"- {a}")

    st.subheader("Approvals")
    st.write(", ".join(project["approvals"]))

    buyer_form(project["name"])

    if st.button("Book a Site Visit"):
        st.success("Our team will contact you shortly.")

    # PROJECT IMAGES
    images = project.get("images", [])

    if images:
        st.subheader("Project Images")

        cols = st.columns(3)
        for i, img_path in enumerate(images):
            if os.path.exists(img_path):
                with cols[i % 3]:
                    st.image(img_path, use_container_width=True)
    else:
        st.info("Project images will be updated soon.")
