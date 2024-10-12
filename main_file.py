import streamlit as st
from pymongo import MongoClient
from datetime import datetime

import P1, P2, p3, P4

# Connect to MongoDB
client = MongoClient("mongodb+srv://test_user1:test_user1@cluster0.7wn3d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['library']
users_collection = db['hour_tracker']
sessions_collection = db['sessions']


def main():
    
    
    #P1.call_P1()
    P2.call_P2()
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()


def add_user(name, email, netID):
    #Validate first 
    
    user = {"name": name, "NetID": netID, "Student Email": email}
    result = users_collection.insert_one(user)
    
    return result.inserted_id

