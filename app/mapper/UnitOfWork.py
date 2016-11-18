
import UserMapper
import RoomMapper
import ReservationMapper

from app.core.user import User
from app.core.room import Room
from app.core.reservation import Reservation

newUserList = []
userChangedList = []
userDeletedList = []

newRoomList = []
roomChangedList = []
roomDeletedList =[]

newReservationList = []
reservationChangedList = []
reservationDeletedList = []

def __int__(self):
	pass

def registerNewUser(self,user):
    newUserList.append(user)

def registerDirtyUser(self, user):
    userChangedList.append(user)

def registerDeletedUser(self, user):
    userDeletedList.add(user)

def registerNewRoom(self, room):
    newRoomList.append(room)

def registerDirtyRoom(self, room):
    roomChangedList.append(room)

def registerDeletedRoom(self, room):
    roomDeletedList.append(room)

def registerNewReservation(self, reservation):
    newReservationList.append(reservation)

def registerDirtyReservation(self, reservation):
    reservationChangedList.append(reservation)

def registerDeletedReservation(self, reservation):
    reservationDeletedList.append(reservation)

def commit(self):
    if type(self) is User:
        UserMapper.addUser(newUserList)
        UserMapper.updateUser(userChangedList)
        UserMapper.deleteUser(userDeletedList)
        del newUserList[:]
        del userChangedList[:]
        del userDeletedList[:]
    if type(self) is Room:
        RoomMapper.addRoom(newRoomList)
        RoomMapper.updateRoom(roomChangedList)
        RoomMapper.deleteRoom(roomDeletedList)
        del newRoomList[:]
        del roomChangedList[:]
        del roomDeletedList[:]
    if type(self) is Reservation:
        ReservationMapper.addReservation(newReservationList)
        ReservationMapper.updateReservation(reservationChangedList)
        ReservationMapper.deleteReservation(reservationDeletedList)
        del newReservationList[:]
        del reservationChangedList[:]
        del reservationDeletedList[:]
    