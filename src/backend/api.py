from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib  # or pickle, depending on how model was saved
from pycaret.classification import load_model, predict_model  # or regression
from pathlib import Path

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
    Embarked_S: int
    Embarked_C: int
    Embarked_Q: int
    Parch: int
    Age: float
    Fare: float


@app.get("/")
def home():
    return {"message": "PyCaret Model API is running!"}

@app.post("/predict")
def predict(data: InputData):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Make prediction
    predictions = predict_model(model, data=input_df)

    # Extract prediction
    prediction = predictions["prediction_label"][0]
    prediction_score = predictions.get("prediction_score", [None])[0]

    return {
        "input_data": data.dict(),
        "prediction": prediction,
        "prediction_score": prediction_score,
    }

