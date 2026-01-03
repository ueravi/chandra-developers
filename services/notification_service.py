import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

def send_email(subject, body):
    if not all([SENDER_EMAIL, SENDER_PASSWORD, ADMIN_EMAIL]):
        return

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = ADMIN_EMAIL
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
