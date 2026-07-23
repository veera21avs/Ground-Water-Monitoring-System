import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# Read Dataset
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(BASE_DIR, "..", "data", "final_dataset.csv")

df = pd.read_csv(DATASET)

print(df.head())

# -----------------------------
# Convert YES / NO
# -----------------------------
le = LabelEncoder()

df["leakage"] = le.fit_transform(df["leakage"])

# -----------------------------
# Features
# -----------------------------
X = df[[
    "water_level",
    "flow_rate",
    "pressure",
    "temperature",
    "ph",
    "tds",
    "risk_score"
]]

# Target
y = df["leakage"]

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nConfusion Matrix")

print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")

print(classification_report(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
MODEL = os.path.join(BASE_DIR, "model.pkl")

joblib.dump(model, MODEL)

print("\nModel Saved Successfully!")