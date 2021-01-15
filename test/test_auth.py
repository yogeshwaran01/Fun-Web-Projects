from .fixtures import client


def test_login(client):
    response = client.post(
        "/auth/login",
        data=dict(username="admin", password="admin"),
        follow_redirects=True,
    )
    assert b"TODO" in response.data


def test_logout(client):
    client.post(
        "/auth/login",
        data=dict(username="admin", password="admin"),
        follow_redirects=True,
    )
    response = client.get("/auth/logout", follow_redirects=True)
    assert b"Login" in response.data


def test_register(client):
    response = client.post(
        "/auth/register",
        data=dict(username="test", password="test", email="test@test.com"),
        follow_redirects=True,
    )
    assert b"Sign in" in response.data
