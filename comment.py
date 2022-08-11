from db import db
from flask import session

def get_comments():
    sql = "SELECT C.content, C.sent_at, U.username FROM comments C, users U WHERE C.user_id = U.id AND C.location_id = :location_id"
    