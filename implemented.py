# Файл для создания DAO и сервисов, чтобы импортировать их везде
from dao.model.movie import MovieSchema
from dao.movie import MovieDAO
from service.movie import MovieService

from dao.model.director import DirectorSchema
from dao.director import DirectorDAO
from service.director import DirectorService

from dao.model.genre import GenreSchema
from dao.genre import GenreDAO
from service.genre import GenreService

from setup_db import db

movie_dao = MovieDAO(db.session)
movie_schema = MovieSchema(many=True)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_schema = DirectorSchema(many=True)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_schema = GenreSchema(many=True)
genre_service = GenreService(dao=genre_dao)
