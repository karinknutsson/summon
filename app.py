import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import *
from forms import *

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = EventForm()
    if form.validate_on_submit():

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
        message = f"The data for {name} has been submitted."
        return render_template('new_event.html', message=message)

    return render_template('new_event.html')


if __name__ == '__main__':
    app.run()
