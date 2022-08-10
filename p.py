from flask import Flask, flash, redirect, render_template, request, url_for,session
from datetime import timedelta
from teacher.teacher import teacher 
from student.student import student

app = Flask(__name__)  
app.register_blueprint(teacher, url_prefix="/teacher")
app.register_blueprint(student, url_prefix="/student")
app.secret_key = "hello"     
app.permanent_session_lifetime = timedelta(minutes = 5)

@app.route("/")
def home():
    return render_template("homee.html")
    
@app.route("/user")
def user():
    if "user" in session:
        session.permanent = True
        user = session["user"]
        return render_template("userr.html", user = user)
    else:
        flash("not logged in ")
        return redirect(url_for("login"))
    
@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        flash("Login succesfull")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Aldready logged in ")
            return redirect(url_for("user"))
        else:
            flash("Enter details to login ")
            return render_template("loginn.html")

@app.route("/logout")
def logout():
    if "user" in session:
        flash("you have been logged out", "info")
        session.pop("user", None)
        return redirect(url_for("login"))
    else:
        flash("please login first")
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)
