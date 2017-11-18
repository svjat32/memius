import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")
userId = form.getvalue("userId")
if sessionId is None or userId is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status, "MemesId": []})


print("Content-type: application/json")
print()
print(answer)
