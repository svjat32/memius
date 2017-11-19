import sqlite3

def GetUserIdBySessionId(session_id):
    connection = sqlite3.connect("ServerDB.db")
    cursor = connection.cursor()

    cursor.execute("SELECT User_id FROM Sessions WHERE Id = ?", (session_id,))
    user_id = int(cursor.fetchone()[0])

    connection.commit()
    connection.close()
    return user_id