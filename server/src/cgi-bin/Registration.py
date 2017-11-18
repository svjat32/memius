import cgi
import json

form = cgi.FieldStorage()

username = form.getvalue("Username")
password = form.getvalue("Password")

if username is None or password is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status})

print("Content-type: application/json")
print()
print(answer)