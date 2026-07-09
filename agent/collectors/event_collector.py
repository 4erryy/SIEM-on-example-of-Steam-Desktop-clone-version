import time

class EventCollector:

    def enrich(self, events):

        result = []

        for e in events:
            e["timestamp"] = time.time()
            e["source"] = "agent"
            result.append(e)

        return result