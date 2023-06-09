from api.models import User, Room, RoomImage

import uuid

def add_user_txn(session, name, image):
    u = User(id=str(uuid.uuid4()), name=name, image=image, score=0)
    session.add(u)
    return {
        'id': str(u.id),
        'name': u.name,
        'image': u.image,
        'score': u.score
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
        'image': user.image,
        'score': user.score,
        'room': str(user.room)
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
        'score': u.score,
        'room': str(u.room)
    }

def add_room_image_txn(session, room_code, user_id, image):
    r = session.query(Room).filter(Room.code == room_code).first()
    u = session.query(User).filter(User.id == user_id).first()
    i = RoomImage(id=str(uuid.uuid4()), image=image, room=r.id)
    u.score += 1
    session.add(i)
    session.add(u)

def penalty_txn(session, user_id):
    u = session.query(User).filter(User.id == user_id).first()
    u.score -= 2
    session.add(u)

def get_images_txn(session, room_id):
    images = session.query(RoomImage).filter(RoomImage.room == room_id).all()
    return list(map(lambda image: {
        'id': str(image.id),
        'image': image.image,
        'room': str(image.room)
    }, images))

def delete_images_txn(session, room_id):
    images = session.query(RoomImage).filter(RoomImage.room == room_id).all()
    for image in images:
        session.delete(image)

# def remove_room_user_txn(session, room_id, user_id):
#     u = session.query(User).filter(User.id == user_id).first()
#     u.room = None
#     session.add(u)
#     return {
#         'id': str(u.id),
#         'name': u.name,
#         'image': u.image,
#         'room': u.room
#     }
