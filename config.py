import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#connect to dataase
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Intel1234@localhost/development'
SQLALCHEMY_TRACK_MODIFICATIONS = True