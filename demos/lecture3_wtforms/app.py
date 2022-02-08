from flask import Flask, render_template, redirect, request, session
from forms import *


app = Flask(__name__)

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = WelcomeForm()
    if request.method == 'POST':
        if form.validate():
            session['name'] = form.name.data
            session['location'] = form.location.data
            session['age'] = form.location.data
            session.modified = True
        else:
            print('validation failed')

        return redirect(request.path)

    message = None
    if 'name' in session:
        message = f'Welcome {session["name"]} of {session["location"]}'

    return render_template('index.html', title='Front page', message=message, form=form)
