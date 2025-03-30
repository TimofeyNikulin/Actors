from .. import app, db, actual_user
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask import render_template, redirect
from flask_login import current_user
from ..models.company import *
from ..models.users import *


@app.route("/vacancy/<id>")
def vacancy(id):
    vacancy = db.session.scalars(sa.select(Vacancy).where(Vacancy.id == id)).first()
    return render_template("/workpage/vacancy.html", vacancy=vacancy)