import pandas as pd
import os

# Raw URL for the CSV file
url = "https://raw.githubusercontent.com/sibadrita23/Kasparro-Applied-AI-Engineer-Assignment-Agentic-Facebook-Performance-Analyst/main/synthetic_fb_ads_undergarments.csv"

# Desired column order and names according to your structure
columns = [
    "date",
    "spend",
    "impressions",
    "clicks",
    "ctr",
    "purchases",
    "revenue",
    "roas",
    "creative_type",
    "creative_message",
    "audience_type",
    "platform",
    "country"
]

# Load CSV from URL
df = pd.read_csv(url)

# Rename columns if necessary (based on your example image snippet and typical CSV naming)
df = df.rename(columns={
    "impressio": "impressions",
    "creative_t": "creative_type",
    "creative_r": "creative_message",
    "udience_": "audience_type"
})

# Reorder columns to desired structure
df = df[columns]

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save to CSV in data directory
output_path = 'data/synthetic_fb_ads_undergarments_structured.csv'
df.to_csv(output_path, index=False)

print(f"Structured CSV data saved to {output_path}")
