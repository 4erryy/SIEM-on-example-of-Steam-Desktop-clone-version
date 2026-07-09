import random

class SystemMonitor:

    def collect(self):

        pool = [
            {"type": "LOGIN", "message": "user login ok"},
            {"type": "LOGIN_FAIL", "message": "failed login attempt"},
            {"type": "PROCESS", "message": "unknown process started"},
            {"type": "SECURITY", "message": "inject attempt detected"}
        ]

        return [random.choice(pool)]