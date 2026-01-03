import streamlit as st
from services.lead_service import save_lead

def landowner_form():
    with st.form("landowner_form"):
        st.subheader("Start Joint Development Discussion")

        name = st.text_input("Name")
        location = st.text_input("Land Location")
        land_size = st.text_input("Land Size (Acres / Sq.ft)")
        phone = st.text_input("Phone Number")
        email = st.text_input("Email")

        submitted = st.form_submit_button("Request a Call Back", use_container_width=True)

        if submitted:
            if not name or not phone:
                st.error("Name and Phone are mandatory")
                return

            save_lead("landowner", {
                "name": name,
                "location": location,
                "land_size": land_size,
                "phone": phone,
                "email": email
            })

            st.success("Thank you! Our team will contact you shortly.")


def buyer_form(project_name=None):
    with st.form("buyer_form"):
        st.subheader("Book a Site Visit")

        name = st.text_input("Name")
        phone = st.text_input("Phone Number")
        email = st.text_input("Email")
        project = project_name or st.text_input("Project Interested In")

        submitted = st.form_submit_button("RBook Site Visit", use_container_width=True)

        if submitted:
            if not name or not phone:
                st.error("Name and Phone are mandatory")
                return

            save_lead("buyer", {
                "name": name,
                "phone": phone,
                "email": email,
                "project": project
            })

            st.success("Site visit request submitted successfully.")
