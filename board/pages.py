from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("pages/home.html")
@bp.route("/itilcert")
def itilcert():
    return render_template("pages/itilcert.html")
@bp.route("/projects")
def projects():
    return render_template("pages/projects.html")
# @bp.route("/recommendations")
# def recommendations():
#     return render_template("pages/recommendations.html")
# @bp.route("/about")
# def about():
#     return render_template("pages/about.html")
