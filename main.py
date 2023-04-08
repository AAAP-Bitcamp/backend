from flask import Flask, render_template, abort, redirect, url_for
from flask_socketio import SocketIO

import string
import secrets
from pydantic import BaseModel
from flask_pydantic import validate

from api import create_app, socketio

class Room(BaseModel):
    ID: string
    admin_id: string

class User(BaseModel):
    ID: string
    name: string
    image: string
    room_id: string

app = create_app()

if __name__ == '__main__':
    socketio.run(app)

@app.route('/')
def index():
    return "<p>Home Page</p>"

@app.route('/users')
def add_user(name: string, image: string):
    return 

@app.route('/room/create')
def create():
    return {
        'room_code': ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7))
    }

@app.route('/room/:room_code')
def create_room(room_code: string):
    # store image in cockroachdb
    return "add return here"
