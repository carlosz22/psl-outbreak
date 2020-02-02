#!/usr/bin/python3
"""
Populates the database with necessary data
"""

from flask import Flask, render_template, jsonify
from models.report import Report
from models.news import News
from models.state import State
import models
from models import storage




first_state = storage.session.query(State).filter_by(name="Antioquia").first()
new_report = Report(infections=12, state_id=first_state.id)
print(new_report.to_dict())
print(first_state.to_dict())
storage.new(new_report)
storage.save()
print(first_state.reports)
