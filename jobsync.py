from flask import Flask
from flask import render_template

app = Flask(__name__)

class Board:
    title = ""

    def __init__(self, title):
        self.title = title

boards = [
    Board("Potential"),
    Board("Applied"),
    Board("Responded"),
    Board("Interviewed")
]

@app.route("/")
def home():
    return render_template("home.html.j2", boards=boards)

@app.route("/login")
def login():
    return render_template("login.html.j2")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html.j2")

@app.route("/history")
def history():
    return render_template("history.html.j2")
