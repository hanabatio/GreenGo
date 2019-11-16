from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField
from wtforms.validators import DataRequired, NumberRange, ValidationError, EqualTo, Email
from webapp.models import *


class registrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Insert')

    def validate_userid(self, uid):
        user = db.session.query(User.username).filter_by(email=uid.data).scalar()
        if user:
            raise ValidationError("Email already in system.")

class logInForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def validate_userid(self, uid, pw):
        user = db.session.query(User.username).filter_by(email=uid.data).scalar()
        if not user:
            raise ValidationError("Email not found.")
        elif user.password != password.data:
            raise ValidationError("Incorrect Password.")