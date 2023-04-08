from api import movr, socketio
from flask import Blueprint
from flask_socketio import join_room, leave_room, send

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
        join_room(room)
        send(users, to=room)
    else:
        send('error', f'Could not join room: {room_code}')

@socketio.on('leave')
def on_leave(data):
    user_id = data['user_id']
    room_code = data['room_code']
    user = movr.get_user(user_id)
    room = movr.get_room(room_code)
    if user and room and room.creator != user.id:
        movr.remove_room_user(room.id, user.id)
        users = movr.get_users(room.id)
        leave_room(room)
        send(users, to=room)
    else:
        send('error', f'Could not leave room: {room_code}')