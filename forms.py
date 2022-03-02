from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields import DateTimeLocalField
from wtforms.validators import DataRequired, Length


class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Cannot be blank')])
    description = TextAreaField('Description')
    startDate = DateTimeLocalField('Start time', format='%Y-%m-%dT%H:%M')
    endDate = DateTimeLocalField('End time', format='%Y-%m-%dT%H:%M')
    url = StringField('Link')
    submit = SubmitField('Submit')
