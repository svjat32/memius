import cgi
import json
import sqlite3
import datetime
import DefUserId


form = cgi.FieldStorage()

session_id = form.getvalue("SessionId")
meme = form.getvalue("Meme")

answer = {}

if session_id is None or meme is None:
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
        user_id = DefUserId.GetUserIdBySessionId(session_id)

        connection = sqlite3.connect("ServerDB.db")
        cursor = connection.cursor()

        #TODO: Form binary_meme

        for d in cursor.fetchall():
            date_and_time = str(d[1])
            results = bytearray(d[0])
            meme = ""
            for c in results:
                meme = meme + chr(c)

        binary_meme = ""
        cursor.execute("INSERT INTO Memes (User_id, Meme, Date_and_time) VALUES (?, ?, ?)", (user_id, binary_meme, str(date_and_time)))

        connection.commit()
        connection.close()

        answer["Status"] = "Success"
    except:
        answer["Status"] = "Failure"


print("Content-type: application/json")
print()
print(json.dumps(answer))
