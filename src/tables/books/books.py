from src.config import Base, engine
from src.db.load.load import load_to_db
from sqlalchemy import Column, Integer,String


class Books(Base):
    __tablename__='books'
    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    def as_dict(self):
        """Convert object to dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save(self,data):
        load_to_db(self,data_record=data)


Base.metadata.create_all(engine)