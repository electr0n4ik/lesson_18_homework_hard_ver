# Здесь бизнес логика, в виде классов или методов, сюда импортируются DAO классы из пакета dao
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from dao.director import DirectorDAO

class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all(self):
        return self.director_dao.get_all()

    def get_one(self, did):
        return self.director_dao.get_one(did)