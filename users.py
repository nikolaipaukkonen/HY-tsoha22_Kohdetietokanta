from db import db
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def login(username, password):
    sql_command = "SELECT id, password, admin FROM users WHERE username=:username"
    result = db.session.execute(sql_command, {"username": username})
    user = result.fetchone()

    if not user:
        return False
    else: 
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["admin"] = user.admin
            session["csrf_token"] = secrets.token_hex(16)
            print(session["csrf_token"])
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username, password, admin):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, admin) VALUES (:username,:password, :admin)"
        db.session.execute(sql, {"username":username, "password":hash_value, "admin":admin})
        db.session.commit()
    except:
        return False
    return login(username, password)

def user_id():
    return session.get("user_id", 0)