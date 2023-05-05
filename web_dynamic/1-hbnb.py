#!/usr/bin/python3
"""This function starts a flask web application"""
import os
import uuid
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

# Create the Flask application
app = Flask(__name__)

# Define a function to be called when the application context is popped
@app.teardown_appcontext
def close_db(error):
    """ Closes the database connection at the end of a request. """
    storage.close()

# Define a route for the '/0-hbnb/' URL
@app.route('/1-hbnb/', strict_slashes=False)
def hbnb():
    """ Renders a template with data from the database. """
    # Get all states from the database and sort them alphabetically
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)

    # Get all amenities from the database and sort them alphabetically
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    # Get all places from the database and sort them alphabetically
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    # Group states and cities together
    st_ct = []
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    # Generate a unique cache ID for the request
    cache_id = str(uuid.uuid4())

    # Render the template with the data and cache ID
    return render_template('1-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)

# Define the main function
def main():
    """ Runs the Flask application. """
    # Get the host and port from environment variables, or use default values
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)

    # Start the Flask application
    app.run(host=host, port=port, debug=True)

# If this script is being run as the main program, call the main function
if __name__ == '__main__':
    main()
