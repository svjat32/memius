import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")
avatar = form.getvalue("Avatar")

if sessionId is None or avatar is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status})


print("Content-type: application/json")
print()
print(answer)
