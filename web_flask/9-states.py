#!/usr/bin/python3
"""
flask web application listening on 0.0.0.0 port 5000 listing all states and associated cities
Routes:
    /states: render html with the list of all states
    /states/<id>: render state object
"""

from flask import Flask
from models import storage
from flask import render_templtate


@app.route('/states', strict_slashes=False)
def states_list():
    """render html with list of all states and associated cities"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """render html with info of an id if it exists"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
        return render_template("9-states.html")



@app.teardown_appcontext
def cleanup_db(exception):
    """remove current session after each request"""
    storage.close()


if __name__ == "__main__":
    """by default listening on 0.0.0.0, port=5000"""
    app.run()
