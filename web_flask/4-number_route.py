#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, on the default port: 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB!'
    /c/<text>: Displays its own bla bla bla'
    /python/<text>: Displays its own bla bla bla'
    /number/<n>: Displays its own bla bla bla'
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
    return "HBNB!"


@app.route("/c/<string:text>", strict_slashes=False)
def hello_hbnb3(text="cool"):
    """Displays specified message"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def hello_hbnb4(text="is cool"):
    """Displays specified message"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def hello_hbnb5(n):
    """Displays specified message"""
    try:
        return "{} is a number".format(int(n))
    except ValueError:
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
