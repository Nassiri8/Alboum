from sqlalchemy import Column, DateTime, String, Integer, func, Float, Boolean  

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Items(Base):  
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    type = Column(String)
    price = Column(Float)
    is_offer = Column(Boolean)

    def __repr__(self):
        return 'id: {}, name: {}'.format(self.id, self.name)