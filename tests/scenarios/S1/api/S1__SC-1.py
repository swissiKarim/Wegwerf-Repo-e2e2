# scenario-id: S1/SC-1
"""GET /health liefert Status 200 mit Body 'ready'."""
import json
import os
import urllib.request

base = os.environ.get("ASB_SVC_WEB_URL", os.environ.get("ASB_API_BASE", "http://127.0.0.1:8099"))
url = base.rstrip("/") + "/health"

req = urllib.request.Request(url, method="GET")
with urllib.request.urlopen(req) as resp:
    status = resp.status
    body = resp.read().decode()

print(json.dumps({"status": status, "body": body}))
