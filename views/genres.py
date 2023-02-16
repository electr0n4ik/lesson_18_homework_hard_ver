# Здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# Сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace
from implemented import genre_dao, genre_schema

genre_ns = Namespace('genres')

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_dao.get_all()
        return genre_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        genre = genre_dao.get_one(gid)
        return genre_schema.dump(genre), 200
