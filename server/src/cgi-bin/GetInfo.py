import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")

if sessionId is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"SessionId": sessionId, "Container": {"Name": "String",
                                                     "Avatar": "Binary",
                                                     "Description": "String"}})


print("Content-type: application/json")
print()
print(answer)
