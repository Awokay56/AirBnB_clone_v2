#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """
    This is the home route handler.
    """
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """

    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_with_params(text):
    """
    Display 'c' followed by the value of <text>.

    """
    text_no_underscore = text.replace('_', ' ')
    return "c ()".format(text_no_underscore)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
