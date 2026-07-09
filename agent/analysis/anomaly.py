class AnomalyDetector:

    def check(self, event):

        text = str(event).lower()

        patterns = [
            "inject",
            "hack",
            "exploit",
            "fail",
            "error",
            "unauthorized"
        ]

        return any(p in text for p in patterns)