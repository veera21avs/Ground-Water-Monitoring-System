from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import pandas as pd
import joblib
import os

app = Flask(__name__)
CORS(app)

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(BASE_DIR, "..", "database", "groundwater.db")
MODEL_PATH = os.path.join(BASE_DIR, "..", "ml", "model.pkl")

# Load ML model
model = joblib.load(MODEL_PATH)

# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return jsonify({
        "message": "Groundwater AI Monitoring API Running"
    })

# -----------------------------
# Live Data
# -----------------------------
@app.route("/live")
def live():

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query("""
        SELECT *
        FROM groundwater_data
        ORDER BY id DESC
        LIMIT 1
    """, conn)

    conn.close()

    return jsonify(df.to_dict(orient="records"))

# -----------------------------
# Prediction
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    sample = pd.DataFrame([{
        "water_level": data["water_level"],
        "flow_rate": data["flow_rate"],
        "pressure": data["pressure"],
        "temperature": data["temperature"],
        "ph": data["ph"],
        "tds": data["tds"],
        "risk_score": data["risk_score"]
    }])

    prediction = model.predict(sample)
    probability = model.predict_proba(sample)

    return jsonify({
        "Leakage": "YES" if prediction[0] == 1 else "NO",
        "Probability": round(max(probability[0]) * 100, 2)
    })

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)