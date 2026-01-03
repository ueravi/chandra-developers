import json
import streamlit as st

def render():
    st.markdown("<h1>Testimonials</h1>", unsafe_allow_html=True)

    with open("data/testimonials.json") as f:
        testimonials = json.load(f)["testimonials"]

    for t in testimonials:
        st.markdown(
            f"""
            <div class="project-card">
                <strong>{t['name']}</strong> <br/>
                <em>{t['type']}</em>
                <p style="margin-top:10px;">“{t['message']}”</p>
            </div>
            """,
            unsafe_allow_html=True
        )

