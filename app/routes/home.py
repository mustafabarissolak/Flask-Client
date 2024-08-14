from flask import render_template, Blueprint

API_BASE_URL = "http://127.0.0.1:5000/"

home_bp = Blueprint("home_bp", __name__)


@home_bp.route("/")
def home():
    return render_template("home.html")
