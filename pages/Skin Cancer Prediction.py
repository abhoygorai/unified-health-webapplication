import streamlit as st


# Function to generate iframe
def generate_iframe(url):
    iframe = f'<iframe src="{url}" width="1000" height="1600" scrolling="no" ;"></iframe>'
    return iframe


# Main Streamlit app
def main():

    # Get the URL from the user
    website_url = "https://aadarsh-nagrath.github.io/sc/"

    if website_url:
        # Generate and display the iframe
        st.write(generate_iframe(website_url), unsafe_allow_html=True)


if _name_ == "_main_":
    main()