from src.config import Base, engine
from sqlalchemy import Column, Integer,String


class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String,nullable=False)

    def as_dict(self):
        """Convert object to dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)