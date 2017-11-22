import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")
userId = form.getvalue("userId")

answer = {}

if sessionId is None or userId is None:
    answer["Status"] = "Failure"
else:
    answer["Status"] = "Success"

print("Content-type: application/json")
print()
print(json.dumps(answer))
