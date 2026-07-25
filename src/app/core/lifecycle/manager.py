from app.core.container import container
from app.core.logging import configure_logging
from app.core.logger_factory import get_logger


class ApplicationLifecycleManager:
    """
    Controls application startup and shutdown.
    """

    def __init__(self):
        self.logger = None

    def startup(self):
        # Step 1
        configure_logging()
        # Step 2
        container.initialize()
        # Step 3
        self.logger = get_logger("application")
        self.logger.info("Application startup completed")

    def shutdown(self):
        if self.logger:
            self.logger.info("Application shutdown initiated")
        self.cleanup()

    def cleanup(self):
        """
        Release application resources.
        """
        if self.logger:
            self.logger.info("Resources released")
