#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask
from model import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """display HTML page"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
