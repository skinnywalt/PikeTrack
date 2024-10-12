#Clock in/Clock out
import streamlit as st

import main_file as mf
import P1, P2, P3


def call_P4(user_id):
    if st.button("Clock In"):
        clkInId = mf.clock_in(user_id)
    elif st.button("Clock out"):
       clkOuId =  mf.clock_out(user_id)