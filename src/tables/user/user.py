from src.config import Base, engine
from sqlalchemy import Column, Integer,String, PrimaryKeyConstraint
from src.db.load.load import load_to_db


class User(Base):

    __tablename__ = 'users'

    name = Column(String, primary_key=True,nullable=False)
    age = Column(Integer, nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(name),
        {'schema': 'public'},
    )


    def as_dict(self):
        """Convert object to dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save(self, data):
        load_to_db(self, data_record=data)


Base.metadata.create_all(engine)