import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Define page content
def main():
    # Custom CSS styling
    st.markdown(
        """
        <style>
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-bottom: 30px;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 20px;
        }
        .category {
            font-size: 20px;
            font-weight: bold;
            color: #1E90FF;
        }
        .disease {
            font-size: 18px;
            color: #666;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title
    st.markdown("<h1 class='title'>Disease Prediction Platform</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Introduction
    st.markdown("Welcome to our platform for disease prediction and analysis. We utilize machine learning and deep learning algorithms to predict and analyze various diseases.")
    st.markdown("---")
    
    # Main content
    st.subheader("Available Disease Predictions:")
    
    # Define disease categories
    categories = {
        "Cancer Detection": ["Breast Cancer", "Lung Cancer"],
        "Neurological Disorders": ["Parkinson's Disease"],
        "Cardiovascular Diseases": ["Cardiovascular Disease", "Heart Failure"],
        "Dermatology": ["Skin Cancer"]
    }
    
    # Display disease categories and options
    for category, diseases in categories.items():
        st.markdown(f"<p class='category'>{category}</p>", unsafe_allow_html=True)
        for disease in diseases:
            st.markdown(f"<p class='disease'>- {disease}</p>", unsafe_allow_html=True)
        st.markdown("---")

# Run the app
if __name__ == "__main__":
    main()