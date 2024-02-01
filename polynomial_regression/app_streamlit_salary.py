import streamlit as st
import json
import requests


# Title of the app
st.title('Salary Prediction App')

# Input fields for the user
st.write("How many months have you been working at the company?")
tempo_na_empresa = st.slider(
    'Months', min_value=1, max_value=120, value=60, step=1)

st.write("What is your level at the company?")
nivel_na_empresa = st.slider(
    'Level', min_value=1, max_value=10, value=5, step=1)

# Prepare data to be sent to the API
input_features = {
    'tempo_na_empresa': tempo_na_empresa,
    'nivel_na_empresa': nivel_na_empresa
}


# Criate a button and capture the click event to send the data to the API
if st.button('Predict Salary'):
    res = requests.post(
        'http://127.0.0.1:8000/predict', json=json.dumps(input_features))
    res_json = json.loads(res.text)
    print(res_json)
    salario_em_reais = round(res_json['salario_em_reais'], 2)
    st.subheader(f'The predicted salary is R$ {salario_em_reais}')
