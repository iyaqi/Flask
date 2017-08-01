import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "kndjkadnjkandska"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
    CSRF_ENABLED = True

    @staticmethod
    def init_app(app):
        pass
# dev
class Dev_Config(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USE_TLS = True
    MAIL_PORT = 587
    MAIL_USERNAME = 'ls_xyq@126.com'
    MAIL_PASSWORD = 'XU8023JUAN'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'dev_data.sqlite')

# test
class Test_Config(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test_data.sqlite')

# product
class Product_Config(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development' : Dev_Config,
    "testing" : Test_Config,
    'production' :Product_Config,

    'default' : Dev_Config
}

