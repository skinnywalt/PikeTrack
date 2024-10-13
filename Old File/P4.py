#Clock in/Clock out
import streamlit as st
import time
from bson import ObjectId

import main_file as mf
import P1, P2, P3


def call_P4(user_id, users_collection):
    user_obj_id = ObjectId(user_id)
    
    user = users_collection.find_one({"_id": user_obj_id})
    
    if user:
        #import pdb; pdb.set_trace()
        #clkin = #users_collection.find({"clock_in_status" : True})
        # if user.get("clock_in_status") == True:
        #     st.button("Clock Out")
        #     mf.clock_out(user_id)
        # else:
        #     st.button("Clock In")
        #     mf.clock_in(user_id) 
        status = st.selectbox("Select Status", ("Clock In", "Clock Out"))
        if status == "Clock In":
            mf.clock_in(user_id)
        elif status == "Clock Out":
            mf.clock_out(user_id)
            
                
    
    
    # elif st.button("Clock out"):
    #     mf.clock_in(user_id)
    
#     crop_variety = st.text_input("Crop Variety", "TME 419", key="crop_variety",disabled=True,label_visibility="visible")
# plot_name = st.selectbox("Plot Name/Code", plot_name_options, key="plot_name")