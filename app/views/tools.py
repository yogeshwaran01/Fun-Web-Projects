from flask import Blueprint
from flask import request
from flask import render_template

from app.utils.mask_url import MaskUrl
from app.utils.mask_url import Shortner

bp = Blueprint("tools", __name__, url_prefix="/tools")


@bp.route("/maskurl", methods=["GET", "POST"])
def mask_url():
    if request.method == "POST":
        turl = request.form.get("turl")
        hurl = request.form.get("hurl")
        kw = request.form.get("kw")
        masked_url = MaskUrl(turl, hurl, kw)
        return render_template("mask_url.html", url=masked_url, title="Mask Url")
    return render_template("mask_url.html", title="Mask Url")


@bp.route("/shorturl", methods=["GET", "POST"])
def short_url():
    if request.method == "POST":
        turl = request.form.get("url")
        shorted_url = Shortner(turl)
        return render_template("short_url.html", url=shorted_url, title="Short Url")
    return render_template("short_url.html", title="Short Url")
