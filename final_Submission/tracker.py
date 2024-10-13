import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
client = MongoClient("mongodb+srv://test_user1:test_user1@cluster0.7wn3d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['library']
users_collection = db['hour_tracker']
sessions_collection = db['sessions']

#def validate(netID)


# Functions to interact with MongoDB
def add_user(name, email, netID):
    user = {"name": name, "NetID": netID, "Student Email": email}
    result = users_collection.insert_one(user)
    return result.inserted_id

def find_user(email):
    return users_collection.find_one({"email": email})

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

<<<<<<< HEAD
# Sidebar Navigation
page = st.sidebar.radio("Select Page", ("Home", "Track Hours"))

# User Registration/Login Section
if page == "Home":
    st.header("User Registration/Login")

    if 'user_id' not in st.session_state:
        # Registration form
        with st.form(key='registration_form'):
            st.subheader("Register New User")
            reg_name = st.text_input("Name")
            reg_email = st.text_input("Email")
            reg_submit = st.form_submit_button("Register")

            if reg_submit:
                if reg_name and reg_email:
                    if find_user(reg_email) is None:
                        user_id = add_user(reg_name, reg_email)
                        st.success(f"User {reg_name} registered with ID: {user_id}")
                    else:
                        st.error("Email already registered.")

        # Login form
        with st.form(key='login_form'):
            st.subheader("Login")
            login_email = st.text_input("Email")
            login_submit = st.form_submit_button("Login")

            if login_submit:
                user = find_user(login_email)
                if user:
                    st.session_state.user_id = str(user['_id'])
                    st.session_state.user_name = user['name']
                    st.success(f"Welcome back, {user['name']}!")
                else:
                    st.error("User not found. Please register.")
    else:
        st.success(f"Welcome back, {st.session_state.user_name}!")

# Session Tracking Section
if page == "Track Hours":
    if 'user_id' in st.session_state:
        st.header("Session Tracking")

        # Start Session Section
        if st.button("Start Session"):
            session_id = start_session(st.session_state.user_id)
            st.success(f"Session started with Session ID: {session_id}")

        # End Session Section
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
        active_sessions = sessions_collection.find({"user_id": st.session_state.user_id, "end_time": None})
        for session in active_sessions:
            st.write(f"Session ID: {session['_id']}, Start Time: {session['start_time']}")
    else:
        st.error("Please log in to track hours.")
=======
# Add User Section
st.header("Add a New User")
name = st.text_input("Name")
email = st.text_input("Email")
netID = st.text_input("NetId")
if st.button("Add User"):
    if name and email:
        user_id = add_user(name, email, netID)
        st.success(f"User {name} added with ID: {user_id}")
    else:
        st.error("Please provide both name and email.")

# # Start Session Section
# st.header("Start a Session")
# user_id = st.text_input("User ID to Start Session")
# if st.button("Start Session"):
#     if user_id:
#         session_id = start_session(user_id)
#         st.success(f"Session started for User ID {user_id} with Session ID: {session_id}")
#     else:
#         st.error("Please provide a valid User ID.")

# # End Session Section
# st.header("End a Session")
# session_id = st.text_input("Session ID to End")
# if st.button("End Session"):
#     if session_id:
#         hours_logged = end_session(session_id)
#         if hours_logged:
#             st.success(f"Session ended. Hours logged: {hours_logged:.2f}")
#         else:
#             st.error("Invalid Session ID or session already ended.")
#     else:
#         st.error("Please provide a valid Session ID.")

# # Show Active Sessions
# st.header("Active Sessions")
# active_sessions = sessions_collection.find({"end_time": None})
# for session in active_sessions:
#     user = users_collection.find_one({"_id": session["user_id"]})
#     st.write(f"Session ID: {session['_id']}, User: {user['name']} ({user['email']}), Start Time: {session['start_time']}")
>>>>>>> aab2206 (Working version of DB)
