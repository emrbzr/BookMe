from app.TDG import ReservationTDG
from app.core.reservation import Reservation
import ReservationIdMap
import UnitOfWork

def makeNew(self, room,holder,time,description,reservationId):
    reservation = Reservation(room, holder,time,description,reservationId)
    ReservationIdMap.addTo(reservation)
    UnitOfWork.registerNewReservation(reservation)
    return reservation

def getReservation(self, reservationId):
    reservation = ReservationIdMap.find(reservationId)
    result = []
    if reservation == None:
        result = ReservationTDG.find(reservationId)
    if result == None:
        return
    else:
        reservation = Reservation(result[0], result[1],result[2],result[3],result[4])
        ReservationIdMap.addTo(reservation)
        return reservation

def setReservation(self, reservationId):
    reservation = getReservation(reservationId)
    reservation.setId(reservationId)
    UnitOfWork.registerDirtyReservation(reservationId)

def deleteReservation(self, reservationId):
    reservation = ReservationIdMap.find(reservationId)
    if reservation is not None:
        ReservationIdMap.removeFrom(reservation)
    UnitOfWork.registerDeletedReservation(reservation)

#save all work
def save():
    UnitOfWork.commit()
#adds room object
def addReservation(reservation):
    ReservationTDG.insert(reservation)
#updates room Object
def updateReservation(reservation):
    ReservationTDG.update(reservation)
#deletes room object
def deleteReservation(reservation):
    ReservationTDG.delete(reservation)