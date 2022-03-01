from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields import DateTimeLocalField
from wtforms.validators import DataRequired, Length

class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Cannot be blank')])
    description = StringField('Description')
    startDate = DateTimeLocalField('Start time', validators=[DataRequired(message='Cannot be blank')])
    endDate = DateTimeLocalField('End time', validators=[DataRequired(message='Cannot be blank')])
    url = StringField('URL')
    submit = SubmitField('Submit')
