from db import db
from flask import session

def get_comments():
    sql = "SELECT C.content, C.sent_at, U.username FROM comments C, users U WHERE C.user_id = U.id AND C.location_id = :location_id"

def add_comment(content, user_id, location_id):
    sql = "INSERT INTO comments (content, user_id, location_id) VALUES (:content, :user_id, :location_id)"
    db.session.execute(sql, {"content": content, "user_id": user_id, "location_id": location_id})
    db.session.commit()
    return True