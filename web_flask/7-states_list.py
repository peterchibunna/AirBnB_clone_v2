#!/usr/bin/python3
""" Start Flask web app
The application listens on 0.0.0.0, on the default port: 5000.
Routes:
    /states_list: Shows the states in the db?
    """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ return list of State Objects """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(ctx):
    """ removes the current Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
