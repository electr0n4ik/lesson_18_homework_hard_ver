# Это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.director import Director

# CRUD
class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """
        Получение всех режиссеров.
        """
        return self.session.query(Director).all()

    def get_one(self, did):
        """
        Получение режиссера по id.
        """
        return self.session.query(Director).get(did)
