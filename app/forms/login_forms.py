from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginUser(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")
    

class LoginCompany(FlaskForm):
    email_company = StringField("Email", validators=[DataRequired()])
    password_company = StringField("Пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")