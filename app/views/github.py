from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from app.utils.github_utils import UserStats
from app.utils.plots import pie_chart

bp = Blueprint("github", __name__, url_prefix="/github")


@bp.route("/<username>")
def github_stats_render(username):
    possible_query = [
        "repos_per_langs",
        "star_per_langs",
        "commit_per_repo",
        "star_per_repo",
    ]
    query = request.args.get("q")
    user = UserStats(username)
    if query in possible_query:
        data = user.__getattribute__(query)()
        return pie_chart(data, query)
    links = [f"/github/{username}?q={i}" for i in possible_query]
    return render_template(
        "github.html", name=user.name, links=links, title=user.name, stats=user.stats()
    )


@bp.route("/", methods=["GET", "POST"])
def home_render():
    if request.method == "POST":
        username = request.form.get("username")
        return redirect(url_for("github.github_stats_render", username=username))
    return render_template("github_index.html")
