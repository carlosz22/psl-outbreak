#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from urllib.parse import urlparse
from os import environ
from models.base_model import Base
from models.state import State
from models.report import Report
from models.news import News
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"State": State, "Report": Report, "News": News}


class DBStorage:
    """interacts with the MySQL database"""
    __engine = None
    session = None

    def __init__(self):
        """Instantiate a DBStorage object"""

        MYSQL_URL = getenv('CLEARDB_DATABASE_URL')
        self.__engine = create_engine('mysql+mysqldb://{}'.
                                      format(MYSQL_URL[7:]))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.session.close()

    def get(self, cls, id):
        """return a count of objects within a class"""
        if cls is None or id is None:
            return None
        obj = self.session.query(classes[cls]).get(id)
        return obj

    def count(self, cls=None):
        """return a count of objects within a class"""
        count = 0
        if cls is None:
            for clss in classes.keys():
                count += self.session.query(classes[clss]).count()
        else:
            count = self.session.query(classes[cls]).count()
        return count
