from fastapi import FastAPI
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    values = list(data.values())
    result = model.predict([values])
    return {"fraud": int(result[0])}
