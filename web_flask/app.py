#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, jsonify
from models.report import Report
from models.news import News
from models.state import State
import models
from models import storage
app = Flask(__name__)


@app.route('/')
def fetch_index():
    return render_template('index.html')


@app.route('/states')
def show_states():
    states_list = []
    objs = storage.all()
    for obj in objs.values():
        states_list.append(obj.to_dict())
    return jsonify({'states': states_list})


@app.route('/data')
def show_data():
    states = storage.all(State)
    return render_template("data.html", states=states)


@app.route('/report')
def show_report():
    states = storage.all(State)
    return render_template("report.html", states=states)


if __name__ == "__main__":
    app.run(debug=True)
