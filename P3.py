#login verification

import streamlit as st
import main_file as mf
import P1, P2, P4


def call_P3(users_collection):
    st.header("Login")
    #netID = st.text_input("NetId")
    # Use a unique key here
    
    netID = st.text_input("NetId", key="netid_input")  
    if st.button("Login"):
        if netID:
            user = users_collection.find_one({"NetID": netID})
            if user:
                #Goto Clock In/Out Page As the user is already in db
                P4.call_P4(user_id, users_collection)
            else:
                #Don't exist in system go SignUp
                st.error(f"NetID : {netID} exists, Please Sign Up.")
                P2.call_P2(users_collection)
        else:
            st.error("NetId is empty")
    
    
    
        
    
