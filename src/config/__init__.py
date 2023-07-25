from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.config.config import SQLConnection
from multiprocessing import cpu_count
from sqlalchemy_utils import database_exists, create_database
import sqlalchemy
from loguru import logger
import os
from datetime import date


# Getting cpu count
CPU_CNT = cpu_count()
Base = declarative_base()
engine = SQLConnection.engine_instance()
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)

connection = engine.connect()
metadata = sqlalchemy.MetaData()

today = date.today()
file_name = str(today.strftime("sql_db_wrapper_log_%B_%d_%Y"))+'.log'
if not os.path.exists('log'):
    os.makedirs('log')
logger.add(f"{os.getcwd()}/log/{file_name}", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")