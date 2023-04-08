from api import movr
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify, request

db = SQLAlchemy()
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return jsonify({'message': 'Home page for Photo Assassin API!'})

@routes.route('/users', methods=['POST'])
def add_user():
    data = request.get_json() or {}
    if 'name' not in data or 'image' not in data:
        return {
            'code': 400,
            'message': 'Must include name and image!'
        }, 400
    user = movr.add_user(data['name'], data['image'])
    return user

@routes.route('/rooms', methods=['POST'])
def add_room():
    data = request.get_json() or {}
    if 'code' not in data or 'user_id' not in data:
        return {
            'code': 400,
            'message': 'Error! Unable to find account name.'
        }, 400
    room = movr.add_room(data['code'], data['user_id'])
    return room
