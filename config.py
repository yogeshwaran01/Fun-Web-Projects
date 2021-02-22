import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Configuartion:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = "postgresql:///users"
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin"
    ADMIN_MAIL = "admin@admin.com"
    UPLOAD_DIR = base_dir + "/app/uploads"
