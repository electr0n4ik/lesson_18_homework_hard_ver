# Здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки).
# Сюда импортируются сервисы из пакета service

# Пример
from flask_restx import Resource, Namespace

book_ns = Namespace('books')


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201
