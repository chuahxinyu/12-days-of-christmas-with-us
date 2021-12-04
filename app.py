from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")
    print(request.method)

@app.route("/signup", methods=["GET"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    return redirect("/")