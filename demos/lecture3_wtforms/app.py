from flask import Flask, render_template, redirect, request, session, url_for
from forms import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'test132'

app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(session)
    form = WelcomeForm()
    # if form is submitted
    if request.method == 'POST':
        if form.validate():
            session['name'] = form.name.data
            session['location'] = form.location.data
            session['age'] = form.location.data
            session.modified = True
        else:
            print('validation failed')

        return redirect(request.path)

    #any other regular request
    message = None
    if 'name' in session and session['name'] is not None:
        message = f'Welcome {session["name"]} of {session["location"]}'

    return render_template('index.html', title='Front page', message=message, form=form)


@app.route('/reset')
def reset():
    session['name'] = None
    session['location'] = None
    session['age'] = None
    session.modified = True
    print(session)
    return redirect(url_for('index'))

profiles = []

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_profile = {
                'name': form.name.data,
                'username': form.username.data,
                'status': form.status.data,
                'bio': form.bio.data
            }
            profiles.append(new_profile)
            return redirect(url_for('profile'))
        else:
            print('validation failed')
    return render_template('profile.html', profiles=profiles, form=form)


@app.route('/profile/<username>')
def view_profile(username):
    p = list(filter(lambda profile: profile['username'] == username, profiles))
    if p is not None and len(p) != 0:
        return render_template("user_profile.html", profile=p[0])
    return redirect(url_for('profile'))
