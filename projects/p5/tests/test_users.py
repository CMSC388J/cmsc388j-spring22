from flask import session, request
import pytest

from types import SimpleNamespace

from flask_app.forms import RegistrationForm
from flask_app.models import User


def test_register(client, auth):
    """ Test that registration page opens up """
    resp = client.get("/register")
    assert resp.status_code == 200

    response = auth.register()

    assert response.status_code == 200
    user = User.objects(username="test").first()

    assert user is not None


@pytest.mark.parametrize(
    ("username", "email", "password", "confirm", "message"),
    (
        ("test", "test@email.com", "test", "test", b"Username is taken"),
        ("p" * 41, "test@email.com", "test", "test", b"Field must be between 1 and 40"),
        ("username", "test", "test", "test", b"Invalid email address."),
        ("username", "test@email.com", "test", "test2", b"Field must be equal to"),
    ),
)
def test_register_validate_input(auth, username, email, password, confirm, message):
    if message == b"Username is taken":
        auth.register()

    response = auth.register(username, email, password, confirm)

    assert message in response.data


def test_login(client, auth):
    """ Test that login page opens up """
    resp = client.get("/login")
    assert resp.status_code == 200

    auth.register()
    response = auth.login()

    with client:
        client.get("/")
        assert session["_user_id"] == "test"


@pytest.mark.parametrize(("username", "password", "message"), ())
def test_login_input_validation(auth, username, password, message):
    assert False


def test_logout(client, auth):
    assert False


def test_change_username(client, auth):
    assert False


def test_change_username_taken(client, auth):
    assert False


@pytest.mark.parametrize(
    ("new_username",), 
    (
    )
)
def test_change_username_input_validation(client, auth, new_username):
    assert False
