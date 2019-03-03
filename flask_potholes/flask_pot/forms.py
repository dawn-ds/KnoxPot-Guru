from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange


class RegistrationForm(FlaskForm):
    location = StringField('Location (Adress)',validators=[DataRequired(), Length(min=2, max=50)])
    size = FloatField('Size (approximate)') #validators=[DataRequired(), NumberRange(0,100)])
    depth = FloatField('Depth (Approximate)')#, validators=[DataRequired()])
    photo = PasswordField('Photo', validators=[DataRequired()])
    #confirm_password = PasswordField('Confirm Password',
    #                                 validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password')
    #remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
