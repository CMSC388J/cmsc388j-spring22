from datetime import datetime
from flask import current_app
from . import db


class User(db.Document):
    username = db.StringField(required=True, unique=True)
