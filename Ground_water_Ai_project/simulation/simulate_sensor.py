import random
import time
from datetime import datetime
import pandas as pd
import os
from config import *
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database.db_manager import insert_data
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_file = os.path.join(BASE_DIR, "data", "water_data.csv")

if not os.path.exists(csv_file):

    df = pd.DataFrame(columns=[
        "Timestamp",
        "Water_Level",
        "Flow_Rate",
        "Pressure",
        "Temperature",
        "pH",
        "TDS",
        "Leakage",
        "Overflow",
        "Risk_Score",
        "Scenario"
    ])

    df.to_csv(csv_file,index=False)
scenarios = [

    "Normal",

    "Leakage",

    "Overflow",

    "Low Water"

]
def generate_sensor_data():

    scenario = random.choice(scenarios)

    if scenario == "Normal":

        water_level = random.randint(60,85)
        flow = round(random.uniform(5,12),2)
        pressure = round(random.uniform(1.3,2.2),2)

    elif scenario == "Leakage":

        water_level = random.randint(50,80)
        flow = round(random.uniform(16,20),2)
        pressure = round(random.uniform(0.5,0.9),2)

    elif scenario == "Overflow":

        water_level = random.randint(96,100)
        flow = round(random.uniform(10,15),2)
        pressure = round(random.uniform(1.5,2.2),2)

    else:

        water_level = random.randint(20,35)
        flow = round(random.uniform(2,5),2)
        pressure = round(random.uniform(1.0,1.5),2)

    temperature = round(random.uniform(22,38),2)

    ph = round(random.uniform(6.5,8.5),2)

    tds = random.randint(150,600)

    leakage = "YES" if scenario=="Leakage" else "NO"

    overflow = "YES" if scenario=="Overflow" else "NO"

    return {

        "Timestamp":datetime.now(),

        "Water_Level":water_level,

        "Flow_Rate":flow,

        "Pressure":pressure,

        "Temperature":temperature,

        "pH":ph,

        "TDS":tds,

        "Leakage":leakage,

        "Overflow":overflow,

        "Scenario":scenario

    }
def calculate_risk(sensor):

    score = 0

    if sensor["Water_Level"] > 95:
        score += 40

    if sensor["Flow_Rate"] > 15:
        score += 30

    if sensor["Pressure"] < 1:
        score += 30

    return score
while True:

    sensor = generate_sensor_data()

    sensor["Risk_Score"] = calculate_risk(sensor)

    insert_data(sensor)

    df = pd.DataFrame([sensor])

    df.to_csv(csv_file,mode="a",header=False,index=False)

    print(df)

    time.sleep(UPDATE_INTERVAL)