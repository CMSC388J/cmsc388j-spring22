from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Create extension objects
db = MongoEngine()

# import blueprints
from .main.routes import main_bp

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py", silent=False)

    # initialize extensions
    db.init_app(app)

    app.register_blueprint(main_bp)

    return app
