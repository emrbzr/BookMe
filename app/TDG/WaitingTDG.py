#WaitingTDG
import psycopg2
from psycopg2.extensions import AsIs


def find(id):
	conn = psycopg2.connect(database="development", user="postgres", password="Intel1234", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	cur.execute("""SELECT * FROM waitingTable WHERE waitingId = %s """, (id,))
	data = cur.fetchall()
	conn.close()
	#returns table row as list
	return data

def insert(waiting):
	conn = psycopg2.connect(database="development", user="postgres", password="Intel1234", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	room = waiting.getRoom()
	room = room.getId()
	reservee = waiting.getUser()
	reservee = reservee.getId()
	description = waiting.getDescription()
	timeslot = waiting.getTimeslot()
	timeslot = timeslot.getId()

	cur.execute("""INSERT INTO waitingTable(room, reservee, description, timeslot) VALUES 
		(%s, %s, %s, %s);""", (room, reservee, description, timeslot))

	conn.close()

def update(id, roomId, userId, description, timeslotId):
	conn = psycopg2.connect(database="development", user="postgres", password="Intel1234", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""UPDATE waitingTable SET room = %s, reservee = %s, 
		description = %s, timeslot = %s WHERE waitingId = %s;""", 
		(roomId, userId, description, timeslotId,id))
	conn.commit()
	conn.close()

def delete(id):
	conn = psycopg2.connect(database="development", user="postgres", password="Intel1234", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""DELETE FROM waitingTable WHERE waitingId = %s;""", (id,))
	conn.commit()
	conn.close()


def findAll():
	conn = psycopg2.connect(database="development", user="postgres", password="Intel1234", host="127.0.0.1",
							port="5432")
	cur = conn.cursor()
	cur.execute("""SELECT * FROM waitingTable """)
	data = cur.fetchall()
	conn.close()
	# returns table row as list
	return data

def findByRoom(roomId, date):
	conn = psycopg2.connect(database="development", user="postgres", password="Intel1234", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	cur.execute("""SELECT waitingId, room, reservee, timeslot, startTime, endTime FROM waitingTable LEFT OUTER JOIN timeslotTable
		ON (waitingTable.timeslot = timeslotTable.timeid) WHERE room = %s AND date = %s;""", (roomId, date))
	data = cur.fetchall()

	conn.close()
	return data



	