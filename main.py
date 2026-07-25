from venv import logger
from app.core.logging import configure_logging
from app.core.logger_factory import get_logger
from app.core.lifecycle import ApplicationLifecycleManager


def main():
    lifecycle = ApplicationLifecycleManager()
    try:
        lifecycle.startup()
        print("AI Personal Communication Assistant running")
        configure_logging()
        applog = get_logger("application")
        applog.info("Application starting")

    except Exception as error:
        print(f"Application failed: {error}")

    finally:
        lifecycle.shutdown()


if __name__ == "__main__":
    main()
