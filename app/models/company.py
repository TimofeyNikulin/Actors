from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class Company(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    companyname: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    vacancies: so.WriteOnlyMapped["Vacancy"] = so.relationship(back_populates="author")
    type: so.Mapped[str] = so.mapped_column(sa.String(64), server_default="c")
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "Company {}".format(self.companyname)
    
    
class Vacancy(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title_of_vacancy: so.Mapped[str] = so.mapped_column(sa.String(64), index=True)
    description_of_vacancy: so.Mapped[str] = so.mapped_column(sa.String(256), index=True)
    company_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Company.id),
                                               index=True)
    author: so.Mapped[Company] = so.relationship(back_populates='vacancies')
    
    def __repr__(self):
        return "Vacancy {} {} {}".format(self.title_of_vacancy, self.author, self.description_of_vacancy)
    