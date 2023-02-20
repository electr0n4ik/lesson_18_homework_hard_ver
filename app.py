from flask_restx import Api
from flask import Flask
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config):
    """
    Создание приложения
    """
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application):
    """
    Конфигурация приложения
    """
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


def create_data(app, db):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app(Config)

    app.run(host="localhost", port=10001, debug=True)
