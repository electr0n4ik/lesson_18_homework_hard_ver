# Здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# Сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_dao, movie_schema

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_dao.get_all()
        return movie_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_dao.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_dao.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json["id"] = mid

        movie_dao.update(req_json)

        return "", 204


    def delete(self, mid: int):
        movie_dao.delete(mid)
        return "", 204
