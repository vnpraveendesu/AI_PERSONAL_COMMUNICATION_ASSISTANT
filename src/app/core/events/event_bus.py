from collections import defaultdict
from venv import logger

from app.core.events.event import Event
from app.core.events.handlers import EventHandler
from app.core.logger_factory import get_logger


class EventBus:
    def __init__(self):
        self.handlers = defaultdict(list)
        self.logger = get_logger("event_bus")

    def subscribe(self, event_name, handler: EventHandler):
        self.handlers[event_name].append(handler)
        self.logger.info(f"Handler registered for {event_name}")

    def publish(self, event: Event):
        handlers = self.handlers.get(event.name, [])
        self.logger.info(f"Publishing event {event.name}")
        for handler in handlers:
            handler.handle(event)
