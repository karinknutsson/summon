# coding=utf-8

from sqlalchemy import Table, Column, String, Text, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry

from .entity import Entity, Base


class Event(Entity, Base):
    __tablename__ = 'events'

    name = Column(String, nullable=False)
    description = Column(Text)
    dateTimeStart = Column(DateTime, nullable=False)
    dateTimeEnd = Column(DateTime, nullable=False)
    location = Column(Geometry('POINT'))
    url = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    image_file = Column(String)

    def __init__(self, name, description, dateTimeStart, dateTimeEnd, location, url, image_file):
        Entity.__init__(self, created_by)
        self.name = name
        self.description = description
        self.dateTimeStart = dateTimeStart
        self.dateTimeEnd = dateTimeEnd
        self.location = location
        self.url = url
        self.image_file = image_file

