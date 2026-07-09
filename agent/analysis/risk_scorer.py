class RiskScorer:

    def score(self, anomaly, rules):

        score = 0

        if anomaly:
            score += 70

        score += len(rules) * 15

        return min(score, 100)