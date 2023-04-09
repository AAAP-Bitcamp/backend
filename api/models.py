import face_recognition

from PIL import Image, ImageOps
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


def transform(file):
    image = Image.open(file)

    try:
        image = ImageOps.exif_transpose(image)
    except:
        print(f'Cannot perform exif transpose on file: {file}')
        pass

    image.thumbnail((800,800))
    image.save(file)


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID, primary_key=True)
    name = Column(String)
    image = Column(String)
    score = Column(Integer)
    room = Column(UUID, ForeignKey('rooms.id'))

    @staticmethod
    def verify_image(file):
        transform(file)
        image = face_recognition.load_image_file(file)
        face_encodings = face_recognition.face_encodings(image)
        return len(face_encodings) > 0
    

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(UUID, primary_key=True)
    code = Column(String, index=True)
    creator = Column(UUID, ForeignKey('users.id'))


class RoomImage(Base):
    __tablename__ = 'room_images'
    id = Column(UUID, primary_key=True)
    image = Column(String)
    room = Column(UUID, ForeignKey('rooms.id'))