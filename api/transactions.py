from api.models import User, Room

import uuid

def add_user_txn(session, name, image):
    u = User(id=str(uuid.uuid4()), name=name, image=image)
    session.add(u)
    return {
        'id': u.id,
        'name': u.name,
        'image': u.image
    }

def get_user_txn(session, id):
    u = session.query(User).filter(User.id == id).first()
    if u:
        session.expunge(u)
    return u

def get_users_txn(session, room_id):
    users = session.query(User).filter(User.room_id == room_id).all()
    return list(map(lambda user: {
        'id': user.id,
        'name': user.name,
        'image': user.image
    }, users))

def add_room_txn(session, code, user_id):
    r = Room(id=str(uuid.uuid4()), code=code, creator=user_id)
    u = session.query(User).filter(User.id == user_id).first()
    u.room = r.id
    session.add(r)
    session.add(u)
    return {
        'id': r.id,
        'code': r.code,
        'creator': r.creator
    }

def get_room_txn(session, code):
    r = session.query(Room).filter(Room.code == code).first()
    if r:
        session.expunge(r)
    return r

def add_room_user(session, room_id, user_id):
    u = session.query(User).filter(User.id == user_id).first()
    u.room = room_id
    session.add(u)
    return {
        'id': u.id,
        'name': u.name,
        'image': u.image,
        'room': u.room
    }

def remove_room_user(session, room_id, user_id):
    u = session.query(User).filter(User.id == user_id).first()
    u.room = None
    session.add(u)
    return {
        'id': u.id,
        'name': u.name,
        'image': u.image,
        'room': u.room
    }
