#!/usr/bin/python3
"""
 script that starts a Flask web application
"""
from flask import Flask
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a HTML page with states"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a HTML page with cities of a state"""
    state = storage.get(State, state_id)
    if state:
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
