import firebase_admin
from firebase_admin import credentials, db, firestore
import json
from datetime import datetime
from Person import Person
from faceData import *
cred_obj = credentials.Certificate('storeDB.json')
databaseURL = 'https://storelytics-app-default-rtdb.firebaseio.com/'

default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': databaseURL
})

time_in_name = 'time_in'
time_out_name = 'time_out'
id_name = 'id'

realtime_db = db.reference("/Customers")
db = firestore.client()
# data = {'time_in': "07/27/2022 06:53PM", "time_out": "07/27/2022 06:56PM"}


def enter_user(count: int) -> str:
    data = {
        time_in_name: datetime.now().strftime('%m/%d/%Y %I:%M %p'),
        time_out_name: None,
        id_name: count
    }
    data = json.dumps(data)
    new_post = realtime_db.push(data)
    return new_post.key

def leave_user(key: str, meta):
    ref = realtime_db.child(key)
    user = json.loads(ref.get())
    ref.delete()
    user[time_out_name] = datetime.now().strftime('%m/%d/%Y %I:%M %p')
    user['race'] = meta.dominant_race
    user['emotion'] = meta.dominant_emotion
    user['gender'] = meta.gender
    db.collection('customers').add(user)


def get_difference(key: str):
    time_out = datetime.strptime(
        realtime_db.get()[key][time_out_name], '%m/%d/%Y %I:%M %p')
    time_in = datetime.strptime(
        realtime_db.get()[key][time_in_name], '%m/%d/%Y %I:%M %p')
    difference = time_out - time_in

    return difference.total_seconds() / 60

def get_user(key : str):
    return realtime_db.get()[key]

def get_data():
    customers = db.collection('customers').stream()
    data = {}
    for customer in customers:
        data[customer.id] = customer.to_dict()
    return data
