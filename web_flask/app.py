#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def fetch_index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
