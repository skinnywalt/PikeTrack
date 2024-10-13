#Clock in/Clock out
import streamlit as st
import time
from bson import ObjectId

import main_file as mf
import P1, P2, P3


def call_P4(user_id, users_collection, netID):
    user_obj_id = ObjectId(user_id)
    
    user = users_collection.find_one({"_id": user_obj_id})
    
    if user:
        status = st.selectbox("Select Status", ("Clock In", "Clock Out"))
        
        if status == "Clock In":
            mf.clock_in(user_id, netID)
            
        if status == "Clock Out":
            mf.clock_out(user_id, netID)