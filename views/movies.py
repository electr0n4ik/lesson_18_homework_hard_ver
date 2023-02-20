# Здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# Сюда импортируются сервисы из пакета service
import flask
from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service, movie_schema, movies_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """
        Метод для получения всех фильмов
        """
        args = flask.request.args
        if len(args):
            movies = movie_service.get_by_args(args)
            return movies_schema.dump(movies), 200
        else:
            all_movies = movie_service.get_all()
            return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):

        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
