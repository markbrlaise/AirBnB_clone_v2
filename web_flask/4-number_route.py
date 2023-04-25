#!/usr/bin/python3
"""
starts a flask web application
listening on port 5000 at localhost
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Displays C <text>
    /python/<text>: Displays Python <text> or Python is cool by default
    /number/<n>: Display <n> is a number only if its an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display c <text>"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text='is_cool'):
    """Displays Python <text>"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """Display if n is an integer"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
