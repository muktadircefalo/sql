from src.config import Base, engine
from src.db.load.load import load_to_db
from sqlalchemy import Column, Integer,String, PrimaryKeyConstraint


class Books(Base):

    __tablename__='books'

    name = Column(String, nullable=False, primary_key=True)
    published = Column(String, nullable=False, primary_key=True)
    year = Column(Integer, nullable=False)
    writer = Column(String, nullable= False)
    __table_args__ = (
        PrimaryKeyConstraint(name, published),
        {'schema': 'public'},
    )


    def as_dict(self):
        """Convert object to dictionary"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def save(self,data):
        load_to_db(self,data_record=data)


Base.metadata.create_all(engine)