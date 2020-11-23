from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea


class SubForm(FlaskForm):
    name = StringField(validators=[DataRequired()], render_kw={
                       'Placeholder': 'Name'})
    email = StringField(validators=[DataRequired(), Email()], render_kw={
                        'Placeholder': 'Email'})
    message = TextAreaField(
        render_kw={'Placeholder': 'Message', "rows": 5})
    submit = SubmitField('Submit')
