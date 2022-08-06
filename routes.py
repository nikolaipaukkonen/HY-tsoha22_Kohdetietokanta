from app import app
from flask import render_template, request, redirect
from db import db
from os import getenv
import new, users

@app.route("/")
def index():
    message = "Welcome to the application!"
    result = db.session.execute("SELECT * FROM locations")
    sites = result.fetchall()
    return render_template("index.html", message=message, items=sites)

@app.route("/new", methods=["GET", "POST"])
def new():
    mapbox_access_token = getenv("MAPBOX_ACCESS_TOKEN")
    x = request.form.get("x")
    y = request.form.get("y")
    z = request.form.get("z")
    dating = request.form["dating"]
    type = request.form["id"]
    return render_template("map.html", mapbox_access_token=mapbox_access_token)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Wrong username or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("create_user.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="User register failed")
