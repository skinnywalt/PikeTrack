import streamlit as st
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import time

import P1, P2, P3, P4

#def connect_db():
# Connect to MongoDB
client = MongoClient("mongodb+srv://test_user1:test_user1@cluster0.7wn3d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['library']
users_collection = db['hour_tracker']
sessions_collection = db['sessions']
users_collection.create_index("NetID", unique=True)


def main():
    start_prog = P1.call_P1()
    # if p2_redirect:
    if start_prog:
        P2.call_P2(users_collection)
        
    
if __name__ == "__main__":
    main()


def add_user(name, email, netID):
    #Validate first 
    
    #User Validation
    #If NewUser already exists goto Login Page
    # user_obj_id = ObjectId(user_id)
    # user = users_collection.find_one({"_id": user_obj_id})
    
    user = users_collection.find_one({"NetID": netID})
    
    if user:
        return user["_id"], 0  
    else:
        user = {"Name": name, "Student Email": email, "NetID": netID, "clock_in_status" : False}
        result = users_collection.insert_one(user) 
        #st.error(f"Invalid NedID: {netID} or Email : {email}")
        return result.inserted_id, 1
    
    
    
    

def clock_in(user_id, netID):
    st.success(f"{netID} Clock In Successfull!")
    
    clkin = users_collection.find({"clock_in_status" : True})
   
    user_obj_id = ObjectId(user_id)  # Convert user_id to ObjectId
    user = users_collection.find_one({"_id": user_obj_id})
        
    if user.get("clock_in_status") == True:
        st.error("Already Clocked in, Clocking Out...")
        clock_out(user_id, netID)
    
    #fetch the user_id and then add clock_in tiem as key      
    user_obj_id = ObjectId(user_id)
    time1 =  time.time()
    new_field = {"$set": {"clock_in": time1}}
    result = users_collection.update_one({"_id": user_obj_id}, new_field)
    
    users_collection.update_one({"_id": user_obj_id}, {"$set": {"clock_in_status": True}})
    #P3.call_P3(users_collection, user_id, netID)
    #return 

def clock_out(user_id, netID):
    st.success(f"{netID} Clock Out Successfull!")
    user_obj_id = ObjectId(user_id)
    time2 =  time.time()
    new_field = {"$set": {"clock_out": time2}}
    result = users_collection.update_one({"_id": user_obj_id}, new_field)

    users_collection.update_one({"_id": user_obj_id}, {"$set": {"clock_in_status": False}})
                                
    # users_collection.update_one(
    # {"_id": user_obj_id},  # Match the document by user_id
    # {"$unset": {"clock_in": ""}})  # Remove the clock_out field)
    
    #P3.call_P3(users_collection, user_id, netID)
    