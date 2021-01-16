from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required

from app.models.users import DB

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/", methods=["POST", "GET"])
@login_required
def todo_index():
    return render_template("todo.html", message="Logged In Sucessfully")


@login_required
@bp.route("/task/add", methods=["GET", "POST"])
def todo_add():
    if request.method == "POST":
        task = request.form.get("task")
        DB.add_todo(current_user.username, task)
        return redirect(url_for("todo.todo_index"))
    return redirect(url_for("todo.todo_index"))


@login_required
@bp.route("/task/remove")
def todo_remove():
    task = request.args.get("task")
    DB.remove_todo(current_user.username, task)
    return redirect(url_for("todo.todo_index"))
