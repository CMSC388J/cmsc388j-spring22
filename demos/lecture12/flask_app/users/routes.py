from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_mongoengine import MongoEngine
from flask_login import login_user, current_user, logout_user, login_required

from .. import bcrypt
from ..models import User, Post
from .forms import RegistrationForm, LoginForm, UpdateForm

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    return "Register"


@users.route("/login", methods=["GET", "POST"])
def login():
    return "Login"


@users.route("/logout")
def logout():
    return "Logout"


@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    return "Account"


@users.route("/user/<username>")
def user_detail(username):
    return "User detail"
