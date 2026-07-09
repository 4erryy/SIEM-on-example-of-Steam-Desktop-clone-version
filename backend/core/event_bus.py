class EventBus:
    def __init__(self):
        self.handlers = {}

    def on(self, event, fn):
        self.handlers.setdefault(event, []).append(fn)

    def emit(self, event, data):
        for fn in self.handlers.get(event, []):
            fn(data)