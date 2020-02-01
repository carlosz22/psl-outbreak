#!/usr/bin/python3
""" holds class State"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Representation of State """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    reports = relationship("Report", backref="state", cascade="delete")

    def __init__(self, *args, **kwargs):
        """initializes State"""
        super().__init__(*args, **kwargs)
