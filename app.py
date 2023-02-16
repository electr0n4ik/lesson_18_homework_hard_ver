# Основной файл приложения.
# Конфигурируется Flask, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# Этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movie_ns

# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    """
    Конфигурация приложения
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    create_data(app, db)


# функция создания основного объекта app
def create_app(config: Config):
    """
    Создание приложения
    """
    app = Flask(__name__)
    app.config.from_object(сonfig)
    register_extensions(app)
    return app


# функция
def create_data(app, db):
    with app.app_context():
        db.create_all()
#
#         создание нескольких сущностей, чтобы добавить их в БД
#
        # with db.session.begin():
        #     db.session.add_all(здесь список созданных объектов)
#
#
app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
