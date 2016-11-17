from room import Room
from user import User
from timeslot import Timeslot

# Waiting object
class Waiting:

    # Constructor
    def __init__(self,room:Room,holder:User,time:Timeslot,description:str, waitingId:int):
        self.user = holder
        self.time = time
        self.room = room
        self.description = description
        self.waitingId = waitingId

    # Print method for debugging
    def print(self):
        print("Waiting Info")
        print("Holder: " + str(self.user.getName()))
        self.time.print()
        print("Description: " + str(self.description))
        print("WID: " + str(self.waitingId))

    # Accessors and Mutators
    def getId(self):
        return self.waitingId

    def setId(self,waitingId:int):
        self.waitingId = waitingId

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

