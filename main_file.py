import streamlit as st
from pymongo import MongoClient
from datetime import datetime


def main():
    
    
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://test_user1:test_user1@cluster0.7wn3d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client['library']
    users_collection = db['hour_tracker']
    sessions_collection = db['sessions']
    
    
    
    
    
    
    
    
    
    
    
    
    
    main()


def add_user(name, email, netID):
    user = {"name": name, "NetID": netID, "Student Email": email}
    result = users_collection.insert_one(user)
    return result.inserted_id

