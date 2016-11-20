from app.TDG import WaitingTDG
from app.TDG import ReservationTDG
from app.core.reservation import Reservation
from app.core.mapper import UserMapper
from app.core.mapper import RoomMapper
from app.core.mapper import TimeslotMapper

#waitingList: list containing (waitingId, room, reservee, timeslotid, starttime, endtime) entries
#availabilityList: availabilities for that room (array of strings)
def updateWaiting(roomId, date, availabilityList):
	waitingList = WaitingTDG.findByRoom(roomId, date)
	for index, w in waitingList:
		for i, a in availabilityList:
			if a == "Available" and availabilityList[i+1]=="unavailable" and (i+10)!=21:
				if w[4]==(i+9) and w[5]==(i+9):
					room = RoomMapper.find(w[1])
					holder = UserMapper.find(w[2])
					time = TimeslotMapper.find(w[3])
					reservation = Reservation(room,holder,time,'was waiting',0)
					ReservationTDG.insert(reservation)
					WaitingTDG.delete(w[0])
			elif a == "Available" and availabilityList[i+1]=="Available" and (i+10)!=21:
				if w[4]==(i+9) and w[5]==(i+10):
					room = RoomMapper.find(w[1])
					holder = UserMapper.find(w[2])
					time = TimeslotMapper.find(w[3])
					reservation = Reservation(room,holder,time,'was waiting',0)
					ReservationTDG.insert(reservation)
					WaitingTDG.delete(w[0])
			elif (i+10)==21 and a == "Available":
				if w[4]==21 and w[5]==21:
					room = RoomMapper.find(w[1])
					holder = UserMapper.find(w[2])
					time = TimeslotMapper.find(w[3])
					reservation = Reservation(room,holder,time,'was waiting',0)
					ReservationTDG.insert(reservation)
					WaitingTDG.delete(w[0])
