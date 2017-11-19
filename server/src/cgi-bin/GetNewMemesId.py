import cgi
import json
import sqlite3
import DefUserId

form = cgi.FieldStorage()

session_id = form.getvalue("SessionId")

answer = {}

if session_id is None:
    answer["Status"] = "Failure"
else:

    try:
        user_id = DefUserId.GetUserIdBySessionId(session_id)
        connection = sqlite3.connect("ServerDB.db")
        cursor = connection.cursor()

        #TODO: Write right code

        # cursor.execute("SELECT Meme_id FROM Likes WHERE User_id == ?", (user_id,))
        # liked_memes = {}
        # i = 0
        # for res in cursor.fetchall():
        #     liked_memes[i] = int(res[0])
        #     i = i + 1
        #
        # cursor.execute("SELECT Meme_id FROM Dislikes WHERE User_id == ?", (user_id,))
        # disliked_memes = {}
        # i = 0
        # for res in cursor.fetchall():
        #     disliked_memes[i] = int(res[0])
        #     i = i + 1

        cursor.execute("SELECT Id FROM Memes")
        all_memes = {}
        i = 0
        for res in cursor.fetchall():
            all_memes[i] = int(res[0])
            i = i + 1

        # deleting_memes = {}
        # i = 0
        # for l in liked_memes:
        #     for dl in disliked_memes:
        #         deleting_memes[i] = l
        #         i = i + 1

        # cursor.execute("SELECT Id FROM Memes")
        # memes = {}
        # all_memes = {}
        # i = 0
        # for res in cursor.fetchall():
        #     flag1 = True
        #     flag2 = True
        #     all_memes[i] = int(res[0])
        #     for l in liked_memes:
        #         if int(res[0]) == l:
        #             flag1 = False
        #     for dl in disliked_memes:
        #         if int(res[0]) == dl:
        #             flag2 = False
        #     if flag1 == True or flag2 == True:
        #         memes[i] = int(res[0])
        #     i = i + 1

        connection.commit()
        connection.close()

        answer["Status"] = "Success"
        # answer["liked"] = liked_memes
        # answer["disliked"] = disliked_memes
        answer["Container"] = all_memes

    except:
        answer["Status"] = "Failure"

print("Content-type: application/json")
print()
print(json.dumps(answer))
