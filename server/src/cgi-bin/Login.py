import cgi
import json

form = cgi.FieldStorage()

username = form.getvalue("Username")
password = form.getvalue("Password")
rememberMe = form.getvalue("Remember Me")

if username is None or password is None or rememberMe is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status, "Container": {"SessionId": "",
                                                     "StartTime": "",
                                                     "EndTime": ""}})


print("Content-type: application/json")
print()
print(answer)