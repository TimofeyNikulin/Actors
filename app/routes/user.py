from .. import app, db, login, actual_user
from ..models.users import User, CurriculumVitae
from ..models.company import Company, Vacancy
from ..forms.sign_forms import SignUser, SignCompany
from ..forms.login_forms import LoginUser, LoginCompany
from ..forms.add_cv_form import addCVForm
from ..forms.add_vacancy_form import addVacancyForm
from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
import sqlalchemy as sa


@login.user_loader
def load_user(id):
    global actual_user
    try:
        if actual_user == "u":
            return db.session.get(User, int(id))
        elif actual_user == "c":
            return db.session.get(Company, int(id))
    except:
        return False


@app.route("/logout")
def logout():
    global actual_user
    actual_user = ""
    logout_user()
    return redirect(url_for("index"))


def create_record(name, email, password, type, surname="", patronymic=""):
    if type == "u":
        record = User(username=name, surname=surname, patronymic=patronymic, email=email, password_hash=password)
        record.set_password(record.password_hash)
    elif type == "c":
        record = Company(companyname=name, email=email, password_hash=password)
        record.set_password(record.password_hash)
    db.session.add(record)
    db.session.commit()


def add_cv_func(body, link, user_id):
    cv = CurriculumVitae(body=body, link=link, user_id=user_id)
    db.session.add(cv)
    db.session.commit()
    
    
def add_vacancy_func(body, title, company_id):
    vacancy = Vacancy(description_of_vacancy=body, title_of_vacancy=title, company_id=company_id)
    db.session.add(vacancy)
    db.session.commit()


@app.route("/sign_up", methods=["get", "post"])
def sign_up():
    form_user = SignUser()
    form_company = SignCompany()
    if form_user.validate_on_submit():
        create_record(name=form_user.username.data, surname=form_user.surname.data, patronymic=form_user.patronymic.data, email=form_user.email.data, password=form_user.password.data, type="u")
        return redirect("/")
    if form_company.validate_on_submit():
        create_record(name=form_company.companyname.data, email=form_company.email.data, password=form_company.password.data, type="c")
        return redirect("/")
    return render_template("user/sign_up.html", form_user=form_user, form_company=form_company)


@app.route("/login", methods=["get", "post"])
def login_user_or_company():
    global actual_user
    form_user = LoginUser()
    form_company = LoginCompany()
    if form_user.validate_on_submit() or form_company.validate_on_submit():
        if form_company.email_company.data == None:
            user = db.session.scalar(sa.select(User).where(User.email == form_user.email.data))
            if user is None or not user.check_password(form_user.password.data):
                return redirect("/login")
            login_user(user)
            actual_user = "u"
            return redirect(url_for("home"))
        elif form_user.email.data == None:
            company = db.session.scalar(sa.select(Company).where(Company.email == form_company.email_company.data))
            if company is None or not company.check_password(form_company.password_company.data):
                return redirect("/login")
            login_user(company)
            actual_user = "c"
            print(actual_user)
            return redirect(url_for("home"))
    return render_template("user/login.html", form_user=form_user, form_company=form_company)


@login_required
@app.route("/lk", methods=["get", "post"])
def home():
    cv = db.session.scalar(sa.select(CurriculumVitae).where(CurriculumVitae.user_id == current_user.id))
    if cv:
        return render_template("user/lk.html", user=current_user, cv=cv)
    else:
        return render_template("user/lk.html", user=current_user, cv=False)


@login_required
@app.route("/add_cv", methods=["get", "post"])
def create_cv():
    form = addCVForm()
    if form.validate_on_submit():
        add_cv_func(body=form.body.data, link=form.link.data, user_id=current_user.id)
        return redirect(url_for("home"))
    return render_template("user/cv.html", form=form, user=current_user)


@login_required
@app.route("/add_vacancy", methods=["get", "post"])
def create_vacancy():
    form = addVacancyForm()
    if form.validate_on_submit():
        add_vacancy_func(body=form.body.data, title=form.title.data, company_id=current_user.id)
        return redirect(url_for("home"))
    return render_template("user/cv.html", form=form, user=current_user)