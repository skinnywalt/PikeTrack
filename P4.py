#Clock in/Clock out
import streamlit as st
import time

import main_file as mf
import P1, P2, P3


def call_P4(user_id):
    st.button("Clock In")
    mf.clock_in(user_id)
    
    # elif st.button("Clock out"):
    #     mf.clock_in(user_id)