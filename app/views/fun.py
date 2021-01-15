from flask import Blueprint
from flask import request
from flask import render_template

from app.utils.flames import flames_for

bp = Blueprint("fun", __name__, url_prefix="/fun")


@bp.route("/flames", methods=["GET", "POST"])
def flames():
    if request.method == "POST":
        p1 = request.form.get("p1")
        p2 = request.form.get("p2")
        result = flames_for(p1, p2)
        return render_template(
            "flames.html", game=result, title="Flames", signal=result["result"][0]
        )
        print(result["result"][0])
    return render_template("flames.html", title="Flames")
