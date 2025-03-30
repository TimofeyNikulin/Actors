from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class addVacancyForm(FlaskForm):
    title = StringField("Название вакансии", validators=[DataRequired()])
    body = TextAreaField("Описание вакансии", validators=[DataRequired()])