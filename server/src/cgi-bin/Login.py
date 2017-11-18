import cgi
import json
import sqlite3
import datetime
import uuid

form = cgi.FieldStorage()

username = form.getvalue("Username")
password = form.getvalue("Password")
remember_me = form.getvalue("RememberMe") in ['true', '1', 't', 'y', 'yes', 'True', 'TRUE']

answer = {}

if username is None or password is None or remember_me is None:
    answer["Status"] = "Failure"
else:
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second

    start_time = datetime.datetime(year, month, day, hour, minute, second)

    if remember_me == True:
        end_time = datetime.datetime(year + 100, month, day, hour, minute, second)
    else:
        end_time = datetime.datetime(year, month, day + 2, hour, minute, second)

    session_id = uuid.uuid4()
    try:
        connection = sqlite3.connect("ServerDB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT Id FROM Users WHERE Username = ? AND Password = ?", (username, password))
        user_id = int(*(cursor.fetchall()[0]))

        cursor.execute("INSERT INTO Sessions (Id, User_id, Start_time, End_time) VALUES (?, ?, ?, ?)",
                       (str(session_id), user_id, str(start_time), str(end_time)))
        connection.commit()
        connection.close()
    except:
        answer["Status"] = "Failure"
    else:
        answer["Status"] = "Success"

print("Content-type: application/json")
print()
print(json.dumps(answer))
