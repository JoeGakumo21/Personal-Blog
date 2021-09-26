import os
class Config:
    '''
    General configuration parent class

    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'joe12hsadjhnsdmas9122134144sa56c'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/personalblog'
    
class ProdConfig(Config):
    '''
    production configuration child class

    Args:
        config:  The parent configuration class with General configuration settings

    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class DevConfig(Config):
    '''
    Development configuration child class

    '''
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}        
   


   