import streamlit as st

import main_file as mf

def call_P2():
    # Add User Section
    st.header("Add a New User")
    name = st.text_input("Name")
    email = st.text_input("Email")
    netID = st.text_input("NetId")
    if st.button("Add User"):
        if name and email:
            user_id = mf.add_user(name, email, netID)
            if user_id:
                st.success(f"User {name} added with ID: {user_id}")
            else:
                st.error(f"Invalid NetID : {netID} or email : {email}")
        else:
            st.error("Please provide both name and email.")


