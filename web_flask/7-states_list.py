#!/usr/bin/python3
"""
flask web application listening on 0.0.0.0 port 5000 listing all states
Routes:
    /states_list: render html with the list of all states
"""

from flask import Flask
from models import storage
from flask import render_templtate


@app.route('/states_list', strict_slashes=False)
def states_list():
    """render html with list of all states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def cleanup_db(exception):
    """remove current session after each request"""
    storage.close()


if __name__ == "__main__":
    """by default listening on 0.0.0.0, port=5000"""
    app.run()
