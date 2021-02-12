from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Configuartion

app = Flask(__name__)
app.config.from_object(Configuartion)

database = SQLAlchemy(app)
migrate = Migrate(app, database)

login = LoginManager(app)
login.login_view = "auth.login"

from .views import auth
from .views import todo
from .views import tools
from .views import fun


@app.route("/")
def index():
    return render_template("index.html", title="Home")


app.register_blueprint(auth.bp)
app.register_blueprint(todo.bp)
app.register_blueprint(tools.bp)
app.register_blueprint(fun.bp)

from .models.users import User, Todo
