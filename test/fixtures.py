import os
import tempfile
from contextlib import contextmanager

import pytest
from flask import template_rendered

from app import app
from app import login
from app import database
from app.models.users import User
from app.models.users import Todo


@pytest.fixture
def client():
    file = tempfile.mkstemp()
    db, app.config["SQLALCHEMY_DATABASE_URI"] = file[0], "sqlite:///" + file[1] + ".db"
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            database.init_app(app)
            database.create_all()
            database.session.commit()
            login.init_app(app)
            test_user = User(username="admin", email="admin@admin.com")
            test_user.set_password("admin")
            database.session.add(test_user)
            database.session.commit()

            @login.user_loader
            def load_user(user_id):
                return User.query.get(int(user_id))

        yield client

    os.close(db)


@pytest.fixture
def authenticated_client():
    file = tempfile.mkstemp()
    db, app.config["SQLALCHEMY_DATABASE_URI"] = file[0], "sqlite:///" + file[1] + ".db"
    app.config["TESTING"] = True
    with app.test_client() as client:
        with app.app_context():
            database.init_app(app)
            database.create_all()
            database.session.commit()
            login.init_app(app)
            test_user = User(username="admin", email="admin@admin.com")
            test_user.set_password("admin")
            database.session.add(test_user)
            database.session.commit()
            test_todo_1 = Todo(task="Cooking", owner=test_user)
            test_todo_2 = Todo(task="Playing", owner=test_user)
            database.session.add(test_todo_1)
            database.session.add(test_todo_2)
            database.session.commit()
        yield client

    os.close(db)


@pytest.fixture
def simple_client():
    with app.test_client() as client:
        yield client


@contextmanager
def captured_templates():
    """ Function return the data from jinja templates """
    recorded = []

    def record(sender, template, context, **kwags):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
