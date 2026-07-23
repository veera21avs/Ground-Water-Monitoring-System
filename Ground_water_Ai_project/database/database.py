import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "groundwater.db")

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS groundwater_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    water_level REAL,
    flow_rate REAL,
    pressure REAL,
    temperature REAL,
    ph REAL,
    tds REAL,
    leakage TEXT,
    overflow TEXT,
    risk_score INTEGER,
    scenario TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")