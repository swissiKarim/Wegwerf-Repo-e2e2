# Story-Entwurf (E2E2 Dienstpfad Lab)

**Titel:** Health-Endpoint bereitstellen

## Akzeptanzkriterien

1. **AC-1 (HTTP):** `GET /health` antwortet mit Status **200** und Body, der `ready` enthält.

2. **AC-2 (Qualität):** `ruff check .` und `pytest` laufen im Workspace ohne Fehler durch.

Hinweis: Der Verify-Dienst wird von der Plattform gestartet; AC-Texte nennen keine `ASB_`-Umgebungsvariablen.
