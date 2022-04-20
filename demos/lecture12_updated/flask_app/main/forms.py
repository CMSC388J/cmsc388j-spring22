from tokenize import String
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import Length, InputRequired


class PopulateForm(FlaskForm):
    submit = SubmitField("Click here to populate the web app with data!")


class DerivativeForm(FlaskForm):
    equation = StringField(
        "Equation/Expression",
        validators=[
            InputRequired(),
            Length(min=1, message="Equation/Expression is empty!"),
        ],
    )
    variable = StringField(
        "Variable differentiating with respect to",
        validators=[
            InputRequired(),
            Length(
                min=1,
                max=1,
                message="Must be a single variable expression, i.e. 'x', 'y', etc.",
            ),
        ],
    )
    submit = SubmitField("Calculate the derivative!")
