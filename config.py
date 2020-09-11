import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    _db_user = os.getenv('DATABASE_USER')
    _db_password = os.getenv('DATABASE_PASSWORD')
    _db_host = os.getenv('DATABASE_HOST')
    _db_name = os.getenv('DATABASE_NAME')

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(
        _db_user, _db_password, _db_host, _db_name
    )


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
