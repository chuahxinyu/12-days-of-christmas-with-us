from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

from christmas.db import get_db

bp = Blueprint('internal', __name__)

@bp.route('/movie', methods=["GET", "POST"])
def add_movie():
    db = get_db()
    if request.method == "POST":
        movie = {}
        movie["title"] = request.form.get("movie-title")
        movie["description"] = request.form.get("movie-desc")
        movie["link"] = request.form.get("movie-link")
        movie["img"] = request.form.get("movie-img")

        error = None

        if not (movie["title"] and movie["description"] and movie["img"] and movie["link"]):
            error = "Something is missing"

        if error is None:
            print(movie)
            try:
                db.execute(
                    "INSERT INTO movies (title, description, img, external_link) VALUES (?, ?, ?, ?)",
                    (movie["title"], movie["description"], movie["img"], movie["link"])
                )
                db.commit()
            except db.IntegrityError:
                error = f"{movie['title']} is already used "
            else:
                return redirect(url_for("internal.add_movie"))


        flash(error)

    movies = db.execute("SELECT * FROM movies").fetchall()
    for movie in movies:
        print(movie[0])

    return render_template("movie_update.html", movies=movies)
            
    
    