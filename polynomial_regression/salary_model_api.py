from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import uvicorn
import joblib

# Create a FastAPI instance
app = FastAPI()

# Criate a class with the input data


class request_body(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int


# Load the model
poly_model = joblib.load('./salary_model.pkl')


@app.post('/predict')
def predict_salary(data: request_body):
    input_features = {
        'tempo_na_empresa': data.tempo_na_empresa,
        'nivel_na_empresa': data.nivel_na_empresa
    }

    pred_df = pd.DataFrame(input_features, index=[1])

    # Predict the salary
    y_pred = poly_model.predict(pred_df)[0].astype(float)

    return {
        'salario_em_reais': y_pred.tolist()
    }
