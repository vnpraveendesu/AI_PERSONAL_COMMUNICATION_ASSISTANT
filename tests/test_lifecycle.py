from app.core.lifecycle import ApplicationLifecycleManager


def test_application_startup():
    lifecycle = ApplicationLifecycleManager()
    lifecycle.startup()
    assert lifecycle.logger is not None
    lifecycle.shutdown()
