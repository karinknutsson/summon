import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from models import *
from forms import EventForm


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/events')
def all_events():
    events = Event.query.all()
    return render_template('events.html', events=events)


@app.route('/events/<id>')
def show_events(id):
    event = Event.query.get(id)
    return render_template('event.html', event=event)


@app.route('/create', methods=['GET', 'POST'])
def new_event():
    form = EventForm()
    if request.method == 'POST' and form.validate():

        # get values from form
        name = request.form['name']
        description = request.form['description']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        url = request.form['url']
        record = Event(url, startDate, endDate, name, description)
        print(record)

        # add record to database
        db.session.add(record)
        db.session.commit()

        # create a message to send to the template
        message = f"Thanks! The data for {name} has been submitted."
        return render_template('message.html', message=message)

    elif request.method == 'POST':
        message="Thanks! Something went wrong."
        return render_template('message.html', message=message)

    return render_template('new_event.html', form=form)


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_event(id):
    form = EventForm()
    event = Event.query.get(id)
    if request.method == 'POST':
        message="Your event has been updated."
        return render_template('message.html', message=message)

    return render_template('edit_event.html', event=event)



if __name__ == '__main__':
    app.run()
