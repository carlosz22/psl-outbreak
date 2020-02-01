#!/usr/bin/python3
""" holds class News"""
import models
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime


class News(BaseModel, Base):
    """Representation of News"""
    __tablename__ = 'last_news'
    author_name = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    short_description = Column(String(256), nullable=True, default="")
    body = Column(String(2048), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes News"""
        super().__init__(*args, **kwargs)
