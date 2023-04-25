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
    /number_template/<n>: render html only if n is an integer
"""
from flask import Flask
from flask import render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """render html only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """render html only if n an integer and showing whether its even or odd"""
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    decision = "{} is {}".format(n, odd_or_even)
    return render_template("6-number_odd_or_even.html", decision=decision)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
