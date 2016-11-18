#UserTDG
import psycopg2
from psycopg2.extensions import AsIs


def find(id):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	cur.execute("""SELECT * FROM timeslotTable WHERE timeslotId = %s;""", (id,))
	data = cur.fetchall()
	conn.close()
	#returns table row as list
	return data

def insert(timeslot):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	startTime = timeslot.getStartTime()
	endTime = timeslot.getEndTime()
	date = timeslot.getDate()
	block = timeslot.getBlock()

	cur.execute("""INSERT INTO waitingTable(startTime, endTime, date, block) VALUES 
		(%s, %s, %s, %s);""", (AsIs(startTime), AsIs(endTime), AsIs(date), AsIs(block)))

	conn.close()

def update(id, st, et, date, block):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""UPDATE waitingTable SET startTime = %s, endTime = %s, 
		date = %s, block = %s WHERE waitingId = %s;""", (AsIs(st), AsIs(et), AsIs(date), AsIs(block), AsIs(id)))

	conn.close()

def delete(id):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""DELETE FROM timeslotTable WHERE timeslotId = %s;""", (id,))

	conn.close()







	