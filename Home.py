import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# Set up search bar with icon
search_query = st.text_input("",
                             placeholder="🔍 Search...",
                             key="search_input",
                             )


st.sidebar.markdown("Page 3 🎉")

#sidebar for navigation
# with st.sidebar:
#     selected = option_menu('Multiple Disease Prediction System',

#                            ['Diabetes Prediction',
#                             'Heart Disease Prediction',
#                             'Parkinsons Prediction'],
#                            menu_icon='hospital-fill',
#                            icons=['activity', 'heart', 'person'],
#                            default_index=0)
