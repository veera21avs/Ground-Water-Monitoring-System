import pandas as pd
import os

# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Input file path
INPUT_FILE = os.path.join(BASE_DIR, "..", "data", "clean_water_data.csv")

# Output file path
OUTPUT_FILE = os.path.join(BASE_DIR, "..", "data", "final_dataset.csv")

# Read cleaned dataset
df = pd.read_csv(INPUT_FILE)

# -----------------------------
# Feature 1 : Water Usage (L/hour)
# -----------------------------
df["water_usage"] = df["flow_rate"] * 60

# -----------------------------
# Feature 2 : Pressure Status
# -----------------------------
df["pressure_status"] = df["pressure"].apply(
    lambda x: "LOW" if x < 1 else "NORMAL"
)

# -----------------------------
# Feature 3 : Water Level Status
# -----------------------------
def water_status(level):
    if level > 95:
        return "OVERFLOW"
    elif level < 30:
        return "LOW"
    else:
        return "NORMAL"

df["water_status"] = df["water_level"].apply(water_status)

# -----------------------------
# Feature 4 : Risk Category
# -----------------------------
def risk_category(score):
    if score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    else:
        return "LOW"

df["risk_category"] = df["risk_score"].apply(risk_category)

# -----------------------------
# Feature 5 : Flow Status
# -----------------------------
def flow_status(flow):
    if flow > 15:
        return "HIGH"
    elif flow < 5:
        return "LOW"
    else:
        return "NORMAL"

df["flow_status"] = df["flow_rate"].apply(flow_status)

# -----------------------------
# Feature 6 : Water Quality
# -----------------------------
def water_quality(ph, tds):
    if 6.5 <= ph <= 8.5 and tds < 500:
        return "GOOD"
    elif tds < 800:
        return "MODERATE"
    else:
        return "POOR"

df["water_quality"] = df.apply(
    lambda row: water_quality(row["ph"], row["tds"]),
    axis=1
)

# -----------------------------
# Save Final Dataset
# -----------------------------
df.to_csv(OUTPUT_FILE, index=False)

print("✅ Feature Engineering Completed Successfully!")
print(df.head())