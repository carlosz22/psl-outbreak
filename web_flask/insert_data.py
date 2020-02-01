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


department_list = ["Amazonas", "Antioquia", "Arauca", "Atlantico",
                   "Bolivar", "Boyaca", "Caldas", "Caqueta", "Casanare",
                   "Cauca", "Cesar", "Choco", "Cordoba", "Cundinamarca",
                   "Guainia", "Guaviare", "Huila", "La Guajira",
                   "Magdalena", "Meta", "Nariño", "Norte de Santander",
                   "Putumayo", "Quindio", "Risaralda", "San Andres y Providencia",
                   "Santander", "Sucre", "Tolima", "Valle del Cauca",
                   "Vaupes", "Vichada"]
for obj in department_list:
    new_state = State(name=obj)
    storage.new(new_state)
storage.save()