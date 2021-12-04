import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from christmas.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

TOTAL_DAYS = 12

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        db = get_db()
        error = None

        if not email:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif password != request.form.get("password-confirm"):
            error = 'Passwords do not match.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (email, password, notes) VALUES (?, ?, ?)",
                    (email, generate_password_hash(password), "Enter notes here ...")
                )
                db.commit()
            except db.IntegrityError:
                error = f"{email} is already used"
            else:
                user_id = db.execute(
                    "SELECT id FROM user ORDER BY id DESC LIMIT 1"
                ).fetchone()
                print(user_id)
                for day_num in range(1, TOTAL_DAYS+1):
                    db.execute(
                        "INSERT INTO user_days VALUES (?, ?, ?, ?, ?)",
                        (user_id, day_num, 2+day_num, 5+day_num, day_num)
                    )
                return redirect(url_for("auth.login"))
        
        flash(error)

    return render_template('signup.html')


@bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email, )
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user['password'], password):
            error = "Incorrect password."
        
        if error is None:
            session.clear()
            session["user_id"] = user['id']
            return redirect(url_for('index'))

        flash(error)
    
    return render_template('login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', user_id
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view