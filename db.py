import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from datetime import datetime

cred_obj = firebase_admin.credentials.Certificate('storeDB.json')
databaseURL = 'https://storelytics-app-default-rtdb.firebaseio.com/'

default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': databaseURL
	})
ref = db.reference("/")

ref = db.reference("/Customers")
# push data into database
# with open("test.json", "r") as f:
# 	file_contents = json.load(f)
# for key, value in file_contents.items():
#     print(value)

# access individual users using id
# print(ref.get()['-N80tiay7lpOT-at_CvE']['time_in']) 


def enterUser():
	data = {
		
			'time_in': datetime.now().strftime('%m/%d/%Y %I:%M%p'),
			'time_out': None
		}
	data = json.dumps(data, indent = 2)
	ref.push().set(data)

# modify entry of specific customer using their key to access the data
def leaveUser(key):
	time_in = json.loads(ref.get()[key])['time_in']
	user = ref.child(key)
	user.update({'time_in': time_in, 'time_out' : datetime.now().strftime('%m/%d/%Y %I:%M%p')})

def getDifference(key):
	time_out = datetime.strptime(ref.get()[key]['time_out'], '%m/%d/%Y %I:%M%p')
	time_in = datetime.strptime(ref.get()[key]['time_in'], '%m/%d/%Y %I:%M%p')
	difference = time_out - time_in

	return difference.total_seconds() / 60


print('yes')
