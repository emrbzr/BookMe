from app.TDG import ReservationTDG
from app.core.reservation import Reservation
import ReservationIdMap
from app.TDG import RoomTDG
from app.TDG import UserTDG
from app.TDG import TimeslotTDG
import UnitOfWork

def makeNewReservation(room,holder,time,description,reservationId):
    reservation = Reservation(room, holder,time,description,reservationId)
    ReservationIdMap.addTo(reservation)
    UnitOfWork.registerNew(reservation)
    return reservation

def find(reservationId):
    reservation = ReservationIdMap.find(reservationId)
    result = []
    if reservation == None:

        result = ReservationTDG.find(reservationId)
        print(result)
        if result == None:
            return
        else:
            #must make a reference to timeslottable and create a timeslot object
            room = RoomTDG.find(result[0][1])
            holder = UserTDG.find(result[0][3])
            timeslot = TimeslotTDG.find(result[0][4])
            reservation = Reservation(room, holder,timeslot,result[0][2],result[0][0])
            ReservationIdMap.addTo(reservation)
    return reservation

def findByDate(date):
    return ReservationTDG.findByDate(date)

def findByUser(userId):
    userReservation = []
    result = ReservationTDG.findByUserId(userId)
    print(result)
    for index, userR in enumerate(result):
        userReservation.append(find(userR[0]))
    return userReservation

def setReservation(reservationId):
    reservation = find(reservationId)
    reservation.setId(reservationId)
    UnitOfWork.registerDirty(reservationId)

def deleteReservation(reservationId):
    reservation = ReservationIdMap.find(reservationId)
    if reservation is not None:
        ReservationIdMap.removeFrom(reservation)
    UnitOfWork.registerDeleted(reservation)

#save all work
def done():
    UnitOfWork.commit()
#adds room object
def save(reservation):
    ReservationTDG.insert(reservation)
#updates room Object
def update(reservation):
    ReservationTDG.update(reservation)
#deletes room object
def delete(reservation):
    ReservationTDG.delete(reservation)