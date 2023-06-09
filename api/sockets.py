from api import movr, socketio
# from api.models import User
from flask import Blueprint, request
from flask_socketio import join_room, emit

sockets = Blueprint('sockets', __name__)

@socketio.on('join')
def on_join(data):
    user_id = data['user_id']
    room_code = data['room_code'] 
    user = movr.get_user(user_id)
    room = movr.get_room(room_code)
    if user and room:
        movr.add_room_user(room.id, user.id)
        users = movr.get_users(room.id)
        # join_room(room_code)
        # emit('join', users, to=room_code)
        emit('join', users, broadcast=True)
    else:
        emit('join', {'error': f'Could not join room: {room_code}'})
        
        
@socketio.on('start')
def on_start(data):
    room_code = data['room_code']
    room = movr.get_room(room_code)
    if room:
        users = movr.get_users(room.id)
        user_data = {user['name'] : user['score'] for user in users}
        # emit('start', user_data, broadcast=False, to=room_code)
        emit('start', user_data, broadcast=True)
    else:
        emit('start', {'error': f'Could not start game in room: {room_code}'}, broadcast=True)

@socketio.on('verify')
def on_verify(data):
    room_code = data['room_code']
    user_id = data['user_id']
    image = data['image']
    user = movr.get_user(user_id)
    room = movr.get_room(room_code)
    if user and room and image:
        movr.add_room_image(room_code, user_id, image)
        users = movr.get_users(room.id)
        user = movr.get_user(user_id)
        if user.score >= 5:
            user_data = {user['name'] : user['score'] for user in users}
            user_data = sorted(user_data, key=lambda d:d.value, reverse=True)
            images = movr.get_images(room.id)
            movr.delete_images(room.id)
            emit('end', {'scoreboard': user_data, 'images': images}, broadcast=True)
        else:
            emit('verify', users, broadcast=True)
    else:
        emit('verify', {'error': f'Could not verify image'})

@socketio.on('penalty')
def on_penalty(data):
    room_code = data['room_code']
    user_id = data['user_id']
    user = movr.get_user(user_id)
    room = movr.get_room(room_code)
    if user and room:
        movr.penalty(user_id)
        users = movr.get_users(room.id)
        emit('verify', users, broadcast=True)
    else:
        emit('penalty', {'error': f'Could not apply penalty'})
    

# @socketio.on('leave')
# def on_leave(data):
#     user_id = data['user_id']
#     room_code = data['room_code']
#     user = movr.get_user(user_id)
#     room = movr.get_room(room_code)
#     if user and room and room.creator != user.id:
#         movr.remove_room_user(room.id, user.id)
#         users = movr.get_users(room.id)
#         leave_room(room)
#         emit('leave', users, to=room, broadcast=True)
#     else:
#         emit('error', f'Could not leave room: {room_code}')