from agent.analysis.anomaly import AnomalyDetector
from agent.analysis.risk_scorer import RiskScorer
from agent.rules.rule_engine import RuleEngine


class Engine:

    def __init__(self):

        self.anomaly = AnomalyDetector()
        self.rules = RuleEngine()
        self.scorer = RiskScorer()

    def process(self, event):

        anomaly = self.anomaly.check(event)
        rules = self.rules.check(event)

        risk = self.scorer.score(anomaly, rules)

        return {
            "event": event,
            "anomaly": anomaly,
            "rules": rules,
            "risk": risk
        }