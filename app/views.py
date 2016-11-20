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
#if 404 error render 404.html
from app.TDG import ReservationTDG

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
	userReservation = ReservationMapper.findByUser(session['userId'])
	for index, reservation in enumerate(userReservation):
		print(reservation)
		reservation1.append(reservation.getRoom().getId())
		reservation1.append(reservation.getTimeslot().getStartTime())
		endTime = reservation.getTimeslot().getEndTime() + 1
		reservation1.append(endTime)
		reservation1.append(reservation.getTimeslot().getDate())
		reservation1.append(reservation.getDescription())
		reservation1.append(reservation.getId())
	return render_template('index.html',user=user, reservation=reservation1)


@app.route('/cancel/<reservationId>')
@login_required
@nocache
def cancel(reservationId):
	registry.getDirectory().setRoomList(RoomMapper.findAll())
	registry.getReservationBook().setReservationList(ReservationMapper.findAll())
	registry.getReservationBook().setWaitingList(WaitingMapper.findAll())
	roomId = 1
	registry.initiateAction(roomId)
	registry.cancelReservation(reservationId)
	registry.endAction(roomId)
	ReservationTDG.delete(reservationId)
	TimeslotTDG.delete(reservationId)
	return redirect(url_for('dashboard', user=session['user']))


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
		date = '2016-' + month + '-0' + day
	else:
		date = '2016-' + month + '-' + day

	rooms = []
	for i in range(5):
		availabilities = []
		for j in range(12):
			availabilities.append("Available")
		rooms.append(availabilities)

	allReservation = ReservationTDG.findByDate(date)
	print(allReservation)
	print("all Reservation")
	for roomtime in allReservation:
		print(roomtime[1])
		if roomtime[1] == 1:
			print(roomtime[0])
			if roomtime[6] == 9:
				rooms[0][0] = "unavailable"
				if roomtime[7] == 10:
					rooms[0][1] = "unavailable"
			if roomtime[6] == 10:
				rooms[0][1] = "unavailable"
				if roomtime[7] == 11:
					rooms[0][2] = "unavailable"
			if roomtime[6] == 11:
				rooms[0][2] = "unavailable"
				if roomtime[7] == 12:
					rooms[0][3] = "unavailable"
			if roomtime[6] == 12:
				rooms[0][3] = "unavailable"
				if roomtime[7] == 13:
					rooms[0][4] = "unavailable"
			if roomtime[6] == 13:
				rooms[0][4] = "unavailable"
				if roomtime[7] == 14:
					rooms[0][5] = "unavailable"
			if roomtime[6] == 15:
				rooms[0][5] = "unavailable"
				if roomtime[7] == 16:
					rooms[0][6] = "unavailable"
			if roomtime[6] == 16:
				rooms[0][6] = "unavailable"
				if roomtime[7] == 17:
					rooms[0][7] = "unavailable"
			if roomtime[6] == 17:
				rooms[0][7] = "unavailable"
				if roomtime[7] == 18:
					rooms[0][8] = "unavailable"
			if roomtime[6] == 18:
				rooms[0][8] = "unavailable"
				if roomtime[7] == 19:
					rooms[0][9] = "unavailable"
			if roomtime[6] == 19:
				rooms[0][9] = "unavailable"
				if roomtime[7] == 20:
					rooms[0][10] = "unavailable"
			if roomtime[6] == 20:
				rooms[0][10] = "unavailable"
				if roomtime[7] == 21:
					rooms[0][11] = "unavailable"
			if roomtime[7] == 21:
				rooms[0][11] = "unavailable"
		if roomtime[1] == 2:
			if roomtime[6] == 9:
				rooms[1][0] = "unavailable"
				if roomtime[7] == 10:
					rooms[1][1] = "unavailable"
			if roomtime[6] == 10:
				rooms[1][1] = "unavailable"
				if roomtime[7] == 11:
					rooms[1][2] = "unavailable"
			if roomtime[6] == 11:
				rooms[1][2] = "unavailable"
				if roomtime[7] == 12:
					rooms[1][3] = "unavailable"
			if roomtime[6] == 12:
				rooms[1][3] = "unavailable"
				if roomtime[7] == 13:
					rooms[1][4] = "unavailable"
			if roomtime[6] == 13:
				rooms[1][4] = "unavailable"
				if roomtime[7] == 14:
					rooms[1][5] = "unavailable"
			if roomtime[6] == 15:
				rooms[1][5] = "unavailable"
				if roomtime[7] == 16:
					rooms[1][6] = "unavailable"
			if roomtime[6] == 16:
				rooms[1][6] = "unavailable"
				if roomtime[7] == 17:
					rooms[1][7] = "unavailable"
			if roomtime[6] == 17:
				rooms[1][7] = "unavailable"
				if roomtime[7] == 18:
					rooms[1][8] = "unavailable"
			if roomtime[6] == 18:
				rooms[1][8] = "unavailable"
				if roomtime[7] == 19:
					rooms[1][9] = "unavailable"
			if roomtime[6] == 19:
				rooms[1][9] = "unavailable"
				if roomtime[7] == 20:
					rooms[1][10] = "unavailable"
			if roomtime[6] == 20:
				rooms[1][10] = "unavailable"
				if roomtime[7] == 21:
					rooms[1][11] = "unavailable"
			if roomtime[7] == 21:
				rooms[1][11] = "unavailable"
		if roomtime[1] == 3:
			if roomtime[6] == 9:
				rooms[2][0] = "unavailable"
				if roomtime[7] == 10:
					rooms[2][1] = "unavailable"
			if roomtime[6] == 10:
				rooms[2][1] = "unavailable"
				if roomtime[7] == 11:
					rooms[2][2] = "unavailable"
			if roomtime[6] == 11:
				rooms[2][2] = "unavailable"
				if roomtime[7] == 12:
					rooms[2][3] = "unavailable"
			if roomtime[6] == 12:
				rooms[2][3] = "unavailable"
				if roomtime[7] == 13:
					rooms[2][4] = "unavailable"
			if roomtime[6] == 13:
				rooms[2][4] = "unavailable"
				if roomtime[7] == 14:
					rooms[2][5] = "unavailable"
			if roomtime[6] == 15:
				rooms[2][5] = "unavailable"
				if roomtime[7] == 16:
					rooms[2][6] = "unavailable"
			if roomtime[6] == 16:
				rooms[2][6] = "unavailable"
				if roomtime[7] == 17:
					rooms[2][7] = "unavailable"
			if roomtime[6] == 17:
				rooms[2][7] = "unavailable"
				if roomtime[7] == 18:
					rooms[2][8] = "unavailable"
			if roomtime[6] == 18:
				rooms[2][8] = "unavailable"
				if roomtime[7] == 19:
					rooms[2][9] = "unavailable"
			if roomtime[6] == 19:
				rooms[2][9] = "unavailable"
				if roomtime[7] == 20:
					rooms[2][10] = "unavailable"
			if roomtime[6] == 20:
				rooms[2][10] = "unavailable"
				if roomtime[7] == 21:
					rooms[2][11] = "unavailable"
			if roomtime[7] == 21:
				rooms[2][11] = "unavailable"
		if roomtime[1] == 4:
			if roomtime[6] == 9:
				rooms[3][0] = "unavailable"
				if roomtime[7] == 10:
					rooms[3][1] = "unavailable"
			if roomtime[6] == 10:
				rooms[3][1] = "unavailable"
				if roomtime[7] == 11:
					rooms[3][2] = "unavailable"
			if roomtime[6] == 11:
				rooms[3][2] = "unavailable"
				if roomtime[7] == 12:
					rooms[3][3] = "unavailable"
			if roomtime[6] == 12:
				rooms[3][3] = "unavailable"
				if roomtime[7] == 13:
					rooms[3][4] = "unavailable"
			if roomtime[6] == 13:
				rooms[3][4] = "unavailable"
				if roomtime[7] == 14:
					rooms[3][5] = "unavailable"
			if roomtime[6] == 15:
				rooms[3][5] = "unavailable"
				if roomtime[7] == 16:
					rooms[3][6] = "unavailable"
			if roomtime[6] == 16:
				rooms[3][6] = "unavailable"
				if roomtime[7] == 17:
					rooms[3][7] = "unavailable"
			if roomtime[6] == 17:
				rooms[3][7] = "unavailable"
				if roomtime[7] == 18:
					rooms[3][8] = "unavailable"
			if roomtime[6] == 18:
				rooms[3][8] = "unavailable"
				if roomtime[7] == 19:
					rooms[3][9] = "unavailable"
			if roomtime[6] == 19:
				rooms[3][9] = "unavailable"
				if roomtime[7] == 20:
					rooms[3][10] = "unavailable"
			if roomtime[6] == 20:
				rooms[3][10] = "unavailable"
				if roomtime[7] == 21:
					rooms[3][11] = "unavailable"
			if roomtime[7] == 21:
				rooms[3][11] = "unavailable"
		if roomtime[1] == 5:
			if roomtime[6] == 9:
				rooms[4][0] = "unavailable"
				if roomtime[7] == 10:
					rooms[4][1] = "unavailable"
			if roomtime[6] == 10:
				rooms[4][1] = "unavailable"
				if roomtime[7] == 11:
					rooms[4][2] = "unavailable"
			if roomtime[6] == 11:
				rooms[4][2] = "unavailable"
				if roomtime[7] == 12:
					rooms[4][3] = "unavailable"
			if roomtime[6] == 12:
				rooms[4][3] = "unavailable"
				if roomtime[7] == 13:
					rooms[4][4] = "unavailable"
			if roomtime[6] == 13:
				rooms[4][4] = "unavailable"
				if roomtime[7] == 14:
					rooms[4][5] = "unavailable"
			if roomtime[6] == 15:
				rooms[4][5] = "unavailable"
				if roomtime[7] == 16:
					rooms[4][6] = "unavailable"
			if roomtime[6] == 16:
				rooms[4][6] = "unavailable"
				if roomtime[7] == 17:
					rooms[4][7] = "unavailable"
			if roomtime[6] == 17:
				rooms[4][7] = "unavailable"
				if roomtime[7] == 18:
					rooms[4][8] = "unavailable"
			if roomtime[6] == 18:
				rooms[4][8] = "unavailable"
				if roomtime[7] == 19:
					rooms[4][9] = "unavailable"
			if roomtime[6] == 19:
				rooms[4][9] = "unavailable"
				if roomtime[7] == 20:
					rooms[4][10] = "unavailable"
			if roomtime[6] == 20:
				rooms[4][10] = "unavailable"
				if roomtime[7] == 21:
					rooms[4][11] = "unavailable"
			if roomtime[7] == 21:
				rooms[4][11] = "unavailable"


	if request.method == 'POST':
		if request.form.getlist('chosenTime'):
			print("chosenTime")
			chosenTime = request.form.getlist('chosenTime')
			print(chosenTime)
			endTime = int(chosenTime[-1])
			startTime = int(chosenTime[0])
			roomId = request.form.getlist('room')
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
				room = Room(roomId[0],False)
				block = block + 1
				if registry.initiateAction(room.getId()):
					#Instantiate parameters
					user = UserMapper.find(session['userId'])
					timeSlot = TimeslotMapper.makeNew(startTime,endTime,date,block, user.getId())
					TimeslotMapper.save(timeSlot)
					timeslotId = TimeslotMapper.findId(user.getId())
					timeSlot.setId(timeslotId)
					description = request.form['description']
					processed_description = description.upper()
					#Make Reservation
					reservation = ReservationMapper.makeNewReservation(room, user, timeSlot, processed_description,timeslotId)
					ReservationMapper.save(reservation)
				registry.endAction(room.getId())
	return render_template('add.html',rooms=rooms)

# annee mois jour
# fetch dans le timeslottable de ses meme temps
