import streamlit as st

import main_file as mf

def call_P1():
    # Title
    st.title("PikeTrack")
    
    # Load and center the image
    st.image("assets/Letter.png", caption="P1_page", use_column_width=True)

    # checkbox_value = st.checkbox("START")
    
    checkbox_value = st.checkbox("START")

    if checkbox_value:
        return True