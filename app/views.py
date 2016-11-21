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
from app.mapper import RoomMapper
from app.core.directory import *
from app.core.registry import *
from app.mapper import WaitingMapper
from app.core.reservationbook import ReservationBook
from app.core.user import User
from app.core import update
#if 404 error render 404.html
from app.TDG import ReservationTDG
from app.core import checkAvailabilities
from app.TDG import WaitingTDG
rListDb = ReservationMapper.findAll()
reservationList = []
waitingList = []
waitingList = WaitingMapper.findAll()
for index, rId in enumerate(rListDb):
	reservationList.append(ReservationMapper.find(rId.getId()))
reservationBook = ReservationBook(reservationList, waitingList)

# create directory
roomList = []
directory = Directory(roomList)

# create registry
registry = Registry(directory, reservationBook)

@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html')

#if 500 error render 500.html
@app.errorhandler(500)
def internal_error(error):
    #db.session.rollback()
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
				#fetch all user reservation
				#i.e from timeslottable
				#reservationtable
				#merge reservationdata with timeslottable then store in reservation[]
				#waitingtable
				#store the waitingtable in waiting[]

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
	reservation1 = []
	userReservation = ReservationTDG.findUserRes(session['userId'])


	for reservation in userReservation:
		print(reservation)
		reservation1.append(reservation[1])
		reservation1.append(reservation[6])
		endTime = reservation[7] + 1
		reservation1.append(endTime)
		reservation1.append(reservation[8])
		reservation1.append(reservation[2])
		reservation1.append(reservation[0])

	waitings1 = []
	userWaiting = WaitingTDG.findByUser(session['userId'])

	for waitingRes in userWaiting:
		print(reservation)
		waitings1.append(waitingRes[1])
		waitings1.append(waitingRes[6])
		endTime = waitingRes[7] + 1
		waitings1.append(endTime)
		waitings1.append(waitingRes[8])
		waitings1.append(waitingRes[3])
		waitings1.append(waitingRes[0])

	return render_template('index.html',user=user, reservation=reservation1, waitings=waitings1)


@app.route('/cancel/<reservationId>')
@login_required
@nocache
def cancel(reservationId):
	registry.getDirectory().setRoomList(RoomMapper.findAll())
	registry.getReservationBook().setReservationList(ReservationMapper.findAll())
	registry.getReservationBook().setWaitingList(WaitingMapper.findAll())
	reservation = ReservationTDG.find(reservationId)
	roomId = reservation[0][1]
	print(reservation[0][4])
	timeslot = TimeslotTDG.find(reservation[0][4])
	print(timeslot[0][4])
	registry.initiateAction(roomId)
	registry.cancelReservation(reservationId)
	registry.endAction(roomId)
	ReservationTDG.delete(reservationId)
	TimeslotTDG.delete(reservationId)
	roomsAvailable = checkAvailabilities.checkAvailabilities(timeslot[0][3])
	if(roomId == 1):
		update.updateWaiting(roomId,timeslot[0][3],roomsAvailable[0])
	if(roomId == 2):
		update.updateWaiting(roomId, timeslot[0][3], roomsAvailable[1])
	if(roomId == 3):
		update.updateWaiting(roomId, timeslot[0][3], roomsAvailable[2])
	if(roomId == 4):
		update.updateWaiting(roomId, timeslot[0][3], roomsAvailable[3])
	if(roomId == 5):
		update.updateWaiting(roomId, timeslot[0][3], roomsAvailable[4])
	return redirect(url_for('dashboard', user=session['user']))

@app.route('/cancelWaiting/<waitingId>')
@login_required
@nocache
def canceWaiting(waitingId):
	timesslotId = WaitingTDG.findTimeslot(waitingId)
	print(timesslotId[0][0])
	WaitingTDG.delete(waitingId)
	TimeslotTDG.delete(timesslotId[0][0])
	return redirect(url_for('dashboard', user=session['user']))

