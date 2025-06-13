# 🔍 BetterStack Status Monitor

This is a modular Python-based status monitor that tracks the public status of third-party services (e.g., Cloudflare, Zoho Mail) and automatically creates or resolves incidents on your BetterStack status page.

## 📦 Features

- Checks public status APIs or pages
- Creates incidents via BetterStack API if a provider has an issue
- Resolves them automatically when the provider recovers
- Easy to add new providers

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/youruser/status-monitor.git
cd status-monitor
````

### 2. Install Requirements

```bash
pip install requests
```

### 3. Set Your BetterStack API Key

Edit `config.py`:

```python
BETTERSTACK_API_KEY = "your_betterstack_api_key_here"
```

### 4. Run the Monitor

```bash
python3 main.py
```

You’ll see output showing which services were checked and whether incidents were triggered or resolved.

---

## ➕ Adding More Providers

### Step-by-step:

1. Create a new file in `providers/`, e.g. `myprovider.py`
2. Define a `check()` function that:

   * Fetches and evaluates the status
   * Calls `create_incident()` or `resolve_incident()` from `betterstack_api.py`
3. Import and run the checker in `main.py`

### Example:

```python
# providers/github.py
import requests
from betterstack_api import create_incident, resolve_incident, is_incident_active

def check():
    r = requests.get("https://www.githubstatus.com/api/v2/status.json")
    if r.json()['status']['indicator'] != "none":
        if not is_incident_active("github"):
            create_incident("github", "GitHub Issue", "GitHub is reporting problems.")
    else:
        resolve_incident("github")
```

Then update `main.py`:

```python
from providers import cloudflare, zoho, github

def run_all():
    cloudflare.check()
    zoho.check()
    github.check()
```

---

## 🔁 Automating It

### Linux

Edit crontab:

```bash
crontab -e
```

Add:

```cron
*/5 * * * * /usr/bin/python3 /path/to/main.py
```

### Windows

Use Task Scheduler to run `python main.py` every 5 minutes.

---

## 📂 File Structure

```
status_monitor/
├── main.py
├── config.py
├── betterstack_api.py
├── providers/
│   ├── cloudflare.py
│   ├── zoho.py
│   └── ... other providers
├── incident_*.txt  # Temp incident tracking files
```

---

## 🧠 Notes

* Incident files are used to track what’s already been reported so it doesn't duplicate.
* You can improve this with a database or memory cache if running long-term.

---

## 🛠 Future Ideas

* Telegram/Slack webhook integration
* Email alerts
* Dashboard view

```

---

