class EvaluatorAgent:
    def evaluate(self, hypos, stats, df):
        for h in hypos:
            if h["confidence"] < 0.7:
                recent_data = df[df["date"] >= df["date"].max()[:7]]
                recent_roas = recent_data["roas"].mean()
                if recent_roas < 2.0:
                    h["confidence"] += 0.1
                    h["evidence"] += f"; Recent ROAS: {recent_roas:.2f}"
            if h["confidence"] < 0.7:
                h["summary"] = "NEEDS_FURTHER_INVESTIGATION: " + h["summary"]
        return hypos
