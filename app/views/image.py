from urllib.parse import urlparse

from flask import Blueprint
from flask import request
from flask import render_template
from werkzeug.utils import secure_filename

from app.models.image import DATABASE
from config import Configuartion

bp = Blueprint("image", __name__, url_prefix="/image")


@bp.route("/upload", methods=["GET", "POST"])
def image_upload():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(Configuartion.UPLOAD_DIR + f"/{filename}")
        file_source = Configuartion.UPLOAD_DIR + f"/{filename}"
        code = DATABASE.store_image(file_source)
        host_components = urlparse(request.host_url)
        host_base = host_components.scheme + "://" + host_components.netloc
        return f"{host_base}/image/{code}"
    return render_template("image.html")


@bp.route("/<code>")
def render_image(code):
    return DATABASE.get_image_from_shortcode(code)
