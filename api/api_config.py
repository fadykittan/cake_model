from dotenv import load_dotenv
import os
import logging
load_dotenv()

def get_config():
    environment = os.getenv("ENVIRONMENT", "dev")

    config_by_name = {
        'dev': DevelopmentConfig,
        'test': TestingConfig,
        'prod': ProductionConfig
    }

    return config_by_name.get(environment)



class Config:
    """Base Config Class"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    LOG_LEVEL = logging.INFO
    DEBUG = False
    TESTING = False

    # API settings
    API_TITLE = 'My RESTful API'
    API_VERSION = '1.0'
    API_DESCRIPTION = 'A scalable RESTful API with Flask-RESTx'
    API_DOC_PATH = '/swagger'

class DevelopmentConfig(Config):
    """Development Config Class"""
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite')

class TestingConfig(Config):
    """Testing Config Class"""
    DEBUG = True
    LOG_LEVEL = logging.INFO
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite')

class ProductionConfig(Config):
    """Production Config Class"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING
    DATABASE_URI = os.getenv('DATABASE_URI')

