from backend.core.event_center import EventCenter
from backend.security.security_processor import SecurityProcessor

class Orchestrator:

    def __init__(self):
        self.center = EventCenter()
        self.security = SecurityProcessor()

        self.center.on("event", self.handle)

    def handle(self, event):

        result = self.security.process(event)

        return {
            "event": event,
            "security": result
        }

    def emit(self, event):
        self.center.emit("event", event)