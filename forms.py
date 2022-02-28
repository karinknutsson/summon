from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    startDate = DateTimeField('Start time', validators=[DataRequired()])
    endDate = DateTimeField('End time', validators=[DataRequired()])
    url = StringField('URL')
    submit = SubmitField('Submit')
