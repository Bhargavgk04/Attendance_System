import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendance-b877a-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "852741":
        {
            "name": "Emly Blunt",
            "branch": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "Grade": "G",
            "year": 2,
            "last_attendance_time": "06-03-2024 09:11:00"
        },
    "963852":
        {
            "name": "Elon Musk",
            "branch": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "Grade": "G",
            "year": 3,
            "last_attendance_time":  "06-03-2024 09:11:00"
        },
    "143911":
        {
            "name": "Bhargav Katkam",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 7,
            "Grade": "A",
            "year": 2,
            "last_attendance_time": "07-03-2024 09:11:00"

        },
    "230405":
        {
            "name": "Rohit Shalgar",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 0,
            "Grade": "B+",
            "year": 2,
            "last_attendance_time": "07-03-2024 09:11:00"
        },
    "191804" :
        {
            "name": "Yash Waghmare",
            "branch": "CSE",
            "starting_year": 2022,
            "total_attendance": 0,
            "Grade": "B+",
            "year": 2,
            "last_attendance_time": "07-03-2024 09:11:00"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
    