import streamlit as st
from components.forms import landowner_form

def render():
    st.markdown("<h1>Joint Development</h1>", unsafe_allow_html=True)

    st.write(
        "Unlock the full potential of your land without selling it. "
        "We partner with landowners through transparent and flexible joint development models."
    )

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    
    st.subheader("Why Partner With Us")
    st.write("""
    - No upfront investment  
    - Complete legal & approval handling  
    - Transparent revenue sharing  
    - End-to-end execution  
    """)

    landowner_form()
