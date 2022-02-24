# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.event import Event

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
events = session.query(Event).all()

if len(events) == 0:
    # create and persist mock event
    python_event = Event("SQLAlchemy Event", "Celebrate your excitement about SQLAlchemy.", "script")
    session.add(python_event)
    session.commit()
    session.close()

    # reload events
    events = session.query(Event).all()

# show existing events
print('### Event:')
for event in events:
    print(f'({event.id}) {event.title} - {event.description}')
