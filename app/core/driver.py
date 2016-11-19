from user import User
from room import Room
from directory import Directory
from registry import Registry
from timeslot import Timeslot
from reservationbook import ReservationBook
from reservation import Reservation
# File for testing the methods and debugging
u1 = User(1,"u1", "password1")
u2 = User(2,"u2", "password2")
u3 = User(3,"u3", "password3")
room1 = Room(1,False)
room2 = Room(2,False)
roomList = [room1, room2]
directory = Directory(roomList)
reservationList = []
waitingList = []
reservationBook = ReservationBook(reservationList,waitingList)
registry = Registry(directory,reservationBook)
# Reserving a room
registry.initiateAction(1)
room1.printLock()
time1 = Timeslot(1,2,"2016-11-15",registry.genTid())
registry.makeNewReservation(1,u1,time1,"des1")
registry.endAction(1)
room1.printLock()
print()
registry.initiateAction(2)
room2.printLock()
time2 = Timeslot(1,3,"2016-11-15",registry.genTid())
registry.makeNewReservation(2,u2,time2,"des2")
registry.endAction(2)
room2.printLock()
print()
# Print Info
registry.getReservationBook().getReservationList()[0]._print()
print()
registry.getReservationBook().getReservationList()[1]._print()
print()
# Attempting to lock a locked room
registry.initiateAction(1)
room1.printLock()
registry.initiateAction(1)
room1.printLock()
registry.endAction(1)
room1.printLock()
print()
# Current Number of Reservations and Waitings in the System
registry.printNb()
print()
# Attempt to reserve a room at the same timeslot or overlapping timeslot
time3 = Timeslot(1,3,"2016-11-15",registry.genTid())
registry.makeNewReservation(1,u3,time3,"des3")
print()
# Add to waiting list
registry.addToWaitingList(1,u3,time3,"des3")
registry.getReservationBook().getWaitingList()[0]._print()
print()
# Current Number of Reservations and Waitings in the System
registry.printNb()
print()
# Modify Reservation
print("Modifying a room: ")
time4 = Timeslot(3,4,"2016-11-15",registry.genTid())
print("Before:")
registry.getReservationBook().getReservationList()[1]._print()
print()
print("After:")
registry.modifyReservation(registry.getReservationBook().getReservationList()[1].getId(),time4)
registry.getReservationBook().getReservationList()[1]._print()
print()
# Current Number of Reservations and Waitings in the System
registry.printNb()
print()
# Cancel Reservation
print("Cancel a reservation")
updatedRoomId = registry.getReservationBook().getReservationList()[0].getRoom().getId()
registry.cancelReservation(registry.getReservationBook().getReservationList()[0].getId())
# Current Number of Reservations and Waitings in the System
registry.printNb()
print()
# Update the waiting list
registry.updateWaiting(updatedRoomId)
registry.getReservationBook().getReservationList()[1]._print()
print()
# Current Number of Reservations and Waitings in the System
registry.printNb()
print()
# View Schedule
print("Schedule:")
schedule = registry.viewSchedule()
for index in range(len(schedule)):
    schedule[index]._print()
    print()
# Make another reservation
time5 = Timeslot(5,7,"2016-11-17",registry.genTid())
registry.makeNewReservation(2,u3,time5,"des5")
registry.getReservationBook().getReservationList()[2]._print()
print()
# Current Number of Reservations and Waitings in the System
registry.printNb()
print()
# View My Reservations
print("My Reservations (u3):")
myReservations = registry.viewMyReservation(u3)
for index in range(len(myReservations)):
    myReservations[index]._print()
    print()
# Recreating reservation from database, overload
time6 = Timeslot(1,2,"2016-11-16",registry.genTid())
reservationD = Reservation(room1,u1,time6,"des6",reservationBook.genRid())
reservationD._print()
# Make another reservation on the day
time7 = Timeslot(8,10,"2016-11-17",registry.genTid())
registry.makeNewReservation(1,u3,time7,"des7")
print()
# Make another reservation
time8 = Timeslot(8,10,"2016-11-21",registry.genTid())
registry.makeNewReservation(1,u3,time8,"des8")
print()
# Make another reservations at max reservationNb
time9 = Timeslot(8,10,"2016-11-22",registry.genTid())
registry.makeNewReservation(1,u3,time9,"des9")
print()
time10 = Timeslot(8,10,"2016-11-23",registry.genTid())
registry.makeNewReservation(1,u3,time10,"des10")
print()
# this one will fail...
time11 = Timeslot(8,10,"2016-11-24",registry.genTid())
registry.makeNewReservation(1,u3,time11,"des11")
print()