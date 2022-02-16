from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/my_database"
app.config['SECRET_KEY'] = 'test132'


mongo = PyMongo(app)

from app.routes import *