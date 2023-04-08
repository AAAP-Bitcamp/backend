from pydantic import BaseModel
from flask_pydantic import validate

from api import create_app, socketio

# class Room(BaseModel):
#     ID: string
#     admin_id: string

# class User(BaseModel):
#     ID: string
#     name: string
#     image: string
#     room_id: string

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)
