# scenario-id: S1/SC-4
"""ruff check läuft ohne Fehler durch."""
import json
import subprocess

result = subprocess.run(
    ["ruff", "check", "."],
    capture_output=True,
    text=True,
)

print(json.dumps({
    "exit_code": result.returncode,
    "output": result.stdout + result.stderr,
}))
