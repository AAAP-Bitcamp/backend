from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ == 'users'
    id = Column(UUID, primary_key=True)
    name = Column(String)
    image = Column(String)
    room = Column(UUID, ForeignKey('rooms.id'))


class Room(Base):
    __tablename__ == 'rooms'
    id = Column(UUID, primary_key=True)
    code = Column(String, index=True)
    creator = Column(UUID, ForeignKey('users.id'))