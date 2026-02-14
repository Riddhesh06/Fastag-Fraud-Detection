import joblib
import numpy as np
from App.model.config import THRESHOLD, FEATURE_COLUMNS

model = joblib.load("App/model/logistic_regression_model.pkl")
scaler = joblib.load("App/model/scaler.pkl")
FEATURE_COLUMNS = joblib.load("App/model/feature_columns.pkl")


def predict_fraud(data: dict):
    features = np.array([[data[col] for col in FEATURE_COLUMNS]])
    features_scaled = scaler.transform(features)

    prob = model.predict_proba(features_scaled)[0][1]
    is_fraud = int(prob >= THRESHOLD)

    return {
        "fraud_probability": round(prob, 4),
        "is_fraud": is_fraud
    }

    print("Incoming data:", data)
    print("Expected features:", FEATURE_COLUMNS)    