@app.route('/modify/<reservationId>',methods=['GET', 'POST'])
@login_required
@nocache
def modify(reservationId):
	registry.getDirectory().setRoomList(RoomMapper.findAll())
	registry.getReservationBook().setReservationList(ReservationMapper.findAll())
	registry.getReservationBook().setWaitingList(WaitingMapper.findAll())
	reservation = ReservationTDG.find(reservationId)
	#fetch room
	roomId = reservation[0][1]
	#fetch date
	timeslot = TimeslotTDG.find(reservation[0][4])
	date = timeslot[0][3]
	#query
	allResDateRoom = ReservationTDG.findDateRoom(roomId,date)
	rTime = checkAvailabilities.checkModifyAvail(allResDateRoom)
	if request.method == 'POST':
		allTime = request.form.getlist('time')
		block = allTime[1] - allTime[0]
		TimeslotTDG.update(timeslot[0][0],allTime[0],allTime[1],allTime[0][3],block)
		return redirect(url_for('dashboard', user=session['user']))
	return render_template('modify.html', reservationId=reservationId)


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
	if month == 'september':
		m = '09'
	if month == 'october':
		m = '10'
	if month == 'november':
		m = '11'
	if month == 'december':
		m = '12'
	if month == 'january':
		m = '01'
	if month == 'february':
		m = '02'
	if month == 'march':
		m = '03'
	if month == 'april':
		m = '04'
	if month == 'may':
		m = '05'
	if month == 'june':
		m = '06'
	if month == 'july':
		m = '07'
	if month == 'august':
		m = '08'
	if day < 10:
		date = '2016-' + m + '-0' + day
	else:
		date = '2016-' + m + '-' + day

	rooms = checkAvailabilities.checkAvailabilities(date)


	if request.method == 'POST':
		if request.form.getlist('chosenTime'):
			chosenTime = request.form.getlist('chosenTime')
			endTime = int(chosenTime[-1])
			startTime = int(chosenTime[0])
			roomId = request.form.getlist('room')
			block = endTime + 1 - startTime
			if block < 3:
				if month == 'september':
					m = '09'
				if month == 'october':
					m = '10'
				if month == 'november':
					m = '11'
				if month == 'december':
					m = '12'
				if month == 'january':
					m = '01'
				if month == 'february':
					m = '02'
				if month == 'march':
					m = '03'
				if month == 'april':
					m = '04'
				if month == 'may':
					m = '05'
				if month == 'june':
					m = '06'
				if month == 'july':
					m = '07'
				if month == 'august':
					m = '08'
				if day < 10:
					date = '2016-'+m+'-0'+day
				else:
					date = '2016-'+m+'-'+day

				block = block + 1
				description = request.form['description']
				processed_description = description.upper()
				user = UserMapper.find(session['userId'])
				if checkAvailabilities.validateAvailability(roomId[0],date,startTime, endTime):
					room = Room(roomId[0],False)
					if registry.initiateAction(room.getId()):
						#Instantiate parameters
						timeSlot = TimeslotMapper.makeNew(startTime,endTime,date,block, user.getId())
						TimeslotMapper.save(timeSlot)
						timeslotId = TimeslotMapper.findId(user.getId())
						timeSlot.setId(timeslotId)
						#Make Reservation
						reservation = ReservationMapper.makeNewReservation(room, user, timeSlot, processed_description,timeslotId)
						ReservationMapper.save(reservation)
						registry.endAction(room.getId())
						return redirect(url_for('dashboard', user=session['user']))
				else:
					room = Room(roomId[0], False)
					timeSlot = TimeslotMapper.makeNew(startTime, endTime, date, block, user.getId())
					TimeslotMapper.save(timeSlot)
					timeslotId = TimeslotMapper.findId(user.getId())
					timeSlot.setId(timeslotId)
					waiting = WaitingMapper.makeNew(room,description,user,timeSlot)
					WaitingMapper.save(waiting)
					return redirect(url_for('dashboard', user=session['user']))
	return render_template('add.html',rooms=rooms)

# annee mois jour
# fetch dans le timeslottable de ses meme temps
