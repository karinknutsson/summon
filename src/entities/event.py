# coding=utf-8

from sqlalchemy import Table, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from .entity import Entity, Base


class Event(Entity, Base):
    __tablename__ = 'events'

    name = Column(String, nullable=False)
    description = Column(String)
    dateTimeStart = Column(DateTime, nullable=False)
    dateTimeEnd = Column(DateTime, nullable=False)
    location = Column(Geometry('POINT'))
    url = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    image_file = Column(Text)

    def __init__(self, name, description, created_by):
        Entity.__init__(self, created_by)
        self.name = name
        self.description = description
        self.dateTimeStart = dateTimeStart
        self.dateTimeEnd = dateTimeEnd
        self.location = location
        self.url = url
        self.image_file = image_file

