import streamlit as st

import main_file as mf
import P1, P3, P4


def call_P2(users_collection):
    #st.image("assets/Letter.png", caption="Letter Image", use_column_width=True)
    st.header("Add a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    netID = st.text_input("NetId")
    
    if st.button("Add User"):
        if name and email and netID:
            user_id, boo = mf.add_user(name, email, netID)
            #If we are able to add user as they do not already exist
            if boo == 1:
                #import pdb; pdb.set_trace()
                st.success(f"User {name} added with ID: {user_id}")
                P4.call_P4(user_id, users_collection, netID)
            elif boo == 0 and user_id:
                #The user already exist so Login
                st.error(f"NetID : {netID} already exists, Logging In Automatically.")
                P3.call_P3(users_collection, user_id, netID)
        else:
            st.error("Please provide both name and email.")