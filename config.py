import os
class Config:
    '''
    General configuration parent class

    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(32)
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/personalblog'
    
class ProdConfig(Config):
    '''
    production configuration child class

    Args:
        config:  The parent configuration class with General configuration settings

    '''
class DevConfig(Config):
    '''
    Development configuration child class

    '''
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}        
   


   