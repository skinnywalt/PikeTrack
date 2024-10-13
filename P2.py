import streamlit as st

import main_file as mf
import P1, P3, P4


def call_P2(users_collection):
    st.image("assets/Letter.png", caption="Letter Image", use_column_width=True)
    st.header("Add a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    netID = st.text_input("NetId")
    
    if st.button("Add User"):
        if name and email:
            user_id = mf.add_user(name, email, netID)
            #If we are able to add user as they do not already exist
            if user_id:
                #import pdb; pdb.set_trace()
                st.success(f"User {name} added with ID: {user_id}")
                P4.call_P4(user_id, users_collection)
            else:
                #The user already exist so Login
                P3.call_P3(users_collection)
        else:
            st.error("Please provide both name and email.")