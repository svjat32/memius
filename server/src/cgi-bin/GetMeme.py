import cgi
import json
import sqlite3
import DefUserId


form = cgi.FieldStorage()

session_id = form.getvalue("SessionId")
meme_id = form.getvalue("MemeId")

answer = {}

if session_id is None or meme_id is None:
    answer["Status"] = "Failure"
else:
    try:
        user_id = DefUserId.GetUserIdBySessionId(session_id)

        connection = sqlite3.connect("ServerDB.db")
        cursor = connection.cursor()

        cursor.execute("SELECT Meme, Date_and_time FROM Memes WHERE Id = ?", (meme_id,))

        for d in cursor.fetchall():
            date_and_time = str(d[1])
            results = bytearray(d[0])
            meme = ""
            for c in results:
                meme = meme + chr(c)


        cursor.execute("SELECT * FROM Likes WHERE Meme_id = ?", (meme_id,)).rowcount
        like_count = len(cursor.fetchall())

        cursor.execute("SELECT * FROM Dislikes WHERE Meme_id = ?", (meme_id,))
        dislike_count = len(cursor.fetchall())

        connection.commit()
        connection.close()

        answer["Status"] = "Success"
        container = {}
        container["AuthorId"] = user_id
        container["DateAndTime"] = date_and_time
        container["LikeCount"] = like_count
        container["DislikeCount"] = dislike_count
        container["Meme"] = meme
        answer["Container"] = container
    except:
        answer["Status"] = "Failure"


print("Content-type: application/json")
print()
print(json.dumps(answer))
