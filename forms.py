from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields import DateTimeLocalField
from wtforms.validators import DataRequired, Length, Email


class EventForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Cannot be blank')])
    description = TextAreaField('Description')
    startDate = DateTimeLocalField('Start time', format='%Y-%m-%dT%H:%M')
    endDate = DateTimeLocalField('End time', format='%Y-%m-%dT%H:%M')
    url = StringField('Link')
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    email = StringField('E-mail', validators=[
        DataRequired(message='Cannot be blank'),
        Length(max=150),
        Email(message='Please provide a valid E-mail')
    ])
    password = StringField('Password', validators=[DataRequired(message='Cannot be blank'), Length(max=150)])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[
        DataRequired(message='Cannot be blank'),
        Length(max=150),
        Email(message='Please provide a valid E-mail')
    ])
    password = StringField('Password', validators=[DataRequired(message='Cannot be blank'), Length(max=150)])
    submit = SubmitField('Login')
