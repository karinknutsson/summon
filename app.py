import os, logging
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, current_user, logout_user
from functools import wraps

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config.from_object(os.environ['SECRET_KEY'])
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.logger.setLevel(logging.INFO)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from models import *
from forms import EventForm, UserForm, LoginForm


db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def requires_logged_in(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        if '_user_id' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapped_func


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/events')
@requires_logged_in
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


@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        try:
            user = User(email, password)
            db.session.add(user)
            db.session.commit()
            app.logger.info(f"Created user {user.email}")
            message = f"Thanks! User {email} has been registered."
            return render_template('message.html', message=message)
        except IntegrityError:
            message = f"User with E-mail {email} already exists, please try a different one"
            return render_template('new_user.html', form=form, message=message)
    return render_template('new_user.html', form=form)


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/user/logout')
@requires_logged_in
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
