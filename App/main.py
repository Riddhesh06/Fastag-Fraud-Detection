from fastapi import FastAPI
from App.schemas import TransactionInput
from App.services.prediction import predict_fraud

app = FastAPI(title="Fraud Detection API")

@app.post("/predict")
def predict(transaction: TransactionInput):
    return predict_fraud(transaction.dict())
