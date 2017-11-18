import cgi
import json

form = cgi.FieldStorage()

session_id = form.getvalue("SessionId")

answer = {}

if session_id is None:
    answer["Status"] = "Failure"
else:
    img_file = open("img1.png", "rb")
    img = img_file.read()
    img_file.close()

    answer["Status"] = "Success"
    container = {}
    container["AuthoorId"] = "sfeee"
    container["DateAndTime"] = "hfdhdfh"
    container["LikeCount"] = 12
    container["DislikeCount"] = 3
    container["Meme"] = str(img)
    answer["Container"] = container

print("Content-type: application/json")
print()
print(json.dumps(answer))