from flask import Blueprint
from flask import request
from flask import render_template

from app.utils.mask_url import MaskUrl
from app.utils.mask_url import Shortner
from app.utils.age import parse_html_date
from app.utils.age import Age

bp = Blueprint("tools", __name__, url_prefix="/tools")


@bp.route("/maskurl", methods=["GET", "POST"])
def mask_url():
    if request.method == "POST":
        turl = request.form.get("turl")
        hurl = request.form.get("hurl")
        kw = request.form.get("kw")
        try:
            masked_url = MaskUrl(turl, hurl, kw)
            return render_template("mask_url.html", url=masked_url, title="Mask Url")
        except KeyError:
            return render_template("mask_url.html", url="Incorrect Url")
    return render_template("mask_url.html", title="Mask Url")


@bp.route("/shorturl", methods=["GET", "POST"])
def short_url():
    if request.method == "POST":
        turl = request.form.get("url")
        shorted_url = Shortner(turl)
        return render_template("short_url.html", url=shorted_url, title="Short Url")
    return render_template("short_url.html", title="Short Url")


@bp.route("/age", methods=["GET"])
def age_cal():
    date = request.args.get("date")
    if date:
        d_ = parse_html_date(date)
        return render_template(
            "age.html",
            age=Age(*d_).age(),
            title="Age Calculator",
            q="{}-{}-{}".format(*list(map(lambda x: str(x).zfill(2), d_))),
        )
    return render_template("age.html", title="Age Calculator")
