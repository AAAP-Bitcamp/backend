import string
import secrets

from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return "<p>Home Page</p>"

@routes.route('/users')
def add_user(name: str, image: str):
    return 'add return here'

@routes.route('/room/create')
def create():
    return {
        'room_code': ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7))
    }

@routes.route('/room/:room_code')
def create_room(room_code: string):
    # store image in cockroachdb
    return "add return here"
