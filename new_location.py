from db import db
import users

def add_location(dating, type):
    try:
        user_id = users.user_id()
        print("New location created by user", user_id)
        sql = "INSERT INTO locations (dating, type) VALUES (:dating, :type)"
        db.session.execute(sql, {"dating":dating, "type":type})
        db.session.commit()
        return True
    except:
        return False