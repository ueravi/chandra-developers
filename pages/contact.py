import streamlit as st
from components.forms import landowner_form, buyer_form

def render():
    st.markdown("<h1>Contact Us</h1>", unsafe_allow_html=True)

    st.write("Let’s discuss how we can work together.")

    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Reach Us")
        st.write("""
        📍 **Office Address**  
        Ballari, Karnataka  

        📞 **Phone / WhatsApp**  
        +91-XXXXXXXXXX  

        ✉ **Email**  
        info@chandradevelopers.com  
        """)

    with col2:
        st.subheader("Send an Enquiry")
        landowner_form()
