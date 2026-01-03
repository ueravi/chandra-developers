import json
import streamlit as st

PROJECT_FILE = "data/projects.json"

@st.cache_data
def load_projects():
    with open(PROJECT_FILE, "r") as f:
        return json.load(f)["projects"]

def get_project_by_id(project_id):
    projects = load_projects()
    for p in projects:
        if p["id"] == project_id:
            return p
    return None
