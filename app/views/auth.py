from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user

from app.models.users import DB
from app.models.users import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("todo.todo_index"))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return render_template("login.html", message="Username Not Found")
        login_user(user)
        return redirect(url_for("todo.todo_index"))

    return render_template("login.html", title="Login")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        if username in DB.all_users():
            return render_template(
                "register.html", title="Register", message="Username Already Found"
            )
        if email in DB.all_email():
            return render_template(
                "register.html", title="Register", message="Email Already Found"
            )
        DB.add_user(username, password, email)
        return render_template("login.html", message="Register Sucessfully")
    return render_template("register.html", title="Register")


@bp.route("/logout")
def logout():
    logout_user()
    return render_template("index.html", message="Logout Sucessfully")
