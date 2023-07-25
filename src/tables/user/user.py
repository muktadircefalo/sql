from src.config import Base, engine
from sqlalchemy import Column, Integer,String


class User(Base):
    __tablename__='users'
    id = Column(Integer)
    name = Column(String)

    Base.metadata.create_all(engine)