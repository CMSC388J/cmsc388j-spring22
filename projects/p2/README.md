# P2: First Flask App - Poke-Info

**Assigned**: Week 2, February 3rd, 2022

**Due**: Week 4, February 15th, 2022, 11:59 PM

**Late Deadline**: Friday, February 18th, 11:59 PM

## Description

You will be creating a website allowing users to pick a Pokemon and get more info
about the pokemon, as well as to see which pokemon have a certain ability.

## Setup

We recommend using the same virtual environment for all projects, so you can
use a common one created in `CMSC388J-spring22/`, the root of the class repository.

Once you have a virtual environment, activate it,
use the appropriate command for your system.
Then, to install the necessary packages, navigate to
`p2/` and run `pip3 install -r requirements.txt`.

Alternatively: `pip3 install Flask requests python-dotenv`.

More detail on virtual environments are on the slides.

For this project, we'll be using the `requests`, `Flask`, and `python-dotenv`
packages. If you ran the above command to install from `requirements.txt`, 
you're all set.

## Project

The project will not run in its starter form, because not all of the routes
have been configured yet. To run your project after making some progress, refer to the
[Testing](#testing) section below.

In `model.py`, we've defined a class named `PokeClient`. In `app.py`, we create
an instance of the class. This is the only instance of the class that you need.
You **should not** modify the `PokeClient` class. Look at the methods in the 
class definition; you can call these methods with dot syntax, i.e. `poke_client.get_pokemon_list()`
or `poke_client.get_pokemon_info(self, 'bulbasaur')`.

In `model.py`, we've included sample usages of the `PokeClient` class. If you run
the `model.py` class directly with `python model.py`, you'll see the output
corresponding to each `print` statement in your console.

We provided a `base.html` file from which *you should extend all* of your other templates.
There's an example `index.html` file that just displays `"Poke-Info website!"` when
the website is first opened. 

You should create two more templates (so you will have a total of four HTML templates when
the project is finished) for the Pokemon info and ability info pages. These pages
are explained below.

Implement the following functions with the corresponding routes:

1. `index()` - Should show a list of all Pokemon, with links to pages that give more info

    The list of pokemon should be seen at the route `/`.

    Each element in the list should be a link to another page which will give more info about
    the chosen Pokemon with a certain name.
    The additional Pokemon info page should be located at `/pokemon/<pokemon_name>`.

    You can get a list of Pokemon names with the `get_pokemon_list()` method of the 
    `PokeClient` class.

2. `pokemon_info(pokemon_name)` - Should show all info about the specified Pokemon. 

    We should be able to navigate to `/pokemon/<pokemon_name>` and see info about the Pokemon
    identified by `pokemon_name`. The info includes the name, weight, and other data. 
    
    The `get_pokemon_info()` method of the `PokeClient` class returns a dictionary with all of 
    the info that you need. The dictionary of info will have a list of names of abilities.
    Each of these abilities must be presented as a clickable link to another page,
    located at `/ability/<ability_name>`.

    There should be a clearly visible link to go back to the front-page of the website, located
    at `/`.

3. `pokemon_with_ability(ability_name)` - Should show a list of Pokemon who have the specified 
    ability.

    We should be able to navigate to `/ability/<ability_name>` and see a list of Pokemon names
    identifying Pokemon that have the ability specified by `ability_name`.
    
    The `get_pokemon_with_ability()` method of
    the `PokeClient` class returns a list of Pokemon names with the ability. The list of
    Pokemon names should be presented as a series of clickable links that will take the 
    website user to the info page for that Pokemon, located at `/pokemon/<pokemon_name>`.

    There should be a clearly visible link to go back to the front-page of the website, located
    at `/`.

**Reminder:** Make lists in HTML by using what we went over in class.

All the tools and functions you need are imported or provided in the code 
and specified in the slides. Please refer to the week 2 lecture materials 
to see examples of how to
render templates, call functions, create links, and etc.

## Testing

When your current directory is `flask_app/`, you can simply run the command `flask run`
in your terminal or command line to see your website. It's **important** to
be in the `flask_app/` directory so that you can use the values set in the
`.flaskenv` file automatically.

The `.flaskenv` file makes it so that you don't have to set the `FLASK_APP` environment variable
manually and the environment is set to development so that errors will be shown
in the browser instead of crashing your app. 

Additionally, if you reload the page when in the development mode, you can see the
changes made to your website without having to manually shut down the running app and
restarting it.

Run your flask app, make sure you have a long list of Pokemon names that are links, and try
clicking on some of them to see if the correct info page pops up. Try clicking on one
of the abilities under each Pokemon to see if you get working links to the Pokemon with 
that ability. Check that you have a link clearly visible on the page for Pokemon info and
ability info to go back to the frontpage of our website. 

If you check a few pokemon and abilities throughout the entire list, you should be fine, 
because its fairly certain that your logic is sound at that point.

## Submissions

Make sure that you've tested parts of your website and that links to the frontpage
exist and are clearly visible, and then zip the `flask_app/` directory. 

**The directory, along with its contents, should be zipped, not the contents of the directory.**
In other words, when we unzip your file, we should see the `flask_app/` directory. If you
have any questions on how to submit, please contact us.

If you don't submit according to the instructions above, you may lose **up to 25%** of your
score on this project.

## Grading

Please don't load all of the data when your app is starting up. You should
be calling the methods of `PokeClient` only as you need them.
If you load all of your data this way, then you
may lose **up to 25%** of your score on this project. We include this penalty
because some projects have taken a minute to load, since they were loading
everything at website startup.

After zipping, submit the zip file to the appropriate ELMS page. No test results will be shown.

Your project will be graded according to (1) correctness, and (2) robustness. Here are the **correctness** requirements:

**Correctness**:

| Requirement                                                                                                           | Points            |
| --------------------------------------------------------------------------------------------------------------------- | ----------------- |
| All Pokemon visible on front page as clickable links, with no duplicate info.                                         | 15                |
| All Pokemon info returned from the `PokeClient` class is visible on the respective info page, with no duplicate info. | 20                |
| All Pokemon names visible and presented as links to Pokemon info pages on the ability pages, with no duplicate info.  | 15                |
| Link on Pokemon and ability info pages to the front page clearly visible and works.                                   | 10                |
| Two more templates created for the Pokemon and ability info pages extending `base.html`                               | 10, (5 for each)  |
| Correct routes in app                                                                                                 | 10                |
| `url_for` used to create links and `render_template` used                                                             | 10                |
| `Jinja2` control flow statements used to dynamically create HTML in template files.                                   | 10                |

**Robustness**:

If we perform any typical user actions on the website (clicking on links, navigating to different parts of the website using links, navigating to
different parts of the website with direct URLs) and this causes a crash (a Flask error shows up on screen or the app crashes), then
you may lose **up to 50%** of your final score, depending on the severity of the error.

An example of a small error: syntax error in a Jinja template. 

An example of a large error: a view function not being configured properly.


The project will be graded out of a 100 points. You won't be graded for style, but make
sure your code is readable.
