"""Minimal health helper used by unit tests (no HTTP server)."""


def health_body() -> str:
    return "ready"


def health_ok() -> bool:
    return health_body() == "ready"
