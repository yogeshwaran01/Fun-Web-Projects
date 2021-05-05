from flask import Blueprint
from flask import request
from flask import render_template
from flask import jsonify

from app.utils.flames import flames_for
from app.utils.countdown import new_year
from app.utils.countdown import india_zone
from app.utils.countdown import count_down

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


@bp.route("/new-year-countdown")
def countdown():
    return render_template("new_year.html", year=new_year)


@bp.route("/time")
def lapse():
    tz = request.args.get("tz")
    if tz is None:
        return jsonify(count_down(india_zone))
    else:
        return jsonify(count_down(tz))


@bp.route("/dice")
def dice():
    return render_template("dice.html")
