import pandas as pd
import os

# URL of the raw CSV file on GitHub
url = "https://raw.githubusercontent.com/sibadrita23/Kasparro-Applied-AI-Engineer-Assignment-Agentic-Facebook-Performance-Analyst/main/synthetic_fb_ads_undergarments.csv"

# Load CSV directly from GitHub
df = pd.read_csv(url)

# Ensure the 'data' folder exists; create if needed
os.makedirs('data', exist_ok=True)

# Save the DataFrame to a CSV file in the data directory without the index column
output_path = 'data/synthetic_fb_ads_undergarments.csv'
df.to_csv(output_path, index=False)

print(f"Data saved successfully to {output_path}")
