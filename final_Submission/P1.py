import streamlit as st

import main_file as mf

def call_P1():
    # Load an image from the assets folder
    st.image("assets/P1.png", caption="P1_page")

    # checkbox_value = st.checkbox("START")
    
    checkbox_value = st.checkbox("START")

    if checkbox_value:
        return True