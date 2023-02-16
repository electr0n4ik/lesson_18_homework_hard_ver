# Это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.movie import Movie

# CRUD
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Получение всех фильмов.
        """
        return self.session.query(Movie).all()

    def get_one(self, mid):
        """
        Получение фильма по id.
        """
        return self.session.query(Movie).get(mid)

    def create(self, data):
        """
        Добавление.
        """
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie
    def update(self, data):
        """
        Изменение.
        """
        mid = data.get("id")
        movie = self.get_one(mid)
        movie.title = data.get("title")

        return movie

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)

        if "title" in data:
            movie.title = data.get("title")

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        """
        Удаление.
        """
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.commit()
