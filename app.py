from flask import Flask
from flask import render_template, request, url_for, redirect, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    message = "Welcome to the application!"
    result = db.session.execute("SELECT * FROM locations")
    sites = result.fetchall()
    return render_template("index.html", message=message, items=sites)

@app.route("/map", methods=["GET", "POST"])
def my_maps():
    mapbox_access_token = getenv("MAPBOX_TOKEN")
    # korjaa tokeni pois
    return render_template("map.html", mapbox_access_token=mapbox_access_token)

@app.route("/create_user")
def create_user():
    return render_template("create_user.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", username=request.form["username"], email=request.form["email"])

@app.route("/create_location")
def create_location():
    return "Tämä on sijainti-sivu"

@app.route("/site/<int:id>")
def site(id):
    return "Tämä on sivu, jonka id on " + str(id)

if __name__ == '__main__':
    app.run(debug=True)