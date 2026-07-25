from app.core.events import Event, EventBus, EventHandler


class TestHandler(EventHandler):
    def __init__(self):
        self.received = False

    def handle(self, event):
        self.received = True


def test_event_bus():
    bus = EventBus()
    handler = TestHandler()
    bus.subscribe("test.event", handler)
    event = Event(name="test.event")
    bus.publish(event)
    assert handler.received
