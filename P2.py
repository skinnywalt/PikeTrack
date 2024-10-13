import streamlit as st

import main_file as mf
import P1, P3, P4


def call_P2():
    st.image("assets/letter.png", caption="Letter Image", use_column_width=True)
    st.header("Add a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    netID = st.text_input("NetId")
    
    if st.button("Add User"):
        if name and email:
            user_id = mf.add_user(name, email, netID)
            if user_id:
                #import pdb; pdb.set_trace()
                st.success(f"User {name} added with ID: {user_id}")
                P4.call_P4(user_id)
                #P4.call_P4(user_id)
            else:
                st.error(f"Invalid NedID: {netID} or Email : {email}")
        else:
            st.error("Please provide both name and email.")