from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'user': 'Nikolay Pomytkin',
        'text': 'I like cycling!',
        'location': 'New York',
        'likes': 2,
    },
    {
        'user': 'Not Nikolay',
        'text': 'Nikolay\'s opinions are lame',
        'location': 'College Park',
        'likes': 5
    }
]


@app.route('/')
def hello():
    return render_template('base.html')


@app.route('/feed')
def feed():
    return render_template('posts.html', posts=posts, title='The Feed')


@app.route('/u/<username>')
def profile(username):
    return f'This is {username}\'s user profile'
