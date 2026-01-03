import streamlit as st

def render():
    st.markdown("<h1>Why Choose Us</h1>", unsafe_allow_html=True)

    st.write(
        "We don’t just develop land — we build long-term relationships based on trust, "
        "transparency, and consistent delivery."
    )

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    st.subheader("Joint Development Expertise")
    st.write(
        "Deep understanding of joint development models ensuring fair outcomes for landowners."
    )

    st.subheader("Transparent Dealings")
    st.write(
        "Clear agreements, honest communication, and no hidden clauses."
    )

    st.subheader("Local Market Knowledge")
    st.write(
        "Strong understanding of local regulations, approvals, and market demand."
    )

    st.subheader("End-to-End Execution")
    st.write(
        "From land evaluation and approvals to development, marketing, and sales — we handle it all."
    )
