from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib  # or pickle, depending on how model was saved
from pycaret.classification import load_model, predict_model  # or regression
from pathlib import Path
import numpy as np

# Initialize FastAPI app
app = FastAPI(title="PyCaret Model API", version="1.0")

# Load your saved PyCaret model
model = load_model(Path('../../Models/best_model'))  # Don't include .pkl if PyCaret was used to save_model("model")
# If you used joblib.dump(model, "model.pkl"), use joblib.load("model.pkl") instead.

# Define the data structure for input
class InputData(BaseModel):
    # Example fields — use the same feature names as your training data
    Sex: str
    Pclass: int
    SibSp: int
    Embarked: str
    Parch: int
    Age: float
    Fare: float


@app.get("/")
def home():
    return {"message": "PyCaret Model API is running!"}


from fastapi.encoders import jsonable_encoder

@app.post("/predict")
def predict(data: InputData):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Make prediction
    predictions = predict_model(model, data=input_df)

    # Extract results
    prediction = predictions.loc[0, "prediction_label"]
    prediction_score = (
        predictions.loc[0, "prediction_score"]
        if "prediction_score" in predictions.columns
        else None
    )

    # ✅ Convert numpy types → Python
    if isinstance(prediction, (np.generic,)):  # catches np.int64, np.float64, etc.
        prediction = prediction.item()
    if isinstance(prediction_score, (np.generic,)):
        prediction_score = prediction_score.item()

    # ✅ Build plain-Python response
    response = {
        "input_data": data.dict(),
        "prediction": prediction,
        "prediction_score": prediction_score,
    }

    # ✅ Use FastAPI's safe encoder
    return jsonable_encoder(response)
