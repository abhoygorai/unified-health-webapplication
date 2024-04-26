# Heart Disease Prediction Page
import os
import pickle
import streamlit as st

from prediction_utils import *

# Assuming this file is in the 'pages' directory
# working_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# heart_disease_model = pickle.load(
#     open(f"{working_dir}/saved_models/heart_disease_model.sav", "rb")
# )

# sex, age, race, height, weight, smoking, alcohol, general_health, sleep_time, mental_health, physical_health, physical_activity, diff_walking, stroke, diabetic, asthma, skin_cancer, kidney_disease

# page title
st.title("Cardio Vascular")
col1, col2, col3 = st.columns(3)
with col1:
    sex = st.selectbox(
        "Sex",
        ("Male", "Female"),
    )
with col2:
    age = st.selectbox(
        "Age",
        (
            "18-24",
            "25-29",
            "30-34",
            "35-39",
            "40-44",
            "45-49",
            "50-54",
            "55-59",
            "60-64",
            "65-69",
            "70-74",
            "75-79",
        ),
    )
with col3:
    race = st.selectbox(
        "Race",
        ("Black", "Hispanic", "White", "Other"),
    )
with col1:
    height = st.text_input("Height")
with col2:
    weight = st.text_input("Weight")
with col3:
    sleep_time = st.text_input(
        "On average, how many hours of sleep do you get in a 24-hour period?"
    )
with col1:
    alcohol = st.selectbox(
        "Heavy alcohol drinkers (Male: >14 drinks & Female: >7 drinks per week)",
        ("Yes", "No"),
    )
with col2:
    general_health = st.selectbox(
        "Would you say that in general your health is..",
        (
            "Excellent",
            "Very good",
            "Good",
            "Fair",
            "Poor",
        ),
    )
with col3:
    smoking = st.selectbox(
        "Have you smoked at least 100 cigarettes in your entire life?",
        ("Yes", "No"),
    )
with col1:
    mental_health = st.text_input(
        "How many days during the past 30 days was your mental health not good?"
    )
with col2:
    physical_health = st.text_input(
        "How many days during the past 30 days was your physical health not good?"
    )
with col3:
    physical_activity = st.selectbox(
        "Did you do exercise during the past 30 days other than their regular job?",
        ("Yes", "No"),
    )
with col1:
    diff_walking = st.selectbox(
        "Do you have serious difficulty walking or climbing stairs?",
        ("Yes", "No"),
    )

with col2:
    stroke = st.selectbox(
        "Have you ever had a stroke?",
        ("Yes", "No"),
    )
with col3:
    diabetic = st.selectbox(
        "Have you ever had a diabetes?",
        ("Yes", "No"),
    )

with col1:
    asthma = st.selectbox(
        "Have you ever had an asthma?",
        ("Yes", "No"),
    )

with col2:
    skin_cancer = st.selectbox(
        "Have you ever had a skin cancer?",
        ("Yes", "No"),
    )
with col3:
    kidney_disease = st.selectbox(
        "Have you ever had a kidney disease?",
        ("Yes", "No"),
    )


# code for Prediction
heart_diagnosis = ""

# creating a button for Prediction
if st.button("Calculate Heart Disease risk rate"):
    user_input = [
        sex,
        age,
        race,
        height,
        weight,
        smoking,
        alcohol,
        general_health,
        sleep_time,
        mental_health,
        physical_health,
        physical_activity,
        diff_walking,
        stroke,
        diabetic,
        asthma,
        skin_cancer,
        kidney_disease,
    ]
    # user_input = [float(x) for x in user_input]
    # heart_prediction = heart_disease_model.predict([user_input])

    model_prediction = predict(
        sex,
        age,
        race,
        height,
        weight,
        smoking,
        alcohol,
        general_health,
        sleep_time,
        mental_health,
        physical_health,
        physical_activity,
        diff_walking,
        stroke,
        diabetic,
        asthma,
        skin_cancer,
        kidney_disease,
    )
    
    st.info(f"Your Heart Disease risk rate is: {model_prediction}%")
