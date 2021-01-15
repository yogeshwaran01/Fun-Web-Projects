from flask_login import current_user

from .fixtures import authenticated_client
from .fixtures import captured_templates


def test_todo(authenticated_client):
    authenticated_client.post(
        "/auth/login",
        data=dict(username="admin", password="admin"),
        follow_redirects=True,
    )

    response = authenticated_client.get("/todo/", follow_redirects=True)

    assert "Cooking" in current_user.todos[0].task


def test_add_todo(authenticated_client):
    authenticated_client.post(
        "/auth/login",
        data=dict(username="admin", password="admin"),
        follow_redirects=True,
    )

    response = authenticated_client.post(
        "/todo/task/add", data=dict(task="Driving"), follow_redirects=True
    )
    assert "Driving" in current_user.todos[2].task
    assert len(current_user.todos) == 3


def test_remove_todo(authenticated_client):
    authenticated_client.post(
        "/auth/login",
        data=dict(username="admin", password="admin"),
        follow_redirects=True,
    )

    response = authenticated_client.get(
        "/todo/task/remove", data=dict(task="Driving"), follow_redirects=True
    )
    assert len(current_user.todos) == 2
