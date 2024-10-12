import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['library_hour_tracker']
users_collection = db['users']
sessions_collection = db['sessions']

# Functions to interact with MongoDB
def add_user(name, email):
    user = {"name": name, "email": email}
    result = users_collection.insert_one(user)
    return result.inserted_id

def start_session(user_id):
    session = {
        "user_id": user_id,
        "start_time": datetime.now(),
        "end_time": None,
        "hours_logged": None
    }
    result = sessions_collection.insert_one(session)
    return result.inserted_id

def end_session(session_id):
    session = sessions_collection.find_one({"_id": session_id})
    if session and session["end_time"] is None:
        end_time = datetime.now()
        start_time = session["start_time"]
        hours_logged = (end_time - start_time).total_seconds() / 3600  # Calculate hours
        sessions_collection.update_one(
            {"_id": session_id},
            {"$set": {"end_time": end_time, "hours_logged": hours_logged}}
        )
        return hours_logged
    return None

# Streamlit UI
st.title("Library Hour Tracker")

# Add User Section
st.header("Add a New User")
name = st.text_input("Name")
email = st.text_input("Email")
if st.button("Add User"):
    if name and email:
        user_id = add_user(name, email)
        st.success(f"User {name} added with ID: {user_id}")
    else:
        st.error("Please provide both name and email.")

# Start Session Section
st.header("Start a Session")
user_id = st.text_input("User ID to Start Session")
if st.button("Start Session"):
    if user_id:
        session_id = start_session(user_id)
        st.success(f"Session started for User ID {user_id} with Session ID: {session_id}")
    else:
        st.error("Please provide a valid User ID.")

# End Session Section
st.header("End a Session")
session_id = st.text_input("Session ID to End")
if st.button("End Session"):
    if session_id:
        hours_logged = end_session(session_id)
        if hours_logged:
            st.success(f"Session ended. Hours logged: {hours_logged:.2f}")
        else:
            st.error("Invalid Session ID or session already ended.")
    else:
        st.error("Please provide a valid Session ID.")

# Show Active Sessions
st.header("Active Sessions")
active_sessions = sessions_collection.find({"end_time": None})
for session in active_sessions:
    user = users_collection.find_one({"_id": session["user_id"]})
    st.write(f"Session ID: {session['_id']}, User: {user['name']} ({user['email']}), Start Time: {session['start_time']}")
