# Diabetes Prediction Page
import os
import pickle
import streamlit as st

# Assuming this file is in the 'pages' directory
working_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

# page title
st.title('Diabetes Prediction using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)
with col1:
    Pregnancies = st.text_input('Number of Pregnancies')
with col2:
    Glucose = st.text_input('Glucose Level')
with col3:
    BloodPressure = st.text_input('Blood Pressure value')
with col1:
    SkinThickness = st.text_input('Skin Thickness value')
with col2:
    Insulin = st.text_input('Insulin Level')
with col3:
    BMI = st.text_input('BMI value')
with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
with col2:
    Age = st.text_input('Age of the Person')


# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction
if st.button('Diabetes Test Result'):
    user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                    BMI, DiabetesPedigreeFunction, Age]
    user_input = [float(x) for x in user_input]
    diab_prediction = diabetes_model.predict([user_input])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is diabetic'
        st.error(diab_diagnosis)
    else:
        diab_diagnosis = 'The person is not diabetic'
        st.success(diab_diagnosis)