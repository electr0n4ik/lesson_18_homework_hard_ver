# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

# Например

class BookDAO:
    def get_all_books(self):
        books = Book.query.all()
        return