from flask import Blueprint, render_template

views = Blueprint(__name__ ,"views")


@views.route("/Alice")
def Alice():
    return render_template("Alice1.html")

@views.route("")
def Home():
    return render_template("Alice1.html")