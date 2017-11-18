import cgi
import json

form = cgi.FieldStorage()

sessionId = form.getvalue("getSessionId")
memeId = form.getvalue("memeId")
if sessionId is None or memeId is None:
    status = "Failure"
else:
    status = "Success"

answer = json.dumps({"Status": status, "Container": {"AuthorId": "Int",
                                                     "Comment": "String",
                                                     "DataAndTime": "String",
                                                     }})

print("Content-type: application/json")
print()
print(answer)
