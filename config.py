import os


class Config:
    '''
    General configuration parent class

    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(32)
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/personalblog'
    
    
   


   