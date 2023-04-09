from api.models import User, Room

import uuid

def add_user_txn(session, name, image):
    u = User(id=str(uuid.uuid4()), name=name, image=image)
    session.add(u)
    return {
        'id': str(u.id),
        'name': u.name,
        'image': u.image
    }

def get_user_txn(session, id):
    u = session.query(User).filter(User.id == id).first()
    if u:
        session.expunge(u)
    return u

def get_users_txn(session, room_id):
    users = session.query(User).filter(User.room == room_id).all()
    return list(map(lambda user: {
        'id': str(user.id),
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
        'id': str(r.id),
        'code': r.code,
        'creator': u.name
    }

def get_room_txn(session, code):
    r = session.query(Room).filter(Room.code == code).first()
    if r:
        session.expunge(r)
    return r

def add_room_user_txn(session, room_id, user_id):
    u = session.query(User).filter(User.id == user_id).first()
    u.room = room_id
    session.add(u)
    return {
        'id': str(u.id),
        'name': u.name,
        'image': u.image,
        'room': str(u.room)
    }

def remove_room_user_txn(session, room_id, user_id):
    u = session.query(User).filter(User.id == user_id).first()
    u.room = None
    session.add(u)
    return {
        'id': str(u.id),
        'name': u.name,
        'image': u.image,
        'room': u.room
    }
