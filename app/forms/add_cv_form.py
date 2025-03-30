from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class addCVForm(FlaskForm):
    body = TextAreaField("Опишите ваш опыт", validators=[DataRequired()])
    link = StringField("Добавьте ссылку на ваше портфолио", validators=[DataRequired()])