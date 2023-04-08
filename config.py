import os

# from dotenv import load_dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DATABASE_URL=os.environ.get('DATABASE_URL') or \
        "postgresql://photo-assassin:5o7fNilGATDHLegUKGwJtg@photo-assassin-10081.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=require&sslrootcert=./cc-ca.crt"
    SECRET_KEY=os.environ.get('SECRET_KEY') or \
        "cecd8872ccf950afb116091ccb2129d5af31906091bdc730ca373d38f91e4c43"
    ACCESS_TOKEN_EXPIRE_MINUTES=os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES') or 720