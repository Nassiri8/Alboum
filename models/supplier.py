from sqlalchemy import Column, DateTime, String, Integer, func  

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Suppliers(Base):  
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    siret = Column(String)

    def __repr__(self):
        return 'id: {}, siret: {}'.format(self.id, self.siret)