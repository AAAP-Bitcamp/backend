from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ == 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    room = Column(Integer, ForeignKey('rooms.id'))


class Room(Base):
    __tablename__ == 'rooms'
    id = Column(Integer, primary_key=True)
    code = Column(String)
    creator = Column(Integer, ForeignKey('users.id'))