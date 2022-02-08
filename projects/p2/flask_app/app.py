from flask import Flask, render_template
from model import PokeClient
app = Flask(__name__)

poke_client = PokeClient()

@app.route('/')
def index():
    """
    Must show all of the pokemon names as clickable links

    Check the README for more detail.
    """
    return render_template('index.html')

@app.route()
def pokemon_info(pokemon_name):
    """
    Must show all the info for a pokemon identified by name

    Check the README for more detail
    """
    pass

@app.route()
def pokemon_with_ability(ability_name):
    """
    Must show a list of pokemon 

    Check the README for more detail
    """
    pass
