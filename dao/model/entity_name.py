# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)

# Пример

from setup_db import db

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    author = db.Column(db.String)
    year = db.Column(db.Integer)

