from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import email_validator

class RegistrationForm(FlaskForm):
    usrname = StringField('Usrname',
                    validators=[DataRequired(), Length(min=2, max=22)])
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    confirm_passwd = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo(passwd)])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')
