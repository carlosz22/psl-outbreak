#!/usr/bin/python3
""" holds class Report"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey


class Report(BaseModel, Base):
    """Representation of a report"""
    __tablename__ = 'reports'
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    infections = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes report"""
        super().__init__(*args, **kwargs)
