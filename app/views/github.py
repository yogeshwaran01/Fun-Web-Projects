from flask import Blueprint
from flask import render_template
from flask import render_template_string
from flask import request
from flask import jsonify

from app.utils.github_utils import UserStats
from app.utils.plots import pie_chart

bp = Blueprint("github", __name__, url_prefix="/github")

@bp.route("/<username>")
def github_stats_render(username):
    possible_query = ['repos_per_langs', 'star_per_langs', 'commit_per_repo', 'star_per_repo']
    query = request.args.get('q')
    user = UserStats(username)
    if query in possible_query:
        data = user.__getattribute__(query)()
        return pie_chart(data, query)

    return jsonify(user.stats())
