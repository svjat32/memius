import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")
newUsername = form.getvalue("newUsername")

if sessionId is None or newUsername is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status})


print("Content-type: application/json")
print()
print(answer)
