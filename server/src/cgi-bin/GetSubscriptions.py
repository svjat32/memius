import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")

if sessionId is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status, "UserId": []})


print("Content-type: application/json")
print()
print(answer)
