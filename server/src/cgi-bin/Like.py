import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("SessionId")
memeId = form.getvalue("Int")

if sessionId is None or memeId is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status})

print("Content-type: application/json")
print()
print(answer)
