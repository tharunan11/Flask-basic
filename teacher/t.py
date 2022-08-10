from flask import Blueprint,render_template,flash

t = Blueprint("t", __name__ , static_folder="static", template_folder="template")

@t.route("/")
def home():
    return render_template("home.html")

@t.route("/mark")
def mark():
    return render_template("mark.html")

@t.route("/timetable")
def timetable():
    return render_template("timetable.html")

@t.route("/assignment")
def assignment():
    return render_template("assignment.html")
