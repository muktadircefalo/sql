from src.config import Base, engine
from sqlalchemy import Column, Integer,String


class Books(Base):
    __tablename__='books'
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    def as_dict(self):
        """Convert object to dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


Base.metadata.create_all(engine)