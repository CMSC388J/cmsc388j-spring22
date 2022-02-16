from app import app, mongo
from flask import render_template, redirect, request, session, url_for
from app.forms import *


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
            mongo.db.profiles.insert_one(new_profile)
            print(list(mongo.db.profiles.find()))
            return redirect(url_for('profile'))
        else:
            print('validation failed')
    profiles = mongo.db.profiles.find()
    print(type(profiles))
    return render_template('profile.html', profiles=profiles, form=form)


@app.route('/profile/<username>')
def view_profile(username):
    profile = mongo.db.profiles.find_one({'username': username})
    if profile: 
        return render_template('user_profile.html', profile=profile)
    return redirect(url_for('profile'))



@app.route('/dummy_test_db')
def test_db():
    new_profile = {
        'name': 'test',
        'username': 'test',
        'status': 'test',
    }
    mongo.db.profiles.insert_one(new_profile)
    return redirect(url_for('profile'))