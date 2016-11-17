#all schemas are created here
from app import db

#User schema
class User(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(), unique=True)
	password = db.Column(db.String(), unique=True)

	def __init__(self, username, password):
		self.username = username
		self.password = password



