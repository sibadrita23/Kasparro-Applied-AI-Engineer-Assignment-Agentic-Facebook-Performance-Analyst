import pandas as pd

class DataAgent:
    def load_and_summarize(self, path):
        df = pd.read_csv(path)
        stats = {
            "roas_mean": df["roas"].mean(),
            "ctr_mean": df["ctr"].mean(),
            "campaigns": df["campaign_name"].nunique(),
            "date_range": [df["date"].min(), df["date"].max()],
            "sample_creative_messages": df["creative_message"].unique()[:3].tolist()
        }
        return stats, df
