import cgi
import json
import sqlite3

form = cgi.FieldStorage()

username = form.getvalue("Username")
password = form.getvalue("Password")

answer = {}

if username is None or password is None:
    answer["Status"] = "Failure"
else:
    try:
        connection = sqlite3.connect("ServerDB.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (username, password))
        results = cursor.fetchall()
        connection.commit()
        connection.close()
    except:
        answer["Status"] = "Failure"
    else:
        answer["Status"] = "Success"


print("Content-type: application/json")
print()
print(json.dumps(answer))