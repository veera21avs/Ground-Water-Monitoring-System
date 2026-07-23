import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "groundwater.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

print(cursor.fetchall())

conn.close()
