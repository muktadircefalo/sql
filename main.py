from src.config.config import SQLConnection
from src.config import logger
engine = SQLConnection.engine_instance()
logger.info('Instance created')
