from app import database as db
from app.utils.utils import generate_shortcode
from app.utils.image_compress import Decoder, Encoder, decompress, compressor


class Codes(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String())
    short_code = db.Column(db.String(150))


class DATABASE:

    @staticmethod
    def get_shortcode_from_code(code):
        data = Codes.query.filter_by(code=code).first()
        return data.short_code

    @staticmethod
    def store_image(image):
        all_short_code = [i.short_code for i in Codes.query.all()]
        all_code = [i.code for i in Codes.query.all()]
        encoder = Encoder(image)
        compressed_data = compressor(encoder.encoded_string())
        if compressed_data in all_code:
            return DATABASE.get_shortcode_from_code(compressed_data)
        short_code = generate_shortcode(all_short_code)
        code = Codes(code=compressed_data, short_code=short_code)
        db.session.add(code)
        db.session.commit()

        return short_code

    @staticmethod
    def get_image_from_shortcode(code):
        data = Codes.query.filter_by(short_code=code).first()
        if data is None:
            return "404"
        decompressed_data = decompress(bytes(data.code))
        decoder = Decoder(decompressed_data)
        return decoder.response()
