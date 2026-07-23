import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "groundwater.db")

def insert_data(sensor):

    conn=sqlite3.connect(DATABASE)

    cur=conn.cursor()

    cur.execute("""

    INSERT INTO groundwater_data(

    timestamp,

    water_level,

    flow_rate,

    pressure,

    temperature,

    ph,

    tds,

    leakage,

    overflow,

    risk_score,

    scenario

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?)

    """,(sensor["Timestamp"],

         sensor["Water_Level"],

         sensor["Flow_Rate"],

         sensor["Pressure"],

         sensor["Temperature"],

         sensor["pH"],

         sensor["TDS"],

         sensor["Leakage"],

         sensor["Overflow"],

         sensor["Risk_Score"],

         sensor["Scenario"]))

    conn.commit()

    conn.close()