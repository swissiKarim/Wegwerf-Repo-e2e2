# scenario-id: S1/SC-2
"""GET /health antwortet auch bei wiederholten Anfragen korrekt (Stabilität)."""
import json
import os
import urllib.request

base = os.environ.get("ASB_SVC_WEB_URL", os.environ.get("ASB_API_BASE", "http://127.0.0.1:8099"))
url = base.rstrip("/") + "/health"

last_status = None
last_body = None
for _ in range(3):
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req) as resp:
        last_status = resp.status
        last_body = resp.read().decode()

print(json.dumps({"status": last_status, "body": last_body}))
