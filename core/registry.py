from directory import Directory
from reservationbook import ReservationBook
from room import Room
from user import User
from timeslot import Timeslot

# Registry Object
class Registry:

    # Constructor
    def __init__(self,directory: Directory, reservationBook:ReservationBook):
        self.directory = directory
        self.reservationBook = reservationBook

    # Method to initiate an action
    def initiateAction(self,roomId):
        room = self.directory.getRoom(roomId)
        if(room.getLock() == False):
            room.setLock(True)
        else:
            print("Room Occupied")

    # Method to end an action
    def endAction(self,roomId):
        room = self.directory.getRoom(roomId)
        if (room.getLock() == True):
            room.setLock(False)

    # Method to make a reservation
    def makeNewReservation(self,roomId:int,holder:User,time:Timeslot,description:str):
        # Verifiy if there is any restrictions
        if self.isRestricted(holder,time) == False:
            self.reservationBook.makeReservation(self.directory.getRoom(roomId),holder,time,description)

    # Method to add to the waiting list
    def addToWaitingList(self,roomId:int,holder:User,time:Timeslot,description:str):
        self.reservationBook.addToWaitingList(self.directory.getRoom(roomId),holder,time,description)

    # Method to modify a reservation
    def modifyReservation(self,reservationId:int, time:Timeslot):
        self.reservationBook.modifyReservation(reservationId, time)

    # Method to cancel a reservation
    def cancelReservation(self,reservationId:int):
        self.reservationBook.cancel(reservationId)

    # Method to view ALL reservations
    def viewSchedule(self):
        return self.reservationBook.view()

    # Method to update the waiting list
    def updateWaiting(self,roomId:int):
        self.reservationBook.updateWaiting(roomId)

    # Method to view MY reservations only
    def viewMyReservation(self, user:User):
        return self.reservationBook.viewMyReservation(user)

    # Print method for debugging
    def printNb(self):
        self.reservationBook.printNb()

    # Method to generate a time id
    def genTid(self):
        return self.reservationBook.genTid()

    # Method for restriction
    def isRestricted(self, user:User, time:Timeslot):
        return self.reservationBook.isRestricted(user,time)

    # Accessors and Mutators
    def getDirectory(self):
        return self.directory

    def setDirectory(self,directory:Directory):
        self.directory = directory

    def getReservationBook(self):
        return self.reservationBook

    def setReservationBook(self, reservationBook:ReservationBook):
        self.reservationBook = reservationBook