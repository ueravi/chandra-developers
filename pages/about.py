import streamlit as st

def render():
    st.markdown("<h1>About Us</h1>", unsafe_allow_html=True)

    st.write(
        "We are a real estate development firm focused on creating win-win partnerships "
        "with landowners and delivering reliable investment opportunities to buyers."
    )

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.subheader("Our Vision")
    st.write(
        "To transform land into sustainable, value-driven communities that benefit "
        "landowners, buyers, and future generations."
    )

    st.subheader("Our Mission")
    st.write(
        "To develop land responsibly, transparently, and profitably through joint development, "
        "professional planning, and ethical execution."
    )

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.subheader("Our Core Values")
    st.write("""
    - Transparency in every transaction  
    - Trust-based long-term relationships  
    - Ethical development practices  
    - Local market expertise  
    """)
