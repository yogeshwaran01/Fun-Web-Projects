import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Configuartion:

    SECRET_KEY = "ondevolp"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'users.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin"
    ADMIN_MAIL = "admin@admin.com"
