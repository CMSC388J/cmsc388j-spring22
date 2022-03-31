from flask_app import create_app, db
from mongoengine.connection import disconnect


def test_config():
    """
    Tests whether `testing` attribute is not set by
    default and is enabled with a custom configuration
    """
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_csrf_setting():
    """ Tests whether CSRF enabled config is set properly """
    key = "WTF_CSRF_ENABLED"
    assert key not in create_app().config

    app = create_app({key: False})
    assert app.config[key] is False
