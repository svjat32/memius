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
                                                     "Meme": "Binary",
                                                     "DataAndTime": "String",
                                                     "LikeCount": "Int",
                                                     "DislikeCount": "Int"
                                                     }})

print("Content-type: application/json")
print()
print(answer)
