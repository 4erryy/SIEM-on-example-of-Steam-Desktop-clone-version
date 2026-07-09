from backend.core.event_bus import EventBus

bus = EventBus()

class EventCenter:
    def emit(self, event, data):
        bus.emit(event, data)

    def on(self, event, fn):
        bus.on(event, fn)