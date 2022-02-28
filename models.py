from app import db


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), nullable=True)
    startDate = db.Column(db.DateTime(), nullable=False)
    endDate = db.Column(db.DateTime(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text())

    def __init__(self, url, startDate, endDate, name, description):
        self.url = url
        self.startDate = startDate
        self.endDate = endDate
        self.name = name
        self.description = description


    def __repr__(self):
        return '<id {}>'.format(self.id)
