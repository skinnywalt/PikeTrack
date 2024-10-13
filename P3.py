#login verification

import streamlit as st
import main_file as mf
import time

import pdb;

import P1, P2, P4

def check_Id():
    netID = st.text_input("NetID", key="netid_input")
    if netID:
        if st.button("Submit"):
            # Check if the NetID exists in the database
            user = users_collection.find_one({"NetID": netID})
            
            if user is not None:
                # If user exists, go to Clock In/Out Page
                P4.call_P4(user_id, users_collection)
            else:
                # If user does not exist, show an error and redirect to sign-up
                st.error(f"NetID : {netID} does not exist, Please Sign Up.")
                P2.call_P2(users_collection)
    else:
        st.error("Please enter a valid NetID.")


def call_P3(users_collection, user_id):
    # st.header("Login")
    # #netID = st.text_input("NetId")
    # # Use a unique key here
    
    # # if st.button("Login"):
    # #     if netID:
    # #         user = users_collection.find_one({"NetID": netID})
    # #         if user:
    # #             #Goto Clock In/Out Page As the user is already in db
    # #             P4.call_P4(user_id, users_collection)
    # #         else:
    # #             #Don't exist in system go SignUp
    # #             st.error(f"NetID : {netID} exists, Please Sign Up.")
    # #             P2.call_P2(users_collection)
    # #     else:
    # #         st.error("NetID is empty")
    # #status = st.selectbox("Select Status", ("Login", "Not Login"))
    # checked = st.checkbox("Check to Login")    
    # #pdb.set_trace()
    
    # # if checked:
    # #     st.write("Checkbox was checked!")
        
    # #     if st.button("Submit"):
        
    # #         netID = st.text_input("NetID", key="netid_input")  
        
    # #         if netID:
    # #             user = users_collection.find_one({"NetID": netID})
    # #             if user is not None:
    # #                 #Goto Clock In/Out Page As the user is already in db
    # #                 P4.call_P4(user_id, users_collection)
    # #             else:
    # #                 #Don't exist in system go SignUp
    # #                 st.error(f"NetID : {netID} does not exists, Please Sign Up.")
    # #                 P2.call_P2(users_collection)
    # #         else:
    # #             st.error("NetID is empty") 
    # # else:
    # #     st.error("NetID is empty")
    # #     P4.call_P4(user_id, users_collection) 
    
    st.header("Login")
    
    # Display a checkbox for login
    #checked = st.checkbox("Check to Login")    

    check_Id()
    # if checked:
    #     st.write("Checkbox was checked!")

        
        
        
    
    
    
    
        
    
