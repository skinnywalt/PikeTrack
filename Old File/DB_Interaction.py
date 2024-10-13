from pymongo import MongoClient
from datetime import datetime

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['library_hour_tracker']
users_collection = db['users']
sessions_collection = db['sessions']

# Function to add a new user
def add_user(name, email):
    user = {"name": name, "email": email}
    result = users_collection.insert_one(user)
    return result.inserted_id

# Function to start a session
def start_session(user_id):
    session = {
        "user_id": user_id,
        "start_time": datetime.now(),
        "end_time": None,
        "hours_logged": None
    }
    result = sessions_collection.insert_one(session)
    return result.inserted_id

# Function to end a session and log hours
def end_session(session_id):
    session = sessions_collection.find_one({"_id": session_id})
    if session and not session["end_time"]:
        end_time = datetime.now()
        hours_logged = (end_time - session["start_time"]).total_seconds() / 3600
        sessions_collection.update_one(
            {"_id": session_id},
            {"$set": {"end_time": end_time, "hours_logged": hours_logged}}
        )
        return hours_logged
    return None

# Function to get total hours for a user
def get_total_hours(user_id):
    sessions = sessions_collection.find({"user_id": user_id, "hours_logged": {"$ne": None}})
    total_hours = sum(session["hours_logged"] for session in sessions)
    return total_hours
