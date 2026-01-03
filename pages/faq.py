import json
import streamlit as st

def render():
    st.markdown("<h1>FAQs</h1>", unsafe_allow_html=True)

    with open("data/faqs.json") as f:
        faqs = json.load(f)["faqs"]

    for faq in faqs:
        with st.expander("❓ " + faq["q"]):
            st.write(faq["a"])
