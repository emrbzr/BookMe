import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#create app
app = Flask(__name__)
#connect to config.py
app.config.from_object('config')
#secret key
app.secret_key = os.urandom(24)
#create db instance
db = SQLAlchemy(app)
#import models
from app import models
#create all tables in models views
db.create_all()
#import views
from app import views, decorators
