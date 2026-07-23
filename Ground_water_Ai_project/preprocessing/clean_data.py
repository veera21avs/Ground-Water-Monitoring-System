import sqlite3
import pandas as pd
import os

# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build database path
DB_PATH = os.path.join(BASE_DIR, "..", "database", "groundwater.db")

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Read table
df = pd.read_sql_query("SELECT * FROM groundwater_data", conn)

print(df.head())
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Remove invalid values
df = df[df["pressure"] >= 0]
df = df[(df["water_level"] >= 0) & (df["water_level"] <= 100)]
df = df[df["flow_rate"] >= 0]

# Save cleaned dataset
# Create data folder path
DATA_PATH = os.path.join(BASE_DIR, "..", "data")

# Create the folder if it doesn't exist
os.makedirs(DATA_PATH, exist_ok=True)

# Output file path
OUTPUT_FILE = os.path.join(DATA_PATH, "clean_water_data.csv")

# Save cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaning Completed Successfully!")

conn.close()