from flask import Blueprint,render_template

student = Blueprint("student", __name__ , static_folder="static", template_folder="templates")

@student.route("/")
def home():
    return render_template("home.html")

@student.route("/mark")
def mark():
    return render_template("mark.html")

@student.route("/timetable")
def timetable():
    return render_template("timetable.html")

@student.route("/assignment")
def assignment():
    return render_template("assignment.html")
