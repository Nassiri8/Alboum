from sqlalchemy import Column, DateTime, String, Integer, func  

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Orders(Base):  
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True)

    def __repr__(self):
        return 'id: {}, number: {}'.format(self.id, self.number)