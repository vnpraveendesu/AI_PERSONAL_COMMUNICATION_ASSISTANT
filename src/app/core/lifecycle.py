from app.core.container import container
from app.core.logging import configure_logging


class ApplicationLifecycle:

    @staticmethod
    def startup():
        configure_logging()
        container.initialize()

        logger = container.get("logger")
        logger.info("Application started")

    @staticmethod
    def shutdown():
        logger = container.get("logger")
        logger.info("Application stopped")