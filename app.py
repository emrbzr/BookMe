#!/usr/bin/env python

from flask import Flask, render_template, request, url_for, redirect, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = "secret"

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('you need to login first.')
			return redirect(url_for('home'))
	return wrap

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login')
def signin():
	return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'invalid credentials. Pleas try again.'
		else: 
			session['logged_in'] = True
			return redirect(url_for('reservation'))
	return render_template('index.html', error='Invalid credentials. Please try again')

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('home'))

@app.route('/reservation')
@login_required
def reservation():
		return render_template('reservation.html')
	

if __name__ == '__main__':
	app.run(debug=True)