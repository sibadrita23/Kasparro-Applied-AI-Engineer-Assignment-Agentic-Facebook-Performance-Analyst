import json

def log_run(log_path, insights, creatives):
    data = {"insights": insights, "creatives": creatives}
    with open(log_path, "w") as f:
        json.dump(data, f, indent=2)
