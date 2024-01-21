from pydantic import BaseModel
from fastapi import FastAPI

import uvicorn
import joblib

# Instantiate the app
app = FastAPI()


class request_body(BaseModel):
    study_hours: float


# Load the model
model = joblib.load('./regression_model.pkl')


@app.post('/predict')
def predict(data: request_body):
    # Prepare the data for prediction
    input_feature = [[data.study_hours]]

    # Make the prediction
    y_pred = model.predict(input_feature)[0].astype(int)

    # Return the prediction as a dictionary
    return {'test_score': y_pred.tolist()}
