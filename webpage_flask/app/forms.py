from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    mobile = IntegerField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Message',render_kw={"rows": 10, "cols": 11}, validators=[DataRequired()])
    submit = SubmitField('Submit')
