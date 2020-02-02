#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template, jsonify, request
from sqlalchemy import desc
from models.report import Report
from models.state import State
import models
from models import storage
from word2number import w2n


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
            .order_by(desc('updated_at')).first()
        if report is not None and report.infections > 0:
            states_affected += 1
            total_infections += report.infections
    storage.close()
    return render_template('index.html', total_states=total_states,
                           states_affected=states_affected,
                           total_infections=total_infections)


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
            .order_by(desc('updated_at')).first()
        if report is None:
            state_dict['infections'] = 0
        else:
            state_dict['infections'] = report.infections
            total_infections += report.infections
        states_list.append(state_dict)
    storage.close()
    return render_template('data.html', states=states_list, total_infections=total_infections)


@app.route('/report')
def fetch_report():
    states = storage.all(State)
    storage.close()
    return render_template("report.html", states=states)


@app.route('/send_report', methods=['POST'])
def send_report():
    state_id = request.form.get('state_id')
    check_state = storage.get('State', state_id)
    if check_state is None:
        return jsonify({'error': 'Department selected does not exist'})
    number_infections = request.form.get('number_infections')
    try:
        number_infections = w2n.word_to_num(number_infections)
        if number_infections < 0 or type(number_infections) is not int:
            raise ValueError('Invalid number')
    except:
        return jsonify({'error': 'The number you typed is invalid'})
    new_report = Report(state_id=state_id, infections=number_infections)
    new_report.save()
    storage.close()
    return jsonify({'success': 'Your data was registered correctly'})


@app.route('/states')
def show_states():
    states_list = []
    objs = storage.all()
    for obj in objs.values():
        states_list.append(obj.to_dict())
    storage.close()
    return jsonify({'states': states_list})


if __name__ == "__main__":
    app.run(debug=True)
