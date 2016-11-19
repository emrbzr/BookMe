#ReservationTDG
import psycopg2
from psycopg2.extensions import AsIs


def find(id):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	cur.execute("""SELECT * FROM reservationTable WHERE reservationId = %s;""", (id,))
	data = cur.fetchall()
	conn.close()
	#returns row as list
	return data

def insert(reservation):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	room = reservation.getRoom()
	room = room.getId()
	description = reservation.getDescription()
	holder = reservation.getUser()
	holder = holder.getId()
	timeslot = reservation.getTimeslot()
	timeslot = timeslot.getId()

	cur.execute("""INSERT INTO reservationTable(room, description, holder, timeslot) VALUES 
		(%s, %s, %s, %s);""", (AsIs(room), AsIs(description), AsIs(holder), AsIs(timeslot)))

	conn.close()

def update(id, roomId, userId, description, timeslot):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""UPDATE reservationTable SET room = %s, holder = %s, 
		 description = %s, timeslot = %s WHERE reservationId = %s;""",
		  (AsIs(roomId), AsIs(userId), AsIs(description), AsIs(timeslot), AsIs(id)))

	conn.close()

def delete(id):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""DELETE FROM reservationTable WHERE reservationId = %s;""", (id,))

	conn.close()

def findByDate(date):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""SELECT * FROM reservationTable LEFT OUTER JOIN timeslotTable 
		ON (reservationTable.timeslot = timeslotTable.timeslotId) WHERE date = %s;""", (date,))
	data = cur.fetchall()
	
	conn.close()

	return data

	




	