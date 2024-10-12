import streamlit as st
from pymongo import MongoClient
from datetime import datetime

import P1, P2, P3, P4

#def connect_db():
# Connect to MongoDB
client = MongoClient("mongodb+srv://test_user1:test_user1@cluster0.7wn3d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['library']
users_collection = db['hour_tracker']
sessions_collection = db['sessions']


def main():
    # Connect to MongoDB
    #connect_db()
    
    #Signup = True & Login = False 
    # p2_redirect = P1.call_P1()
    
    # if p2_redirect:
    P2.call_P2()
    # else:
    #     P3.call_P3()
    
    # P4.call_P4()
        
    
        
    
    
    
    
if __name__ == "__main__":
    main()


def add_user(name, email, netID):
    #Validate first 
    
    user = {"name": name, "NetID": netID, "Student Email": email}
    result = users_collection.insert_one(user)
    
    return result.inserted_id

def clock_in(user_id):
    session = {
        "user_id": user_id,
        "start_time": datetime.now(),  # Capture current time
        "end_time": None,  # End time will be updated when the session ends
        "hours_logged": None
    }
    result = sessions_collection.insert_one(session)
    return result.inserted_id
    
def clock_out(user_id):
    pass

