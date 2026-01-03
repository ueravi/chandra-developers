import datetime
from services.google_sheets_service import append_row
from services.notification_service import send_email


def save_lead(lead_type, data):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    if lead_type == "landowner":
        append_row("landowners", [
            timestamp,
            data.get("name"),
            data.get("phone"),
            data.get("email"),
            data.get("location"),
            data.get("land_size"),
            ""
        ])

    elif lead_type == "buyer":
        append_row("buyers", [
            timestamp,
            data.get("name"),
            data.get("phone"),
            data.get("email"),
            "",
            "",
            data.get("project")
        ])

    send_email(
        f"New {lead_type.capitalize()} Lead",
        str(data)
    )

    return True
