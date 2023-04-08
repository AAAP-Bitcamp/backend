from config import Config
from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

cors = CORS()
socketio = SocketIO(cors_allowed_origins='*')
movr = None

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    cors.init_app(app)
    socketio.init_app(app)

    @app.route('/')
    def index():
        return jsonify({'success': 'Hello World!'})

    from api.movr import MovR
    movr = MovR(app.config.get('DATABASE_URL'))

    from api.routes import routes
    app.register_blueprint(routes, url_prefix='/api')
    from api.sockets import sockets
    app.register_blueprint(sockets, url_prefix='/sockets')

    return app