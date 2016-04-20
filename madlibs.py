from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game', methods=['POST', 'GET'])
def show_game_form():
    """Plays game"""

    if request.method == 'POST':
        answer = request.form.get("play-game")
    else:
        answer = request.args.get("play-game")

    if answer == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():

    madlib_color = request.args.get("usercolor")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    # Use .getlist to return ALL values for the parameter "adjectives2" from multi-dict 
    adjectives2 = request.args.getlist("adjectives2")

    # HTML_files = ["madlib.html", "madlib2.html"]
    random_html = choice(["madlib.html", "madlib2.html"])
    return render_template(random_html,
                            color=madlib_color,
                            noun=noun,
                            person=person,
                            adjective=adjective,
                            adjectives2=adjectives2)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
