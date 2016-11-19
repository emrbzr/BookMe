#RoomTDG
import psycopg2
from psycopg2.extensions import AsIs


def find(id):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	cur.execute("""SELECT * FROM roomTable WHERE roomId = %s;""", (id,))
	data = cur.fetchall()
	conn.close()
	#returns table row as list
	return data

def insert(room):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()
	
	lock = room.getLock()

	cur.execute("""INSERT INTO roomTable(lock) VALUES 
		(%s);""", lock)
	conn.commit()
	conn.close()

def update(id, availability):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""UPDATE roomTable SET roomLock = %s 
		WHERE roomId = %s;""", (availability, id))
	conn.commit()
	conn.close()

def delete(id):
	conn = psycopg2.connect(database="development", user="postgres", password="sqlpw", host="127.0.0.1", port="5432")
	cur = conn.cursor()

	cur.execute("""DELETE FROM roomTable WHERE userId = %s;""", (id,))
	conn.commit()
	conn.close()







	