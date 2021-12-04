from flask import (
    Blueprint, g, redirect, render_template, request, session, url_for
)

from christmas.db import get_db

bp = Blueprint('internal', __name__, url_prefix='/api')

@bp.route('/movie', methods=["GET", "POST"])
def add_item():
    if request.method == "GET":
        return render_template("movie_update.html")
    if request.method == "POST":
        movie = {}
        movie["title"] = request.form.get("movie-title")
        movie["description"] = request.form.get("movie-desc")
        movie["link"] = request.form.get("movie-link")
        movie["img"] = request.form.get("movie-img")
    
    