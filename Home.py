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
