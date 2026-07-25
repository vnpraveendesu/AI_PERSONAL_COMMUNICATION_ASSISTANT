from app.config import settings


def test_configuration_loaded():
    assert settings.app_name == ("AI Personal Communication Assistant")
    assert settings.sync_interval_minutes > 0
