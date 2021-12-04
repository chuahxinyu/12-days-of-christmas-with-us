from flask import Blueprint, render_template, request

from christmas.db import get_db

bp = Blueprint("day", __name__)

@bp.route("/day/<day_num>", methods=["GET", "POST"])
def day(day_num):

    db = get_db()
    day_info = {
        "day_num": 1,
        "img": "/static/santa/bell.png",
        "movie_id": 2,
        "song_id": 3,
        "recipe_id": 1
    }
    # db.execute(
    #     "SELECT * FROM user_days WHERE day_num = ?", (day_num)
    # ).fetchone()

    fallback_info = {
        "name": "Fallback Name",
        "title": "Fallback Title",
        "artist": "Fallback Artist",
        "link": "/static/song-mp3/1-Happy_Xmas.mp3",
        "external_link": "https://duckduckgo.com/?t=ffab",
        "img": "/static/song-img/1-Happy_Xmas_John_Lennon.jpg",
        "description": "Fallback description"
    }

    movie_info = db.execute(
        "SELECT * FROM movies WHERE id = ?", (day_info["movie_id"], )
    ).fetchone()

    if movie_info is None:
        movie_info = fallback_info

    recipe_info = db.execute(
        "SELECT * FROM recipes WHERE id = ?", (day_info["recipe_id"], )
    ).fetchone()

    if recipe_info is None:
        recipe_info = fallback_info

    song_info = db.execute(
        "SELECT * FROM songs WHERE id = ?", (day_info["song_id"], )
    ).fetchone()

    if song_info is None:
        song_info = fallback_info

    return render_template("day.html",
        logged_in=False,

        day_num=str(day_num),
        day_image=day_info["img"],

        movie_name=movie_info["title"],
        movie_link=movie_info["external_link"],
        movie_img=movie_info["img"],
        movie_descrip=movie_info["description"],

        recipe_name=recipe_info["name"],
        recipe_link=recipe_info["external_link"],
        recipe_img=recipe_info["img"],
        recipe_descrip=recipe_info["description"],

        song_name=song_info["title"],
        song_artists=song_info["artist"],
        song_mp3=song_info["link"],
        song_img=song_info["img"],

        notes="Lorem ipsum notenotenotenotenotenotenotenotenos"
        # notes = user_info["notes"]
    )