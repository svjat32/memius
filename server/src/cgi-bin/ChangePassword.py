import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")
oldPassword = form.getvalue("oldPassword")
newPassword = form.getvalue("newPassword")

if sessionId is None or oldPassword is None or newPassword is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status})


print("Content-type: application/json")
print()
print(answer)
