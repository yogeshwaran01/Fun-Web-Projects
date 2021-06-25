from flask import Blueprint, redirect, request, render_template

from app.utils.utils import generate_seq
from urllib.parse import urlparse

bp = Blueprint("redirecter", __name__, url_prefix="/redirecter")


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("link")
        times = request.form.get("times")
        host_components = urlparse(request.host_url)
        host_base = host_components.scheme + "://" + host_components.netloc
        return render_template(
            "redirecter.html",
            url=f"{host_base}/redirecter/redirect?link={link}&times={times}",
            title="Redirecting Tool",
        )
    return render_template("redirecter.html", title="Redirecting Tool")


@bp.route("/redirect")
def redirecter():
    link = request.args.get("link")
    times = request.args.get("times")

    return redirect(f"redirecting?link={link}&times={times}")


@bp.route("/<fake>")
def fake_router(fake):
    link = request.args.get("link")
    times = int(request.args.get("times"))

    if times == 1:
        return redirect(link)

    else:
        times = times - 1
        code = generate_seq()

        return redirect(f"{code}?times={times}&link={link}")
