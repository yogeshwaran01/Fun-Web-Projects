import base64
import io
import zlib

from PIL import Image
from flask import make_response


def compressor(sen):
    return zlib.compress(sen, 9)


def decompress(sen):
    return zlib.decompress(sen)


class Encoder:
    def __init__(self, source):
        self.source = source

    def encoded_string(self):
        with open(self.source, "rb") as img:
            encoded_string = base64.b64encode(img.read())
        return encoded_string


class Decoder:
    def __init__(self, string):
        f = io.BytesIO(base64.b64decode(string))
        self.img = Image.open(f)

    def response(self):
        buffer = io.BytesIO()
        self.img.save(buffer, format="png")
        buffer.seek(0)
        res = make_response(buffer.getvalue())
        res.mimetype = "image/png"
        return res
