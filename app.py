import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config.from_object(os.environ['SECRET_KEY'])
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from models import *
from forms import EventForm


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/events')
def all_events():
    events = Event.query.all()
    return render_template('events.html', events=events)


@app.route('/events/<event_id>')
def show_event(event_id):
    event = Event.query.get(event_id)
    return render_template('event.html', event=event)


@app.route('/new', methods=['GET', 'POST'])
def new_event():
    form = EventForm()
    if request.method == 'POST' and form.validate_on_submit():

        # get values from form
        name = request.form['name']
        description = request.form['description']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        url = request.form['url']
        record = Event(url, startDate, endDate, name, description)

        # add record to database
        db.session.add(record)
        db.session.commit()

        # create a message to send to the template
        message = f"Thanks! The data for {name} has been submitted."
        return render_template('message.html', message=message)

    elif request.method == 'POST':
        message = "Oops! Something went wrong."
        return render_template('message.html', message=message)

    return render_template('new_event.html', form=form)


@app.route('/edit/<event_id>', methods=['GET', 'POST', 'PUT'])
def edit_event(event_id):
    form = EventForm()
    event = Event.query.get(event_id)

    # add event properties to form
    form.name.data = event.name
    form.description.data = event.description
    form.startDate.data = event.startDate
    form.endDate.data = event.endDate
    form.url.data = event.url

    if request.method == 'POST' and form.validate_on_submit():

        # add values submitted to form to event
        event.name = request.form['name']
        event.description = request.form['description']
        event.startDate = request.form['startDate']
        event.endDate = request.form['endDate']
        event.url = request.form['url']

        # save changes in database
        db.session.add(event)
        db.session.commit()

        message = "Your event has been updated."
        return render_template('message.html', message=message)

    elif request.method == 'POST':
        message = "Oops! Something went wrong."
        return render_template('message.html', message=message)

    return render_template('edit_event.html', event_id=event_id, form=form)


@app.route('/delete/<event_id>', methods=['GET', 'DELETE'])
def delete_event(event_id):
    event = Event.query.get(event_id)
    db.session.delete(event)
    db.session.commit()
    if Event.query.get(event_id):
        message = "Something went wrong."
    else:
        message = "The event has been deleted."
    return render_template('message.html', message=message)


if __name__ == '__main__':
    app.run()
