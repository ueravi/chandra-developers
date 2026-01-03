import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

CREDS_FILE = "gcp_credentials.json"
SHEET_NAME = "CD_Leads"

def get_sheet(sheet_name):
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).worksheet(sheet_name)
    return sheet

def append_row(sheet_name, row):
    sheet = get_sheet(sheet_name)
    sheet.append_row(row)
