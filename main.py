from src.config.config import SQLConnection
from src.config import logger
engine = SQLConnection.engine_instance()
logger.info('Instance created')

from src.tables.user.user import User
from src.tables.books.books import Books

books = Books(
    name='BB1',
    year=2023,
    published='NUN'
)
logger.info(engine)
user = User(
    name='HI1'
)
logger.debug(books.as_dict())
b = Books()
b.save(data=[books.as_dict()])
logger.debug(user.as_dict())
u = User()
# u.save(data=[user.as_dict()])

