import requests
from betterstack_api import create_incident, resolve_incident, is_incident_active

def check():
    page = requests.get("https://status.zoho.com/")
    if "All systems are operational" not in page.text:
        if not is_incident_active("zoho"):
            create_incident("zoho", "Zoho Mail Issues", "Zoho is reporting issues: https://status.zoho.com/")
    else:
        resolve_incident("zoho")
