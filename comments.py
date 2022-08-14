from db import db
from flask import session

def add(content, location_id):
    sql = "INSERT INTO comments (content, user_id, location_id, sent_at) VALUES (:content, :user_id, :location_id, NOW())"
    db.session.execute(sql, {"content": content, "user_id": session["user_id"], "location_id": location_id})
    db.session.commit()
    return True