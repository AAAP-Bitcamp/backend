from api.transactions import add_user_txn, get_user_txn, get_users_txn, add_room_txn, get_room_txn, add_room_user_txn, add_room_image_txn, penalty_txn, get_images_txn, delete_images_txn
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import registry
registry.register("cockroachdb", "cockroachdb.sqlalchemy.dialect",
                  "CockroachDBDialect")


class MovR:
    """
    Wraps the database connection. The class methods wrap database transactions.
    """

    def __init__(self):
        pass

    def init_app(self, app):
        """
        Establish a connection to the database, creating Engine and Sessionmaker objects.

        Arguments:
            conn_string {String} -- CockroachDB connection string.
        """
        conn_string = app.config.get('DATABASE_URL')
        conn_string = conn_string.replace("postgresql://", "cockroachdb+psycopg2://")
        self.engine = create_engine(conn_string)
        self.sessionmaker = sessionmaker(bind=self.engine)

    def add_user(self, name, image):
        return run_transaction(self.sessionmaker, lambda session: add_user_txn(session, name, image))
    
    def get_user(self, id):
        return run_transaction(self.sessionmaker, lambda session: get_user_txn(session, id))
    
    def get_users(self, room_id):
        return run_transaction(self.sessionmaker, lambda session: get_users_txn(session, room_id))

    def add_room(self, code, user_id):
        return run_transaction(self.sessionmaker, lambda session: add_room_txn(session, code, user_id))
    
    def get_room(self, code):
        return run_transaction(self.sessionmaker, lambda session: get_room_txn(session, code))
    
    def add_room_user(self, room_id, user_id):
        return run_transaction(self.sessionmaker, lambda session: add_room_user_txn(session, room_id, user_id))
    
    def add_room_image(self, room_code, user_id, image):
        return run_transaction(self.sessionmaker, lambda session: add_room_image_txn(session, room_code, user_id, image))
    
    def penalty(self, user_id):
        return run_transaction(self.sessionmaker, lambda session: penalty_txn(session, user_id))
    
    def get_images(self, room_id):
        return run_transaction(self.sessionmaker, lambda session: get_images_txn(session, room_id))
    
    def delete_images(self, room_id):
        return run_transaction(self.sessionmaker, lambda session: delete_images_txn(session, room_id))
    
    # def remove_room_user(self, room_id, user_id):
    #     return run_transaction(self.sessionmaker, lambda session: remove_room_user_txn(session, room_id, user_id))
    