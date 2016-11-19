from app import app
from .decorators import *
from .models import *
from flask import render_template, request
from app.TDG import UserTDG
from app.TDG import ReservationTDG
from app.mapper import ReservationMapper
from app.mapper import UserMapper
from app.core.room import Room
from app.core.reservation import Reservation
from app.core.timeslot import Timeslot
from app.TDG import TimeslotTDG
from app.mapper import TimeslotMapper
from app.core.user import User
#if 404 error render 404.html
@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html')

#if 500 error render 500.html
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/')
def home():
	return redirect(url_for('index'))
#login
@app.route('/login', methods=['GET', 'POST'])
def index():
	error = 'Invalid credentials. Please try again'
	if request.method == 'POST':
		user = UserMapper.find(request.form['username'])
		if user.getId() is int(request.form['username']):
			if user.getPassword() == request.form['password']:
				session['logged_in'] = True
				session['userId'] = user.getId()
				return redirect(url_for('dashboard',user=user.getName()))
			else:
				return render_template('login.html',error=error)
		else:
			return render_template('login.html',error=error)
	else:
		return render_template('login.html')

#logout
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	session.clear()
	return redirect(url_for('index'))

#reservation
@app.route('/dashboard/<user>')
@login_required
@nocache
def dashboard(user):
	session['user'] = user
	return render_template('index.html',user=user)

@app.route('/month')
@login_required
@nocache
def month():
	return render_template('month.html')

@app.route('/<month>')
@login_required
@nocache
def chooseMonth(month):
	if month == 'september':
		return render_template('january.html')
	if month == 'october':
		return render_template('october.html')
	if month == 'november':
		return render_template('november.html')
	if month == 'december':
		return render_template('december.html')
	if month == 'january':
		return render_template('january.html')
	if month == 'february':
		return render_template('february.html')
	if month == 'march':
		return render_template('march.html')
	if month == 'april':
		return render_template('april.html')
	if month == 'may':
		return render_template('may.html')
	if month == 'june':
		return render_template('june.html')
	if month == 'july':
		return render_template('july.html')
	if month == 'august':
		return render_template('august.html')
	else:
		return render_template('month.html')

@app.route('/<month>/<day>',methods=['GET','POST'])
def addNewReservation(month,day):
	print("hello")
	if request.method == 'POST':
		print('inPost')
		if request.form.getlist('chosenTime') is not None:
			print('inChosentime')
			chosenTime = request.form.getlist('chosenTime')
			endTime = int(chosenTime[-1])
			print(endTime)
			startTime = int(chosenTime[0])
			print(startTime)
			block = endTime - startTime
			if block < 3:
				if month == 'september':
					month = '09'
				if month == 'october':
					month = '10'
				if month == 'november':
					month = '11'
				if month == 'december':
					month = '12'
				if month == 'january':
					month = '01'
				if month == 'february':
					month = '02'
				if month == 'march':
					month = '03'
				if month == 'april':
					month = '04'
				if month == 'may':
					month = '05'
				if month == 'june':
					month = '06'
				if month == 'july':
					month = '07'
				if month == 'august':
					month = '08'
				if day < 10:
					date = '2016-'+month+'-0'+day
					print(date)
				else:
					date = '2016-'+month+'-'+day
				room = Room(1,True)
				user = UserMapper.find(session['userId'])
				timeSlot = TimeslotMapper.makeNew(startTime,endTime,date,user.getId())
				TimeslotMapper.save(timeSlot)
				timeslotId = TimeslotMapper.findId(user.getId())
				timeSlot.setId(timeslotId)
				description = request.form['description']
				processed_description = description.upper()
				reservation = ReservationMapper.makeNewReservation(room,user,timeSlot,processed_description,timeslotId)
				ReservationTDG.insert(reservation)
	return render_template('add.html')
