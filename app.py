#!/usr/bin/env python
from flask import Flask, render_template, request, url_for, redirect, session, flash, Blueprint
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.secret_key = "b',|V\xa2^\xf8y%/\xee\x81\x91\xe6\xba\xe3/RW\x97|k:\xa0\x1f'"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Intel1234@localhost/reservation'
db = SQLAlchemy(app)

# user schema

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(), unique=True)
	password = db.Column(db.String(), unique=True)

	def __init__(self, username, password):
		self.username = username
		self.password = password

# adding user to table user into database Reservation
@app.route('/post_user', methods=['POST'])
def post_user():
	userexists = "Username already in use."
	checkuser = User.query.filter(db.or_(User.username == request.form['username'])).first()
	if not checkuser:
		user = User(request.form['username'], request.form['password'])
		db.session.add(user)
		db.session.commit()
		return render_template('reservation.html')
	else:
		return render_template('register.html', userexists=userexists)


# login required
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('you need to login first.')
			return redirect(url_for('home'))
	return wrap

# home 
@app.route('/')
def home():
	return redirect(url_for('index'))

# render register template
@app.route('/register')
def getRegister():
	return render_template('register.html')

# render reservation template if login with correct credentials
@app.route('/login', methods=['GET', 'POST'])
def index():
	error = 'Invalid credentials. Please try again'
	if request.method == 'POST':
		user = User.query.filter(db.or_(User.username == request.form['username'])).first()
		password = User.query.filter(db.or_(User.password == request.form['password'])).first()
		if user:
			if password:
				session['logged_in'] = True
				return redirect(url_for('reservation'))
			else:
				return render_template('index.html',error=error)
		else:
			return render_template('index.html',error=error)
	return render_template('index.html')

# logout 
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('home'))

# render reservation
@app.route('/reservation')
@login_required
def reservation():
		return render_template('reservation.html')
	

if __name__ == '__main__':
	app.run(debug=True)