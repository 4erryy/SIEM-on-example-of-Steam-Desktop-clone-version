class RuleEngine:
    def __init__(self):
        self.rules = []

    def add(self, rule):
        self.rules.append(rule)

    def run(self, event):
        return [r for r in self.rules if r(event)]