from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, TextField
from wtforms.validators import InputRequired, NumberRange, Length


class WelcomeForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=4, max=30)])

    location = StringField('Location', validators=[InputRequired(), Length(min=3, max=50)])

    age = IntegerField('Age', validators=[InputRequired(), NumberRange(min=1, max=140, message='Must be between 1 and 140')])

    submit = SubmitField('Submit')


class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=4, max=30)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=30)])
    status = StringField('Status', validators=[InputRequired(), Length(min=4, max=200)])
    bio = TextField('Bio', validators=[InputRequired(), Length(min=4, max=2000)])
    submit = SubmitField('Create Profile')

