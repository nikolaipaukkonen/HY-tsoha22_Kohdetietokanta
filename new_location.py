from db import db
from flask import session
import users

def add_location(name, dating, type):
    #try:
        user_id = users.user_id()
        print("Test")
        print("Input:", name, dating, type)
        #print(type(dating))
        print("New location created by user", user_id)
        sql = "INSERT INTO locations (name, dating_id, type_id) VALUES (:name, :dating_id, :type_id)"
        db.session.execute(sql, {"name":name, "dating_id":int(dating[1]), "type_id":int(type[1])})
        db.session.commit()
        return True
    #except:
        #return False
