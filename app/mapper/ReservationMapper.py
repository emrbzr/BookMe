from app.TDG import ReservationTDG
from app.core.reservation import Reservation
import ReservationIdMap
import UnitOfWork

def makeNewReservation(room,holder,time,description,reservationId):
    reservation = Reservation(room, holder,time,description,reservationId)
    ReservationIdMap.addTo(reservation)
    UnitOfWork.registerNew(reservation)
    return reservation

def getReservation(reservationId):
    reservation = ReservationIdMap.find(reservationId)
    result = []
    if reservation == None:
        result = ReservationTDG.find(reservationId)
        if result == None:
            return
        else:
            reservation = Reservation(result[0][0], result[0][1],result[0][2],result[0][3],result[0][4])
            ReservationIdMap.addTo(reservation)
    return reservation

def setReservation(reservationId):
    reservation = getReservation(reservationId)
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