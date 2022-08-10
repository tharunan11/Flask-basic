from flask import Blueprint,render_template,flash

teacher = Blueprint("teacher", __name__ , static_folder="static", template_folder="template")
from teacher.catalog import routes

@teacher.route("/")
def home():
    return render_template("home.html")

@teacher.route("/mark")
def mark():
    return render_template("mark.html")

@teacher.route("/timetable")
def timetable():
    return render_template("timetable.html")

@teacher.route("/assignment")
def assignment():
    return render_template("assignment.html")
