from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()


class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    def get_id(self):
        return self.username


class Post(db.Document):
    title = db.StringField(required=True)
    date = db.StringField(required=True)
    content = db.StringField(required=True)
    author = db.ReferenceField(User, required=True)

    def get_title(self):
        return self.title