from app.main import get_app_name


def test_get_app_name() -> None:
    assert get_app_name() == "AI Agent Sample"
