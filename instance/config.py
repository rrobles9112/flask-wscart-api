import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('FLASK_SECRET')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (os.getenv('MYSQL_USER'),
                                                                   os.getenv('MYSQL_PASSWORD'),
                                                                   os.getenv('MYSQL_DATABASE_NAME'))
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@localhost:3306/WSCartAPI' % (os.getenv('MYSQL_USER'),
    #                                                                       os.getenv('MYSQL_PASSWORD'))


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@localhost:3306/test_WSCartAPI' % (os.getenv('MYSQL_USER'),
                                                                          os.getenv('MYSQL_PASSWORD'))
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
