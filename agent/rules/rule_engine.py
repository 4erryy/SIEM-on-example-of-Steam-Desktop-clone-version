class RuleEngine:

    def __init__(self):

        self.rules = [
            self.rule_login_fail,
            self.rule_process,
            self.rule_admin
        ]

    def check(self, event):

        return [r.__name__ for r in self.rules if r(event)]

    def rule_login_fail(self, event):
        return event.get("type") == "LOGIN_FAIL"

    def rule_process(self, event):
        return event.get("type") == "PROCESS"

    def rule_admin(self, event):
        return "admin" in str(event).lower()