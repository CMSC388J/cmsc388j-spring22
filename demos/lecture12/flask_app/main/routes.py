from flask import render_template, request, Blueprint
from flask_app.models import Post

main = Blueprint("main", __name__)


@main.route("/")
def index():
    # posts = Post.query.all()
    posts = Post.objects()
    return render_template("index.html", title="Home", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html", title="About")
