from app import app
from flask import render_template, request, redirect
from db import db
from os import getenv
import users
import new_location

@app.route("/")
def index():
    message = "Welcome to the archaeological location application!"
    result = db.session.execute("SELECT * FROM locations")
    sites = result.fetchall()
    return render_template("index.html", message=message, items=sites)

@app.route("/new", methods=['GET'])
def new_location():
    types = db.session.execute("SELECT * FROM types")
    datings = db.session.execute("SELECT * FROM datings")
    mapbox_access_token = getenv("MAPBOX_TOKEN")
    return render_template("map.html", mapbox_access_token=mapbox_access_token, datings=datings, types=types)
    
@app.route("/send", methods=["GET", "POST"])
def send():
    #x = request.form.get("x")
    #y = request.form.get("y")
    if request.method == "POST":
        dating = request.form["datings"]
        type = request.form["types"]
        if new_location.add_location(dating, type):
            return redirect("/")
        else:
            return render_template("error.html", message="New location not added possibly due to name being already in use.")

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
