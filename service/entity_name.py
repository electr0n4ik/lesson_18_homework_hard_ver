# Здесь бизнес логика, в виде классов или методов, сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from marshmallow.fields import List

from dao.entity_name import BookDAO


# Пример

class BookService:

    def __init__(self, book_dao: BookDAO):
        self.book_dao = book_dao

    def get_books(self) -> List["Book"]:
        return self.book_dao.get_books()
