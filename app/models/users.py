from datetime import datetime

from app import database as db
from app import login
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    """
    Database Model for Table Users
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    todos = db.relationship("Todo", backref="owner")

    def set_password(self, password: str):
        """ Set the hashed password for the user """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        """ Check the users password """
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        """ True, as all users are active. """
        return True

    def get_id(self):
        """ Return the email address to satisfy Flask-Login's requirements. """
        return self.id

    def is_authenticated(self):
        """ Return True if the user is authenticated. """
        return self.authenticated

    def is_anonymous(self):
        """ False, as anonymous users aren't supported. """
        return False

    def __repr__(self):
        return f"{self.username} -> {self.email}"

    def remove_todo(self, task: str):
        """ Remove Todo from the user """
        for i in self.todos:
            if i.task == task:
                db.session.delete(i)
                db.commit()
            else:
                continue

    def add_todo(self, task: str):
        """ Add Todo to the user """
        td = Todo(task=task, owner=User.query.filter_by(username=self.username).first())
        db.session.add(td)
        db.session.commit()


class Todo(db.Model):
    """
    Database Model for Table Todos of Users
    """

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"{self.task}"


@login.user_loader
def load_user(id):
    """ Function for load User for Login """
    return User.query.get(int(id))


class DB:

    """ Class for Handel the Database Quickly """

    @staticmethod
    def add_user(username: str, password: str, email: str):
        usr = User(username=username, email=email)
        usr.set_password(password)
        db.session.add(usr)
        db.session.commit()

    @staticmethod
    def add_todo(username: str, task: str):
        td = Todo(task=task, owner=User.query.filter_by(username=username).first())
        db.session.add(td)
        db.session.commit()

    @staticmethod
    def remove_todo(username: str, task: str):
        u = User.query.filter_by(username=username).first()
        for i in u.todos:
            if i.task == task:
                db.session.delete(i)
                db.session.commit()
            else:

                continue

    @staticmethod
    def list_todo(username: str):
        u = User.query.filter_by(username=username).first()
        return list(u.todos)

    @staticmethod
    def all_users():
        return [i.username for i in User.query.all()]

    @staticmethod
    def all_email():
        return [i.email for i in User.query.all()]
