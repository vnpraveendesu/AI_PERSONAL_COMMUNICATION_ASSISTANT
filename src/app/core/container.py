from app.config import settings
from app.core.logger_factory import get_logger
from app.core.service_registry import ServiceRegistry
from app.core.events import EventBus

class ApplicationContainer:
    """Application-wide dependency container."""

    def __init__(self):
        self.registry = ServiceRegistry()

    def initialize(self):
        self.registry.register("settings", settings)
        self.registry.register("logger", get_logger("application"))
        self.registry.register("event_bus", EventBus())

    def get(self, service_name: str):
        return self.registry.get(service_name)


container = ApplicationContainer()