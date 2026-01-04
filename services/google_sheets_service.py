import os
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

SHEET_NAME = "CD_Leads"


def get_credentials():
    """
    Priority:
    1. Streamlit Cloud secrets (st.secrets["gcp"])
    2. Local file (gcp_credentials.json)
    """

    # ---- STREAMLIT CLOUD ----
    try:
        if hasattr(st, "secrets") and "gcp" in st.secrets:
            return ServiceAccountCredentials.from_json_keyfile_dict(
                st.secrets["gcp"], SCOPE
            )
    except Exception:
        pass  # secrets not available locally

    # ---- LOCAL DEVELOPMENT ----
    if os.path.exists("gcp_credentials.json"):
        return ServiceAccountCredentials.from_json_keyfile_name(
            "gcp_credentials.json", SCOPE
        )

    # ---- FAIL SAFE ----
    raise FileNotFoundError(
        "Google credentials not found. "
        "Add gcp_credentials.json locally or configure Streamlit secrets."
    )


def get_sheet(sheet_name):
    creds = get_credentials()
    client = gspread.authorize(creds)
    return client.open(SHEET_NAME).worksheet(sheet_name)


def append_row(sheet_name, row):
    sheet = get_sheet(sheet_name)
    sheet.append_row(row)
