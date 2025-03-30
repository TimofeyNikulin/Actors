from .. import app, db, actual_user
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask import render_template, redirect
from flask_login import current_user
from ..models.company import *
from ..models.users import *


@app.route("/")
def index():
    if current_user:
        if current_user.is_authenticated:
            vacancies = db.session.scalars(sa.select(Vacancy)).all()
            return render_template("index/index.html", user=current_user, actual_user=current_user.type, vacancies=vacancies)
        else:
            return render_template("index/index.html", user=False, actual_user=current_user)
    else:
        return render_template("index/index.html", user=False, actual_user=current_user)
        