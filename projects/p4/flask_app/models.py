from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    pass


class User(db.Document, UserMixin):
    pass

    # Returns unique string identifying our object
    def get_id(self):
        pass


class Review(db.Document):
    pass
