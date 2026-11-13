# scenario-id: S1/SC-5
"""pytest läuft ohne Fehler durch."""
import json
import subprocess

result = subprocess.run(
    ["pytest", "--tb=short", "-v"],
    capture_output=True,
    text=True,
)

print(json.dumps({
    "exit_code": result.returncode,
    "output": result.stdout + result.stderr,
}))
