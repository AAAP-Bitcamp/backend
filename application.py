from api import create_app, socketio

application = create_app()

if __name__ == '__main__':
    # socketio.run(application, debug=True)
    socketio.run(application, debug=True, log_output=True)
