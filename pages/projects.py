import streamlit as st
from services.project_service import load_projects
from components.project_card import project_card

def render():
    st.markdown("<h1>Projects</h1>", unsafe_allow_html=True)

    projects = load_projects()

    cols = st.columns(3)

    for idx, project in enumerate(projects):
        with cols[idx % 3]:
            project_card(project)
