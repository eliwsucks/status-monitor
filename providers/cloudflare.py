import requests
from betterstack_api import create_incident, resolve_incident, is_incident_active

def check():
    status_url = "https://www.cloudflarestatus.com/api/v2/status.json"
    r = requests.get(status_url)
    indicator = r.json()['status']['indicator']

    if indicator != "none":
        if not is_incident_active("cloudflare"):
            create_incident("cloudflare", "Cloudflare Degradation", "Cloudflare is reporting issues.")
    else:
        resolve_incident("cloudflare")
