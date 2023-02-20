# Здесь бизнес логика, в виде классов или методов, сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from dao.movie import MovieDAO


class MovieService:
    """
    Сервис для работы с фильмами
    """
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_all(self):
        """
        Получение всех фильмов
        """
        return self.movie_dao.get_all()

    def get_one(self, mid):
        """
        Получение одного фильма
        """
        return self.movie_dao.get_one(mid)

    def create(self, data):
        """
        Добавление фильма в базу данных
        """
        return self.movie_dao.create(**data)

    def update(self, mid, data):
        """
        Обновление информации о фильме
        """
        return self.movie_dao.update(mid, data)

    def get_by_args(self, args):
        """
        Метод для получения всех фильмов по выбранным параметрам
        """
        return self.movie_dao.get_by_args(**args)

    def delete(self, mid):
        """
        Удаление фильма из базы данных
        """
        return self.movie_dao.delete(mid)
