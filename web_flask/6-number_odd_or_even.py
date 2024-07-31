#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask, render_template, request

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

@app.route('/python/<text>', strict_slashes=False, defaults={'text': 'is_cool'})
def python_with_params(text):
    """
    Display 'python' followed by the value of <text>.
    """
    text_no_underscore = text.replace('_', ' ')
    return "python {}".format(text_no_underscore)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """

    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """

    """
    return render_template('5-number.html', number=n)


    @app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
    def number_old_or_even(n):
        """
        """
        even_or_old = "even" if n % 2 == 0 else "old"
        values = {
            "number": n,
            "even_or_old": even_or_old
        }
        return render_template('6-number_odd_or_even.html', values=values)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
