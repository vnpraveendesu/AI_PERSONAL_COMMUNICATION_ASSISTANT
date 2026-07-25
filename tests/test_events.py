from app.core.events import Event, EventBus, EventHandler, EventType


class DummyHandler(EventHandler):
    def __init__(self):
        self.event = None

    def handle(self, event):
        self.event = event


def test_event_publish():
    bus = EventBus()
    handler = DummyHandler()

    bus.subscribe(EventType.EMAIL_RECEIVED, handler)
    event = Event(name=EventType.EMAIL_RECEIVED, payload={"email_id": "123"})

    bus.publish(event)
    assert handler.event is not None
    assert handler.event.payload["email_id"] == "123"
