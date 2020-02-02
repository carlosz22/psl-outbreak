#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, jsonify
from models.report import Report
from models.state import State
import models
from models import storage
app = Flask(__name__)


@app.route('/')
def fetch_index():
    total_infections = 0
    total_states = 0
    states_affected = 0
    states = storage.all(State)
    for state in states.values():
        total_states += 1
        report = storage.session.query(Report).filter_by(state_id=state.id)\
            .order_by('updated_at').first()
        if report is not None and report.infections > 0:
            states_affected += 1
            total_infections += report.infections
    return render_template('index.html', total_states=total_states,
                           states_affected=states_affected,
                           total_infections=total_infections)


@app.route('/states')
def show_states():
    states_list = []
    objs = storage.all()
    for obj in objs.values():
        states_list.append(obj.to_dict())
    return jsonify({'states': states_list})



@app.route('/report')
def fetch_report():
    states = storage.all(State)
    return render_template("report.html", states=states)


@app.route('/data')
def fetch_states_list():
    states_list = []
    total_infections = 0
    states = storage.all(State)
    for state in states.values():
        state_dict = {}
        state_dict['name'] = state.name
        state_dict['id'] = state.id
        report = storage.session.query(Report).filter_by(state_id=state.id)\
            .order_by('updated_at').first()
        if report is None:
            state_dict['infections'] = 0
        else:
            state_dict['infections'] = report.infections
            total_infections += report.infections
        states_list.append(state_dict)
        print(states_list)
    return render_template('data.html', states=states_list, total_infections=total_infections)


if __name__ == "__main__":
    app.run(debug=True)
