# Здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# Сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace
from implemented import genre_schema, genre_service, genres_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    """
    Представление для всех жанров
    """
    def get(self):
        """
        Метод для получения всех жанров
        """
        return genres_schema.dump(genre_service.get_all()), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    Представление для одного жанра
    """
    def get(self, gid):
        """
        Метод для получения одного жанра
        """
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200