from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name')
    last_name = StringField('Last Name')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), 
        ('other', 'Other')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
            'Repeat Password', validators=[DataRequired(),
                EqualTo('password')])
    submit = SubmitField('Request Password Reset')
