from db import db
from flask import session
import users

def add_location(name, dating, type, x, y):
    try:
        user_id = users.user_id()
        print("Test")
        print("Input:", name, dating, type, x, y)
        print("New location created by user", user_id)
        sql = "INSERT INTO locations (name, dating_id, type_id, createdby_id) VALUES (:name, :dating_id, :type_id, :user_id);"
        db.session.execute(
            sql, 
            {"name":name, 
            "dating_id":int(dating[1]), 
            "type_id":int(type[1]), 
            "user_id":session["user_id"]})
        db.session.commit()
        location_fetch = db.session.execute("SELECT id FROM locations WHERE name = :name", {"name": name})
        location_id = location_fetch.fetchone()
        print(location_id)
        db.session.execute("INSERT INTO coordinates (x, y, location_id) VALUES (:x, :y, :location_id);", {"x":x, "y":y, "location_id":location_id[0]})
        db.session.commit()
        return True
    except:
        return False
