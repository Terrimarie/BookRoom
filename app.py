import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from os import path
if os.path.exists("env.py"):
    import env 


app = Flask(__name__)

app.config["DB_NAME"] = "book_room"
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_books")
def get_books():
    return render_template("books.html", books=mongo.db.books.find())


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/browse")
def browse():
    return render_template("browse.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", '0.0.0.0'),
            port=int(os.environ.get("PORT", '5000')),
            debug=True)
            