#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, on the default port: 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays message at the root of the web app"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb2():
    """Displays specified message"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
