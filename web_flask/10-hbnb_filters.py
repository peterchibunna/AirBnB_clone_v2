#!/usr/bin/python3
""" Start Flask app"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ List State, City and Amenity objects from DBStorage """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """ remove the current Session  """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
