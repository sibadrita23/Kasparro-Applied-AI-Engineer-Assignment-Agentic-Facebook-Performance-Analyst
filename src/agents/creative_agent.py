import random

class CreativeAgent:
    def recommend(self, df, ctr_threshold=0.012):
        low_ctr_df = df[df["ctr"] < ctr_threshold]
        headlines = ["Unlock Savings!", "Your Perfect Find Awaits", "Season's New Arrivals!"]
        messages = ["Biggest deals now!", "Don't miss out.", "Discover what everyone's talking about."]
        ctas = ["Shop Now", "Learn More", "Claim Offer"]
        ideas = []
        for _, row in low_ctr_df.iterrows():
            ideas.append({
                "campaign_name": row["campaign_name"],
                "headline": random.choice(headlines),
                "message": random.choice(messages),
                "cta": random.choice(ctas)
            })
        return ideas
