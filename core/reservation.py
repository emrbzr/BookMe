from room import Room
from user import User
from timeslot import Timeslot

# Reservation object
class Reservation:

    # Constructor
    def __init__(self, room:Room,holder:User,time:Timeslot,description:str,reservationId:int):
        self.user = holder
        self.time = time
        self.room = room
        self.description = description
        self.reservationId = reservationId

    # Print method for debugging
    def print(self):
        print("Reservation Info")
        print("Holder: " + str(self.user.getName()))
        self.time.print()
        print("Description: " + str(self.description))
        print("RID: " + str(self.reservationId))

    # Accessors and Mutators
    def getId(self):
        return self.reservationId

    def setId(self,reservationId: int):
        self.reservationId = reservationId

    def getTimeslot(self):
        return self.time

    def setTimeslot(self, time: Timeslot):
        self.time = time

    def getRoom(self):
        return self.room

    def setRoom(self,room:Room):
        self.room = room

    def getUser(self):
        return self.user

    def setUser(self, user: User):
        self.user = user

    def getDescription(self):
        return self.description

    def setDescription(self, description:str):
        self.description = description

