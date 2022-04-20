from bs4 import BeautifulSoup
from flask import render_template, request, Blueprint, redirect, url_for, flash
import plotly.graph_objects as go
import requests
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, diff, latex

from collections import Counter
import io
import random
import string

from .forms import DerivativeForm, PopulateForm
from ..models import User


main_bp = Blueprint("main_bp", __name__)


def populate_sample_data():
    usernames = [
        "USERNAME",
        "PASSWORD",
        "EMAIL",
        "CAPTCHA",
        "REQUESTS",
        "SECLISTS",
        "PYTHON",
        "FLASK",
        "JAVASCRIPT",
        "HTML",
        "CSS",
    ]

    pop = string.ascii_letters

    for _ in range(50):
        rand_user = "".join(random.choices(pop, k=random.randint(8, 25)))
        usernames.append(rand_user)

    for name in usernames:
        user = User(username=name)
        user.save()


@main_bp.route("/", methods=["GET", "POST"])
def index():
    form = PopulateForm()
    if form.validate_on_submit():
        num_users = User.objects().count()

        if num_users == 0:
            populate_sample_data()

            flash("Populated the database with sample data!")
        else:
            flash("Database is already filled with sample data!")

    return render_template("index.html", title="Home", form=form)


# Note: should use the DELETE http method normally
@main_bp.route("/clear_db", methods=["GET"])
def clear_db():
    User.drop_collection()

    flash("Cleared the database!")

    return redirect(url_for("main_bp.index"))


@main_bp.route("/plotly")
def plotly():
    users = User.objects()

    names_string = "".join(user.username for user in users)
    frequencies = list(names_string)

    fig = go.Figure(data=[go.Histogram(x=frequencies)])
    f = io.StringIO()
    fig.write_html(f)

    return render_template("plot.html", plot=f.getvalue())


@main_bp.route("/dummy_request")
def dummy_request():
    r = requests.post("https://httpbin.org/post", data={"key": "value"})

    return render_template("dummy_request.html", title="Dummy Request", response=r)


# Note: not necessarily an equation; the string might just be an expression.
@main_bp.route("/derivative", methods=["GET", "POST"])
def derivative():
    form = DerivativeForm()
    if form.validate_on_submit():
        eq_str = form.equation.data
        try:
            equation = parse_expr(eq_str)
            var = symbols(form.variable.data)
        except Exception as e:
            flash(f"Received error when processing your input: {str(e)}")
            return render_template("sympy.html", form=form)

        result = latex(diff(equation, var))
        return render_template("sympy.html", form=form, derivative=result)

    return render_template("sympy.html", form=form)


# Note: requires a lot more processing to be nice to see/use for a real website
@main_bp.route("/table-parser")
def table_parser():
    url = "https://en.wikipedia.org/wiki/List_of_most-streamed_artists_on_Spotify"
    resp = requests.get(url)
    content = resp.content

    root = BeautifulSoup(content, "html.parser")
    tables = root.find_all("table")

    return render_template("table_parser.html", tables=tables)


@main_bp.route("/about")
def about():
    return render_template("about.html", title="About")
