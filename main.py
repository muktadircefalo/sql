from src.config.config import SQLConnection
from src.config import logger
engine = SQLConnection.engine_instance()
logger.info('Instance created')

from src.tables.user.user import User
from src.tables.books.books import Books

books = Books(
    id=1,
    name='books'
)

user = User(
    id=1,
    name='HI'
)

