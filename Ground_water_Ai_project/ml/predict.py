import joblib
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(MODEL)

sample = pd.DataFrame([{

    "water_level":96,

    "flow_rate":18,

    "pressure":0.8,

    "temperature":30,

    "ph":7.2,

    "tds":350,

    "risk_score":90

}])

prediction = model.predict(sample)

if prediction[0] == 1:
    print("🚨 Leakage Predicted")
else:
    print("✅ Normal Condition")