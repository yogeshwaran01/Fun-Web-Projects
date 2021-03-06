from urllib.parse import urlparse

from flask import Blueprint
from flask import request
from flask import render_template

from app.models.image import DATABASE
from config import Configuartion

bp = Blueprint("image", __name__, url_prefix="/image")


@bp.route("/upload", methods=["GET", "POST"])
def image_upload():
    if request.method == "POST":
        file = request.files["file"]
        source = Configuartion.UPLOAD_DIR + f"/{file.filename}"
        file.save(source)
        code = DATABASE.store_image(source)
        host_components = urlparse(request.host_url)
        host_base = host_components.scheme + "://" + host_components.netloc
        return render_template(
            "image.html",
            url=f"{host_base}/image/{code}",
            message="Image uploaded Sucessfully",
        )
    return render_template(
        "image.html", title="Free Image Hosting", images=DATABASE.get_all_images()
    )


@bp.route("/<code>")
def render_image(code):
    return DATABASE.get_image_from_shortcode(code)
