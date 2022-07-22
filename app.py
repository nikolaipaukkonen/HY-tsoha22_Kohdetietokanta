from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy

MAPBOX_TOKEN = ""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///kohdetietokanta'
db = SQLAlchemy(app)

@app.route("/")
def index():
    message = "Welcome to the application!"
    sites = ["Parthenon", "Colosseum", "Olympia"]
    return render_template("index.html", message=message, items=sites)

@app.route("/map", methods=["GET", "POST"])
def my_maps():
    mapbox_access_token = MAPBOX_TOKEN
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