from sqlalchemy import Column, DateTime, String, Integer, func  
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):  
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    lastname = Column(String, unique=True)
    firstname = Column(String)
    email = Column(String)
    phone = Column(String)
    password = Column(String)

    def __repr__(self):
        return 'id: {}, lastname: {}'.format(self.id, self.lastname)