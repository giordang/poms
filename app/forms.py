from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
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


class PomsForm(FlaskForm):
    tense = SelectField('Tense', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    angry = SelectField('Angry', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    wornOut = SelectField('Worn out', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    unhappy = SelectField('Unhappy', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    proud = SelectField('Proud', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    lively = SelectField('Lively', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    confused = SelectField('Confused', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    sad = SelectField('Sad', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    active = SelectField('Active', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    onEdge = SelectField('On-edge', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    grouchy = SelectField('Grouchy', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    ashamed = SelectField('Ashamed', choices=[(104, 'Not at all'), (103, 'A little'), (102, 'Moderately'), (101, 'Quite a lot'), (100, 'Extremely')], validators=[DataRequired()], coerce=int)
    energetic = SelectField('Energetic', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    hopeless = SelectField('Hopeless', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    uneasy = SelectField('Uneasy', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    restless = SelectField('Restless', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    unableToConcentrate = SelectField('Unable to concentrate', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    fatigued = SelectField('Fatigued', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    competent = SelectField('Competent', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    annoyed = SelectField('Annoyed', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    discouraged = SelectField('Discouraged', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    resentful = SelectField('Resentful', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    nervous = SelectField('Nervous', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    miserable = SelectField('Miserable', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    confident = SelectField('Confident', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    bitter = SelectField('Bitter', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    exhausted = SelectField('Exhausted', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    anxious = SelectField('Anxious', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    helpless = SelectField('Helpless', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    weary = SelectField('Weary', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    satisfied = SelectField('Satisfied', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    bewildered = SelectField('Bewildered', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    furious = SelectField('Furious', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    fullOfPep = SelectField('Full of pep', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    worthless = SelectField('Worthless', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    forgetful = SelectField('Forgetful', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    vigorous = SelectField('Vigorous', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    uncertainAboutThings = SelectField('Uncertain about things', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    bushed = SelectField('Bushed', choices=[(100, 'Not at all'), (101, 'A little'), (102, 'Moderately'), (103, 'Quite a lot'), (104, 'Extremely')], validators=[DataRequired()], coerce=int)
    embarrassed = SelectField('Embarrassed', choices=[(104, 'Not at all'), (103, 'A little'), (102, 'Moderately'), (101, 'Quite a lot'), (100, 'Extremely')], validators=[DataRequired()], coerce=int)
    submit = SubmitField('Submit')
