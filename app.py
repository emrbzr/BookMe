#!/usr/bin/env python

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'invalid credentials. Pleas try again.'
		else: 
			return redirect(url_for('reservation'))
	return render_template('index.html', error='Invalid credentials. Please try again')

@app.route('/reservation')
def reservation():
	return render_template('reservation.html')

if __name__ == '__main__':
	app.run(debug=True)