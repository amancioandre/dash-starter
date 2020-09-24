import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('APP_SECRET_KEY', 'secret_key')
    DEBUG = False
    SECURITY_LOGIN_URL = "/"
    SECURITY_POST_LOGIN_VIEW = "/dashboard"
    SECURITY_LOGIN_USER_TEMPLATE = "auth/auth.html"
    SECURITY_PASSWORD_SALT = Config.SECRET_KEY

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABSE_URI", None)
    
class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", None)
    SERVER_NAME = os.getenv("SERVER_NAME", "0.0.0.0:5000")

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("")
    SERVER_NAME = os.getenv("SERVER_NAME", "0.0.0.0:5000")

config_by_env = dict(
    dev=DevelopmentConfig(),
    test=TestingConfig(),
    prod=ProductionConfig()
)

key = Config.SECRET_KEY