from flask import Flask, render_template, request, url_for, redirect, flash, session, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    message = "Welcome to the application!"
    sites = ["Parthenon", "Colosseum", "Olympia"]
    return render_template("index.html", message=message, items=sites)

@app.route("/map", methods=["GET", "POST"])
def my_maps():
    mapbox_access_token = "pk.eyJ1IjoibnBhYSIsImEiOiJjbDV3bHpmMjYwNmQ5M29vYXMydGJjczl4In0.vJQwW2jPoaSZWSzHDy3pNw"

    return render_template("map.html", mapbox_access_token=mapbox_access_token)

@app.route("/create_user")
def create_user():
    return render_template("create_user.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", name=request.form["username"], email=request.form["email"])

@app.route("/create_location")
def create_location():
    return "Tämä on sijainti-sivu"

@app.route("/site/<int:id>")
def site(id):
    return "Tämä on sivu, jonka id on " + str(id)

if __name__ == '__main__':
    app.run(debug=True)