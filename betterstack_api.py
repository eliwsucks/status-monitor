import requests
import os
from config import BETTERSTACK_API_KEY

def get_incident_file(provider_name):
    return f"incident_{provider_name}.txt"

def create_incident(provider_name, title, description):
    url = "https://uptime.betterstack.com/api/v1/incidents"
    headers = {
        "Authorization": f"Bearer {BETTERSTACK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "title": title,
        "description": description,
        "status": "investigating"
        # Add other fields here if needed, check API docs
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        incident_id = response.json().get('id')
        with open(get_incident_file(provider_name), 'w') as f:
            f.write(incident_id)
        print(f"[{provider_name}] Incident created: {incident_id}")
    else:
        print(f"[{provider_name}] Failed to create incident:", response.text)

def resolve_incident(provider_name):
    incident_file = get_incident_file(provider_name)
    if not os.path.exists(incident_file):
        return
    with open(incident_file, 'r') as f:
        incident_id = f.read().strip()

    url = f"https://uptime.betterstack.com/api/v1/incidents/{incident_id}/resolve"
    headers = {
        "Authorization": f"Bearer {BETTERSTACK_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.patch(url, headers=headers)
    if response.status_code == 200:
        os.remove(incident_file)
        print(f"[{provider_name}] Incident {incident_id} resolved.")
    else:
        print(f"[{provider_name}] Failed to resolve incident:", response.text)

def is_incident_active(provider_name):
    return os.path.exists(get_incident_file(provider_name))
