import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DATABASE_URL=os.environ.get('DATABASE_URL')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    ACCESS_TOKEN_EXPIRE_MINUTES=os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES')