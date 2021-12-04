from flask import Blueprint, render_template, request

bp = Blueprint('day', __name__)

@bp.route('/day/<day_num>', methods=['GET', 'POST'])
def day(day_num):
    
    return render_template('day.html',
        logged_in=False,

        day_num=str(day_num),
        day_image="/static/santa/snowman.png",

        movie_name="Santa Claus: The Movie",
        movie_link="",
        movie_img="/static/movies/1-santa-claus-the-movie.jpg",
        movie_descrip="The legend of Santa Claus is put in jeopardy when an\
            unscrupulous toy manufacturer attempts to take over Christmas.",

        recipe_name="Soft Chrismas Cookies",
        recipe_link="https://duckduckgo.com/?t=ffab",
        recipe_img="/static/recipes/1-soft-christmas-cookies.jpg",
        recipe_descrip="Soft cut out sugar cookie that I have used for years. \
            I sprinkle with colored sugar before baking or you could also try \
            icing them when cool.",

        song_name="Happy Xmas",
        song_artists="Name of Singer People",
        song_link="https://duckduckgo.com/?t=ffab",
        song_img="/static/song-img/1-placeholder.jpg",
        song_mp3="/static/song-mp3/Happy Xmas (War Is Over).mp3",

        notes="Lorem ipsum notenotenotenotenotenotenotenotenos"
    )