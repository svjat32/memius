import cgi
import json
import sqlite3
import datetime

form = cgi.FieldStorage()

session_id = form.getvalue("SessionId")
meme_id = form.getvalue("MemeId")

answer = {}

if session_id is None or meme_id is None:
    answer["Status"] = "Failure"
else:
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    date_and_time = datetime.datetime(year, month, day, hour, minute, second)
    try:
        connection = sqlite3.connect("ServerDB.db")
        cursor = connection.cursor()

        cursor.execute("SELECT User_id FROM Sessions WHERE Id = ?", (session_id,))
        user_id = int(cursor.fetchone()[0])

        #TODO: Check dislikes

        cursor.execute("INSERT INTO Likes (Meme_id, User_id, Date_and_time) VALUES (?, ?, ?)", (meme_id, user_id, date_and_time))

        connection.commit()
        connection.close()

        answer["Status"] = "Success"
    except:
        answer["Status"] = "Failure"


print("Content-type: application/json")
print()
print(json.dumps(answer))
