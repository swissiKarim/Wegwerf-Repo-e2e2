from app import health_body, health_ok


def test_health_body():
    assert health_body() == "ready"


def test_health_ok():
    assert health_ok() is True
