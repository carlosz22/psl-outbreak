#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
