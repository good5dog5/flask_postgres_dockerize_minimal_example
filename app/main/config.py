import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://%s:%s@%s/%s' % (
        os.environ['DBUSER'],
        os.environ['DBPASS'],
        os.environ['DBHOST'],
        os.environ['DBNAME']
    )
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig
)
