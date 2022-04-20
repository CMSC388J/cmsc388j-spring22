from flask import Flask
from flask_talisman import Talisman
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = b"\xe6\x86\xbc\x0b\x9a4\xeb\xe4\xd2\x9d\x1b\xfaF\x11\x95q"

app.config["MONGODB_HOST"] = "mongodb://localhost:27017/wk12"

talisman = Talisman(app)
db = MongoEngine(app)
login_manager = LoginManager(app)
login_manager.login_view = "users.login"
bcrypt = Bcrypt(app)

from flask_app.main.routes import main  # Blueprint class
from flask_app.users.routes import users

app.register_blueprint(main)
app.register_blueprint(users)
