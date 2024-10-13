from flask import Flask, render_template, request
from pymongo import MongoClient
from bson import ObjectId
import time

app = Flask(__name__)

client = MongoClient("mongodb+srv://test_user1:test_user1@cluster0.7wn3d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['library']
users_collection = db['hour_tracker']
users_collection.create_index("NetID", unique=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        netID = request.form['netID']

        user = users_collection.find_one({"NetID": netID})
        if user:
            return "User already exists. Please login."
        else:
            user_data = {"Name": name, "NetID": netID, "Student Email": email, "clock_in_status": False}
            result = users_collection.insert_one(user_data)
            return f"User {name} added with ID: {result.inserted_id}"

    return render_template('add_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        netID = request.form['netID']
        user = users_collection.find_one({"NetID": netID})
        if user:
            return render_template('clock_in_out.html', user_id=str(user['_id']))
        else:
            return f"NetID: {netID} does not exist. Please sign up."

    return render_template('login.html')

@app.route('/clock_in/<user_id>')
def clock_in(user_id):
    user_obj_id = ObjectId(user_id)
    time1 = time.time()
    new_field = {"$set": {"clock_in": time1, "clock_in_status": True}}
    users_collection.update_one({"_id": user_obj_id}, new_field)
    return "Clocked In successfully."

@app.route('/clock_out/<user_id>')
def clock_out(user_id):
    user_obj_id = ObjectId(user_id)
    time2 = time.time()
    new_field = {"$set": {"clock_out": time2, "clock_in_status": False}}
    users_collection.update_one({"_id": user_obj_id}, new_field)
    return "Clocked Out successfully."

if __name__ == '__main__':
    app.run(debug=True)