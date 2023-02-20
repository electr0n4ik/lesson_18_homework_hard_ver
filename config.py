# Это файл конфигурации приложения, здесь можно хранить путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

class Config:
    """
    Конфигурация приложения
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data_base.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
