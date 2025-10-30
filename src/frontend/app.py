import streamlit as st
import requests
from pathlib import Path

st.title('Titanic survival prediction')
st.image(str(Path('../../images/titanic_ship.png')), use_container_width=True)

with st.form('form_key'):
    gender = st.selectbox('Please select gender',
                          options=['male', 'female'], index=0
                          )
    
    pclass_val = st.selectbox('Please select passenger class',
                              options=[1, 2, 3],
                              index = 0
                              )
    
    sibsp_val = st.number_input('Enter number of siblings',
                                min_value=0,
                                max_value=None,
                                value=0
                                )
    
    embarked_val = st.selectbox('Enter port of embarkation',
                                options=['S', 'C', 'Q'],
                                index=0
                                )
    
    parch_val = st.number_input('Enter number of parents/children',
                                min_value = 0,
                                max_value=None,
                                value=0
                                )
    
    age_val = st.number_input('Enter age of passenger',
                              min_value = 0,
                              max_value = None,
                              value = 0
                              )
    
    fare_val = st.number_input('Enter the fare amount',
                               min_value = 0,
                               max_value=None,
                               value=0
                               )
    

    submit = st.form_submit_button('Submit')


payload_data = {
    "Sex": gender,
    "Pclass": pclass_val,
    "SibSp": sibsp_val,
    "Embarked": embarked_val,
    "Parch": parch_val,
    "Age": age_val,
    "Fare": fare_val
}

endpoint = "http://127.0.0.1:8000/predict"
if submit:
    response = requests.post(url = endpoint, json = payload_data)
    response_json = response.json()

    survival = response_json['prediction']
    survival_prob = response_json['prediction_score']

    st.write('### Result')
    st.write(f'Prediction: {survival} with probability {survival_prob}')

    