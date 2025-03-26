from .. import app, db
from ..models.users import User
from ..forms.sign_forms import SignUser
from flask import render_template, redirect


def create_user(name, email, password):
    user = User(username=name, email=email, password_hash=password)
    db.session.add(user)
    db.session.commit()


@app.route("/sign_up", methods=["get", "post"])
def sign_up():
    form = SignUser()
    if form.validate_on_submit():
        print(form.email.data)
        return
    return render_template("user/sign_up.html", form=form)