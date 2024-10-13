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

    if start_prog:
        P2.call_P2(users_collection)
        
    
if __name__ == "__main__":
    main()


def add_user(name, email, netID):
    #Validate first 
    
    #User Validation
    #If NewUser already exists goto Login Page
    user = users_collection.find_one({"NetID": netID})
    
    if user:
        #Return 0 as New User already registered
        return user["_id"], 0  
    else:
        user = {"Name": name, "Student Email": email, "NetID": netID, "Total_time" : 0, "clock_in_status" : False}
        result = users_collection.insert_one(user) 
        #st.error(f"Invalid NedID: {netID} or Email : {email}")
        return result.inserted_id, 1
    
    
    
    

def clock_in(user_id, netID):
    
    user_obj_id = ObjectId(user_id)  # Convert user_id to ObjectId
    user = users_collection.find_one({"_id": user_obj_id})
    
    if user.get("clock_in_status") == True:
        st.error("Already Clocked in, Clocking Out...")
        clock_out(user_id, netID)
        return
    
    
    #fetch the user_id and then add clock_in tiem as key      
    user_obj_id = ObjectId(user_id)
    time1 =  time.time()
    new_field = {"$set": {"clock_in": time1}}
    result = users_collection.update_one({"_id": user_obj_id}, new_field)
    
    users_collection.update_one({"_id": user_obj_id}, {"$set": {"clock_in_status": True}})
    
    st.success(f"{netID} Clock In Successfull!")

def clock_out(user_id, netID):
    
    user_obj_id = ObjectId(user_id)
    
    time2 =  time.time()
    new_field = {"$set": {"clock_out": time2}}
    result = users_collection.update_one({"_id": user_obj_id}, new_field)

    users_collection.update_one({"_id": user_obj_id}, {"$set": {"clock_in_status": False}})
    
    #Calculate the Total Time Stayed at the Library
    user = users_collection.find_one({"_id": user_obj_id})
    clock_in_time = user.get("clock_in")
    clock_out_time = user.get("clock_out")
    added_time = clock_out_time - clock_in_time
    
    min_time = added_time
    min_time /= 60
    
    st.success(f"Added Time: {min_time:.2f} minutes")
    
    curr_total = user.get("Total_time")
    total_time = curr_total + added_time
    total_time /= 60
    
    users_collection.update_one({"_id": user_obj_id}, {"$set": {"Total_time": total_time}})
    
    users_collection.update_one({"_id": user_obj_id}, {"$unset": {"clock_in": ""}})  # Remove the clock_out field)
    users_collection.update_one({"_id": user_obj_id}, {"$unset": {"clock_out": ""}})
    
    st.success(f"{netID} Clock Out Successfull!\n Total Time for {netID} = {total_time:.2f} min")
    return 
    
    