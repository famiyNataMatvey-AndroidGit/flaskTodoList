from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CreateTaskForm(FlaskForm):
    task_name = StringField("Task name", validators=[DataRequired()])
    date = StringField("Date", validators=[DataRequired()])
    submit = SubmitField()
