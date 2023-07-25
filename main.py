from src.config.config import SQLConnection
from src.config import logger
engine = SQLConnection.engine_instance()
logger.info('Instance created')

from src.tables.user.user import User
from src.tables.books.books import Books
from src.db.load.load import load_to_db

books = Books(
    name='booksdata'
)

user = User(
    name='HI  sss'
)
logger.debug(books.as_dict())
Books().save(data=[books.as_dict()])
logger.debug(user.as_dict())
User().save(data=[user.as_dict()])

