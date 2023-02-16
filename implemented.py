# файл для создания DAO и сервисов чтобы импортировать их везде

book_dao = BookDAO(db.session)
book_service = BookService(dao=book_dao)

review_dao = ReviewDAO(db.session)
review_service = ReviewService(dao=review_dao)