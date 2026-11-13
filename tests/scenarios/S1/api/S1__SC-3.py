# scenario-id: S1/SC-3
"""POST /health wird nicht als Health-Endpoint akzeptiert (negative Variante)."""
import json
import os
import urllib.error
import urllib.request

base = os.environ.get("ASB_SVC_WEB_URL", os.environ.get("ASB_API_BASE", "http://127.0.0.1:8099"))
url = base.rstrip("/") + "/health"

req = urllib.request.Request(url, data=b"", method="POST")
try:
    with urllib.request.urlopen(req) as resp:
        status = resp.status
        body = resp.read().decode()
except urllib.error.HTTPError as e:
    status = e.code
    body = e.read().decode()

print(json.dumps({"status": status, "body": body}))
