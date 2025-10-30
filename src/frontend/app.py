import streamlit as st

st.title('Titanic survival prediction')


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
                                value=0)
    
    embarked_val = st.selectbox('Enter port of embarkation',
                                options=['S', 'C', 'Q'],
                                index=0)
    
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
                               value=0)
    

    submit = st.form_submit_button('Submit')