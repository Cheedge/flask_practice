from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    usrname = StringField('Usrname',
                    validators=[DataRequired(), Length(min=2, max=22)])
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    confirm_passwd = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('passwd')])
    submit = SubmitField('Sign up')

   # def validate_field(self, field):
    def validate_usrname(self, usrname):
        user = User.query.filter_by(username=usrname.data).first()
        if user:
            raise ValidationError('username has been used, change another')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('this email has been used, change another')

class LoginForm(FlaskForm):
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')
