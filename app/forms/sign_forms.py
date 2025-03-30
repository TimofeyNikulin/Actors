from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class SignUser(FlaskForm):
    surname = StringField("Фамилия", validators=[DataRequired()])
    username = StringField("Имя", validators=[DataRequired()])
    patronymic = StringField("Отчество", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Пароль", validators=[DataRequired()])
    

class SignCompany(FlaskForm):
    companyname = StringField("Название компании", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Пароль", validators=[DataRequired()])