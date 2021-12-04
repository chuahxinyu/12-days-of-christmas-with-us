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
                    (movie["title"], movie["description"],
                     movie["img"], movie["link"])
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


@bp.route('/song', methods=["GET", "POST"])
def add_song():
    db = get_db()
    if request.method == "POST":
        song = {}
        song["title"] = request.form.get("song-title")
        song["artist"] = request.form.get("song-art")
        song["img"] = request.form.get("song-img")
        song["link"] = request.form.get("song-mp3")

        error = None

        if not (song["title"] and song["artist"] and song["img"] and song["link"]):
            error = "Something is missing"

        if error is None:
            print(song)
            try:
                db.execute(
                    "INSERT INTO songs (title, artist, img, link) VALUES (?, ?, ?, ?)",
                    (song["title"], song["artist"], song["img"], song["link"])
                )
                db.commit()
            except db.IntegrityError:
                error = f"{song['title']} is already used "
            else:
                return redirect(url_for("internal.add_song"))

        flash(error)

    songs = db.execute("SELECT * FROM songs").fetchall()
    for song in songs:
        print(song[0])

    return render_template("songs_update.html", songs=songs)


@bp.route('/recipe', methods=["GET", "POST"])
def add_recipe():
    db = get_db()
    if request.method == "POST":
        recipe = {}
        recipe["title"] = request.form.get("recipe-title")
        recipe["description"] = request.form.get("recipe-desc")
        recipe["link"] = request.form.get("recipe-link")
        recipe["img"] = request.form.get("recipe-img")

        error = None

        if not (recipe["title"] and recipe["description"] and recipe["img"] and recipe["link"]):
            error = "Something is missing"

        if error is None:
            print(recipe)
            try:
                db.execute(
                    "INSERT INTO recipes (name, description, img, external_link) VALUES (?, ?, ?, ?)",
                    (recipe["title"], recipe["description"],
                     recipe["img"], recipe["link"])
                )
                db.commit()
            except db.IntegrityError:
                error = f"{recipe['title']} is already used "
            else:
                return redirect(url_for("internal.add_recipe"))

        flash(error)

    recipes = db.execute("SELECT * FROM recipes").fetchall()
    for recipe in recipes:
        print(recipe[0])

    return render_template("recipe_update.html", recipes=recipes)
