import cgi
import json
import sqlite3
import DefUserId


form = cgi.FieldStorage()

session_id = form.getvalue("SessionId")

answer = {}

if session_id is None:
    answer["Status"] = "Failure"
else:
    try:
        user_id = DefUserId.GetUserIdBySessionId(session_id)

        #TODO: Write code here

        # connection = sqlite3.connect("ServerDB.db")
        # cursor = connection.cursor()
        # cursor.execute("SELECT Id FROM Users WHERE Username = ? AND Password = ?", (username, password))
        # user_id = int(*(cursor.fetchall()[0]))
        #
        # cursor.execute("INSERT INTO Sessions (Id, User_id, Start_time, End_time) VALUES (?, ?, ?, ?)",
        #                (str(session_id), user_id, str(start_time), str(end_time)))
        # connection.commit()
        # connection.close()


        answer["Status"] = "Success"
        # container = {}
        # container["Likes"] = likes
        # container["dislikes"] = dislikes
        # answer["Container"] = container
    except:
        answer["Status"] = "Failure"


print("Content-type: application/json")
print()
print(json.dumps(answer))













try:
    answer["Status"] = "Success"
    container = {}
    container["Likes"] = likes
    container["dislikes"] = dislikes
    answer["Container"] = container
except:
    answer["Status"] = "Failure"
