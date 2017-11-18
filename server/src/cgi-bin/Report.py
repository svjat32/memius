import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")
memeId = form.getvalue("memeId")

if sessionId is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status})

print("Content-type: application/json")
print()
print(answer)
