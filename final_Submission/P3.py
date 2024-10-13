#login verification

import streamlit as st
import main_file as mf
import time

import pdb;

import P1, P2, P4


def call_P3(users_collection, user_id, netID):    
    st.header(f"Logging in {netID}")
        # Check if the NetID exists in the database
    user = users_collection.find_one({"NetID": netID})
    
    if user is not None:
        # If user exists, go to Clock In/Out Page
        st.success("Login Successful!")
        P4.call_P4(user["_id"], users_collection, netID)
    else:
        # If user does not exist, show an error and redirect to sign-up
        st.error(f"NetID : {netID} does not exist, Please Sign Up.")
        P2.call_P2(users_collection)
        
        
        
    
    
    
    
        
    