from app.core.container import container


def test_container():
    container.initialize()
    settings = container.get("settings")
    assert settings.app_name == "AI Personal Communication Assistant"
