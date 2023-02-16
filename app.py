# Основной файл приложения.
# Конфигурируется Flask, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# Этот файл часто является точкой входа в приложение

from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns

# функция создания основного объекта app
def create_app(config):
    """
    Создание приложения
    """
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    """
    Конфигурация приложения
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)



if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    create_app(app)
    app.run(host="localhost", debug=True)
