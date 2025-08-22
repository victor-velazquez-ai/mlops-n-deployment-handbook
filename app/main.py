
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI(title="MLOps Handbook — Classifier API")

class PredictRequest(BaseModel):
    features: list[float] = Field(..., description="Feature vector in model order")

class PredictResponse(BaseModel):
    proba: float
    label: int

MODEL_PATH = "rf_model.joblib"
model = None

@app.on_event("startup")
def _load():
    global model
    try:
        model = joblib.load(MODEL_PATH)
    except Exception:
        model = None

@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    assert model is not None, "Model not loaded; place rf_model.joblib in repo root."
    X = np.array(req.features, dtype=float).reshape(1, -1)
    proba = float(model.predict_proba(X)[0,1])
    label = int(proba >= 0.5)
    return {"proba": proba, "label": label}
