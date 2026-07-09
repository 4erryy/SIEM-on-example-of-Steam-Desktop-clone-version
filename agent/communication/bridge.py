import requests

class Bridge:

    def __init__(self):
        self.url = "http://127.0.0.1:8000/event"

    def send(self, payload):

        try:
            requests.post(self.url, json=payload, timeout=2)
        except:
            pass