import random

class InsightAgent:
    def generate(self, stats, df, max_retries=2):
        hypos = []
        mean_roas = stats.get("roas_mean", 0)
        hyp = {
            "reason": "ROAS below threshold",
            "confidence": 0.6,
            "evidence": f"Mean ROAS: {mean_roas:.2f}",
            "summary": "Potential creative or audience fatigue."
        }
        retries = 0
        while hyp["confidence"] < 0.7 and retries < max_retries:
            campaign_sample = random.choice(df["campaign_name"].unique())
            seg_roas = df[df["campaign_name"] == campaign_sample]["roas"].mean()
            hyp["evidence"] += f"; {campaign_sample} segment ROAS: {seg_roas:.2f}"
            if seg_roas < 2.0:
                hyp["confidence"] += 0.15
            retries += 1
        if hyp["confidence"] < 0.7:
            hyp["summary"] = "NEEDS_FURTHER_INVESTIGATION: " + hyp["summary"]
        hypos.append(hyp)
        return hypos
