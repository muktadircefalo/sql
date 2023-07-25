from src.config import Base, engine
from sqlalchemy import Column, Integer,String


class Books(Base):
    __tablename__='books'
    id = Column(Integer)
    name = Column(String)

    Base.metadata.create_all(engine)