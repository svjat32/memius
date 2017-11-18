import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")
description = form.getvalue("Description")

if sessionId is None or description is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status})


print("Content-type: application/json")
print()
print(answer)
